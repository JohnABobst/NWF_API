# Generated by Django 2.1.5 on 2019-01-30 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MagicCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_submitted', models.IntegerField()),
                ('chosen', models.BooleanField(default=False)),
                ('card_name', models.CharField(max_length=1000)),
                ('submitted', models.BooleanField(default=False)),
                ('card_color', models.CharField(max_length=15)),
                ('card_type', models.CharField(max_length=256)),
                ('converted_mana_cost', models.CharField(max_length=240)),
                ('card_text', models.TextField()),
                ('flavor_text', models.TextField()),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='game.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]