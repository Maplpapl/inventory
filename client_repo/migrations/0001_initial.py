# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stockwerk'
        db.create_table('client_repo_stockwerk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
        ))
        db.send_create_signal('client_repo', ['Stockwerk'])

        # Adding model 'Standort'
        db.create_table('client_repo_standort', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('client_repo', ['Standort'])

        # Adding model 'Haus'
        db.create_table('client_repo_haus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('standort', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Standort'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('client_repo', ['Haus'])

        # Adding unique constraint on 'Haus', fields ['standort', 'name']
        db.create_unique('client_repo_haus', ['standort_id', 'name'])

        # Adding model 'Abteilung'
        db.create_table('client_repo_abteilung', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('client_repo', ['Abteilung'])

        # Adding model 'Geraetetyp'
        db.create_table('client_repo_geraetetyp', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('client_repo', ['Geraetetyp'])

        # Adding model 'Hersteller'
        db.create_table('client_repo_hersteller', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('client_repo', ['Hersteller'])

        # Adding model 'Modell'
        db.create_table('client_repo_modell', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hersteller', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Hersteller'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('client_repo', ['Modell'])

        # Adding unique constraint on 'Modell', fields ['hersteller', 'name']
        db.create_unique('client_repo_modell', ['hersteller_id', 'name'])

        # Adding model 'Lieferant'
        db.create_table('client_repo_lieferant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('client_repo', ['Lieferant'])

        # Adding M2M table for field hersteller on 'Lieferant'
        db.create_table('client_repo_lieferant_hersteller', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lieferant', models.ForeignKey(orm['client_repo.lieferant'], null=False)),
            ('hersteller', models.ForeignKey(orm['client_repo.hersteller'], null=False))
        ))
        db.create_unique('client_repo_lieferant_hersteller', ['lieferant_id', 'hersteller_id'])

        # Adding model 'Os'
        db.create_table('client_repo_os', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('client_repo', ['Os'])

        # Adding model 'Warranty'
        db.create_table('client_repo_warranty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('monate', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('client_repo', ['Warranty'])

        # Adding model 'User'
        db.create_table('client_repo_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('client_repo', ['User'])

        # Adding model 'VirtuelleUmgebung'
        db.create_table('client_repo_virtuelleumgebung', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('client_repo', ['VirtuelleUmgebung'])

        # Adding model 'Host'
        db.create_table('client_repo_host', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lfd_nr', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('haus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Haus'])),
            ('stockwerk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Stockwerk'])),
            ('raum_nr', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('abteilung', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Abteilung'])),
            ('typ', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Geraetetyp'])),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('physikalisch', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('virtuelle_umgebung', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.VirtuelleUmgebung'], null=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('inaktive_macs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('dhcp', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dhcp_reserviert', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wlan_hw', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wlan_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('datensicherung', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('systemimage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bestellnummer', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('modell', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Modell'], null=True, blank=True)),
            ('sn', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('lieferant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Lieferant'])),
            ('lieferdatum', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('installationsdatum', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lieferschein_nr', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('rechnungsdatum', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('kauftyp', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('garantie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['client_repo.Warranty'], null=True, blank=True)),
            ('os_oem', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='oem_hosts', null=True, to=orm['client_repo.Os'])),
            ('os_installiert', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='instlliert_hosts', null=True, to=orm['client_repo.Os'])),
            ('medgv', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('systembewertung', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('inventar_nr', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('kostenstelle', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('verschrottungsdatum', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('notizen', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('client_repo', ['Host'])

        # Adding M2M table for field users on 'Host'
        db.create_table('client_repo_host_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('host', models.ForeignKey(orm['client_repo.host'], null=False)),
            ('user', models.ForeignKey(orm['client_repo.user'], null=False))
        ))
        db.create_unique('client_repo_host_users', ['host_id', 'user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Modell', fields ['hersteller', 'name']
        db.delete_unique('client_repo_modell', ['hersteller_id', 'name'])

        # Removing unique constraint on 'Haus', fields ['standort', 'name']
        db.delete_unique('client_repo_haus', ['standort_id', 'name'])

        # Deleting model 'LegacyInventar'
        db.delete_table(u'Inventar')

        # Deleting model 'Stockwerk'
        db.delete_table('client_repo_stockwerk')

        # Deleting model 'Standort'
        db.delete_table('client_repo_standort')

        # Deleting model 'Haus'
        db.delete_table('client_repo_haus')

        # Deleting model 'Abteilung'
        db.delete_table('client_repo_abteilung')

        # Deleting model 'Geraetetyp'
        db.delete_table('client_repo_geraetetyp')

        # Deleting model 'Hersteller'
        db.delete_table('client_repo_hersteller')

        # Deleting model 'Modell'
        db.delete_table('client_repo_modell')

        # Deleting model 'Lieferant'
        db.delete_table('client_repo_lieferant')

        # Removing M2M table for field hersteller on 'Lieferant'
        db.delete_table('client_repo_lieferant_hersteller')

        # Deleting model 'Os'
        db.delete_table('client_repo_os')

        # Deleting model 'Warranty'
        db.delete_table('client_repo_warranty')

        # Deleting model 'User'
        db.delete_table('client_repo_user')

        # Deleting model 'VirtuelleUmgebung'
        db.delete_table('client_repo_virtuelleumgebung')

        # Deleting model 'Host'
        db.delete_table('client_repo_host')

        # Removing M2M table for field users on 'Host'
        db.delete_table('client_repo_host_users')


    models = {
        'client_repo.abteilung': {
            'Meta': {'object_name': 'Abteilung'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'client_repo.geraetetyp': {
            'Meta': {'object_name': 'Geraetetyp'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'client_repo.haus': {
            'Meta': {'unique_together': "(('standort', 'name'),)", 'object_name': 'Haus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'standort': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Standort']"})
        },
        'client_repo.hersteller': {
            'Meta': {'object_name': 'Hersteller'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'client_repo.host': {
            'Meta': {'ordering': "('lfd_nr',)", 'object_name': 'Host'},
            'abteilung': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Abteilung']"}),
            'bestellnummer': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'datensicherung': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dhcp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dhcp_reserviert': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'garantie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Warranty']", 'null': 'True', 'blank': 'True'}),
            'haus': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Haus']"}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inaktive_macs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'installationsdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'inventar_nr': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'kauftyp': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'kostenstelle': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'lfd_nr': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'lieferant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Lieferant']"}),
            'lieferdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lieferschein_nr': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'medgv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modell': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Modell']", 'null': 'True', 'blank': 'True'}),
            'notizen': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_installiert': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'instlliert_hosts'", 'null': 'True', 'to': "orm['client_repo.Os']"}),
            'os_oem': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'oem_hosts'", 'null': 'True', 'to': "orm['client_repo.Os']"}),
            'physikalisch': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'raum_nr': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'rechnungsdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'stockwerk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Stockwerk']"}),
            'systembewertung': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'systemimage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'typ': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Geraetetyp']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'hosts'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['client_repo.User']"}),
            'verschrottungsdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'virtuelle_umgebung': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.VirtuelleUmgebung']", 'null': 'True', 'blank': 'True'}),
            'wlan_hw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wlan_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        'client_repo.legacyinventar': {
            'Meta': {'object_name': 'LegacyInventar', 'db_table': "u'Inventar'"},
            'abteilung': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bestell_nr': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_column': "'bestell_Nr'", 'blank': 'True'}),
            'datensicherung': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dhcp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dhcp_reserviert': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'empfaenger': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'garantie_ende': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'geraetetyp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'haus': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hersteller': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'inaktive_macs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'installationsdatum': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'inventar_nr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'kauftyp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'kostenstelle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lfd_nr': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lieferant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lieferdatum': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lieferschein_nr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'medgv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modell': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notizen': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'os_install': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'os_kauf': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'os_Kauf'", 'blank': 'True'}),
            'raum_nr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rechnungsdatum': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rechnungsnummer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sn': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'standort': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'stockwerk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'systembewertung': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'systemimage': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vergebene_berechtigung': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'verschrottungsdatum': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'virtuelle_umgebung': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vm_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'warranty': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'Warranty'", 'blank': 'True'}),
            'wlan_hw': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'wlan_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'client_repo.lieferant': {
            'Meta': {'object_name': 'Lieferant'},
            'hersteller': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['client_repo.Hersteller']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'client_repo.modell': {
            'Meta': {'unique_together': "(('hersteller', 'name'),)", 'object_name': 'Modell'},
            'hersteller': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Hersteller']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'client_repo.os': {
            'Meta': {'object_name': 'Os'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'client_repo.standort': {
            'Meta': {'object_name': 'Standort'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'client_repo.stockwerk': {
            'Meta': {'object_name': 'Stockwerk'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'})
        },
        'client_repo.user': {
            'Meta': {'object_name': 'User'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'client_repo.virtuelleumgebung': {
            'Meta': {'object_name': 'VirtuelleUmgebung'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'client_repo.warranty': {
            'Meta': {'object_name': 'Warranty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monate': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['client_repo']