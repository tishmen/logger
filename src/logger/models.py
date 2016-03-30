from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):

    LEVEL_CHOICES = [
        ['debug', 'debug'],
        ['info', 'info'],
        ['warning', 'warning'],
        ['error', 'error'],
    ]

    user = models.ForeignKey(User)
    entry = models.TextField()
    level = models.CharField(max_length=7, choices=LEVEL_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def debug(user, entry):
        Log.objects.create(user=user, entry=entry, level='debug')

    @staticmethod
    def info(user, entry):
        Log.objects.create(user=user, entry=entry, level='info')

    @staticmethod
    def warning(user, entry):
        Log.objects.create(user=user, entry=entry, level='warning')

    @staticmethod
    def error(user, entry):
        Log.objects.create(user=user, entry=entry, level='error')

    def __str__(self):
        return '[{}: {}] {}'.format(self.timestamp, self.level, self.entry)


class TestModel(models.Model):

    user = models.ForeignKey(User)
    test_field = models.TextField()

    def __str__(self):
        return self.test_field


def test_logging():
    user = User.objects.first()
    Log.debug(user, 'test for debug')
    Log.info(user, 'test for info')
    Log.warning(user, 'test for warning')
    Log.error(user, 'test for error')
