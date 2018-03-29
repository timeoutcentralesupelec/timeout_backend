from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from events.models.Association import Association
from events.models.Event import Event
from events.models.UserAssociation import UserAssociation


class EventInline(admin.StackedInline):
    model = Event
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    exclude = ['status']
    #admin.ModelAdmin.actions_selection_counter = True

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 event a été publié"
        else:
            message_bit = "%s events ont été publiés" % rows_updated
        self.message_user(request, "%s avec succès." % message_bit)

    make_published.short_description = "Publier"

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status='e')
        if rows_updated == 1:
            message_bit = "1 event est passé"
        else:
            message_bit = "%s events sont passés" % rows_updated
        self.message_user(request, "%s en attente avec succès." % message_bit)

    make_draft.short_description = "En attente"

    def make_terminated(self, request, queryset):
        rows_updated = queryset.update(status='t')
        if rows_updated == 1:
            message_bit = "1 event est passé"
        else:
            message_bit = "%s events sont passés" % rows_updated
        self.message_user(request, "%s en mode 'terminé' avec succès." % message_bit)

    make_terminated.short_description = "Événement terminé"

    def make_withdraw_demanded(self, request, queryset):
        rows_updated = queryset.update(status='s')
        if rows_updated == 1:
            message_bit = "1 event est passé"
        else:
            message_bit = "%s events sont passés" % rows_updated
        self.message_user(request, "%s en mode 'terminé' avec succès." % message_bit)

    make_withdraw_demanded.short_description = "Demande de suppression"


    date_hierarchy = 'date'
    admin.ModelAdmin.filter_horizontal
    list_display = ['name','asso', 'date', 'status']
    ordering = ['-date']
    actions = [make_published, make_draft, make_terminated, make_withdraw_demanded]

    def get_actions(self, request):
        actions = super(EventAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            del actions['make_published']
            del actions['make_terminated']
        return actions

    # def get_osm_info(self, request):
    #     print(request.user.username)
    #     #asso = Association.objects.filter(pk = request.user.pk)
    #     asso = Association.objects.all()
    #     for a in asso :
    #         print(a.pk, a.name)
    #         print(request.user.pk == a.pk)
    #     print(asso)
    #     #event = Event.objects.filter
    #
    #     if not request.user.is_superuser:
    #         pass
    #     return {}
    #
    # def changelist_view(self, request, extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['osm_data'] = self.get_osm_info(request)
    #     print("extra_context", extra_context)
    #     print("request", request)
    #     #print('object_id', object_id)
    #     return super(EventAdmin, self).changelist_view(
    #         request, extra_context=extra_context
    #     )





@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    inlines = [
        EventInline,
    ]

class UserAssociationInline(admin.StackedInline):
    model = UserAssociation
    can_delete = False
    verbose_name_plural = 'Association'

class UserAssociationAdmin(BaseUserAdmin):
    inlines = [
        UserAssociationInline,
    ]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAssociationAdmin)
