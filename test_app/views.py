from datetime import datetime

from random import random, randint

from django.views import View
from django.http import HttpRequest, HttpResponse

# Create your views here.


class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)

    def post(self):
        ...

class RandomNumberView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        randomnumber = randint(1, 100)

        return HttpResponse(randomnumber)

