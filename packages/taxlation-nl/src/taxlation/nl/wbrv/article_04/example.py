# import atw package
from taxlation.nl import wbrv

art_4_lid_1_onderdeel_a_voorbeeld= wbrv.Artikel4().Lid1.OnderdeelA(
  aandelen_rechtspersoon= True, 
  waarde_onroerende_zaken= 100, 
  waarde_onroerende_zaken_nl= 100, 
  waarde_onroerende_zaken_vve= 100,
  waarde_bezittingen= 100)

print("Onroerendezaakrechtspersoon:", art_4_lid_1_onderdeel_a_voorbeeld.onroerendezaakrechtspersoon)

art_4_lid_1_voorbeeld = wbrv.Artikel4().Lid1(
  onderdeel_a= art_4_lid_1_onderdeel_a_voorbeeld
)

print("Fictieve onroerende zaak:", art_4_lid_1_voorbeeld.fictieve_onroerende_zaken)