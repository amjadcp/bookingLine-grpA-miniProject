# Generated by Django 4.0.2 on 2022-02-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceprovider', '0003_book_book_email_book_book_name_book_book_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='message',
            field=models.TextField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
