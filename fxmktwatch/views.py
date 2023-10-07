from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from fxmktwatch.models import SignupForm, LoginForm, UserInfo, AlertForm, Alerts, EmailAlertForm, TelegramAlertForm, AlertMedium, CodeVerificationForm
from django.contrib.auth import login, authenticate, logout
from datetime import datetime, timedelta
from django.core.mail import send_mail
import random, math
from fxmktwatch.utils import constants, services
from django.http import Http404

# Create your views here.

def home(request):
    signup_form = SignupForm()
    login_form = LoginForm()
    login_message = None

    # print(request.method)
    if request.method == 'POST' and 'signup' in request.POST:
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            # print(signup_form.cleaned_data.get('first_name'))
            new_user = UserInfo()
            new_user.firstname = signup_form.cleaned_data.get('first_name')
            new_user.lastname = signup_form.cleaned_data.get('last_name')
            new_user.username = signup_form.cleaned_data.get('username')
            new_user.interest = ','.join(signup_form.cleaned_data.get('interests'))
            new_user.save()
            signup_form.save()
            interests = signup_form.cleaned_data.get('interests')
            print(interests)
            return render(request, 'signup_success.html',
                          {'first_name': signup_form.cleaned_data.get('first_name'),
                           'last_name': signup_form.cleaned_data.get('last_name')}
                           )
       
    elif request.method == 'POST' and 'login' in request.POST:
        login_form = LoginForm(request.POST)
        username = login_form.data.get('username')
        password = login_form.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/user')
        else:
            login_form.add_error('username', 'Invalid Username or Password')

        # print(f'{username} . {password}')

    if request.user.is_authenticated:
        print(request.user)
        return redirect('/user')

    return render(request, 'index.html', {'signupform': signup_form, 'loginform': login_form, 'login_error_message': login_message})   

def userPage(request):
    if not request.user.is_authenticated:
         return redirect('/')


    this_user = UserInfo.objects.get(username = request.user)
    user_alerts = Alerts.objects.filter(userid = this_user).order_by('-time_created')
    # print(user_alerts)
    # print(len(user_alerts))
    # print(user_alerts[0].to_dict())

    return render(request, 'user_page.html', {'first_name': this_user.username, 'alert_list': user_alerts})

def record_alert(alert_form:AlertForm, this_user:UserInfo,  alert_method:AlertMedium, new_alert=None):
    """
    Transfer alert data from alert form into alert model
    """

    if new_alert is None:
        new_alert = Alerts()

    if alert_form.is_valid():
        # print(alertForm.data)
        # new_alert = Alerts()

        new_alert.currency_pair = alert_form.cleaned_data['currency_pair']
        new_alert.setup_condition = alert_form.cleaned_data['setup_condition']
        new_alert.timeframe = alert_form.data['timeframe']
        new_alert.repeat_alarm = alert_form.data['repeat_alarm']
        new_alert.expiration_unit = alert_form.data['expiration_unit']
        new_alert.expiration_value = alert_form.data['expiration_value']
        new_alert.target_price = alert_form.data['target_price']
        new_alert.userid = this_user
        # new_alert.expiration = datetime.now()
        new_alert.note = alert_form.data['note']
        new_alert.alert_medium = alert_method

        if alert_form.cleaned_data['expiration_unit'] == constants.hours:
            new_alert.expiration = datetime.utcnow() + timedelta(hours=alert_form.cleaned_data['expiration_value'])
        elif alert_form.cleaned_data['expiration_unit'] == constants.days:
            new_alert.expiration = datetime.utcnow() + timedelta(days=alert_form.cleaned_data['expiration_value'])
        elif alert_form.cleaned_data['expiration_unit'] == constants.months:
            new_alert.expiration = datetime.utcnow() + timedelta(days=(alert_form.cleaned_data['expiration_value'] * 30))
        else:
            HttpResponse('Somethin went wrong with expiraiton date')
       
        return new_alert
    else:
        print('Problem dey here')
        print(f"""{alert_form.data.get('currency_pair')}
                    {alert_form.data.get('setup_condition')}
                    {alert_form.data.get('target_price')}
                    {alert_form.data.get('timeframe')}
                    {alert_form.data.get('repeat_alarm')}
                    {alert_form.data.get('expiration_unit')}
                    {alert_form.data.get('expiration_value')}
                    {alert_form.data.get('note')}
                    {alert_form.data.get('alert_medium')}""")
        return None

