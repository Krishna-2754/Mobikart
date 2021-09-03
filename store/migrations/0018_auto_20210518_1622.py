# Generated by Django 3.0.6 on 2021-05-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_payment_zip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='name_on_card',
        ),
        migrations.AddField(
            model_name='payment',
            name='card_holder',
            field=models.CharField(default='', editable=False, max_length=40),
        ),
    ]