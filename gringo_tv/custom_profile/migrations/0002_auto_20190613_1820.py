# Generated by Django 2.2.1 on 2019-06-13 21:20

import json
from django.db import migrations
from django.conf import settings
from django.contrib.auth import get_user_model

from gringo_tv.dealer.models import Dealer
from gringo_tv.custom_profile.models import Profile

User = get_user_model()

def create_profiles(apps, schema_editor):

    json_file = json.loads(open('{}/backup/edipo.json'.format(settings.BASE_DIR), 'r').read())

    dealer = Dealer.objects.filter(user__username=json_file[0].get('dealer'))
    if dealer.exists():
        dealer = dealer.first()
    else:
        user = User.objects.create(
            username=json_file[0].get('dealer'),
            password='trocar@123'
        )
        dealer = Dealer.objects.create(user=user, phone='999999999')

    for profile in json_file:
        user,_ = User.objects.get_or_create(
            username=profile.get('username'),
            first_name=profile.get('first_name'),
            last_name=profile.get('last_name'),
            password=profile.get('password')
        )
        Profile.objects.get_or_create(
            user=user,
            dealer=dealer,
            phone=profile.get('phone')
        )


class Migration(migrations.Migration):

    dependencies = [
        ('custom_profile', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_profiles)
    ]