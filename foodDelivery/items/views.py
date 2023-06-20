from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'items/detail.html', {
        'item' : item
    })

@login_required
def order(request, pk):
    item = get_object_or_404(Item, pk=pk)
    buyer = request.user
    seller = item.created_by
    order = Order(item=item, seller=seller, buyer=buyer)
    order.save()
    messages.success(request, 'Your food is now in preparation. Please patiently wait.')
    return redirect('/')

def view_order(request):
    orders_made = Order.objects.filter(buyer=request.user)[0:6]
    return render(request, 'items/order.html', {
        'orders_made': orders_made,
    })