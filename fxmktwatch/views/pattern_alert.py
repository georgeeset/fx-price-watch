
from django.http import HttpResponse
from django.shortcuts import redirect, render

from fxmktwatch.models import AlertMedium, PatternAlertForm, UserInfo


def add_pattern_alert(request):
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
    
    if request.method == 'POST':
        pass
    else:
        form = PatternAlertForm(user = this_user)
        # form.fields['alert_medium'].queryset = AlertMedium.objects.filter(user=this_user)
        # form.field['alert_medium'].queryset
    context = {'form': form}
    return render(request, 'pattern_alert.html', context)

    


