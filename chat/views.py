from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs):

        context = {
            'greeting': 'Hello',
            'name': 'World'
        }

        return context


class ChatView(TemplateView):
    template_name = 'chat/chat.html'

    def get_context_data(self, **kwargs):

        context = {
            'greeting': 'Hello',
            'name': 'Django'
        }

        return context
