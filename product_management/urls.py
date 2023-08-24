from django.urls import *
from .views import *

app_name = 'product_management'

urlpatterns = [
    path('product', ProductView.as_view()),
    path('brand', BrandView.as_view()),
    path('category', CategoryView.as_view()),
    path('subcategory', SubCategoryView.as_view()),
]
