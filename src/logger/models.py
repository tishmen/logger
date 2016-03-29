from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext, ugettext_lazy as _

class TestModel(models.Model):

    test_field = models.CharField(max_length=100)

#Inherit LoggerEntery model from LogEntry model of admin
class LoggerEntery(LogEntry):
	log_level = models.TextField(max_length=200)
	app_name  = models.CharField(max_length=100, default="logger")

class AdminLoggerEntery(admin.ModelAdmin):
	list_display = ('log_level', 'change_message', 'action_time')
	list_filter = ['log_level','action_time']
	search_fields = ['change_message']
	list_display_links = None

	def has_achange_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
	def get_actions(self, request):
		pass


