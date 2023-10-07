from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput, TextInput
from fxmktwatch.utils import constants
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
import pytz


# Create your models here.

# class Users(models.Model):
#     """ Model for user information"""
#     firstname = models.CharField(max_length=64)
#     lastname = models.CharField(max_length=64)
#     username = models.CharField(max_length=64, unique=True)
#     uid = models.CharField(max_length=255, primary_key=True)



class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               'id': 'name',
                                                               'autocomplete': 'given-name'
                                                               }))
    last_name = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              'id': 'last_name'
                                                              }))
    username = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             'id': 'reg_username',
                                                             'autocomplete':'username'
                                                             }))
    # email = forms.EmailField(required=True,
    #                          widget=forms.TextInput(attrs={'placeholder': 'Email',
    #                                                        'class': 'form-control',
    #                                                        }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password2',
                                                                  }))
    interests = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple( attrs={
            'class': 'checkBoxes',
        }),
        required=True,
        choices=[
            ('Forex','Forex' ),
            ('Crypto', 'Crypto'),
            ('Deriv', 'Deriv'),
            ('Metals', 'Metals'),
        ],
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UserInfo(models.Model):
    """Model for user interests"""
    interest = models.CharField(max_length=50, null=False)
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'first name : {self.firstname} \n username : {self.username}'


CURRENCY_CHOICES = [
    ('EURUSD', 'EUR/USD'),
    ('EURJPY', 'EUR/JPY'),
    ('USDJPY', 'USD/JPY'),
    ('GBPUSD', 'GBP/USD'),
    ('AUDUSD', 'AUD/USD'),
    ('USDCAD', 'USD/CAD'),
    ('USDCHF', 'USD/CHF'),
    ('CADCHF', 'CAD/CHF'),
    ('USDCNY', 'USD/CNY'),
    ('USDHKD', 'USD/HKD'),
    ('EURGBP', 'EUR/GBP'),

    # {'id':'frxAUDUSD', 'table': 'AUDUSD'},
    # {'id':'frxEURGBP', 'table': 'EURGBP'},
    # {'id':'frxEURJPY', 'table': 'EURJPY'},
    # {'id':'frxEURUSD', 'table': 'EURUSD'},
    # {'id':'frxGBPUSD', 'table': 'GBPUSD'},
    # {'id':'frxUSDCAD', 'table': 'USDCAD'},
    # {'id':'frxUSDCHF', 'table': 'USDCHF'},
    # {'id':'frxUSDJPY', 'table': 'USDJPY'},
    ('frxXAUUSD', 'GoldUSD'),
    ( 'Volatility_50_Index', 'Volatility 50 Index'),
    ( 'Volatility_75_Index', 'Volatility 75 Index'),
    ( 'Volatility_100_Index', 'Volatility 100 Index'),
    ( 'Step_Index', 'Step Index'),
    ( 'Boom_500_Index', 'Boom 500 Index'),
    ( 'Boom_1000_Index', 'Boom 1000 Index'),
    ( 'Crash_500_Index', 'Crash 500 Index'),
    ( 'Crash_1000_Index', 'Crash 1000 Index'),
    ( 'Jump_50_Index', 'Jump 50 Index'),
    ( 'Jump_75_Index', 'Jump 75 Index'),
    ( 'Jump_100_Index','Jump 100 Index'),
    # ('BTC/USDT', 'BTC/USDT'),
    # ('ETH/USDT', 'ETH/USDT'),
]

CONDITION_CHOICES = [
    ('CLOSING PRICE IS GREATER THAN SETPOINT','CLOSING PRICE IS GREATER THAN SETPOINT'),
    ('CLOSING PRICE IS LESS THAN SETPOINT', 'CLOSING PRICE IS LESS THAN SETPOINT'),
    ('OPENING PRICE IS GREATER THAN SETPOINT', 'OPENING PRICE IS GREATER THAN SETPOINT'),
    ('OPENING PRICE IS LESS THAN SETPOINT', 'OPENING PRICE IS LESS THAN SETPOINT'),
    ('HIGHEST PRICE IS GREATER THAN SETPOINT', 'HIGHEST PRICE IS GREATER THAN SETPOINT'),
    ('HIGHEST PRICE IS LESS THAN SETPOINT', 'HIGHEST PRICE IS LESS THAN SETPOINT'),
    ('LOWEST PRICE IS GREATER THAN SETPOINT', 'LOWEST PRICE IS GREATER THAN SETPOINT'),
    ('LOWEST PRICE IS LESS THAN SETPOINT', 'LOWEST PRICE IS LESS THAN SETPOINT'),
]

