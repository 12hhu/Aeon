from django.contrib import admin
from Aeonapp.models import *
@admin.register(ContactusFormDetails)
class ContactusFormDetailsAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone','profession')

@admin.register(WorkshopFormDetails)
class WorkshopFormDetailsAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone','profession')

@admin.register(PublicationFormDetail)                                                                     
class PublicationFormDetailAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone','profession')

class WorkshopDetailAdmin(admin.ModelAdmin):
    list_filter=('id',)
    list_display=['id','title','description']
admin.site.register( WorkshopDetail,WorkshopDetailAdmin)
# Register your models here.



@admin.register(PublicationPaper)
class PublicationPaperAdmin(admin.ModelAdmin):
    list_display = ('year', 'title','authors')
    list_filter = ('year',)
    search_fields = ('title', 'authors')

