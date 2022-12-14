# Generated by Django 4.1.2 on 2022-10-16 05:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('hired_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='default.jpg', upload_to='inventory_pics')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_type', models.TextField()),
                ('stock_level', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplier_id', models.IntegerField(primary_key=True, serialize=False)),
                ('supplier_address', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('net_terms', models.IntegerField()),
                ('date_contracted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SaleOrders',
            fields=[
                ('order_number', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('shipped_date', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontstore.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='SaleInvoices',
            fields=[
                ('invoice_number', models.IntegerField(primary_key=True, serialize=False)),
                ('discount', models.FloatField()),
                ('invoice_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontstore.customers')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontstore.employees')),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontstore.saleorders')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrders',
            fields=[
                ('po_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontstore.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseInvoices',
            fields=[
                ('purchase_number', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('purchase_date', models.DateField()),
                ('po_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontstore.purchaseorders')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontstore.suppliers')),
            ],
        ),
    ]
