from django.contrib import admin

from .forms import BleepModelForm
from .models import Bleep


class BleepModelAdmin(admin.ModelAdmin):
    # form = BleepModelForm
    pass

admin.site.register(Bleep)
