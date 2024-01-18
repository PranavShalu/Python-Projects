from django.urls import path
from . import views

app_name = 'ecom_app'
urlpatterns = [
    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat, name='prods_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='proCatdetail')

]