TIMEFRAME_CHOICES = [
    ('H1', 'H1'),
    ('H4', 'H4'),
    ('D1', 'D1'),
    ('W1', 'W1'),
    ('M1', 'M1'),
]

TIMEUNIT_CHOICES = [
    (constants.hours, constants.hours),
    (constants.days, constants.days),
    (constants.months, constants.months),
]

MEDIUM_CHOICES = [
    (constants.telegram, constants.telegram),
    (constants.email, constants.email),
    # add more as you progress
]

STATUS_CHOICES = [
    ('OPEN', 'OPEN'),
    ('CLOSE', 'CLOSE'),
    ('EXPIRED', 'EXPIRED'),
]

class AlertMedium(models.Model):
    alert_type = models.CharField(max_length=20)
    alert_id = models.CharField(max_length=128, unique=True)
    verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=50)
    verification_expiration = models.DateTimeField()
    chat_id = models.CharField(null=True, max_length=50)
    user = models.ForeignKey(UserInfo, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alert_type}: {self.alert_id}"

    @property
    def is_expired(self):

        if datetime.utcnow().replace(tzinfo=pytz.UTC) > self.verification_expiration.replace(tzinfo=pytz.UTC):
            print('Expired')
            return True
        else:
            return False


class Alerts(models.Model):
    currency_pair = models.CharField(max_length=30, null=False)
    setup_condition = models.CharField(max_length=50, null=False)
    target_price = models.FloatField(null=False, )
    timeframe = models.CharField(max_length=4, null=False)
    repeat_alarm = models.PositiveSmallIntegerField(null=False, default=1)
    alertcount = models.IntegerField(null=False,default=0)
    status = models.CharField(max_length=10, null=False, default=0)
    userid = models.ForeignKey(UserInfo, null=False, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    expiration_unit = models.CharField(max_length=10, null=False)
    expiration_value = models.PositiveSmallIntegerField(null=False, default=1)
    expiration = models.DateTimeField(null=False,)
    alert_medium = models.ForeignKey(AlertMedium, null=False, on_delete=models.CASCADE)

    note = models.CharField(null=False, max_length=100)

    @property
    def is_active(self):
        return datetime.utcnow().replace(tzinfo=pytz.UTC) < self.expiration.replace(tzinfo=pytz.UTC) and self.repeat_alarm > self.alertcount

    def __str__(self):
        return f'{__name__}, currency_pair => {self.currency_pair}, setup_condition => {self.setup_condition}'

    def to_dict(self):
        my_dict = {"pair":  self.currency_pair,
                   "setup_condition": self.setup_condition,
                   "target_price": self.target_price ,
                   "timeframe": self.timeframe,
                   "repeat_alarm":  self.repeat_alarm,
                   "alert_count": self.alertcount,
                   "date_created": self.time_created ,
                   "expiration_date": self.expiration ,
                   "alertMedium": self.alert_medium.alert_type 
                   }
        return dict(my_dict)

class EmailAlertForm(forms.Form):
    # medium = forms.models.CharField(max_length=50, required=True, widget=forms.Select(choices=MEDIUM_CHOICES))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

class TelegramAlertForm(forms.Form):
    telegram_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))

class WhatsappAlertForm(forms.Form):
    number = PhoneNumberField(widget=forms.NumberInput(attrs={
        'class':'form-control'
    }))

class CodeVerificationForm(forms.Form):
    code = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))


class AlertForm(forms.Form):

    currency_pair = forms.CharField(max_length=30, required=True, widget=forms.Select(choices=CURRENCY_CHOICES, attrs={ 'class':'form-control'}) )
    setup_condition = forms.CharField(max_length=50, required=True, widget=forms.Select(choices=CONDITION_CHOICES, attrs={ 'class':'form-control'}))

    target_price = forms.FloatField(required=True, initial=0.001, widget=forms.NumberInput(attrs={'id': 'float_form', 'class':'form-control'}))

    timeframe = forms.CharField(max_length=4, required=True, widget=forms.Select(choices=TIMEFRAME_CHOICES, attrs={ 'class':'form-control'}))
    repeat_alarm = forms.IntegerField(required=True, min_value=1, initial=1, widget=forms.NumberInput(attrs={ 'class':'form-control'},))
    expiration_unit = forms.CharField(max_length=10, required=True, widget=forms.Select(choices=TIMEUNIT_CHOICES, attrs={ 'class':'form-control'}))
    expiration_value = forms.IntegerField(required=True, min_value=1, initial=1, widget=forms.NumberInput(attrs={ 'class':'form-control'}))
    note = forms.CharField(required=True, max_length=100, min_length=10, widget=forms.Textarea(attrs={'size': '30', 'class':'form-note'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'autocomplete': 'username',
         'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
