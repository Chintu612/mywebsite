from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from .models import Customer,Product,Buy
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse 
from django.contrib.auth.models import User,auth
from django.contrib import messages
def login(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'you cannot login')
            return redirect('/login')
    else:
        return render(request,'web/login.html')        

def index_view(request):
    return render(request, "web/index.html") 
def edit_view(request):
    return render(request, "web/edit.html") 
def trans_view(request):
    return render(request, "web/trans.html") 
def editcus_view(request):
    return render(request, "web/editcustomer.html")
def search(request):
    return render( request, "web/searchbynameform.html")
def searchbyname(request):
    inp_value = request.GET.get('resultname', 'This is a default value')
    cus=Customer.objects.get(name=inp_value)
    buy=Buy.objects.filter(customer_id=cus.id)
    return render( request, 'web/searchbyname.html', {'buy':buy})  
def searchdate(request):
    return render( request, "web/searchbydateform.html")
def searchbydate(request):
    inp_value = request.GET.get('resultdate', 'This is a default value')
    buy=Buy.objects.filter(date=inp_value)
    return render( request, 'web/searchbydate.html', {'buy':buy}) 
def searchdatenameform(request):
    return render( request, "web/searchdatenameform.html")   
def searchbydatename(request):
    inp1_value = request.GET.get('resultdate', 'This is a default value')
    buy=Buy.objects.filter(date=inp1_value)
    inp2_value=request.GET.get('resultname', 'This is a default value')
    cus=Customer.objects.get(name=inp2_value)
    buy1=Buy.objects.filter(customer_id=cus.id,date=inp1_value)
    return render( request, 'web/searchbydatename.html', {'buy1':buy1})  
def editpro_view(request):
    return render(request, "web/editproduct.html")
def clist(request):
    customer=Customer.objects.all()
    return render(request, "web/customer_list1.html",{'customer':customer})
def plist(request):
    product=Product.objects.all()
    return render(request, "web/product_list1.html",{'product':product})
class ProductDetailView(DetailView): 
    # specify the model to use 
    model = Product  
class CustomerDetailView(DetailView): 
    # specify the model to use 
    model = Customer  
class createCustomer(CreateView):
    model=Customer

    fields=['name','mobile','amounttobepaid']
    success_url = '/customer/'
class CustomerList(ListView):
    model=Customer
    
class createProduct(CreateView):
    model=Product

    fields=['name','price','stockavailable','stockbought']  
    success_url = '/product/'  

class ProductList(ListView):
    model=Product

class UpdateCustomer(UpdateView):
    model=Customer
    fields=['name','mobile','amounttobepaid']
    success_url = '/edit/'
class UpdateProduct(UpdateView):
    model=Product

    fields=['name','price','stockavailable','stockbought']  
    success_url = '/edit/' 
class DeleteCustomer(DeleteView):
    model=Customer
    success_url = '/edit/'
class DeleteProduct(DeleteView):
    model=Product
    success_url = '/edit/'

class Createtrans(CreateView):
    model=Buy
    fields=['customer','product','quantity']
    success_url = '/trans/'
def logout(request):
    auth.logout(request)
    return redirect("/")
def update(request):
    return render(request,'web/update.html')
