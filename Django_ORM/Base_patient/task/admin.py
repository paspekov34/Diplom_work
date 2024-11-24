from django.contrib import admin
from .models import Patient, Product, Product2


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email')
    search_fields = ('last_name', )
    list_filter = ('last_name', 'age', )
    fields = [('first_name', 'last_name', 'age')]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cost',
        'problem_description',
        'age_limited',
        'created_at',
        'edited_at',

                    )
    search_fields = ('title', )
    list_filter = ('title', 'cost', 'age_limited', 'patient__last_name')
    fieldsets = (
        ('Product Info', {
            'fields': (('title', 'cost'), )
        }),
        ('Product Description', {
            'fields': ('problem_description', ('last_name', 'age_limited'),)
        }),
    )

@admin.register(Product2)
class ProductAdmin2(admin.ModelAdmin):
    list_display = (
        'title',
        'cost',
        'problem_description',
        'age_limited',
        'created_at',
        'edited_at',

                    )
    search_fields = ('title', )
    list_filter = ('title', 'cost', 'age_limited', 'patient__last_name')
    fieldsets = (
        ('Product Info', {
            'fields': (('title', 'cost'), )
        }),
        ('Product Description', {
            'fields': ('problem_description', ('last_name', 'age_limited'),)
        }),
    )