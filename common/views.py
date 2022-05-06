from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

# Create your views here.

class WelcomeStringView(View):
    def get(self, request: HttpRequest) -> render:
        string_ = """<h1>Hello, World</h1>"""

        return HttpResponse(string_)

class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        return render(request, "common/index.html")




