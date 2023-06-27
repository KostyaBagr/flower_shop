from django.urls import path
from  .views import *

urlpatterns = [
    path('', plants_list, name='flower-list'),
    path('flower/<int:pk>/', plants_detail, name='flower-detail'),
    path('category/<int:cat_pk>/', show_category, name='category'),
    path('order/', create_order, name='order')

]