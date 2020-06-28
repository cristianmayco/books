from django.views.generic import ListView
from django.conf import settings
import requests


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        finder = settings.GOOGLE_BOOKS_API_BASE
        if self.request.GET.get('q') is None or self.request.GET.get('q') == '':
            finder += 'Dom Casmurro'
        else:
            finder += self.request.GET.get('q') + '&key=AIzaSyCYagWGmWmKSzsynWSrzSPZP3Ts9NZec4M'
        return requests.get(finder).json()
