from django.contrib import admin

from .models import TestModel


class ReadOnlyAdmin(admin.ModelAdmin):

    list_display_links = None

    def has_add_permission(self, request, obj=None):
        pass

    def has_delete_permission(self, request, obj=None):
        pass

    def get_actions(self, request):
        pass


@admin.register(TestModel)
class TestModelAdmin(ReadOnlyAdmin):

    pass
