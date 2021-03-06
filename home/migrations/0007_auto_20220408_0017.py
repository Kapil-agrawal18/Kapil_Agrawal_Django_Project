# Generated by Django 2.2.9 on 2022-04-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220408_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Walls & Floor', 'Walls & Floor'), ('Lighting', 'Lighting'), ('Furnishing', 'Furnishing')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_sub_category',
            field=models.CharField(choices=[('Gama', 'Gama'), ('beta', 'beta'), ('delta', 'delta'), ('alpha', 'alpha')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(choices=[('Lighting', 'Lighting'), ('Carpet', 'Carpet'), ('Wellness', 'Wellness'), ('Furniture', 'Furniture'), ('Kitchen', 'Kitchen'), ('Bath', 'Bath')], default='', max_length=30),
        ),
    ]
