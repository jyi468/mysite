from django.contrib import admin
from medical.models import MedicalInfo

class MedicalInfoAdmin(admin.ModelAdmin):
	fields = ['license_title']
	list_display = ('license_title', 'maintainer')
	search_fields = ['license_title']
	list_filter = ['maintainer']
	

# Register your models here.
admin.site.register(MedicalInfo, MedicalInfoAdmin)
