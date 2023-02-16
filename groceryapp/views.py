from django.shortcuts import render,redirect
# from .models import Carousel,Category,Product,UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from .models import *
import json
from django.http import HttpResponse
from django.contrib import messages





# Create your views here.


#home
def home(request):
    return render(request, 'home.html')


#index
def index(request):
    return render(request, 'navigation.html')

#about
def about(request):
    return render(request, 'about.html')

#main
def main(request):
    data = Carousel.objects.all()
    dic={'data':data}
    return render(request, 'index.html',dic)







#adninLogin
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






#adminHome
def adminHome(request):
    return render(request, 'admin_base.html')


#admin_dashbord
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')




#add_category
def add_category(request):
    if request.method == "POST":
        name = request.POST['name']
        Category.objects.create(name=name)
        messages.success(request, "Category added")
        return redirect('view-category')
    return render(request, 'add_category.html', locals())



#view_category
def view_category(request):
    category = Category.objects.all()
    return render(request, 'view_category.html', locals())







#edit_category
def edit_category(request, pid):
    category = Category.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        category.name = name
        category.save()
        messages.success(request, "Category Updated")
        return redirect('view-category')
    return render(request, 'edit_category.html', locals())






#delete_category
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







#view_product
def view_product(request):
    product = Product.objects.all()
    return render(request, 'view_product.html', locals())







#edit_product
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






#delect_product
def delete_product(request, pid):
    product = Product.objects.get(id=pid)
    product.delete()
    messages.success(request, "Product Deleted")
    return redirect('view-product')





#registration
def registration(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        mobile = request.POST['mobile']
        image = request.FILES['image']
        user = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=password)
        UserProfile.objects.create(user=user, mobile=mobile, address=address, image=image)
        messages.success(request, "Registeration Successful")
    return render(request, 'registration.html', locals())









#userlogin
def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "User login successfully")
            return redirect('home')
        else:
            messages.success(request,"Invalid Credentials")
    return render(request, 'login.html', locals())







#profile
def profile(request):
    data = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        address = request.POST['address']
        mobile = request.POST['mobile']
        try:
            image = request.FILES['image']
            data.image = image
            data.save()
        except:
            pass
        user = User.objects.filter(id=request.user.id).update(first_name=fname, last_name=lname)
        UserProfile.objects.filter(id=data.id).update(mobile=mobile, address=address)
        messages.success(request, "Profile updated")
        return redirect('profile')
    return render(request, 'profile.html', locals())





# UserLogout
def logoutuser(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('main')







#User Change Password
def change_password(request):
    if request.method == 'POST':
        o = request.POST.get('currentpassword')
        n = request.POST.get('newpassword')
        c = request.POST.get('confirmpassword')
        user = authenticate(username=request.user.username, password=o)
        if user:
            if n == c:
                user.set_password(n)
                user.save()
                messages.success(request, "Password Changed")
                return redirect('main')
            else:
                messages.success(request, "Password not matching")
                return redirect('change-password')
        else:
            messages.success(request, "Invalid Password")
            return redirect('change-password')
    return render(request, 'change_password.html')




#user_product
def user_product(request,pid):
    if pid == 0:
        product = Product.objects.all()
    else:
        category = Category.objects.get(id=pid)
        product = Product.objects.filter(category=category)
    allcategory = Category.objects.all()
    return render(request, "user-product.html", locals())





#Product Details
def product_detail(request, pid):
    product = Product.objects.get(id=pid)
    latest_product = Product.objects.filter().exclude(id=pid).order_by('-id')[:10]
    return render(request, "product_detail.html", locals())






#add to cart
def addToCart(request, pid):
    myli = {"objects":[]}
    try:
        cart = Cart.objects.get(user=request.user)
        myli = json.loads((str(cart.product)).replace("'", '"'))
        try:
            myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) + 1
        except:
            myli['objects'].append({str(pid):1})
        cart.product = myli
        cart.save()
    except:
        myli['objects'].append({str(pid): 1})
        cart = Cart.objects.create(user=request.user, product=myli)
    return redirect('cart')






