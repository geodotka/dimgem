# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.is_approved'
        db.add_column('dimgem_post', 'is_approved',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.is_approved'
        db.delete_column('dimgem_post', 'is_approved')


    models = {
        'dimgem.category': {
            'Meta': {'object_name': 'Category'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'dimgem.post': {
            'Meta': {'ordering': "['-posted_date']", 'object_name': 'Post'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dimgem.Category']"}),
            'dim': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'old_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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