# Generated by Django 3.1 on 2020-11-17 01:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nobu001', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='friend',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-z]*$')]),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobu001.friend')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
