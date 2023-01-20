from django.urls import path
# from .views import homePageView
from .views import HomePageView, AboutPageView

urlpatterns = [
    # path('', homePageView, name='hello-home')
    path('', HomePageView.as_view(), name='hello-home'),
    path('about/', AboutPageView.as_view(), name='hello-about'),
]