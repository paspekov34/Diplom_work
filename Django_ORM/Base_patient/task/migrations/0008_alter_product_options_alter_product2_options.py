# Generated by Django 5.1.3 on 2024-11-30 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_remove_product_patient_product2_product_patient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Годовое сопровождение', 'verbose_name_plural': 'Годовое сопровождение'},
        ),
        migrations.AlterModelOptions(
            name='product2',
            options={'ordering': ['-created_at'], 'verbose_name': 'Марафон похудения', 'verbose_name_plural': 'Марафон похудения'},
        ),
    ]
