# Generated by Django 2.1 on 2018-08-09 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("spirits", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="bottle",
            name="abv",
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        )
    ]
