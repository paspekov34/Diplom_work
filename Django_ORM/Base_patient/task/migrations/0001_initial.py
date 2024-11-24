# Generated by Django 5.1.3 on 2024-11-15 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('problem_description', models.TextField()),
                ('last_name', models.CharField(max_length=70)),
                ('age_limited', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время покупки')),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ManyToManyField(related_name='patients', to='task.patient')),
            ],
        ),
    ]