# Generated by Django 3.1.6 on 2021-02-17 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='RuralGovernment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('ruralgovernment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ruralgovernment')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('sub_category', models.CharField(choices=[('car', 'car'), ('trucks', 'trucks'), ('chicken', 'chicken'), ('duck', 'duck'), ('goose', 'goose'), ('turkey', 'turkey')], max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.village'),
        ),
    ]
