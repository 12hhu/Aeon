from django.contrib import admin
from Aeonapp.models import WorkshopDetail

class WorkshopDetailAdmin(admin.ModelAdmin):
    list_display=['id','title','description']
admin.site.register( WorkshopDetail,WorkshopDetailAdmin)
# Register your models here.
