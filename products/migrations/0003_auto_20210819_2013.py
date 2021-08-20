# Generated by Django 3.2.6 on 2021-08-19 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210819_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'SubCategoria'},
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
            preserve_default=False,
        ),
    ]
