# Generated by Django 2.2.4 on 2020-09-21 20:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('economy', '0003_auto_20200630_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='TXUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('body', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('processed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]