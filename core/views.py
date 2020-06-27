from django.views.generic import TemplateView, ListView
from django.conf import settings
import requests


class IndexView(TemplateView):
    template_name = 'index.html'


class FindView(ListView):
    template_name = 'find.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super(FindView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        finder = settings.GOOGLE_BOOKS_API_BASE \
                 + self.request.GET.get('query') \
                 + '&key=AIzaSyCYagWGmWmKSzsynWSrzSPZP3Ts9NZec4M'
        return requests.get(finder).json()
