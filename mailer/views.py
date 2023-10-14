from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from mailer.models import *
from mailer.forms import MailingForm


class MailingsListView(ListView):
    model = Mailing
    template_name = "mailer/mailings.html"
    context_object_name = 'mailings'
    queryset = Mailing.objects.all()


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailer/mailing_create.html'
    success_url = reverse_lazy("mailer:mailings_list")

    def form_valid(self, form):
        new_mailing = form.save()
        new_mailing.save()
        return super().form_valid(form)


class MailingDetailView(DetailView):
    model = Mailing
    template_name = "mailer/mailing.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing'] = Mailing.objects.get(pk=self.object.pk)
        context_data['recipients'] = Mailing.objects.get(pk=self.object.pk).recipients.all()
        return context_data


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailer/mailing_create.html'
    success_url = reverse_lazy("mailer:mailings_list")

    def form_valid(self, form):
        new_mailing = form.save()
        new_mailing.save()
        return super().form_valid(form)
