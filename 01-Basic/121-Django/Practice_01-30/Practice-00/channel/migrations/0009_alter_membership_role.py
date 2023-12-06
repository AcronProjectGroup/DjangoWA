# Generated by Django 4.2.2 on 2023-08-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0008_membership_share_alter_membership_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='role',
            field=models.CharField(choices=[('owner', 'Owner'), ('admin', 'Admin'), ('normal', 'Normal'), ('vip', 'Vip')], default='normal', max_length=10),
        ),
    ]
