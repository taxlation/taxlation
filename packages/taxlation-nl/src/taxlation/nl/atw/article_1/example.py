from datetime import date, timedelta

from taxlation.nl import atw

atw_art_1 = atw.Artikel1(
  lid_1 = (lid_1 := atw.Artikel1().Lid1(
    wettelijke_termijn = timedelta(days=-1),
    einddatum_wettelijke_termijn = date(2021,9,25)
  )),
  lid_2 = atw.Artikel1().Lid2(
    lid_1 = lid_1
  )
)

print("Verlenging van termijn", atw_art_1.lid_1.verlenging_wettelijke_termijn)
print("Ongedaan maken van verlenging van termijn", atw_art_1.lid_2.vorige_lid_geldt_niet)