from django.urls import path
from mailer.views import MailingsListView, MailingCreateView, MailingDetailView, MailingUpdateView, MailingDeleteView

app_name = 'mailer'

urlpatterns = [
    path('', MailingsListView.as_view(), name='mailings_list'),
    path('mailing/create', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/<int:pk>/update', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete', MailingDeleteView.as_view(), name='mailing_delete'),
]
