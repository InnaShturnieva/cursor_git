# Generated by Django 3.2.5 on 2021-08-09 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренди',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(choices=[('straight', 'Straight engine'), ('inline', 'Inline Engine'), ('flat', 'Flat Engine'), ('v', 'V Engine')], default='straight', max_length=50)),
                ('pollutant_class', models.CharField(choices=[('a+', 'A+'), ('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G')], default='a+', max_length=2)),
                ('price', models.PositiveIntegerField(default=0)),
                ('fuel_type', models.CharField(choices=[('gasoline', 'Gasoline'), ('diesel', 'Diesel'), ('gas', 'Gas'), ('electricity', 'Electricity')], default='gasoline', max_length=30)),
                ('status', models.CharField(choices=[('pending', 'Pending Car Sell'), ('publish', 'Published'), ('sold', 'Sold'), ('archived', 'Archived')], default='pending', max_length=25)),
                ('doors', models.PositiveIntegerField(default=4)),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=3)),
                ('gear_case', models.CharField(choices=[('manual transmission', 'Manual Transmission'), ('automatic transmission', 'Automatic Transmission')], default='manual transmission', max_length=255)),
                ('number', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=100)),
                ('sitting_place', models.PositiveIntegerField(default=5)),
                ('first_registration_date', models.DateTimeField(auto_now_add=True)),
                ('engine_power', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машини',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Колір',
                'verbose_name_plural': 'Кольори',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('metadata', models.TextField(blank=True, null=True)),
                ('url', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
            options={
                'verbose_name': 'Зображення',
                'verbose_name_plural': 'Зображення',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('passanger', 'Passanger car'), ('truck', 'Truck'), ('bus', 'Bus')], default='passanger', max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.brand')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Моделі',
            },
        ),
        migrations.CreateModel(
            name='CarProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.property')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.color'),
        ),
        migrations.AddField(
            model_name='car',
            name='dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.dealer'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.model'),
        ),
    ]
