from django.urls import path
from mailer.views import MailingsListView, MailingDetailView

app_name = 'mailer'

urlpatterns = [
    path('', MailingsListView.as_view(), name='mailings_list'),
    path('mailing/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
]
