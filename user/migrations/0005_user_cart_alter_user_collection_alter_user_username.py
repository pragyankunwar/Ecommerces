# Generated by Django 4.1.6 on 2024-02-10 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_image'),
        ('user', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(related_name='user_cart', to='book.book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='collection',
            field=models.ManyToManyField(related_name='user_collection', to='book.book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user42240', max_length=30),
        ),
    ]