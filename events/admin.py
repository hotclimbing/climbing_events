from django.contrib import admin

from events.models import Event, Participant, Route, Accent


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'pin', 'gender', 'city', 'set_index', 'group_index', )
    search_fields = ('last_name', 'first_name', 'city', )


class RouteAdmin(admin.ModelAdmin):
    list_display = ('number', 'grade', 'color', 'event',)
    list_filter = ('event',)


admin.site.register(Event)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Accent)




