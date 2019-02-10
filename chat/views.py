from django.views.generic import TemplateView

from chat.models import Message


# class IndexView(TemplateView):
#     template_name = 'chat/index.html'
#
#     def get_context_data(self, **kwargs):
#
#         context = {
#             'greeting': 'Hello',
#             'name': 'World'
#         }
#
#         return context


# class ChatView(TemplateView):
#     template_name = 'chat/chat.html'
#
#     def get_context_data(self, **kwargs):
#
#         context = {
#             'greeting': 'Hello',
#             'name': 'Django'
#         }
#
#         return context


class ChatIndex(TemplateView):
    template_name = 'chat/chat.html'

    def get_context_data(self, **kwargs):
        messages = Message.objects.order_by('created')
        context = {'messages': messages}
        return context
