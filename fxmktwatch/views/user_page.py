from django.shortcuts import redirect, render

from fxmktwatch.models import Alerts, UserInfo
from ..utils import constants


def userPage(request):
    if not request.user.is_authenticated:
         return redirect('/')
    this_user = UserInfo.objects.get(username = request.user)
    user_alerts = Alerts.objects.filter(userid = this_user).order_by(constants.time_created_neg)
    return render(request, 'user_page.html', {'first_name': this_user.username, 'alert_list': user_alerts})
