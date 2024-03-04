
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from fxmktwatch.models import AlertMedium, UserInfo, PatternAlertForm


class PatternAlert(View):
    
    def get(self, request, *args, **kwargs):
        """ this route displays the transaction page for
            candlestick  pattern detection
        """
        if not request.user.is_authenticated:
            return redirect('/')

        this_user = UserInfo
        try:
            this_user = UserInfo.objects.get(username = request.user)
        except:
            return HttpResponse('Something went wrong, contact support')
        
       
        form = PatternAlertForm(user = this_user)
        # form.fields['alert_medium'].queryset = AlertMedium.objects.filter(user=this_user)
        # form.field['alert_medium'].queryset
        context = {'form': form}
        return render(request, 'pattern_alert.html', context)
    
    def post(self, request, *args, **kwargs):
        this_user = UserInfo
        try:
            this_user = UserInfo.objects.get(username = request.user)
        except:
            return HttpResponse('Something went wrong, contact support')
        
        alert_form = PatternAlertForm(request.POST)
        

        if alert_form.is_valid():
            pattern_alert = alert_form.save(commit = False)
            pattern_alert.user_id = this_user
            pattern_alert.save()
            print('success')

            print(f"{pattern_alert.user_id} {pattern_alert.currency_pair}")

            return redirect('/')
