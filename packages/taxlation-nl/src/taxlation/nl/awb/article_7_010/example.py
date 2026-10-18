# import date module 
from datetime import date, timedelta

# import atw package
from taxlation.nl import awb

# Voorbeeld los gebruik van Art_7_10: einddatum bezwaartermijn 2021-08-13 met verzoek herstel 2021-09-01
art_7_10_1_voorbeeld= awb.Artikel7_10().Lid1(
  datum_einde_bezwaartermijn= date(2021,8,13),
  commissie_ingesteld= False,
)

print(art_7_10_1_voorbeeld.termijn_beslissing_bezwaar)

art_7_10_2_voorbeeld= awb.Artikel7_10().Lid2(
  datum_einde_bezwaartermijn= date(2021,8,13),
  datum_verzoek_verzuim = date(2021,9,1),
  termijn_verzoek_verzuim = timedelta(days=2),
  datum_herstel_verzuim = date(2021,9,2)
)

print(art_7_10_2_voorbeeld.termijn_opgeschort)

art_7_10_3_voorbeeld= awb.Artikel7_10().Lid3(
  termijn_verdagen=timedelta(days=2),
)

print(art_7_10_3_voorbeeld.termijn_verdaagd)

art_7_10_4_a_voorbeeld = awb.Artikel7_10().Lid4.OnderdeelA(
  instemming_alle_belanghebbenden = False
)

print(art_7_10_4_a_voorbeeld)

art_7_10_4_b_voorbeeld = awb.Artikel7_10().Lid4.OnderdeelB(
  instemming_indiener= False,
  andere_belanghebbende_niet_geschaad = True
)

print(art_7_10_4_b_voorbeeld)

art_7_10_4_c_voorbeeld= awb.Artikel7_10().Lid4.OnderdeelC(
  naleving_wettelijke_procedurevoorschriften = False
)

print(art_7_10_4_c_voorbeeld)

art_7_10_4_voorbeeld = awb.Artikel7_10().Lid4(
  onderdeel_a = art_7_10_4_a_voorbeeld,
  onderdeel_b = art_7_10_4_b_voorbeeld,
  onderdeel_c = art_7_10_4_c_voorbeeld,
  termijn_verder_uitstel = timedelta(days=1)
)

print(art_7_10_4_voorbeeld.termijn_verder_uitgesteld)
