# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Host.version'
        db.add_column('client_repo_host', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'User.version'
        db.add_column('client_repo_user', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Warranty.version'
        db.add_column('client_repo_warranty', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Standort.version'
        db.add_column('client_repo_standort', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Geraetetyp.version'
        db.add_column('client_repo_geraetetyp', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Hersteller.version'
        db.add_column('client_repo_hersteller', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Abteilung.version'
        db.add_column('client_repo_abteilung', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Modell.version'
        db.add_column('client_repo_modell', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Haus.version'
        db.add_column('client_repo_haus', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Stockwerk.version'
        db.add_column('client_repo_stockwerk', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'VirtuelleUmgebung.version'
        db.add_column('client_repo_virtuelleumgebung', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Os.version'
        db.add_column('client_repo_os', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)

        # Adding field 'Lieferant.version'
        db.add_column('client_repo_lieferant', 'version',
                      self.gf('concurrency.fields.IntegerVersionField')(default=1, name='version', db_tablespace=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Host.version'
        db.delete_column('client_repo_host', 'version')

        # Deleting field 'User.version'
        db.delete_column('client_repo_user', 'version')

        # Deleting field 'Warranty.version'
        db.delete_column('client_repo_warranty', 'version')

        # Deleting field 'Standort.version'
        db.delete_column('client_repo_standort', 'version')

        # Deleting field 'Geraetetyp.version'
        db.delete_column('client_repo_geraetetyp', 'version')

        # Deleting field 'Hersteller.version'
        db.delete_column('client_repo_hersteller', 'version')

        # Deleting field 'Abteilung.version'
        db.delete_column('client_repo_abteilung', 'version')

        # Deleting field 'Modell.version'
        db.delete_column('client_repo_modell', 'version')

        # Deleting field 'Haus.version'
        db.delete_column('client_repo_haus', 'version')

        # Deleting field 'Stockwerk.version'
        db.delete_column('client_repo_stockwerk', 'version')

        # Deleting field 'VirtuelleUmgebung.version'
        db.delete_column('client_repo_virtuelleumgebung', 'version')

        # Deleting field 'Os.version'
        db.delete_column('client_repo_os', 'version')

        # Deleting field 'Lieferant.version'
        db.delete_column('client_repo_lieferant', 'version')


    models = {
        'client_repo.abteilung': {
            'Meta': {'object_name': 'Abteilung'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.geraetetyp': {
            'Meta': {'object_name': 'Geraetetyp'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.haus': {
            'Meta': {'object_name': 'Haus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.hersteller': {
            'Meta': {'object_name': 'Hersteller'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.host': {
            'Meta': {'ordering': "('lfd_nr',)", 'object_name': 'Host'},
            'abteilung': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Abteilung']"}),
            'bestellnummer': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'datensicherung': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dhcp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dhcp_reserviert': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'garantie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Warranty']", 'null': 'True', 'blank': 'True'}),
            'haus': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Haus']", 'null': 'True', 'blank': 'True'}),
            'hersteller': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Hersteller']", 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inaktive_macs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'installationsdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'inventar_nr': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'kauftyp': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'kostenstelle': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'lfd_nr': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'lieferant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Lieferant']", 'null': 'True', 'blank': 'True'}),
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
            'rechnungsnummer': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'standort': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Standort']", 'null': 'True', 'blank': 'True'}),
            'stockwerk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Stockwerk']"}),
            'systembewertung': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'systemimage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'typ': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['client_repo.Geraetetyp']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'hosts'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['client_repo.User']"}),
            'verschrottungsdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.modell': {
            'Meta': {'object_name': 'Modell'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.os': {
            'Meta': {'object_name': 'Os'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.standort': {
            'Meta': {'object_name': 'Standort'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.stockwerk': {
            'Meta': {'object_name': 'Stockwerk'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.user': {
            'Meta': {'object_name': 'User'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.virtuelleumgebung': {
            'Meta': {'object_name': 'VirtuelleUmgebung'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        },
        'client_repo.warranty': {
            'Meta': {'object_name': 'Warranty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monate': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'version': ('concurrency.fields.IntegerVersionField', [], {'default': '1', 'name': "'version'", 'db_tablespace': "''"})
        }
    }

    complete_apps = ['client_repo']