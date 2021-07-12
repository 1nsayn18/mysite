from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    #/food/
    path('', views.index, name='index'),
    #/food/item_id
    path('<int:item_id>', views.detail, name='detail'),
]
