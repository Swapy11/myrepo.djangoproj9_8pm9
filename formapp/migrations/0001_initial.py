# Generated by Django 2.2.7 on 2019-12-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
    ]