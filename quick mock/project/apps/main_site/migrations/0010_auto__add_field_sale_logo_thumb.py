# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sale.logo_thumb'
        db.add_column(u'main_site_sale', 'logo_thumb',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sale.logo_thumb'
        db.delete_column(u'main_site_sale', 'logo_thumb')


    models = {
        u'main_site.datapoint': {
            'Meta': {'object_name': 'DataPoint'},
            'buddy_ratio': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_active_users': ('django.db.models.fields.IntegerField', [], {}),
            'num_attended_one_event': ('django.db.models.fields.IntegerField', [], {}),
            'num_authenticated': ('django.db.models.fields.IntegerField', [], {}),
            'num_buddies': ('django.db.models.fields.IntegerField', [], {}),
            'num_buddy_requests': ('django.db.models.fields.IntegerField', [], {}),
            'num_filled_in_profile': ('django.db.models.fields.IntegerField', [], {}),
            'num_hit_home_page': ('django.db.models.fields.IntegerField', [], {}),
            'num_total_users': ('django.db.models.fields.IntegerField', [], {}),
            'num_with_one_buddy': ('django.db.models.fields.IntegerField', [], {}),
            'num_with_one_class': ('django.db.models.fields.IntegerField', [], {}),
            'recorded_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 23, 0, 0)'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main_site.milestone': {
            'Meta': {'ordering': "('recorded_at',)", 'object_name': 'Milestone'},
            'after_pic_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'after_pic_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'after_pic_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'after_pic_thumb_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'after_pic_thumb_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'after_pic_thumb_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'before_pic_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'before_pic_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'before_pic_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'before_pic_thumb_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'before_pic_thumb_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'before_pic_thumb_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recorded_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 23, 0, 0)'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main_site.sale': {
            'Meta': {'object_name': 'Sale'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo_thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recorded_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 23, 0, 0)'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main_site']