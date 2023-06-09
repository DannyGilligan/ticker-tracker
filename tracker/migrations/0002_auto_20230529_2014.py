# Generated by Django 3.2.19 on 2023-05-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='closing_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='date_closed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='profit_loss',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='result',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
