from django.urls import path
from django.conf.urls.static import static
from .views import recommand

urlpatterns = [
    path('', recommand, name='homepage'),
    ]