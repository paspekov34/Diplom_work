# Generated by Django 5.1.3 on 2024-11-16 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_remove_product_last_name_alter_patient_mail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='first_name',
        ),
    ]
