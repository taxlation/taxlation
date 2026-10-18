#import datackasses module
from dataclasses import dataclass
from taxlation.core.result import Result

#import datetime module
from datetime import date, timedelta

@dataclass
class Artikel6_7:  
  """
  Dataclass voor Art. 6:7 Algemene wet bestuursrecht
  """
  datum_aanvang_indieningstermijn: date  # datum waarop indieningstermijn aanvangt

  @property
  def indieningstermijn(self):
    return timedelta(weeks=6)
  
  @property
  def datum_einde_indieningstermijn(self):
    """
    Berekent de einddatum van de indieningstermijn.

    Functie telt de termijn van zes weken op bij de einddatum van de wettelijke termijn en trekt één dag af om de datum te bepalen waarop de termijn om 23:59 eindigt.

    Geeft terug:
      datetime.date: De datum waarop de indieningstermijn eindigt.
    """
    datum_einde_indieningstermijn= self.datum_aanvang_indieningstermijn + self.indieningstermijn - timedelta(days=1)
    return Result("Artikel 6:7 Awb",datum_einde_indieningstermijn , "De einddatum van de indieningstermijn.")