# Generated by Django 5.1.3 on 2024-11-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_patient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
    ]