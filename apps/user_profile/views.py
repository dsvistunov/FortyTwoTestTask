from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'

    def __init__(self, **kwargs):
        super(IndexView, self).__init__(**kwargs)
        self.data = {
            "first_name": "Denis",
            "last_name": "Svistunov",
            "date_birth": "1991-04-19",
            "bio": "Lorem ipsum dolor sit amet.",
            "email": "d.svistunov1991@gmail.com",
            "jabber": "d.svistunov@42cc.co",
            "skype": "d.svistunov",
            "other_contacts": "+380632028013"
        }

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['data'] = self.data
        return context
