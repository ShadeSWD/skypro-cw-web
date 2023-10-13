from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    email = models.CharField(max_length=50, verbose_name='email', unique=True)
    name = models.CharField(max_length=150, verbose_name='name')
    surname = models.CharField(max_length=150, verbose_name='surname')
    patronymic = models.CharField(max_length=150, verbose_name='patronymic')
    comments = models.TextField(verbose_name='comments')


class Message(models.Model):
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    theme = models.CharField(max_length=50, verbose_name='theme')
    content = models.TextField(verbose_name='content')


class Mailing(models.Model):
    CREATED = 0
    RUNNING = 1
    FINISHED = 2

    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2

    MAILING_STATUSES = (
        (CREATED, 'Created'),
        (RUNNING, 'Running'),
        (FINISHED, 'Finished')
    )

    PERIODS = (
        (DAILY, 'Once a day'),
        (WEEKLY, 'Once a week'),
        (MONTHLY, 'Once a month')
    )

    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    mailing_time = models.DateTimeField(verbose_name='mailing time')
    frequency = models.IntegerField(default=WEEKLY, choices=PERIODS, verbose_name='mailing frequency')
    mailing_status = models.IntegerField(default=CREATED, choices=MAILING_STATUSES)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='message')
    recipients = models.ManyToManyField(Client, verbose_name='recipients')


class Log(models.Model):
    SUCCESSFUL = 1
    UNSUCCESSFUL = 0

    STATUSES = (
        (SUCCESSFUL, 'Successful'),
        (UNSUCCESSFUL, 'Unsuccessful')
    )

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='mailing')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='timestamp')
    status = models.BooleanField(choices=STATUSES, verbose_name='status')
    response = models.TextField(blank=True, verbose_name='response')
