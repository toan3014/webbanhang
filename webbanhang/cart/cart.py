from store.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty=str(quantity)
        
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True
    def total(self):
    # Lấy danh sách các product_id từ giỏ hàng
        product_ids = self.cart.keys()
    
    # Lấy thông tin sản phẩm từ cơ sở dữ liệu
        products = Product.objects.filter(id__in=product_ids)
    
        total = 0  # Khởi tạo tổng giá trị
        for product in products:
        # Lấy số lượng từ giỏ hàng
            quantity = self.cart.get(str(product.id), 0)  # Nếu không có sản phẩm, trả về 0
        
        # Tính tổng giá trị
            total += product.price * quantity
        
        return total

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quatities = self.cart
        return quatities
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
