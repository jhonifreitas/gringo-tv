# Generated by Django 2.2.1 on 2019-06-04 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indication',
            options={'ordering': ['-status'], 'verbose_name': 'Indicação', 'verbose_name_plural': 'Indicações'},
        ),
    ]