# Generated by Django 4.0.5 on 2022-07-02 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_allergy_table_alter_image_table_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Nutritions',
            new_name='Nutrition',
        ),
    ]
