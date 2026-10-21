from datetime import date, timedelta

from taxlation.nl import atw

art1_lid1_voorbeeld= atw.Artikel1().Lid1(
  wettelijke_termijn= timedelta(days=-1),
  einddatum_wettelijke_termijn= date(2021,9,25), 
)

print("Verlenging van termijn", art1_lid1_voorbeeld.verlenging_wettelijke_termijn)

art1_lid2_voorbeeld= atw.Artikel1().Lid2(
  lid_1= art1_lid1_voorbeeld
)

print("Ongedaan maken van verlenging van termijn", art1_lid2_voorbeeld.vorige_lid_geldt_niet)