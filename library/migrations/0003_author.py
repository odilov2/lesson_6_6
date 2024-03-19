# Generated by Django 5.0.3 on 2024-03-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_customer_bookrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='library/images/')),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]