# Generated by Django 2.2.6 on 2019-11-11 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('year_of_birth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('origin', models.TextField(default='Origin')),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('genre', models.CharField(choices=[('t', 'Thriller'), ('a', 'Adventure')], max_length=1)),
                ('release_date', models.DateField()),
                ('plot', models.TextField()),
                ('pages', models.PositiveIntegerField(help_text='in Pages')),
                ('authors', models.ManyToManyField(to='yabod.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yabod.Publisher')),
            ],
        ),
    ]
