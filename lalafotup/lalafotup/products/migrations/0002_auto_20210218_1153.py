# Generated by Django 3.1.6 on 2021-02-18 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.village'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='village',
            name='ruralgovernment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ruralgovernment'),
        ),
    ]
