from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('status-list')

class OperationType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('operation-type-list')

class Category(models.Model):
    name = models.CharField(max_length=100)
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('name', 'operation_type')
    
    def __str__(self):
        return f"{self.name}"
    
    def clean(self):
        if not self.operation_type:
            raise ValidationError("Категория должна быть привязана к типу операции")
    
    def get_absolute_url(self):
        return reverse('category-list')

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('name', 'category')
    
    def __str__(self):
        return f"{self.name}"
    def clean(self):
        if not self.category:
            raise ValidationError("Подкатегория должна быть привязана к категории")
        if self.category and self.pk:
            if Subcategory.objects.filter(
                name=self.name, 
                category__operation_type=self.category.operation_type
            ).exclude(pk=self.pk).exists():
                raise ValidationError("Подкатегория с таким именем уже существует для этого типа операции")
    def get_absolute_url(self):
        return reverse('subcategory-list')

class Entry(models.Model):
    date = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    operation_type = models.ForeignKey(OperationType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.date} | {self.amount} | {self.subcategory}"