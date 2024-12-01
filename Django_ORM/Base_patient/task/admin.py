from django.contrib import admin
from .models import Patient, Product, Product2


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """
        Настройка отображения модели Patient в Django admin.

        Attributes:
            list_display (tuple): Поля, отображаемые в списке пациентов.
            search_fields (tuple): Поля, по которым можно осуществлять поиск.
            list_filter (tuple): Поля, по которым можно осуществлять фильтрацию.
            fields (list):  Группировка полей в форме редактирования.
        """
    list_display = ('first_name', 'last_name', 'age', 'email')
    search_fields = ('last_name',)
    list_filter = ('last_name', 'age',)
    fields = [('first_name', 'last_name', 'age')]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
        Настройка отображения модели Product в Django admin.

        Attributes:
            list_display (tuple): Поля, отображаемые в списке продуктов.
            search_fields (tuple): Поля, по которым можно осуществлять поиск.
            list_filter (tuple): Поля, по которым можно осуществлять фильтрацию.
            fieldsets (tuple): Группировка полей в форме редактирования.
        """
    list_display = (
        'title',
        'cost',
        'problem_description',
        'age_limited',
        'created_at',
        'edited_at',

    )
    search_fields = ('title',)
    list_filter = ('title', 'cost', 'age_limited', 'patient__last_name')
    fieldsets = (
        ('Product Info', {
            'fields': (('title', 'cost'),)
        }),
        ('Product Description', {
            'fields': ('problem_description', ('last_name', 'age_limited'),)
        }),
    )


@admin.register(Product2)
class ProductAdmin2(admin.ModelAdmin):
    """
        Настройка отображения модели Product2 в Django admin.  Аналогична ProductAdmin.

        Attributes:
            list_display (tuple): Поля, отображаемые в списке продуктов.
            search_fields (tuple): Поля, по которым можно осуществлять поиск.
            list_filter (tuple): Поля, по которым можно осуществлять фильтрацию.
            fieldsets (tuple): Группировка полей в форме редактирования.
        """
    list_display = (
        'title',
        'cost',
        'problem_description',
        'age_limited',
        'created_at',
        'edited_at',

    )
    search_fields = ('title',)
    list_filter = ('title', 'cost', 'age_limited', 'patient__last_name')
    fieldsets = (
        ('Product Info', {
            'fields': (('title', 'cost'),)
        }),
        ('Product Description', {
            'fields': ('problem_description', ('last_name', 'age_limited'),)
        }),
    )
