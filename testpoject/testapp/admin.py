from django.contrib import admin

from .models import CurrentModel, RelCurrent


class CurrentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count')


class RelCurrentAdmin(admin.ModelAdmin):
    list_display = ('id', 'current', 'text')


admin.site.register(CurrentModel, CurrentAdmin)
admin.site.register(RelCurrent, RelCurrentAdmin)
