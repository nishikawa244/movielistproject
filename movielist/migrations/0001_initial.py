# Generated by Django 3.2 on 2023-09-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('memo', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(0, '☆☆☆☆☆'), (1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')])),
                ('date', models.DateField()),
            ],
        ),
    ]
