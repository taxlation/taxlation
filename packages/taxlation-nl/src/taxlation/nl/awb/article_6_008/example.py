# import date package
from datetime import date

# import awb package
from taxlation.nl import awb

# Voorbeeld los gebruik van Art_6_8: 
art6_8_voorbeeld= awb.Artikel6_8().Lid1(datum_bekendmaking_besluit= date(2023,11,3))

print("Einddatum beslistermijn:", art6_8_voorbeeld.datum_aanvang_indieningstermijn)