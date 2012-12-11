# -*- coding: utf-8 -*-
from django.db import models
from django.forms import model_to_dict
from concurrency.fields import IntegerVersionField
from django.db.models import Max

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
    version = IntegerVersionField()
    name = models.CharField(max_length=16, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="Stockwerke"


class Standort(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="Standorte"

class Haus(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=32)
    standort = models.ForeignKey(Standort)

    def __unicode__(self):
        return "{} - {}".format(self.standort, self.name)

    class Meta:
        verbose_name_plural=u"Häuser"

class Abteilung(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name
    class Meta(object):
        verbose_name="Abteilung"
        verbose_name_plural="Abteilungen"


class Geraetetyp(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name=u"Gerätetyp"
        verbose_name_plural=u"Gerätetypen"

class Hersteller(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name="Hersteller"
        verbose_name_plural="Hersteller"

class Modell(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=64, unique=True)
    hersteller = models.ForeignKey(Hersteller)

    def __unicode__(self):
        return "{} - {}".format(self.hersteller, self.name)

    class Meta:
        verbose_name_plural="Modelle"

class Lieferant(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="Lieferanten"


class Os(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name="Betriebssystem"
        verbose_name_plural="Betriebssysteme"


class Warranty(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=64, unique=True)
    monate = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name="Garantie"
        verbose_name_plural="Garantien"


class User(models.Model):
    version = IntegerVersionField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    phone = models.CharField(max_length=8, blank=True)
    mobile = models.CharField(max_length=8, blank=True)
    username = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return u"{} ({}, {})".format(self.username, self.lastname, self.firstname)

    def host_list(self):
        return u", ".join(self.hosts.all())

    class Meta:
        verbose_name="Benutzer"
        verbose_name_plural="Benutzer"

class VirtuelleUmgebung(models.Model):
    version = IntegerVersionField()
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name="Virtuelle Umgebung"
        verbose_name_plural="Virtuelle Umgebungen"

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

def default_host_lfd_nr():
    return (Host.objects.all().aggregate(Max('lfd_nr'))['lfd_nr__max'] or 0) + 1


class Host(models.Model):
    version = IntegerVersionField()
    lfd_nr = models.IntegerField("Laufende Nummer", help_text=u"Hilfetext für das Lfd Nr Feld", unique=True, default=default_host_lfd_nr)
    haus = models.ForeignKey(Haus, blank=True, null=True)
    stockwerk = models.ForeignKey(Stockwerk)
    raum_nr = models.CharField("Raumnummer", max_length=32, blank=True, null=True)
    abteilung = models.ForeignKey(Abteilung)
    typ = models.ForeignKey(Geraetetyp)
    hostname = models.CharField("Hostname", max_length=255, blank=True, null=True)
    physikalisch = models.BooleanField("Physikalisch", default=True)
    virtuelle_umgebung = models.ForeignKey(VirtuelleUmgebung, verbose_name="Virtuelle Umgebung", blank=True, null=True)
    ip = models.TextField("IPs", blank=True, null=True)
    mac = models.TextField("MACs", blank=True, null=True)
    inaktive_macs = models.CharField(max_length=255, blank=True, null=True)
    dhcp = models.BooleanField("DHCP", default=True)
    dhcp_reserviert = models.BooleanField("DHCP reserviert", default=False)
    wlan_hw = models.BooleanField("WLAN Hardware", default=False)
    wlan_ip = models.IPAddressField("WLAN IP", blank=True, null=True)
    datensicherung = models.BooleanField("Datensicherung", default=False)
    systemimage = models.BooleanField("Systemimage", default=False)
    bestellnummer = models.CharField("Bestellnummer", max_length=64, blank=True, null=True)
    modell = models.ForeignKey(Modell, blank=True, null=True)
    sn = models.CharField("S/N", max_length=64, blank=True, null=True)
    lieferant = models.ForeignKey(Lieferant, blank=True, null=True)
    lieferdatum = models.DateField("Lieferdatum", blank=True, null=True)
    installationsdatum = models.DateField("Installationsdatum", blank=True, null=True)
    lieferschein_nr = models.CharField("Lieferscheinr.", max_length=32, blank=True, null=True)
    rechnungsnummer = models.CharField("Rechnungsnr.", max_length=64, blank=True, null=True)
    rechnungsdatum = models.DateField("Rechnungsdatum", blank=True, null=True)
    kauftyp = models.CharField("Kauftyp", max_length=1, choices=KAUFTYP_CHOICES, blank=True)
    garantie = models.ForeignKey(Warranty, verbose_name="Garantie", blank=True, null=True)
    os_oem = models.ForeignKey(Os, verbose_name="Betriebssytem OEM", help_text="Mitgeliefertes Betriebssystem", blank=True, null=True, related_name="oem_hosts")
    os_installiert = models.ForeignKey(Os, verbose_name="Betriebssystem installiert", blank=True, null=True, related_name="instlliert_hosts")
    medgv = models.BooleanField("MedGV", default=False)
    systembewertung = models.CharField("Systembewertung", max_length=1, choices=SYSTEMBEWERTUNG_CHOICES, blank=True)
    inventar_nr = models.CharField("Inventarnummer", max_length=32, blank=True, null=True)
    kostenstelle = models.CharField("Kostenstelle", max_length=32, blank=True, null=True)
    verschrottungsdatum = models.DateField("Verschrottungsdatum", blank=True, null=True)
    notizen = models.TextField("Notizen", blank=True, null=True)
    users = models.ManyToManyField(User, verbose_name="Benutzer", blank=True, null=True, related_name="hosts")

    def __unicode__(self):
        return u"{}: {}".format(self.lfd_nr, self.hostname)

    def get_dict(self):
        return model_to_dict(self)

    def get_dict_first(self):
        d = self.get_dict()
        l = len(d)/2
        return dict(d.items()[:l])

    def get_dict_second(self):
        d = self.get_dict()
        l = len(d)/2
        return dict(d.items()[l:])

    class Meta(object):
        ordering=('lfd_nr',)
        verbose_name="Host"
        verbose_name_plural="Hosts"
