from django.contrib import admin

from images.models import Images


# Register your models here.

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display_links = ["id"]
    list_display = ["uuid", "name"]
