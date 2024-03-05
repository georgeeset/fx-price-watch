

from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from fxmktwatch.models import PatternAlert, UserInfo


class DeletePatternAlert(View):

    def get(self, request, id, *args, **kwargs):
        this_user = get_object_or_404(UserInfo, username = request.user)

        to_delete = get_object_or_404(PatternAlert ,id=id)

        if to_delete.user_id != this_user:
            return Http404
        
        return render(request, 'delete_pattern_confirm.html', {'item': to_delete})


    def post(self, request, id, *args, **kwargs):
        this_user = get_object_or_404(UserInfo, username = request.user)
        to_delete = get_object_or_404(PatternAlert ,id=id)

        if to_delete.user_id != this_user:
            return Http404
        
        if 'yes' in request.POST:
            to_delete.delete()

        return redirect('/user')
        

