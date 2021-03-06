# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-17 02:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transaction', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='transactioncontract',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Contract'),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transactioncontract',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='transaction_payment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transaction.TransactionContract'),
        ),
    ]
