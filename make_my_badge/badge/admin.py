from django.contrib import admin
from models import Event, BadgeTemplate, Item

class EventAdmin(admin.ModelAdmin):
    pass

class BadgeTemplateAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(BadgeTemplate, BadgeTemplateAdmin)
admin.site.register(Item, ItemAdmin)
