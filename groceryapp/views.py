from django.shortcuts import render,redirect
from .models import Carousel,Category,Product
from django.contrib.auth import authenticate, login
from .models import Category

from django.contrib import messages
# Create your views here.



def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'navigation.html')

def about(request):
    return render(request, 'about.html')

def main(request):
    data = Carousel.objects.all()
    dic={'data':data}
    return render(request, 'index.html',dic)








def adminLogin(request):
    # msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            if user.is_staff:
                login(request, user)
                # msg = "User login successfully"
                messages.success(request, "Login successfully")
                return redirect('admindashboard')
            else:
                messages.success(request, "Invalid Credentials")
        except:
              messages.success(request, "Invalid Credentials")
    # dic = {'msg': msg}
    return render(request, 'admin_login.html')







def adminHome(request):
    return render(request, 'admin_base.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def add_category(request):
    if request.method == "POST":
        name = request.POST['name']
        Category.objects.create(name=name)
        messages.success(request, "Category added")
        return redirect('view-category')
    return render(request, 'add_category.html', locals())


def view_category(request):
    category = Category.objects.all()
    return render(request, 'view_category.html', locals())





def edit_category(request, pid):
    category = Category.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        category.name = name
        category.save()
        messages.success(request, "Category Updated")
        return redirect('view-category')
    return render(request, 'edit_category.html', locals())



def delete_category(request, pid):
    category = Category.objects.get(id=pid)
    category.delete()
    messages.success(request, "Category Deleted")
    return redirect('view-category')




# For Product

def add_product(request):
    category = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        cat = request.POST['category']
        discount = request.POST['discount']
        desc = request.POST['desc']
        image = request.FILES['image']
        catobj = Category.objects.get(id=cat)
        Product.objects.create(name=name, price=price, discount=discount, category=catobj, description=desc, image=image)
        messages.success(request, "Product added")
    return render(request, 'add_product.html', locals())



def view_product(request):
    product = Product.objects.all()
    return render(request, 'view_product.html', locals())






def edit_product(request, pid):
    product = Product.objects.get(id=pid)
    category = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        cat = request.POST['category']
        discount = request.POST['discount']
        desc = request.POST['desc']
        try:
            image = request.FILES['image']
            product.image = image
            product.save()
        except:
            pass
        catobj = Category.objects.get(id=cat)
        Product.objects.filter(id=pid).update(name=name, price=price, discount=discount, category=catobj, description=desc)
        messages.success(request, "Product Updated")
    return render(request, 'edit_product.html', locals())



def delete_product(request, pid):
    product = Product.objects.get(id=pid)
    product.delete()
    messages.success(request, "Product Deleted")
    return redirect('view-product')