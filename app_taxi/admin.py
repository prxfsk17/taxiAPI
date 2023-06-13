from django.contrib import admin

from app_taxi.models import Address
from app_taxi.models import User
from app_taxi.models import Tag


class AddressInline(admin.TabularInline):
    model = Address


@admin.register(User)
class ContactModelAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
    ]


@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    ...


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    ...