#IncreaseDecrease
def incredecre(request, pid):
    cart = Cart.objects.get(user=request.user)
    if request.GET.get('action') == "incre":
        myli = json.loads((str(cart.product)).replace("'", '"'))
        myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) + 1
    if request.GET.get('action') == "decre":
        myli = json.loads((str(cart.product)).replace("'", '"'))
        if myli['objects'][0][str(pid)] == 1:
            del myli['objects'][0][str(pid)]
        else:
            myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) - 1
    cart.product = myli
    cart.save()
    return redirect('cart')





#Cart
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        product = (cart.product).replace("'", '"')
        myli = json.loads(str(product))
        product = myli['objects'][0]
    except:
        product = []
    lengthpro = len(product)
    return render(request, 'cart.html', locals())






#deletecart
def deletecart(request, pid):
    cart = Cart.objects.get(user=request.user)
    product = (cart.product).replace("'", '"')
    myli = json.loads(str(product))
    del myli['objects'][0][str(pid)]
    cart.product = myli
    cart.save()
    messages.success(request, "Delete Successfully")
    return redirect('cart')





 #Booking
def booking(request):
    user = UserProfile.objects.get(user=request.user)
    cart = Cart.objects.get(user=request.user)
    total = 0
    productid = (cart.product).replace("'", '"')
    productid = json.loads(str(productid))
    try:
        productid = productid['objects'][0]
    except:
        messages.success(request, "Cart is empty, Please add product in cart.")
        return redirect('cart')
    for i,j in productid.items():
        product = Product.objects.get(id=i)
        total += int(j) * int(product.price)
    if request.method == "POST":
        return redirect('/payment/?total='+str(total))
    return render(request, "booking.html", locals()) 





#My Order
def myOrder(request):
    order = Booking.objects.filter(user=request.user)
    return render(request, "my-order.html", locals())




#Order Track
def user_order_track(request, pid):
    order = Booking.objects.get(id=pid)
    orderstatus = ORDERSTATUS
    return render(request, "user-order-track.html", locals())






#order Cancel
def change_order_status(request, pid):
    order = Booking.objects.get(id=pid)
    status = request.GET.get('status')
    if status:
        order.status = status
        order.save()
        messages.success(request, "Order status changed.")
    return redirect('myorder')






#UserFeedback
def user_feedback(request):
    user = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        Feedback.objects.create(user=request.user, message=request.POST['feedback'])
        messages.success(request, "Feedback sent successfully")
    return render(request, "feedback-form.html", locals())







#manageFeedback
def manage_feedback(request):
    action = request.GET.get('action', 0)
    feedback = Feedback.objects.filter(status=int(action))
    return render(request, 'manage_feedback.html', locals())





#deletefeedback
def delete_feedback(request, pid):
    feedback = Feedback.objects.get(id=pid)
    feedback.delete()
    messages.success(request, "Deleted successfully")
    return redirect('/manage-feedback/?action=1')







#
def read_feedback(request, pid):
    feedback = Feedback.objects.get(id=pid)
    feedback.status = 1
    feedback.save()
    return HttpResponse(json.dumps({'id':1, 'status':'success'}), content_type="application/json")





#payment
def payment(request):
    total = request.GET.get('total')
    cart = Cart.objects.get(user=request.user)
    if request.method == "POST":
        book = Booking.objects.create(user=request.user, product=cart.product, total=total)
        cart.product = {'objects': []}
        cart.save()
        messages.success(request, "Book Order Successfully")
        return redirect('myorder')
    return render(request, 'payment.html', locals())





#manage order
def manage_order(request):
    action = request.GET.get('action', 0)
    order = Booking.objects.filter(status=int(action))
    order_status = ORDERSTATUS[int(action)-1][1]
    if int(action) == 0:
        order = Booking.objects.filter()
        order_status = 'All'
    return render(request, 'manage_order.html', locals())




#delete order
def delete_order(request, pid):
    order = Booking.objects.get(id=pid)
    order.delete()
    messages.success(request, 'Order Deleted')
    return redirect('/manage-order/?action='+request.GET.get('action'))