def add_alert(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    this_user = UserInfo
    try:
        this_user = UserInfo.objects.get(username = request.user)
    except:
        return HttpResponse('Something went worng, contact support')

    alertForm = AlertForm()
    if request.method == 'POST':
        alert_form = AlertForm(request.POST)

        # print(thisUser.id)
        form_alert_medium = request.POST['alert_medium']
        print(form_alert_medium)
        if not form_alert_medium:
            alert_form.add_error('alert_medium', 'Add alert Mehod if you dont have')
        else:
            alert_method = AlertMedium.objects.get(user=this_user, alert_type=form_alert_medium)

            new_alert = record_alert(alert_form=alert_form, this_user=this_user, alert_method=alert_method)
            if new_alert:
                new_alert.save(force_insert=True)
                print('alert_saved===*')
                return redirect('/user')

            alertForm = AlertForm()
    user_alert_medium = AlertMedium.objects.filter(user=this_user, verified = True)
    return render(request, 'create_alert_page.html',
                  {'first_name': request.user.get_username, 'form': alertForm, 'user_alert_medium': user_alert_medium})


def edit_alert(request, id):

    if not request.user.is_authenticated:
        redirect('/')

    this_user = get_object_or_404(UserInfo, username = request.user)
    to_edit = get_object_or_404(Alerts ,id=id)

    if to_edit.userid != this_user:
        return Http404

    if request.method == 'GET':

        init_data = {
            'currency_pair' : to_edit.currency_pair,
            'setup_condition' : to_edit.setup_condition,
            'timeframe' : to_edit.timeframe,
            'repeat_alarm' : to_edit.repeat_alarm,
            'expiration_unit' : to_edit.expiration,
            'expiration_value' : to_edit.expiration_value,
            'target_price' : to_edit.target_price,
            'note' : to_edit.note,
        }
        
        edit_form = AlertForm(request.POST or None, initial=init_data)


        user_alert_medium = AlertMedium.objects.filter(user=this_user, verified = True)
        return render(request, 'edit_alert_page.html', {'first_name': this_user.username, 'form': edit_form, 'user_alert_medium': user_alert_medium})
    elif request.method == 'POST':
        updated_form = AlertForm(request.POST)

        form_alert_medium = request.POST['alert_medium']

        print(form_alert_medium)

        if not alert_medium:
            updated_form.add_error('alert_medium', 'Add alert Mehod if you dont have')
        else:
            alert_method = AlertMedium.objects.get(user=this_user, alert_type=form_alert_medium)
            my_alert = record_alert(alert_form=updated_form, new_alert=to_edit, this_user=this_user, alert_method=alert_method)
            if my_alert:
                my_alert.save()
                return redirect('/user')

    raise Http404


def delete_alert(request, id):
    this_user = get_object_or_404(UserInfo, username = request.user)
    to_delete = get_object_or_404(Alerts ,id=id)

    if to_delete.userid != this_user: #or not to_delete.is_editable:
        return Http404

    if request.method == 'GET':
        return render(request, 'delete_confirmation.html', {'item':to_delete})

    elif request.method == 'POST' and 'yes' in request.POST:
        to_delete.delete()

    return redirect('/user')

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
        from_email="alert.pricewatch@gmail.com",
        recipient_list=[email],
        fail_silently=False,
        )

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

    


def logout_user(request):
    if request.method == 'GET':
            if request.user.is_authenticated:
                logout(request)
    return redirect('/')