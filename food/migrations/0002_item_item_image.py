# Generated by Django 3.2.5 on 2021-07-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg?compress=1&resize=400x300', max_length=500),
        ),
    ]