from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "home.html", context)
def cart(request):
    context={}
    return render(request,"cart.html", context)
def checkout(request):
    context={}
    return render(request,"checkout.html", context)
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Xác thực người dùng
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG")
            return redirect('home')  # Redirect đến trang home hoặc trang chính
        else:
            messages.error(request, "THỬ LẠI LẦN NỮA")
            return render(request, "login.html")
    else:
        return render(request, "login.html")
def logout_user(request):
    logout(request)
    messages.success(request,("BẠN ĐÃ LOGOUT THÀNH CÔNG"))
    return redirect("home")
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            # Xác thực và đăng nhập người dùng
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Bạn đã đăng ký thành công và đã đăng nhập!")
                return redirect('home')  # Chuyển hướng về trang chủ sau khi đăng ký thành công
        else:
            messages.error(request, "Có lỗi trong quá trình đăng ký. Vui lòng thử lại.")
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def product_detail(request, product_id):
    # Lấy sản phẩm theo product_id (có thể thay thế bằng pk nếu bạn muốn dùng tên pk)
    product = get_object_or_404(Product, id=product_id)
    
    # Trả về thông tin sản phẩm cho template
    return render(request, 'product_detail.html', {'product': product})
def category(request, foo):
    foo = foo.replace('-', '')  # Xóa dấu gạch ngang
    try:
        # Tìm danh mục theo tên
        category = Category.objects.get(name=foo)
        
        # Lọc các sản phẩm theo danh mục
        products = Product.objects.filter(category=category)
        
        # Render kết quả
        return render(request, "category.html", {'products': products, 'category': category})
    
    except Category.DoesNotExist:
        # Nếu không tìm thấy danh mục, hiển thị thông báo lỗi và quay lại trang chủ
        messages.error(request, "Danh mục không tồn tại.")
        return redirect('home')
def about(request):
    return render(request,"gioithieu.html")
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()  # Lấy từ khóa tìm kiếm từ form
        if searched:
            key = Product.objects.filter(name__icontains=searched)  # Tìm kiếm không phân biệt hoa/thường
        else:
            key = Product.objects.none()  # Trả về danh sách rỗng nếu không có từ khóa
        return render(request, 'search.html', {'searched': searched, 'key': key})
    return render(request, 'search.html')