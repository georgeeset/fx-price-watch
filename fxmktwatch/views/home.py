# Create your views here.

from django.shortcuts import redirect, render
from fxmktwatch.models import LoginForm, SignupForm, UserInfo
from ..utils import constants
from django.contrib.auth import login, authenticate


def home(request):
    signup_form = SignupForm()
    login_form = LoginForm()
    login_message = None

    # print(request.method)
    if request.method == 'POST' and 'signup' in request.POST:
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            # print(signup_form.cleaned_data.get('first_name'))
            new_user = UserInfo()
            new_user.firstname = signup_form.cleaned_data.get(constants.first_name)
            new_user.lastname = signup_form.cleaned_data.get(constants.last_name)
            new_user.username = signup_form.cleaned_data.get(constants.username)
            new_user.interest = ','.join(signup_form.cleaned_data.get(constants.interests))
            new_user.save()
            signup_form.save()
            interests = signup_form.cleaned_data.get(constants.interests)
            print(interests)
            return render(request, 'signup_success.html',
                          {constants.first_name: signup_form.cleaned_data.get(constants.first_name),
                           constants.last_name: signup_form.cleaned_data.get(constants.last_name)}
                           )
       
    elif request.method == 'POST' and 'login' in request.POST:
        login_form = LoginForm(request.POST)
        username = login_form.data.get(constants.username)
        password = login_form.data.get(constants.password)

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/user')
        else:
            login_form.add_error(constants.username, constants.Invalid_Username_or_Password)

        # print(f'{username} . {password}')

    if request.user.is_authenticated:
        print(request.user)
        return redirect('/user')

    return render(request, 'index.html', {'signupform': signup_form, 'loginform': login_form, 'login_error_message': login_message})   

