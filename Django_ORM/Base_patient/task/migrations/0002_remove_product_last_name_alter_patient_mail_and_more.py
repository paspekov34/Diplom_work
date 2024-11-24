# Generated by Django 5.1.3 on 2024-11-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='patient',
            name='mail',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='patient',
            field=models.ManyToManyField(related_name='products', to='task.patient'),
        ),
    ]