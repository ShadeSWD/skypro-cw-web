from django.views.generic import ListView
from blog.models import *
from mailer.models import *


class HomeListView(ListView):
    template_name = "home/home.html"
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['random_3'] = Post.objects.order_by('?')[:3]
        context_data['mailings_total'] = Mailing.objects.all().count()
        context_data['mailings_active'] = Mailing.objects.filter(mailing_status=1).count()
        context_data['unique_clients'] = Client.objects.all().count()
        return context_data
