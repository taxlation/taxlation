from taxlation.nl import atw

art_3_voorbeeld = atw.Artikel3(
  lid_1= atw.Artikel3().Lid1(jaar=2026),
  lid_2 = atw.Artikel3().Lid2(jaar=2026),
  lid_3 = atw.Artikel3().Lid3(jaar=2026)
)

print("Algemeen erkende feestdagen volgens lid 1", art_3_voorbeeld.lid_1.algemeen_erkende_feestdagen)
print("Algemeen erkende feestdagen volgens lid 2", art_3_voorbeeld.lid_2.algemeen_erkende_feestdagen)
print("Algemeen erkende feestdagen volgens lid 3", art_3_voorbeeld.lid_3.algemeen_erkende_feestdagen)
print("Algemeen erkende feestdagen totaal", (art_3_voorbeeld.lid_1.algemeen_erkende_feestdagen.result + art_3_voorbeeld.lid_2.algemeen_erkende_feestdagen.result + art_3_voorbeeld.lid_3.algemeen_erkende_feestdagen.result))