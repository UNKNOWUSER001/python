# Generated by Django 4.2.1 on 2023-05-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'หมวดหมู่สินค้า', 'verbose_name_plural': 'ข้อมูลประเภทสินค้า'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'สินค้า', 'verbose_name_plural': 'ข้อมูลสินค้า'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/'),
        ),
    ]
