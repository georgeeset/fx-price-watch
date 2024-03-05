

from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from fxmktwatch.models import PatternAlert, PatternAlertForm, UserInfo


class EditPatternAlert(View):

    def get(self, request, id, *args, **kwargs):
        """
        get request to edit alert page
        id = alert id to be edited
        """
        if not request.user.is_authenticated:
            return redirect('/')
        
        this_user = UserInfo
        
        this_user = get_object_or_404(UserInfo, username = request.user)
        editable = get_object_or_404(PatternAlert, id = id)
        
        if editable.user_id != this_user:
            return Http404
        
        form = PatternAlertForm(instance = editable)
        return render(request, 'edit_pattern_alert.html', context={'form': form, 'edit': True})
    

    def post(self, request, id, *args, **kwargs):
        """
        post request to edit alert
        """
        if not request.user.is_authenticated:
            return redirect('/')

        this_user = UserInfo
        this_user = get_object_or_404(UserInfo, username = request.user)

        editable = get_object_or_404(PatternAlert, id = id)
        
        if editable.user_id != this_user:
            return Http404

        edited = PatternAlertForm(request.POST)
        if edited.is_valid():
            edit = edited.save(commit=False)
            editable.note = edit.note
            editable.alert_medium = edit.alert_medium
            editable.currency_pair = edit.currency_pair
            editable.timeframe = edit.timeframe
            editable.save()

            return redirect('/')
