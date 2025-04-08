from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.db.models import ProtectedError
from django.contrib import messages
from .models import Status, OperationType, Category, Subcategory, Entry
from .forms import EntryForm

# Основные представления для записей ДДС
class EntryListView(ListView):
    model = Entry
    template_name = 'dds/entry_list.html'
    context_object_name = 'entries'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related(
            'status', 'operation_type', 'category', 'subcategory'
        )
        
        # Фильтрация
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
            
        filters = {
            'status': 'status',
            'operation_type': 'operation_type',
            'category': 'category',
            'subcategory': 'subcategory',
        }
        
        for param, field in filters.items():
            value = self.request.GET.get(param)
            if value:
                queryset = queryset.filter(**{f'{field}__id': value})
                
        return queryset.order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['operation_types'] = OperationType.objects.all()
        context['categories'] = Category.objects.all()
        return context

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'dds/entry_form.html'
    success_url = reverse_lazy('entry-list')

class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'dds/entry_form.html'
    success_url = reverse_lazy('entry-list')

class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'dds/entry_confirm_delete.html'
    success_url = reverse_lazy('entry-list')

class StatusListView(ListView):
    model = Status
    template_name = 'dds/reference_list.html'
    context_object_name = 'items'
    extra_context = {'title': 'Статусы', 'model_name': 'status'}

class StatusCreateView(CreateView):
    model = Status
    fields = ['name']
    template_name = 'dds/reference_form.html'
    success_url = reverse_lazy('status-list')
    extra_context = {'title': 'Добавление статуса'}

class StatusUpdateView(UpdateView):
    model = Status
    fields = ['name']
    template_name = 'dds/reference_form.html'
    success_url = reverse_lazy('status-list')
    extra_context = {'title': 'Редактирование статуса'}

class StatusDeleteView(DeleteView):
    model = Status
    success_url = reverse_lazy('status-list')
    template_name = 'dds/reference_confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Невозможно удалить статус, так как существуют связанные записи")
            return redirect('status-list')

class OperationTypeListView(ListView):
    model = OperationType
    template_name = 'dds/reference_list.html'
    context_object_name = 'items'
    extra_context = {'title': 'Типы операций', 'model_name': 'operation-type'}

class OperationTypeCreateView(CreateView):
    model = OperationType
    fields = ['name']
    template_name = 'dds/reference_form.html'
    success_url = reverse_lazy('operation-type-list')
    extra_context = {'title': 'Добавление типа операции'}

class OperationTypeUpdateView(UpdateView):
    model = OperationType
    fields = ['name']
    template_name = 'dds/reference_form.html'
    success_url = reverse_lazy('operation-type-list')
    extra_context = {'title': 'Редактирование типа операции'}

class OperationTypeDeleteView(DeleteView):
    model = OperationType
    success_url = reverse_lazy('operation-type-list')
    template_name = 'dds/reference_confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Невозможно удалить тип операции, так как существуют связанные категории или записи")
            return redirect('operation-type-list')

class CategoryListView(ListView):
    model = Category
    template_name = 'dds/reference_list.html'
    context_object_name = 'items'
    extra_context = {'title': 'Категории', 'model_name': 'category'}

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'operation_type']
    template_name = 'dds/category_form.html'
    success_url = reverse_lazy('category-list')
    extra_context = {'title': 'Добавление категории'}

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'operation_type']
    template_name = 'dds/category_form.html'
    success_url = reverse_lazy('category-list')
    extra_context = {'title': 'Редактирование категории'}

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
    template_name = 'dds/reference_confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Невозможно удалить категорию, так как существуют связанные подкатегории или записи")
            return redirect('category-list')

class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'dds/reference_list.html'
    context_object_name = 'items'
    extra_context = {'title': 'Подкатегории', 'model_name': 'subcategory'}

class SubcategoryCreateView(CreateView):
    model = Subcategory
    fields = ['name', 'category']
    template_name = 'dds/subcategory_form.html'
    success_url = reverse_lazy('subcategory-list')
    extra_context = {'title': 'Добавление подкатегории'}

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    fields = ['name', 'category']
    template_name = 'dds/subcategory_form.html'
    success_url = reverse_lazy('subcategory-list')
    extra_context = {'title': 'Редактирование подкатегории'}

class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    success_url = reverse_lazy('subcategory-list')
    template_name = 'dds/reference_confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Невозможно удалить подкатегорию, так как существуют связанные записи")
            return redirect('subcategory-list')

def categories_by_type(request):
    operation_type_id = request.GET.get('operation_type_id')
    categories = Category.objects.filter(operation_type_id=operation_type_id)
    data = [{'id': c.id, 'name': c.name} for c in categories]
    return JsonResponse(data, safe=False)

def subcategories_by_category(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id)
    data = [{'id': s.id, 'name': s.name} for s in subcategories]
    return JsonResponse(data, safe=False)