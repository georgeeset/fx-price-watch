from datetime import datetime, timedelta
import math
from os import environ
from random import random
from django.shortcuts import get_object_or_404, render

from fxmktwatch.models import AlertMedium, CodeVerificationForm, EmailAlertForm, TelegramAlertForm, UserInfo
from ..utils import constants, services

def alert_medium(request):
    this_user = get_object_or_404(UserInfo, username = request.user)
    user_alert_medium = AlertMedium.objects.filter(user = this_user)

    email_form = EmailAlertForm()
    telegram_form = TelegramAlertForm()
    verification_form = CodeVerificationForm()

    # if request.method == 'GET':
    
    if request.method == 'POST':
        if 'add_email' in request.POST:

            email_form = EmailAlertForm(request.POST)
            if email_form.is_valid():
                # add eht eemail to alertmediem model and send verirification message
                # print(generate_code())
                print(email_form.data.get(constants.e_mail))
                alert_medium = AlertMedium()
                alert_medium.alert_type = constants.e_mail
                alert_medium.alert_id = email_form.data.get(constants.e_mail)
                alert_medium.verification_code = generate_code()
                alert_medium.verification_expiration = datetime.utcnow() + timedelta(minutes=20)
                alert_medium.user = this_user

                #delete existing email alert medium as only one is alowed
                for medium in user_alert_medium:
                    if medium.alert_type == constants.e_mail:
                        medium.delete()
                        user_alert_medium = AlertMedium.objects.filter(user = this_user)
                
                try:
                    alert_medium.save()
                    mail_code(alert_medium.alert_id, alert_medium.verification_code)
                except:
                    email_form.add_error(constants.e_mail, constants.email_already_exist)
                
                user_alert_medium = AlertMedium.objects.filter(user = this_user)

                      
        elif 'add_telegram' in request.POST:
            telegram_form = TelegramAlertForm(request.POST)
            
            if telegram_form.data.get('telegram_id')[0] != '@':
                telegram_form.add_error(field='telegram_id', error='Telegram id starts with @ symbol')
            else:
                print(generate_code())
                print(telegram_form.data.get('telegram_id'))
                #delete existing Telegram alert medium as only one is alowed
                for medium in user_alert_medium:
                    if medium.alert_type == constants.t_elegram:
                        medium.delete()
                        user_alert_medium = AlertMedium.objects.filter(user = this_user)
                
                # Send telegram message and expect result
                alert_medium = AlertMedium()
                alert_medium.alert_type = constants.t_elegram
                alert_medium.alert_id = telegram_form.data.get(constants.telegram_id)
                alert_medium.verification_code = generate_code()
                alert_medium.verification_expiration = datetime.utcnow() + timedelta(minutes=20)
                alert_medium.user = this_user

                try:
                    alert_medium.save()
                except:
                    telegram_form.add_error('telegram_id', error='This Id already exist')
                user_alert_medium = AlertMedium.objects.filter(user = this_user)


        elif 'verify_email' in request.POST:
            verification_form = CodeVerificationForm(request.POST)
            # print(verification_form.data.get('code'))

            for item in user_alert_medium:

                if item.alert_type == constants.e_mail:
                    
                    print(item.verification_code)
                    if  item.verification_code == verification_form.data.get('code'):
                        if item.is_expired:
                            item.delete()
                            verification_form.add_error('code', 'Verificaton code expired. Add email again')
                        else:
                            item.verified = True
                            item.save()

                        break

                    else:
                        verification_form.add_error ('code', 'Wrong code. please try again')

        elif 'resend_email' in request.POST:
            for item in user_alert_medium:
                if item.alert_type == constants.e_mail:
                    mail_code(item.alert_id, item.verification_code)

        elif 'verify_telegram' in request.POST:
            verification_form = CodeVerificationForm(request.POST)
            # print(verification_form.data.get('code'))
            telegram_service = services.TelegramServices()

            for item in user_alert_medium:

                if item.alert_type == constants.t_elegram:
                    
                    # print(item.verification_code)
                    if item.is_expired:
                        item.delete()
                    else:
                        status = telegram_service.search_code(
                            acct_id=item.alert_id, code=item.verification_code
                            )
                        if status != None:
                            item.chat_id = status
                            item.verified = True
                            item.save()
                            telegram_service.send_success()
                        else:
                            verification_form.add_error ('code', 'Confirmation code not found. please try again')
                        break
                        # if  item.verification_code == verification_form.data.get('code'):
                        #     if item.is_expired:
                        #         item.delete()
                        #     else:
                        #         item.verified = True
                        #         item.save()

                        #     break

                        # else:
                        #     verification_form.add_error ('code', 'Wrong code. please try again')

    return render(request, 'alert_methods_page.html', {'email_form': email_form, 'telegram_form': telegram_form, 'verification_form': verification_form, 'alert_medium': user_alert_medium})


def generate_code():
    random_str = ""
    digits = [i for i in range(0, 10)]
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    return random_str


def mail_code(email, code):
    send_mail(
        subject= 'Email Verification - FX market watch',
        message=f"Your are receiving this message because you want to activate your email for price alert\n this is your verification code: {code}",
        from_email=environ.get('FX_EMAIL'),
        recipient_list=[email],
        fail_silently=False,
        )