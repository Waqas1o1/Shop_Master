from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='HomePage'),
    path('product/<int:pid>',views.Product_view,name='productpage'),
    path('shop/',views.Shop_view,name='shoppage'),
    path('shopsorting/<str:shortby>',views.SortShop,name='shoppage'),
    path('filter_catagory/<str:filterby>',views.Filter_products,name='filter_ctg'),
    # Filter's
    path('filter/<str:filter_by>',views.ByPricse,name='filteredpage'),
    path('filter_bysizes/',views.BySizes,name='filtersizepage'),
    path('filter_bytags/',views.ByTags,name='filtertagspage'),
    # Comment
    path('postcomment/<int:pid>',views.Comment_handle,name='filtertagspage'),
]