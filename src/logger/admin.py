from django.contrib import admin

from .models import Log, TestModel


class BaseAdmin(admin.ModelAdmin):

    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        queryset = super(BaseAdmin, self).get_queryset(request)
        return queryset.filter(user=request.user)


class ReadOnlyAdmin(admin.ModelAdmin):

    list_display_links = None

    def has_add_permission(self, request, obj=None):
        pass

    def has_delete_permission(self, request, obj=None):
        pass

    def get_actions(self, request):
        pass


@admin.register(Log)
class LogAdmin(BaseAdmin, ReadOnlyAdmin):

    search_fields = ['entry']
    list_display = ['level', 'entry', 'timestamp']
    list_filter = ['level']


@admin.register(TestModel)
class TestModelAdmin(BaseAdmin):

    pass
