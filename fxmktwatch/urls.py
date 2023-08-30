from django.urls import path

from . import views

urlpatterns = [
     path('', views.home),
     path('user/', views.userPage),
     path('logout/', views.logout_user, ),
     path('user/create-alert', views.add_alert),
     path('user/edit-alert/<int:id>', views.edit_alert),
     path('user/delete-alert/<int:id>', views.delete_alert),
     path('user/alert-methods', views.alert_medium),
]
