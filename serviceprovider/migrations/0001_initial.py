# Generated by Django 4.0.2 on 2022-02-05 07:20

from django.db import migrations, models
import django.db.models.deletion
import serviceprovider.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('catelog', models.ImageField(upload_to=serviceprovider.utils.get_catelog_upload_to)),
                ('about', models.TextField(max_length=300)),
                ('number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('street', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=10)),
                ('post', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to=serviceprovider.utils.get_preview_upload_to)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceprovider.auditorium')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceprovider.auditorium')),
            ],
        ),
    ]