# Generated by Django 2.2.9 on 2022-04-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_sub_category',
            field=models.CharField(choices=[('alpha', 'alpha'), ('beta', 'beta'), ('Gama', 'Gama'), ('delta', 'delta')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Furnishing', 'Furnishing'), ('Walls & Floor', 'Walls & Floor'), ('Lighting', 'Lighting')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(choices=[('Kitchen', 'Kitchen'), ('Furniture', 'Furniture'), ('Lighting', 'Lighting'), ('Carpet', 'Carpet'), ('Bath', 'Bath'), ('Wellness', 'Wellness')], default='', max_length=30),
        ),
    ]