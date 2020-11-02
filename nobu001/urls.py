# from django.conf.urls import url
# from .views import HelloView

# urlpatterns = [
#     url(r'', HelloView.as_view(), name='index'),
      
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
