
from django.http import HttpResponse
from django.shortcuts import redirect, render
from fxmktwatch.models import AlertForm, AlertMedium, Alerts, UserInfo
from ..utils import constants
from datetime import datetime, timedelta

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


def record_alert(alert_form:AlertForm, this_user:UserInfo,  alert_method:AlertMedium, new_alert=None):
    """
    Transfer alert data from alert form into alert model
    """

    if new_alert is None:
        new_alert = Alerts()

    if alert_form.is_valid():
        # print(alertForm.data)
        # new_alert = Alerts()

        new_alert.currency_pair = alert_form.cleaned_data[constants.currency_pair]
        new_alert.setup_condition = alert_form.cleaned_data[constants.setup_condition]
        new_alert.timeframe = alert_form.data[constants.timeframe]
        new_alert.repeat_alarm = alert_form.data[constants.repeat_alarm]
        new_alert.expiration_unit = alert_form.data[constants.expiration_unit]
        new_alert.expiration_value = alert_form.data[constants.expiration_value]
        new_alert.target_price = alert_form.data[constants.target_price]
        new_alert.userid = this_user
        # new_alert.expiration = datetime.now()
        new_alert.note = alert_form.data[constants.note]
        new_alert.alert_medium = alert_method

        if alert_form.cleaned_data[constants.expiration_unit] == constants.hours:
            new_alert.expiration = datetime.utcnow() + timedelta(hours=alert_form.cleaned_data[constants.expiration_value])
        elif alert_form.cleaned_data[constants.expiration_unit] == constants.days:
            new_alert.expiration = datetime.utcnow() + timedelta(days=alert_form.cleaned_data[constants.expiration_value])
        elif alert_form.cleaned_data[constants.expiration_unit] == constants.months:
            new_alert.expiration = datetime.utcnow() + timedelta(days=(alert_form.cleaned_data[constants.expiration_value] * 30))
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
