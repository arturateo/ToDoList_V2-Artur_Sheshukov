from django.views.generic import TemplateView


class PageNotFound(TemplateView):
    template_name = 'error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error'] = 'Такой страницы не существует'
        print(context)
        return context
