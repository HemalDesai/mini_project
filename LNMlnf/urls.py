from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.LNMlnf_home, name='LNMlnf_home'),
    path('insert_products/', views.lnfinsert_product, name='insert_product'),
    path('view_products/', views.lnfview_product, name='view_product'),
    path('delete_product/<int:id>', views.lnfdelete_product, name='delete_product'),
    # path('user_wishlist/', views.user_wishlist, name='user_wishlist'),
    # path('insert_wishlist/<int:id>', views.insert_wishlist, name='insert_wishlist'),
    # path('delete_wishlist_product/<int:id>',
        #  views.delete_wishlist_product, name='delete_wishlist_product'),
    path('update_product/', views.lnfupdate_product, name='update_product')
]
