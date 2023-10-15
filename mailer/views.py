from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mailer.models import *
from mailer.forms import MailingForm


class MailingsListView(ListView):
    model = Mailing
    template_name = "mailer/mailings.html"
    context_object_name = 'mailings'
    queryset = Mailing.objects.all()


class MailingCreateView(CreateView, LoginRequiredMixin):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailer/mailing_create.html'
    success_url = reverse_lazy("mailer:mailings_list")

    def form_valid(self, form):
        new_mailing = form.save()
        new_mailing.owner = self.request.user
        new_mailing.save()
        return super().form_valid(form)


class MailingDetailView(DetailView):
    model = Mailing
    template_name = "mailer/mailing.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing'] = Mailing.objects.get(pk=self.object.pk)
        context_data['recipients'] = Mailing.objects.get(pk=self.object.pk).recipients.all()
        if self.request.user == self.object.owner:
            context_data['authorised'] = True
        else:
            context_data['authorised'] = False
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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user_groups = [group.name for group in self.request.user.groups.all()]
        if self.object.owner == self.request.user or 'Managers' in user_groups:
            return self.object
        raise Http404


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailer:mailings_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user_groups = [group.name for group in self.request.user.groups.all()]
        if self.object.owner == self.request.user or 'Managers' in user_groups:
            return self.object
        raise Http404
