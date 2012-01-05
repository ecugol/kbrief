# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AudienceType'
        db.create_table('brief_audiencetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type_of', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('brief', ['AudienceType'])

        # Adding model 'SiteAim'
        db.create_table('brief_siteaim', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('brief', ['SiteAim'])

        # Adding model 'SiteTask'
        db.create_table('brief_sitetask', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('brief', ['SiteTask'])

        # Adding model 'SiteType'
        db.create_table('brief_sitetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('brief', ['SiteType'])

        # Adding model 'SiteLanguage'
        db.create_table('brief_sitelanguage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('brief', ['SiteLanguage'])

        # Adding model 'SiteAccent'
        db.create_table('brief_siteaccent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('brief', ['SiteAccent'])

        # Adding model 'ScreenResolution'
        db.create_table('brief_screenresolution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('brief', ['ScreenResolution'])

        # Adding model 'Brief'
        db.create_table('brief_brief', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_city', self.gf('django.db.models.fields.CharField')(default=u'\u0421\u0443\u0440\u0433\u0443\u0442', max_length=100)),
            ('contact_address', self.gf('django.db.models.fields.TextField')()),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('sphere', self.gf('django.db.models.fields.TextField')()),
            ('contact_site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('contact_domain_name', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('deadline_date', self.gf('django.db.models.fields.DateField')()),
            ('deadline_info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('marketing_events', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('target_audience_other', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('products_and_services', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('advantage', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('brand', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_curves', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_logo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_logo_curves', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_characters', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_characters_curves', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_colors', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('site_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brief.SiteType'])),
            ('site_type_other', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('makeup', self.gf('django.db.models.fields.CharField')(default='fixed-center', max_length=50)),
            ('layout', self.gf('django.db.models.fields.CharField')(default='2col-left', max_length=50)),
            ('layout_other', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('brief', ['Brief'])

        # Adding M2M table for field target_audience on 'Brief'
        db.create_table('brief_brief_target_audience', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brief', models.ForeignKey(orm['brief.brief'], null=False)),
            ('audiencetype', models.ForeignKey(orm['brief.audiencetype'], null=False))
        ))
        db.create_unique('brief_brief_target_audience', ['brief_id', 'audiencetype_id'])

        # Adding M2M table for field site_aims on 'Brief'
        db.create_table('brief_brief_site_aims', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brief', models.ForeignKey(orm['brief.brief'], null=False)),
            ('siteaim', models.ForeignKey(orm['brief.siteaim'], null=False))
        ))
        db.create_unique('brief_brief_site_aims', ['brief_id', 'siteaim_id'])

        # Adding M2M table for field site_tasks on 'Brief'
        db.create_table('brief_brief_site_tasks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brief', models.ForeignKey(orm['brief.brief'], null=False)),
            ('sitetask', models.ForeignKey(orm['brief.sitetask'], null=False))
        ))
        db.create_unique('brief_brief_site_tasks', ['brief_id', 'sitetask_id'])

        # Adding M2M table for field site_languages on 'Brief'
        db.create_table('brief_brief_site_languages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brief', models.ForeignKey(orm['brief.brief'], null=False)),
            ('sitelanguage', models.ForeignKey(orm['brief.sitelanguage'], null=False))
        ))
        db.create_unique('brief_brief_site_languages', ['brief_id', 'sitelanguage_id'])

        # Adding M2M table for field site_accent on 'Brief'
        db.create_table('brief_brief_site_accent', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brief', models.ForeignKey(orm['brief.brief'], null=False)),
            ('siteaccent', models.ForeignKey(orm['brief.siteaccent'], null=False))
        ))
        db.create_unique('brief_brief_site_accent', ['brief_id', 'siteaccent_id'])

        # Adding M2M table for field screen_resolution on 'Brief'
        db.create_table('brief_brief_screen_resolution', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brief', models.ForeignKey(orm['brief.brief'], null=False)),
            ('screenresolution', models.ForeignKey(orm['brief.screenresolution'], null=False))
        ))
        db.create_unique('brief_brief_screen_resolution', ['brief_id', 'screenresolution_id'])

        # Adding model 'Competitor'
        db.create_table('brief_competitor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brief', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brief.Brief'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('brief', ['Competitor'])

        # Adding model 'Companion'
        db.create_table('brief_companion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brief', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brief.Brief'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('brief', ['Companion'])

        # Adding model 'LikedSite'
        db.create_table('brief_likedsite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brief', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brief.Brief'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('brief', ['LikedSite'])


    def backwards(self, orm):
        
        # Deleting model 'AudienceType'
        db.delete_table('brief_audiencetype')

        # Deleting model 'SiteAim'
        db.delete_table('brief_siteaim')

        # Deleting model 'SiteTask'
        db.delete_table('brief_sitetask')

        # Deleting model 'SiteType'
        db.delete_table('brief_sitetype')

        # Deleting model 'SiteLanguage'
        db.delete_table('brief_sitelanguage')

        # Deleting model 'SiteAccent'
        db.delete_table('brief_siteaccent')

        # Deleting model 'ScreenResolution'
        db.delete_table('brief_screenresolution')

        # Deleting model 'Brief'
        db.delete_table('brief_brief')

        # Removing M2M table for field target_audience on 'Brief'
        db.delete_table('brief_brief_target_audience')

        # Removing M2M table for field site_aims on 'Brief'
        db.delete_table('brief_brief_site_aims')

        # Removing M2M table for field site_tasks on 'Brief'
        db.delete_table('brief_brief_site_tasks')

        # Removing M2M table for field site_languages on 'Brief'
        db.delete_table('brief_brief_site_languages')

        # Removing M2M table for field site_accent on 'Brief'
        db.delete_table('brief_brief_site_accent')

        # Removing M2M table for field screen_resolution on 'Brief'
        db.delete_table('brief_brief_screen_resolution')

        # Deleting model 'Competitor'
        db.delete_table('brief_competitor')

        # Deleting model 'Companion'
        db.delete_table('brief_companion')

        # Deleting model 'LikedSite'
        db.delete_table('brief_likedsite')


    models = {
        'brief.audiencetype': {
            'Meta': {'object_name': 'AudienceType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_of': ('django.db.models.fields.IntegerField', [], {})
        },
        'brief.brief': {
            'Meta': {'object_name': 'Brief'},
            'advantage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'brand': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_characters': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_characters_curves': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_colors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'brand_curves': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_logo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_logo_curves': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_address': ('django.db.models.fields.TextField', [], {}),
            'contact_city': ('django.db.models.fields.CharField', [], {'default': "u'\\u0421\\u0443\\u0440\\u0433\\u0443\\u0442'", 'max_length': '100'}),
            'contact_domain_name': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'contact_site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline_date': ('django.db.models.fields.DateField', [], {}),
            'deadline_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'2col-left'", 'max_length': '50'}),
            'layout_other': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'makeup': ('django.db.models.fields.CharField', [], {'default': "'fixed-center'", 'max_length': '50'}),
            'marketing_events': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'products_and_services': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'screen_resolution': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['brief.ScreenResolution']", 'symmetrical': 'False'}),
            'site_accent': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['brief.SiteAccent']", 'symmetrical': 'False'}),
            'site_aims': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['brief.SiteAim']", 'symmetrical': 'False'}),
            'site_languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['brief.SiteLanguage']", 'symmetrical': 'False'}),
            'site_tasks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['brief.SiteTask']", 'symmetrical': 'False'}),
            'site_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brief.SiteType']"}),
            'site_type_other': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sphere': ('django.db.models.fields.TextField', [], {}),
            'target_audience': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['brief.AudienceType']", 'symmetrical': 'False'}),
            'target_audience_other': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'brief.companion': {
            'Meta': {'object_name': 'Companion'},
            'brief': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brief.Brief']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'brief.competitor': {
            'Meta': {'object_name': 'Competitor'},
            'brief': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brief.Brief']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'brief.likedsite': {
            'Meta': {'object_name': 'LikedSite'},
            'brief': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brief.Brief']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'brief.screenresolution': {
            'Meta': {'object_name': 'ScreenResolution'},
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        'brief.siteaccent': {
            'Meta': {'object_name': 'SiteAccent'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'brief.siteaim': {
            'Meta': {'object_name': 'SiteAim'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'brief.sitelanguage': {
            'Meta': {'object_name': 'SiteLanguage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'brief.sitetask': {
            'Meta': {'object_name': 'SiteTask'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'brief.sitetype': {
            'Meta': {'object_name': 'SiteType'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['brief']
