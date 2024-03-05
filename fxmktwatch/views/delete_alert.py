
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from fxmktwatch.models import Alerts, UserInfo


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
