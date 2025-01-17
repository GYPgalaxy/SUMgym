# Generated by Django 3.1.4 on 2021-01-01 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tel', models.IntegerField()),
                ('gender', models.CharField(choices=[('男', 'Man'), ('女', 'Woman'), ('未知', 'Unkown')], default='未知', max_length=4)),
                ('birthday', models.DateField()),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tel', models.IntegerField()),
                ('gender', models.CharField(choices=[('男', 'Man'), ('女', 'Woman'), ('未知', 'Unkown')], default='未知', max_length=4)),
                ('birthday', models.DateField()),
                ('regtime', models.DateField()),
                ('isvip', models.BooleanField()),
                ('vipstart', models.DateTimeField()),
                ('vipend', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PhyTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('muscle', models.FloatField()),
                ('fat', models.FloatField()),
                ('water', models.FloatField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.coach')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.user')),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('isavailable', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.user')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('maxnum', models.IntegerField()),
                ('info', models.TextField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.coach')),
            ],
        ),
    ]
