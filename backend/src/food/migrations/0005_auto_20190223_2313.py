# Generated by Django 2.1.7 on 2019-02-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20190223_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='tiltle',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='food',
            name='food_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]