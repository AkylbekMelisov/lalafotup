# Generated by Django 3.1.6 on 2021-02-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210219_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ruralgovernment',
            name='image',
            field=models.ImageField(blank=True, default='rural_default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ruralgovernment',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='village',
            name='image',
            field=models.ImageField(blank=True, default='defaultvillage.jpg', null=True, upload_to=''),
        ),
    ]
