# Generated by Django 4.2.11 on 2024-04-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0008_alter_place_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_id',
            field=models.CharField(db_index=True, max_length=100, verbose_name='ID места'),
        ),
    ]