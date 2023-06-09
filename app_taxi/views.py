from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

class MainPageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        assert request
        name = request.GET.get("name")
        msg = [
            "Hello from me",
            f"Hello {name} from me"
        ][bool(name)]

        return HttpResponse(msg)
    #
    # def post(self, request: HttpRequest, **kw) -> HttpResponse:
    #     return HttpResponse("post")




