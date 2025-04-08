from django import forms
from .models import *

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Динамическая фильтрация категорий и подкатегорий
        if 'operation_type' in self.data:
            try:
                operation_type_id = int(self.data.get('operation_type'))
                self.fields['category'].queryset = Category.objects.filter(
                    operation_type_id=operation_type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.operation_type.category_set
            
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(
                    category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set