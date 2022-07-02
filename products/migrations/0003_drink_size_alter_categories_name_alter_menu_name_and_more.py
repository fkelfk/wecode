# Generated by Django 4.0.5 on 2022-07-02 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_categories_table_alter_menu_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=45)),
                ('english_name', models.CharField(max_length=45)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'drinks',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('size_ml', models.CharField(max_length=45)),
                ('size_fluid_ounce', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Nutritions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('saturated_gat_g', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('drink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.size')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('size_ml', models.CharField(max_length=45)),
                ('size_fluid_ounce', models.CharField(max_length=45)),
                ('drinks', models.ManyToManyField(related_name='allergy', to='products.drink')),
            ],
        ),
    ]
