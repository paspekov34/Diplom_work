# Generated by Django 5.1.3 on 2024-11-17 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_product_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Годовое сопровождение', 'verbose_name_plural': 'Марафон похудения'},
        ),
    ]
