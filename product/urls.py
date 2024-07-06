from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('' , views.product , name = "products") ,
    path('<int:id>' , views.single_product , name = "single_product") ,
]

