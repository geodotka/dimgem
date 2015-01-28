# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('icon', models.ImageField(blank=True, verbose_name='Ikonka Kategorii', upload_to='icons')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoteToPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('anon_author', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=75)),
                ('submited_date', models.DateField()),
                ('text', models.TextField(verbose_name='Treść')),
                ('is_accepted', models.BooleanField(default=None)),
                ('accept_date', models.DateField(blank=True, null=True)),
                ('refusal_reason', models.TextField(blank=True, null=True)),
                ('is_refused', models.BooleanField(default=False)),
                ('accept_superuser', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='superuser_corrected_post')),
                ('author', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='note_to_post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('posted_date', models.DateField()),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('dim', models.BooleanField(default=None)),
                ('old_text', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='post_pictures', null=True)),
                ('is_approved', models.BooleanField(default=True)),
                ('categories', models.ForeignKey(to='dimgem.Category')),
            ],
            options={
                'ordering': ['-posted_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('ip', models.IPAddressField()),
                ('vote', models.BooleanField(default=None)),
                ('post', models.ForeignKey(to='dimgem.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notetopost',
            name='post_id',
            field=models.ForeignKey(to='dimgem.Post'),
            preserve_default=True,
        ),
    ]
