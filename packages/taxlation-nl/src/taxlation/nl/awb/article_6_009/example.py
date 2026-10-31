# import date package
from datetime import date

# import awb package
from taxlation.nl import awb

# voorbeeld gebruik Artikel6_9
art6_9_lid1_voorbeeld= awb.Artikel6_9().Lid1(
  einddatum_indieningstermijn= date(2026,10,31),
  ontvangstdatum_bezwaar_beroepschrift= date(2026,10,31)
  )

print(art6_9_lid1_voorbeeld.bezwaar_beroepschrift_tijdig)

art6_9_lid2_voorbeeld= awb.Artikel6_9().Lid2(
  einddatum_indieningstermijn= date(2026,10,31),
  ontvangstdatum_bezwaar_beroepschrift= date(2026,11,7),
  verzending_per_post = True,
  datum_terpostbezorging_bezwaar_beroepschrift = date(2026,10,31),
  )

print(art6_9_lid2_voorbeeld.bezwaar_beroepschrift_tijdig)