import datetime
import socket
from django.core.management.base import BaseCommand, CommandError
from client_repo import models

def _to_bool(s):
    if s in ('ja', 'Ja', 'JA', 'jA'):
        return True
    return False


def _to_date_or_none(datum):
    try:
        return datetime.strptime(datum, "%d.%m.%Y")
    except:
        return None


def _to_kauftyp(kauftyp):
    if kauftyp == "Kauf":
        return "k"
    elif kauftyp == "Miete":
        return "m"
    elif kauftyp == "Leasing":
        return "l"
    return "k"


def _to_systembewertung(systembewertung):
    if systembewertung == "Klein":
        return 'k'
    elif systembewertung == "Mittel":
        return "m"
    elif systembewertung == "Hoch":
        return "h"
    return "m"


def _to_ip(ip):
    if not ip:
        return None
    try:
        ip = ip.strip().split(" ")[0].strip()
        ip = socket.inet_ntoa(socket.inet_aton(ip))
        return ip
    except (socket.error, TypeError):
        return None



class Command(BaseCommand):
    args = ''
    help = 'Converts old Inventar table to Django structure'

    def handle(self, *args, **options):
        models.Stockwerk.objects.all().delete()
        models.Standort.objects.all().delete()
        models.Abteilung.objects.all().delete()
        models.Haus.objects.all().delete()
        models.Geraetetyp.objects.all().delete()
        models.Hersteller.objects.all().delete()
        models.Modell.objects.all().delete()
        models.Lieferant.objects.all().delete()
        models.Os.objects.all().delete()
        models.Warranty.objects.all().delete()
        models.User.objects.all().delete()
        models.VirtuelleUmgebung.objects.all().delete()
        models.Host.objects.all().delete()
        for li in models.LegacyInventar.objects.all():
            if not li.stockwerk:
                li.stockwerk="N/A"
            if not li.standort:
                li.standort="N/A"
            if not li.haus:
                li.haus="N/A"
            if not li.abteilung:
                li.abteilung="N/A"
            if not li.geraetetyp:
                li.geraetetyp="N/A"
            if not li.hersteller:
                li.hersteller="N/A"
            if not li.modell:
                li.modell="N/A"
            if not li.lieferant:
                li.lieferant="N/A"
            if not li.os_install:
                li.os_install="N/A"
            if not li.os_kauf:
                li.os_kauf="N/A"
            if not li.warranty:
                li.warranty="N/A"
            if not li.empfaenger:
                li.empfaenger="N/A"
            stockwerk, created = models.Stockwerk.objects.get_or_create(name=li.stockwerk.strip())
            stockwerk.save()
            standort, created = models.Standort.objects.get_or_create(name=li.standort.strip())
            standort.save()
            haus, created = models.Haus.objects.get_or_create(standort=standort, name=li.haus.strip())
            haus.save()
            abteilung, created = models.Abteilung.objects.get_or_create(name=li.abteilung.strip())
            abteilung.save()
            geraetetyp, created = models.Geraetetyp.objects.get_or_create(name=li.geraetetyp.strip())
            geraetetyp.save()
            hersteller, created = models.Hersteller.objects.get_or_create(name=li.hersteller.strip())
            hersteller.save()
            modell, created = models.Modell.objects.get_or_create(name=li.modell.strip(),hersteller=hersteller)
            modell.save()
            lieferant, created = models.Lieferant.objects.get_or_create(name=li.lieferant.strip())
            lieferant.save()
            os_install, created = models.Os.objects.get_or_create(name=li.os_install.strip())
            os_install.save()
            os_kauf, created = models.Os.objects.get_or_create(name=li.os_kauf.strip())
            os_kauf.save()
            warranty, created = models.Warranty.objects.get_or_create(name=li.warranty.strip(), monate=0)
            warranty.save()
            user, created = models.User.objects.get_or_create(username=li.empfaenger.strip(), firstname="TODO", lastname="TODO")
            user.save()
            virtuelle_umgebung = None
            if li.virtuelle_umgebung:
                virtuelle_umgebung, created = models.VirtuelleUmgebung.objects.get_or_create(name=li.virtuelle_umgebung.strip())
                virtuelle_umgebung.save()
            host = models.Host()
            host.lfd_nr = li.lfd_nr
            host.haus = haus
            host.stockwerk = stockwerk
            host.raum_nr = li.raum_nr
            host.abteilung = abteilung
            host.typ = geraetetyp
            host.hostname = li.hostname
            if virtuelle_umgebung:
                host.physikalisch = False
                host.virtuelle_umgebung = virtuelle_umgebung
            else:
                host.physikalisch = True
            host.ip = _to_ip(li.ip)
            host.mac = li.mac
            host.inaktive_macs = li.inaktive_macs
            host.dhcp = _to_bool(li.dhcp)
            host.dhcp_reserviert = _to_bool(li.dhcp_reserviert)
            host.wlan_hw = _to_bool(li.wlan_hw)
            host.wlan_ip = _to_ip(li.wlan_ip)
            host.datensicherung = _to_bool(li.datensicherung)
            host.systemimage = _to_bool(li.systemimage)
            host.bestellnummer = li.bestell_nr
            host.modell = modell
            host.sn = li.sn
            host.lieferant = lieferant
            host.lieferdatum = _to_date_or_none(li.lieferdatum)
            host.installationsdatum = _to_date_or_none(li.lieferdatum)
            host.lieferschein_nr = li.lieferschein_nr
            host.rechnungsnummer = li.rechnungsnummer
            host.rechnungsdatum = _to_date_or_none(li.rechnungsdatum)
            host.kauftyp = _to_kauftyp(li.kauftyp)
            host.garantie = warranty
            host.os_oem = os_kauf
            host.os_installiert = os_install
            host.medgv = _to_bool(li.medgv)
            host.systembewertung = _to_systembewertung(li.systembewertung)
            host.inventar_nr = li.inventar_nr
            host.kostenstelle = li.kostenstelle
            host.verschrottungsdatum = _to_date_or_none(li.verschrottungsdatum)
            host.notizen = li.notizen
            host.clean()
            host.save()
            host.users.add(user)
            host.save()
            self.stdout.write('Parsed {}\n'.format(li.lfd_nr))