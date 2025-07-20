from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import category_views
from api.views import tag_views
from api.views import product_views
from api.views import attribute_views

urlpatterns = [
    path('auth/login/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('category/all/', category_views.CategoryList),
    path('category/create/', category_views.CategoryCreate),
    path('category/update/<uuid:pk>/', category_views.CategoryUpdate),
    path('category/detail/<uuid:pk>/', category_views.CategoryDetail),
    path('category/delete/<uuid:pk>/', category_views.CategoryDelete),

    path('tag/all/', tag_views.TagList),
    path('tag/create/', tag_views.TagCreate),
    path('tag/update/<uuid:pk>/', tag_views.TagUpdate),
    path('tag/detail/<uuid:pk>/', tag_views.tagDetail),
    path('tag/delete/<uuid:pk>/', tag_views.TagDelete),

    path('product/all/', product_views.ProductList),
    path('product/create/', product_views.ProductCreate),
    path('product/update/<uuid:pk>/', product_views.ProductUpdate),
    path('product/detail/<uuid:pk>/', product_views.ProductDetail),
    path('product/delete/<uuid:pk>/', product_views.ProductDelete),

    path('attribute/all/', attribute_views.AttributeList),
    path('attribute/create/', attribute_views.AttributeCreate),
    path('attribute/update/<uuid:pk>/', attribute_views.AttributeUpdate),
    path('attribute/detail/<uuid:pk>/', attribute_views.AttributeDetail),
    path('attribute/delete/<uuid:pk>/', attribute_views.AttributeDelete),
]
