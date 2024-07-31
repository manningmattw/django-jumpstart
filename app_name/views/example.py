from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from app_name.models.example import Example


class ExampleView(View):
    url = ''
    template = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template, context)


class ExampleApiView(View):
    url = 'api/example'

    def _get_list(self):
        example_list = list(Example.objects.all())
        data = []

        for example in example_list:
            data.append({
                "name": example.name,
                "choice": example.choice,
                "choice_value": example.choice_value,
                "is_something": example.is_something})

        return data

    def get(self, request, *args, **kwargs):
        data = self._get_list()

        return JsonResponse(data, safe=False)
