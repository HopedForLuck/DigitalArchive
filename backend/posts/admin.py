from django.contrib import admin

from .models import (
    Post, Comment, Tag,
    Continent, Region, Country, Area, City,
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "author",
        "description",
        "country",
    )
    search_fields = (
        "name",
        "year",
        "tags",
    )
    list_filter = (
        "author",
        "tags",
        "continent",
        "region",
        "country",
        "area",
        "city",
        "year",
    )
    filter_horizontal = ("tags",)
    list_display_links = ("name",)

    admin.site.empty_value_display = "Не задано"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "post",
        "author",
        "text",
    )
    search_fields = (
        "text",
    )
    list_filter = ("post",)
    list_display_links = ("text",)

    admin.site.empty_value_display = "Не задано"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = ("name",)
    list_display_links = ("name",)

    admin.site.empty_value_display = "Не задано"


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = ("name",)
    list_display_links = ("name",)

    admin.site.empty_value_display = "Не задано"


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = ("name",)
    list_display_links = ("name",)

    admin.site.empty_value_display = "Не задано"


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = ("name",)
    list_display_links = ("name",)

    admin.site.empty_value_display = "Не задано"


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = ("name",)
    list_display_links = ("name",)

    admin.site.empty_value_display = "Не задано"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = ("name",)
    list_display_links = ("name",)

    admin.site.empty_value_display = "Не задано"
