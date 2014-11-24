# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('dimgem_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('dimgem', ['Category'])

        # Adding model 'Post'
        db.create_table('dimgem_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('posted_date', self.gf('django.db.models.fields.DateField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('dim', self.gf('django.db.models.fields.BooleanField')()),
            ('categories', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dimgem.Category'])),
            ('old_text', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('dimgem', ['Post'])

        # Adding model 'Vote'
        db.create_table('dimgem_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('vote', self.gf('django.db.models.fields.BooleanField')()),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dimgem.Post'])),
        ))
        db.send_create_signal('dimgem', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('dimgem_category')

        # Deleting model 'Post'
        db.delete_table('dimgem_post')

        # Deleting model 'Vote'
        db.delete_table('dimgem_vote')


    models = {
        'dimgem.category': {
            'Meta': {'object_name': 'Category'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'dimgem.post': {
            'Meta': {'object_name': 'Post', 'ordering': "['-posted_date']"},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dimgem.Category']"}),
            'dim': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_text': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'posted_date': ('django.db.models.fields.DateField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dimgem.vote': {
            'Meta': {'object_name': 'Vote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dimgem.Post']"}),
            'vote': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['dimgem']