from django.contrib import admin

from images.models import Images


# Register your models here.

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    raw_id_fields = ["id"]
    list_display = ["uuid", "name"]
