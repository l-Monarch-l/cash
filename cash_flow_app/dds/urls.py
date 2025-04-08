from django.urls import path
from .views import (
    EntryListView, EntryCreateView, EntryUpdateView, EntryDeleteView,
    StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView,
    OperationTypeListView, OperationTypeCreateView, OperationTypeUpdateView, OperationTypeDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    SubcategoryListView, SubcategoryCreateView, SubcategoryUpdateView, SubcategoryDeleteView,
    categories_by_type, subcategories_by_category
)

urlpatterns = [
    # Основные URL для записей ДДС
    path('', EntryListView.as_view(), name='entry-list'),
    path('create/', EntryCreateView.as_view(), name='entry-create'),
    path('<int:pk>/update/', EntryUpdateView.as_view(), name='entry-update'),
    path('<int:pk>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
    
    # API
    path('api/categories/', categories_by_type, name='categories-by-type'),
    path('api/subcategories/', subcategories_by_category, name='subcategories-by-category'),
    
    # URL для статусов
    path('reference/status/', StatusListView.as_view(), name='status-list'),
    path('reference/status/create/', StatusCreateView.as_view(), name='status-create'),
    path('reference/status/<int:pk>/update/', StatusUpdateView.as_view(), name='status-update'),
    path('reference/status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status-delete'),
    
    # URL для типов операций
    path('reference/operation-type/', OperationTypeListView.as_view(), name='operation-type-list'),
    path('reference/operation-type/create/', OperationTypeCreateView.as_view(), name='operation-type-create'),
    path('reference/operation-type/<int:pk>/update/', OperationTypeUpdateView.as_view(), name='operation-type-update'),
    path('reference/operation-type/<int:pk>/delete/', OperationTypeDeleteView.as_view(), name='operation-type-delete'),
    
    # URL для категорий
    path('reference/category/', CategoryListView.as_view(), name='category-list'),
    path('reference/category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('reference/category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('reference/category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    
    # URL для подкатегорий
    path('reference/subcategory/', SubcategoryListView.as_view(), name='subcategory-list'),
    path('reference/subcategory/create/', SubcategoryCreateView.as_view(), name='subcategory-create'),
    path('reference/subcategory/<int:pk>/update/', SubcategoryUpdateView.as_view(), name='subcategory-update'),
    path('reference/subcategory/<int:pk>/delete/', SubcategoryDeleteView.as_view(), name='subcategory-delete'),
]