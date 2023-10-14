from django.shortcuts import render
from django.views.generic import ListView, DetailView
from mailer.models import *


class MailingsListView(ListView):
    model = Mailing
    template_name = "mailer/mailings.html"
    context_object_name = 'mailings'
    queryset = Mailing.objects.all()


class MailingDetailView(DetailView):
    model = Mailing
    template_name = "mailer/mailing.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing'] = Mailing.objects.get(pk=self.object.pk)
        context_data['recipients'] = Mailing.objects.get(pk=self.object.pk).recipients.all()
        return context_data
