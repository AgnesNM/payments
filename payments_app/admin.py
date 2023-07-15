from django.contrib import admin

# Register your models here.

from payments_app.models import Payments

admin.site.register(Payments)