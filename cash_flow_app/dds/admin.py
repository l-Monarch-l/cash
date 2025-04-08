from django.contrib import admin
from .models import *

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'operation_type')
    list_filter = ('operation_type',)
    inlines = [SubcategoryInline]

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category__operation_type', 'category')

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'operation_type', 'category', 
                   'subcategory', 'amount')
    list_filter = ('status', 'operation_type', 'category', 'date')
    search_fields = ('comment', 'amount')
    date_hierarchy = 'date'