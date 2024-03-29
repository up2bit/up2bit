# Generated by Django 5.0 on 2024-01-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('active', models.BooleanField(default=True)),
                ('market_cap', models.FloatField()),
                ('volume', models.FloatField()),
                ('profile', models.ImageField(null=True, upload_to='profile_coins/')),
            ],
        ),
    ]
