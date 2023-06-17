from django.contrib import admin
from .models import ServiceCategory, Institute, InstituteEvent

admin.site.register(ServiceCategory)
admin.site.register(Institute)
admin.site.register(InstituteEvent)
