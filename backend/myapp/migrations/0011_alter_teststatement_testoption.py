# Generated by Django 4.0.4 on 2022-06-21 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_test_description_alter_test_test_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teststatement',
            name='testOption',
            field=models.BooleanField(default=False),
        ),
    ]
