from datetime import date, timedelta

from taxlation.nl import atw

art2_voorbeeld= atw.Artikel2(
  wettelijke_termijn= timedelta(hours=72),
  einddatum_wettelijke_termijn= date(2025,12,27), 
)

print("Verlenging van termijn met Art2", art2_voorbeeld.verlenging_wettelijke_termijn)
