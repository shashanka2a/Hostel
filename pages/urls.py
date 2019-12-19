from django.urls import path

from .views import home_page, AboutPageView

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
