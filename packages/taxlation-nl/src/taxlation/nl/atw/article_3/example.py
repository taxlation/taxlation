from taxlation.nl import atw

art3_lid1_voorbeeld= atw.Artikel3().Lid1(jaar=2026)
art3_lid2_voorbeeld= atw.Artikel3().Lid2(jaar=2026)
art3_lid3_voorbeeld= atw.Artikel3().Lid3(jaar=2026)
art3_voorbeeld= atw.Artikel3(jaar=2025)

print("Algemeen erkende feestdagen volgens lid 1", art3_lid1_voorbeeld.algemeen_erkende_feestdagen)
print("Algemeen erkende feestdagen volgens lid 2", art3_lid2_voorbeeld.algemeen_erkende_feestdagen)
print("Algemeen erkende feestdagen volgens lid 3", art3_lid3_voorbeeld.algemeen_erkende_feestdagen)
print("Algemeen erkende feestdagen", art3_voorbeeld.algemeen_erkende_feestdagen)