from django.contrib import admin

from apps.messenger.models import *

# Register your models here.
admin.site.register(ChatMessage)

admin.site.register(ChatGroup)
admin.site.register(GroupMessage)


