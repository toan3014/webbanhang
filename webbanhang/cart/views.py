from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
               cart = Cart(request)
               cart_products = cart.get_prods
               quatities=cart.get_quants
               totals=cart.total()
               return render(request,"cart_summary.html",{"cart_products":cart_products,"quatities":quatities,"totals":totals})
def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == 'post':  # Sửa lỗi chính tả 'actiuon' thành 'action'
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))  # Sửa lỗi chính tả 'produc_id' thành 'product_id'
        product = get_object_or_404(Product, id=product_id)  # Sửa lỗi gọi hàm 'get_objact_or_404' thành 'get_object_or_404'
        cart.add(product=product,quantity=product_qty)
        cart_quantily=cart.__len__()
        response = JsonResponse({'qty': cart_quantily})  # Sửa chính tả 'Poduct name' thành 'Product name'
        return response
def cart_delete(request): 
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product_id)  # Gọi đúng phương thức delete với product_id
        
        response = JsonResponse({'product': product_id})  # Đảm bảo rằng JSON trả về là một dictionary hợp lệ
        return response