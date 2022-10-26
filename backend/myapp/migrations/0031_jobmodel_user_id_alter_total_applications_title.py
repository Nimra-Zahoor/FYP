# Generated by Django 4.0.3 on 2022-10-24 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_rename_job_total_applications_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='user_id',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='total_applications',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='myapp.jobmodel'),
        ),
    ]
