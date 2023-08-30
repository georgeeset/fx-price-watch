from django.contrib import admin
from .models import UserInfo, Alerts, AlertMedium


# Register your models here.


admin.site.register(UserInfo,)
admin.site.register(Alerts)
admin.site.register(AlertMedium)