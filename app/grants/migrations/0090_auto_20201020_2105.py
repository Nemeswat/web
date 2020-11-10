# Generated by Django 2.2.4 on 2020-10-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0089_contribution_checkout_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='admin_address',
            field=models.CharField(blank=True, default='0x0', help_text='The wallet address where subscription funds will be sent.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='grant',
            name='github_project_url',
            field=models.URLField(blank=True, help_text='Grant Github Project URL', null=True),
        ),
    ]
