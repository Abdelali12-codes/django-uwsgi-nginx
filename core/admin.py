from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from core.models import Person, Course, Grade

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

    list_display = ("last_name", "first_name", "show_average")

    def show_average(self, obj):
        from django.db.models import Avg
        result = Grade.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]
    show_average.short_description = "Average Grade"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "view_students_link")

    def view_students_link(self, obj):
        count = obj.person_set.count()
        url = (
            reverse("admin:core_person_changelist")
            + "?"
            + urlencode({"courses__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Students</a>', url, count)

    view_students_link.short_description = "Students"

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass