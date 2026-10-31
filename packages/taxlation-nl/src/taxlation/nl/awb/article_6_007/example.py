# import date module 
from datetime import date

# import atw package
from taxlation.nl import awb

# Voorbeeld los gebruik van Art_6_7: 
art6_7_voorbeeld= awb.Artikel6_7()

print("Einddatum beslistermijn:", art6_7_voorbeeld.indieningstermijn_bezwaar_beroep)