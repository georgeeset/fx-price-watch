from django.urls import path
from .views.home import home
from .views.user_page import userPage
from .views.logout import logout_user
from .views.add_alert import add_alert
from .views.delete_alert import delete_alert
from .views.alert_medium import alert_medium
from .views.edit_alert import edit_alert
from .views.pattern_alert import add_pattern_alert

urlpatterns = [
     path('', home, name='home'),
     path('user/', userPage, name='userPage'),
     path('logout/', logout_user, name='logout'),
     path('user/create-alert', add_alert, name='add_alert'),
     path('user/edit-alert/<int:id>', edit_alert, name='edit_alert'),
     path('user/delete-alert/<int:id>', delete_alert, name='delete_alert'),
     path('user/alert-methods', alert_medium, name='alert_medium'),
     path('user/create-alert/pattern-alert', add_pattern_alert, name='add_alert')
]
