from django.urls import path
from . import views
app_name = 'items'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('order/<int:pk>', views.order, name='order'),
    path('view_order/', views.view_order,name='view_order')
]