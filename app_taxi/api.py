from uuid import UUID

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import View
from orjson import orjson
from pydantic import BaseModel, Extra
from app_taxi.models import User
from django.shortcuts import get_object_or_404
class UserSchema(BaseModel):
    name:str
    phone:int



class MainPageView(View):
    def get(self, request: HttpRequest, user_id: int|None = None) -> JsonResponse:
        if user_id:

            user = get_object_or_404(User, id = user_id)
            payload = {
                "id": user.id,
                "name": user.name,
                "phone": user.phone
            }
            return JsonResponse(payload)

        users: list[User] = list(User.objects.all())
        users_json = [
                {
                    "id": user.id,
                    "name": user.name,
                    "phone": user.phone
                }
                for user in users
            ]
        return JsonResponse(users_json, safe = False)

    def post(self, request : HttpRequest) -> JsonResponse:
        payload = orjson.loads(request.body)
        user=User(name=payload["name"], phone=payload["phone"])
        user.save()
        return JsonResponse(
            {
                "id": user.id,
                "name": user.name,
                "phone": user.phone
            },
            status=201
        )

    def patch(self, request : HttpRequest, user_id : int | None = None) -> JsonResponse:

        payload = orjson.loads(request.body)
        if "name" not in payload and "phone" not in payload:
            return HttpResponse("...", status=422)


        user = get_object_or_404(User, id=user_id)
        if payload.get("name"):
            user = payload["name"]
        if payload.get("phone"):
            user.phone=payload["phone"]
        user.save()
        payload = {
            "id": user.id,
            "name": user.name,
            "phone": user.phone
        }
        return JsonResponse(payload)

    def delete(self, request : HttpRequest, user_id : int | None = None) -> JsonResponse:
        User.objects.filter(id=user_id).delete()
        return JsonResponse({}, status=204)




