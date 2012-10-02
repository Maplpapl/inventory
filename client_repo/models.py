# -*- coding: utf-8 -*-
from django.db import models

class LegacyInventar(models.Model):
    lfd_nr = models.IntegerField(primary_key=True)
    standort = models.CharField(max_length=255, blank=True)
    haus = models.CharField(max_length=255, blank=True)
    stockwerk = models.CharField(max_length=255, blank=True)
    raum_nr = models.CharField(max_length=255, blank=True)
    empfaenger = models.CharField(max_length=255, blank=True)
    abteilung = models.CharField(max_length=255, blank=True)
    telefon = models.CharField(max_length=255, blank=True)
    geraetetyp = models.CharField(max_length=255, blank=True)
    hostname = models.CharField(max_length=255, blank=True)
    virtuelle_umgebung = models.CharField(max_length=255, blank=True)
    vm_name = models.CharField(max_length=255, blank=True)
    mac = models.CharField(max_length=255, blank=True)
    inaktive_macs = models.CharField(max_length=255, blank=True)
    ip = models.CharField(max_length=255, blank=True)
    dhcp = models.CharField(max_length=255, blank=True)
    dhcp_reserviert = models.CharField(max_length=255, blank=True)
    wlan_hw = models.CharField(max_length=255, blank=True)
    wlan_ip = models.CharField(max_length=255, blank=True)
    datensicherung = models.CharField(max_length=255, blank=True)
    systemimage = models.CharField(max_length=255, blank=True)
    bestell_nr = models.CharField(max_length=32, db_column='bestell_Nr', blank=True) # Field name made lowercase.
    hersteller = models.CharField(max_length=255, blank=True)
    modell = models.CharField(max_length=255, blank=True)
    sn = models.CharField(max_length=64, blank=True)
    lieferant = models.CharField(max_length=255, blank=True)
    lieferdatum = models.CharField(max_length=255, blank=True)
    installationsdatum = models.CharField(max_length=255, blank=True)
    lieferschein_nr = models.CharField(max_length=255, blank=True)
    rechnungsnummer = models.CharField(max_length=255, blank=True)
    rechnungsdatum = models.CharField(max_length=255, blank=True)
    kauftyp = models.CharField(max_length=255, blank=True)
    warranty = models.CharField(max_length=255, db_column='Warranty', blank=True) # Field name made lowercase.
    garantie_ende = models.CharField(max_length=255, blank=True)
    os_kauf = models.CharField(max_length=255, db_column='os_Kauf', blank=True) # Field name made lowercase.
    os_install = models.CharField(max_length=255, blank=True)
    medgv = models.CharField(max_length=255, blank=True)
    systembewertung = models.CharField(max_length=255, blank=True)
    vergebene_berechtigung = models.CharField(max_length=255, blank=True)
    inventar_nr = models.CharField(max_length=255, blank=True)
    kostenstelle = models.CharField(max_length=255, blank=True)
    verschrottungsdatum = models.CharField(max_length=255, blank=True)
    notizen = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'Inventar'


class Stockwerk(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __unicode__(self):
        return self.name


class Standort(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Haus(models.Model):
    standort = models.ForeignKey(Standort)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name
    class Meta(object):
        unique_together=('standort', 'name')

class Abteilung(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name="Abteilung"
        verbose_name_plural="Abteilungen"


class Geraetetyp(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name


class Hersteller(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name


class Modell(models.Model):
    hersteller = models.ForeignKey(Hersteller)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name
    class Meta(object):
        unique_together=('hersteller', 'name')

class Lieferant(models.Model):
    name = models.CharField(max_length=64, unique=True)
    hersteller = models.ManyToManyField(Hersteller)

    def __unicode__(self):
        return self.name


class Os(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class Warranty(models.Model):
    name = models.CharField(max_length=64, unique=True)
    monate = models.IntegerField()

    def __unicode__(self):
        return self.name


class User(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    phone = models.CharField(max_length=8, blank=True)
    mobile = models.CharField(max_length=8, blank=True)
    username = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return u"{} ({}, {})".format(self.username, self.lastname, self.firstname)

    def host_list(self):
        return u", ".join(self.hosts.all())


class VirtuelleUmgebung(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

KAUFTYP_CHOICES = (
    ('k', "Kauf"),
    ('l', "Leasing"),
    ('m', 'Miete'),
    )

SYSTEMBEWERTUNG_CHOICES = (
    ('k', 'klein'),
    ('m', 'mittel'),
    ('h', 'hoch'),
    )

class Host(models.Model):
    lfd_nr = models.IntegerField(help_text=u"Hilfetext für das Lfd Nr Feld", unique=True)
    haus = models.ForeignKey(Haus)
    stockwerk = models.ForeignKey(Stockwerk)
    raum_nr = models.CharField(max_length=32, blank=True, null=True)
    abteilung = models.ForeignKey(Abteilung)
    typ = models.ForeignKey(Geraetetyp)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    physikalisch = models.BooleanField(default=True)
    virtuelle_umgebung = models.ForeignKey(VirtuelleUmgebung, blank=True, null=True)
    ip = models.IPAddressField(blank=True, null=True)
    mac = models.CharField(max_length=64, blank=True, null=True)
    inaktive_macs = models.CharField(max_length=255, blank=True, null=True)
    dhcp = models.BooleanField(default=True)
    dhcp_reserviert = models.BooleanField(default=False)
    wlan_hw = models.BooleanField(default=False)
    wlan_ip = models.IPAddressField(blank=True, null=True)
    datensicherung = models.BooleanField(default=False)
    systemimage = models.BooleanField(default=False)
    bestellnummer = models.CharField(max_length=64, blank=True, null=True)
    modell = models.ForeignKey(Modell, blank=True, null=True)
    sn = models.CharField(max_length=64, blank=True, null=True)
    lieferant = models.ForeignKey(Lieferant)
    lieferdatum = models.DateField(blank=True, null=True)
    installationsdatum = models.DateField(blank=True, null=True)
    lieferschein_nr = models.CharField(max_length=32, blank=True, null=True)
    rechnungsnummer = models.CharField(max_length=64, blank=True, null=True)
    rechnungsdatum = models.DateField(blank=True, null=True)
    kauftyp = models.CharField(max_length=1, choices=KAUFTYP_CHOICES, blank=True)
    garantie = models.ForeignKey(Warranty, blank=True, null=True)
    os_oem = models.ForeignKey(Os, blank=True, null=True, related_name="oem_hosts")
    os_installiert = models.ForeignKey(Os, blank=True, null=True, related_name="instlliert_hosts")
    medgv = models.BooleanField(default=False)
    systembewertung = models.CharField(max_length=1, choices=SYSTEMBEWERTUNG_CHOICES, blank=True)
    inventar_nr = models.CharField(max_length=32, blank=True, null=True)
    kostenstelle = models.CharField(max_length=32, blank=True, null=True)
    verschrottungsdatum = models.DateField(blank=True, null=True)
    notizen = models.TextField(blank=True, null=True)
    users = models.ManyToManyField(User, blank=True, null=True, related_name="hosts")

    def __unicode__(self):
        return u"{}: {}".format(self.lfd_nr, self.hostname)

    class Meta(object):
        ordering=('lfd_nr',)
        verbose_name="Host"
        verbose_name_plural="Hosts"