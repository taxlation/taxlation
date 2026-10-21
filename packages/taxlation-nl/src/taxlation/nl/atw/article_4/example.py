from datetime import date, timedelta

from taxlation.nl import atw

art4_lid1_voorbeeld= atw.Artikel4().OnderdeelA(
  einddatum_wettelijke_termijn= date(2025,12,24), 
  wettelijke_termijn= timedelta(days=90), 
  omschrijving_wettelijke_termijn = 'dag')

art4_voorbeeld= atw.Artikel4(onderdeel_a=art4_lid1_voorbeeld)

print("Atw is niet van toepassing dan Art4:", art4_lid1_voorbeeld.uitgezonderde_termijn_omschrijving)
print("Einddatum na eventuele verlenging:", art4_voorbeeld.wet_geldt_niet)