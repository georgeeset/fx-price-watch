
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_user(request):
    if request.method == 'GET':
            if request.user.is_authenticated:
                logout(request)
    return redirect('/')
