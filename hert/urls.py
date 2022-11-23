from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('pandas',views.pandas,name='pandas')
]