# Generated by Django 4.2.1 on 2023-06-05 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ตะกร้าสินค้า',
                'verbose_name_plural': 'ข้อมูลตะกร้าสินค้า',
                'db_table': 'cart',
                'ordering': ('date_added',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'หมวดหมู่สินค้า',
                'verbose_name_plural': 'ข้อมูลประเภทสินค้า',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('postcode', models.CharField(blank=True, max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('token', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'ประวัติผู้ซื้อ',
                'db_table': 'Order',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_store.category')),
            ],
            options={
                'verbose_name': 'สินค้า',
                'verbose_name_plural': 'ข้อมูลสินค้า',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_store.order')),
            ],
            options={
                'verbose_name_plural': 'ประวัติการซื้อสินค้า',
                'db_table': 'OrderItem',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_store.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_store.product')),
            ],
            options={
                'verbose_name': 'รายการสินค้าในตระกร้า',
                'verbose_name_plural': 'ข้อมูลรายการสินค้าในตระกร้า',
                'db_table': 'CartItem',
            },
        ),
    ]
