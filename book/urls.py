from django.urls import path
from . import views
app_name='book'
urlpatterns=[
    path('book_entry',views.book_entry, name='book_entry'),
    path('book_post',views.book_post, name='book_post'),
    path('user_view',views.user_view, name='user_view'),
    path('user_entry',views.user_entry, name='user_entry'),
    path('user_login',views.user_login, name='user_login'),
    path('user_check/<int:current_user>/',views.user_check, name='user_check'),
    path('book_retrieve',views.book_retrieve, name='book_retrieve'),
    path('add_cart/<int:bookid>/<int:current_user>/',views.add_cart, name='add_cart'),
    path('view_cart/<int:current_user>/',views.view_cart,name='view_cart'),
    path('delete_from_cart/<int:bookid>/<int:current_user>/',views.delete_from_cart, name='delete_from_cart'),
    path('home/<int:current_user>/',views.home, name='home'),
]