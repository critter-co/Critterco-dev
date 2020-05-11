# Generated by Django 3.0.5 on 2020-05-11 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_member_since'),
        ('biz', '0015_auto_20200510_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='biz',
            name='claimed_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.User'),
        ),
        migrations.AddField(
            model_name='biz',
            name='is_claimed',
            field=models.BooleanField(default=False),
        ),
    ]
