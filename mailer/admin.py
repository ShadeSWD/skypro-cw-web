from django.contrib import admin
from mailer.models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at', 'email', 'name', 'surname')
    list_filter = ('created_at',)
    search_fields = ('email', 'name')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at', 'theme')
    list_filter = ('created_at',)
    search_fields = ('theme',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at', 'mailing_time', 'frequency', 'mailing_status')
    list_filter = ('created_at', 'frequency')
    search_fields = ('recipients',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mailing', 'timestamp', 'status', 'response')
    list_filter = ('mailing', 'status')
    search_fields = ('mailing',)
