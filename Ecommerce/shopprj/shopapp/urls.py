from django.urls import path
from shopapp import views


app_name='shopapp'

urlpatterns = [
    path('',views.AllProductCat, name='AllProductCat'),
    path('slug/<slug:c_slug>/', views.AllProductCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.Prodetails, name='Prodetails'),

]
