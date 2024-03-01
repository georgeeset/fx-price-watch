

from telnetlib import LOGOUT
from django.shortcuts import redirect


def logout_user(request):
    if request.method == 'GET':
            if request.user.is_authenticated:
                LOGOUT(request)
    return redirect('/')