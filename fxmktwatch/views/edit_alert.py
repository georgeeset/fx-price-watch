from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from fxmktwatch.models import AlertForm, AlertMedium, Alerts, UserInfo
from fxmktwatch.views import alert_medium
from fxmktwatch.views.add_alert import record_alert
from ..utils import constants

def edit_alert(request, id):

    if not request.user.is_authenticated:
        redirect('/')

    this_user = get_object_or_404(UserInfo, username = request.user)
    to_edit = get_object_or_404(Alerts ,id=id)

    if to_edit.userid != this_user:
        return Http404

    if request.method == 'GET':

        init_data = {
            constants.currency_pair : to_edit.currency_pair,
            constants.setup_condition : to_edit.setup_condition,
            constants.timeframe : to_edit.timeframe,
            constants.repeat_alarm : to_edit.repeat_alarm,
            constants.expiration_unit : to_edit.expiration,
            constants.expiration_value : to_edit.expiration_value,
            constants.target_price : to_edit.target_price,
            constants.note : to_edit.note,
        }
        
        edit_form = AlertForm(request.POST or None, initial=init_data)

        user_alert_medium = AlertMedium.objects.filter(user=this_user, verified = True)
        return render(request, 'edit_alert_page.html',
                      {'first_name': this_user.username,
                       'form': edit_form,
                       'user_alert_medium': user_alert_medium
                       })
    
    elif request.method == 'POST':
        updated_form = AlertForm(request.POST)

        form_alert_medium = request.POST['alert_medium']

        # print(form_alert_medium)

        if not alert_medium:
            updated_form.add_error('alert_medium', 'Add alert Mehod if you dont have')
        else:
            alert_method = AlertMedium.objects.get(user=this_user, alert_type=form_alert_medium)
            my_alert = record_alert(alert_form=updated_form, new_alert=to_edit, this_user=this_user, alert_method=alert_method)
            if my_alert:
                my_alert.save()
                return redirect('/user')

    raise Http404

