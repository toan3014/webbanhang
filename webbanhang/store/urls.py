
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name="home"),
    path('checkout/',views.checkout,name="checkout"),
    path('about/',views.about,name="about"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/', views.register_user, name='register'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<str:foo>', views.category, name='category'),
    path('search/', views.search, name='search'),


    
]
