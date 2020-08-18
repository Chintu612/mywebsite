from django.contrib import admin
from django.urls import path
from web.views import createCustomer,createProduct,CustomerList,ProductList,index_view,ProductDetailView,CustomerDetailView
from web.views import UpdateCustomer,edit_view,UpdateProduct,editcus_view,editpro_view,clist,plist,DeleteCustomer,DeleteProduct,logout
from web.views import trans_view,Createtrans,search,searchbyname,searchdate,searchbydate,searchbydatename,searchdatenameform,login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view),
    path('edit/',edit_view),
    path('customer/create/',createCustomer.as_view()),
    path('customer/',CustomerList.as_view()),
    path('customer/detail/<pk>/',CustomerDetailView.as_view()),
    path('product/create/',createProduct.as_view()),
    path('product/',ProductList.as_view()),
    path('product/detail/<pk>/',ProductDetailView.as_view()),
    path('edit/customer/update/<pk>/',UpdateCustomer.as_view()),
    path('edit/product/update/<pk>/',UpdateProduct.as_view()),
    path('edit/customer/',editcus_view),
    path('edit/product/',editpro_view),
    path('edit/customer/update/',clist),
    path('edit/product/update/',plist),
    path('edit/customer/delete/<pk>/',DeleteCustomer.as_view()),
    path('edit/product/delete/<pk>/',DeleteProduct.as_view()),
    path('edit/customer/delete/',clist),
    path('edit/product/delete/',plist),
    path('trans/',trans_view), 
    path('trans/create/',Createtrans.as_view()),
    path('trans/search/',search),
    path('trans/search/name/',searchbyname),
    path('trans/searchd/',searchdate),
    path('trans/search/date/',searchbydate),
    path('trans/searchdatename/',searchdatenameform),
    path('trans/searchdatename/search/',searchbydatename),
    path('login/',login ,name='login'),
    path('logout/',logout ,name='logout'),
    
]
