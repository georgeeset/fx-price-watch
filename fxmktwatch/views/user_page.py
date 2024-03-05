from django.shortcuts import redirect, render

from fxmktwatch.models import Alerts, PatternAlert, UserInfo
from ..utils import constants


def userPage(request):
     if not request.user.is_authenticated:
         return redirect('/')
     try:
          this_user = UserInfo.objects.get(username = request.user)
     except:
          return redirect('/logout')
     user_alerts = Alerts.objects.filter(userid = this_user).order_by(constants.time_created_neg)
     pattern_alerts = PatternAlert.objects.filter(user_id = this_user).order_by(constants.time_created_neg)
     return render(request, 'user_page.html', {'first_name': this_user.username, 'alert_list': user_alerts, 'pattern_alerts': pattern_alerts})
