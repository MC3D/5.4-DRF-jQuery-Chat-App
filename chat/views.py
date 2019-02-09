# from django.http import HttpResponse
#
#
# def index():
#     return HttpResponse('Hello Chat App!')

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs):

        context = {
            'greeting': 'Hello',
            'name': 'World'
        }

        return context
