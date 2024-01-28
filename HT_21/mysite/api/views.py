from django.forms import model_to_dict
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from products.models import Product, Category
from .serializers.product import ProductSerializer
from .serializers.category import CategorySerializer
from .serializers.cart import CartItemSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsLoggedIn(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CartViewSet(viewsets.ViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsLoggedIn]

    def list(self, request):
        cart = request.session.get('cart', {})
        products = Product.objects.filter(id__in=[int(k) for k in cart.keys()])
        cart_items = []
        for product in products:
            quantity = cart[str(product.id)]['quantity']
            cart_items.append({
                'product': product.id,
                'quantity': quantity,
            })
        return Response(cart_items)

    def create(self, request):
        product_id = request.data.get('product_id')
        if 'cart' not in request.session:
            request.session['cart'] = {}

        product_id = str(int(product_id))
        if product_id in request.session['cart']:
            request.session['cart'][product_id]['quantity'] += 1
        else:
            request.session['cart'][product_id] = {'quantity': 1}

        request.session.modified = True
        return Response({'status': 'product added to cart'})

    def retrieve(self, request, pk=None):
        cart = request.session.get('cart', {})
        if pk not in cart:
            return Response({'status': 'Cart item not found'}, status=404)
        product = Product.objects.get(id=int(pk))
        cart_item = {
            'product': model_to_dict(product),
            'quantity': cart[pk]['quantity'],
        }
        return Response(cart_item)

    def destroy(self, request, pk=None):
        cart = request.session.get('cart', {})
        if pk not in cart:
            return Response({'status': 'Product not found in cart'}, status=404)
        del cart[pk]
        request.session['cart'] = cart
        request.session.modified = True
        return Response({'status': 'Product removed from cart'})