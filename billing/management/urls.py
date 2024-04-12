
from django.urls import path
from . import views
urlpatterns = [

    path('list', views.home,name="list_product"),
    path('add', views.productAdd,name="add_product"),
    path('edit/<int:pk>', views.productEdit,name="edit_product"),
    path('delete/<int:pk>', views.productDelete,name="delete_product"),

    
    path('bill', views.billing,name="bill"),
]
