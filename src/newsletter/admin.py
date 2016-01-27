from django.contrib import admin
from .models import signup
from .models import sellerprofile
from .models import notifications
# Register your models here.
admin.site.register(signup)
admin.site.register(sellerprofile)
admin.site.register(notifications)
