# Generated by Django 3.0.3 on 2020-10-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0005_auto_20201020_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
    ]
