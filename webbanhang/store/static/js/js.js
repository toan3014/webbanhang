$(document).on('click', '.add-cart-btn', function(e) {
               e.preventDefault();
               
               // Lấy ID và số lượng của sản phẩm
               var productId = $(this).data('product-id');
               var productQty = $(this).closest('.product').find('.product-quantity').val(); // Lấy giá trị số lượng sản phẩm
           
               // Gửi yêu cầu AJAX
               $.ajax({
                   type: 'POST',
                   url: "{% url 'cart_add' %}",
                   data: {
                       product_id: productId,
                       product_qty: productQty,
                       csrfmiddlewaretoken: "{{ csrf_token }}",
                       action: 'post'
                   },
                   success: function(json) {
                       console.log(json); // Log kết quả phản hồi từ máy chủ để kiểm tra
                       alert("Sản phẩm đã được thêm vào giỏ hàng!"); // Thông báo thành công
                   },
                   error: function(xhr, errmsg, err) {
                       console.error("Error: " + errmsg); // Log lỗi nếu có
                       alert("Có lỗi xảy ra khi thêm sản phẩm vào giỏ hàng!"); // Thông báo lỗi
                   }
               });
           });
  var myCarousel = document.getElementById('carouselExampleAutoplaying')
  var carousel = new bootstrap.Carousel(myCarousel, {
    interval: 1000,  // Thời gian chuyển slide (ms)
    ride: 'carousel' 
  })