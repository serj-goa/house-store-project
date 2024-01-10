# Generated by Django 3.0 on 2024-01-10 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0003_auto_20240109_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
