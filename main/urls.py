from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import (
    get_mentor,
    list_mentors,
    create_mentor,
    get_mentee,
    create_mentee,
    list_mentees,
    change_mentor
)


schema = get_swagger_view(title="Mentor Mentee API")
urlpatterns = [
    path('mentor/{pk:str}/', get_mentor),
    path('mentors/`', list_mentors),
    path('mentor/create', create_mentor),
    path('mentee/{pk:str}', get_mentee),
    path('mentee/create', create_mentee),
    path('mentees/', list_mentees),
    path('mentee/update/', change_mentor),
    path('docs/', schema)
]