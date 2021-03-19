from django.urls import re_path
from django.conf.urls import url

from .views import (
    Home
)

app_name = 'main'
urlpatterns = [
    re_path(
        '^$',
        Home.as_view(),
        name='home'
    )
]
