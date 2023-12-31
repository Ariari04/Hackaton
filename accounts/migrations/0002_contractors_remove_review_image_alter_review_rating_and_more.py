# Generated by Django 4.2.1 on 2023-06-16 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('status', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Streets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_title', models.CharField(max_length=100)),
                ('importance', models.BooleanField(default=False)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.contractors')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_complains', models.PositiveSmallIntegerField(default=0)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.review')),
            ],
        ),
    ]
