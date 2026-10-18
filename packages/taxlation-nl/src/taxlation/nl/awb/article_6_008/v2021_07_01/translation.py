#import datackasses module
from dataclasses import dataclass
from taxlation.core.result import Result

#import datetime module
from datetime import date, timedelta

@dataclass
class Artikel6_8:
  """
  Dataclass voor artikel 6:8 Awb
  """

  @dataclass
  class Lid1:
    """
    Dataclass voor artikel 6:8 lid 1 Awb
    """

    datum_bekendmaking_besluit: date # de dag waarop het besluit op de voorgeschreven wijze is bekendgemaakt.

    @property
    def datum_aanvang_termijn(self):
      datum_aanvang_termijn= self.datum_bekendmaking_besluit + timedelta(days=1)
      return Result("Artikel 6:8 lid 1 Awb",datum_aanvang_termijn, "De dag waarop de termijn aanvangt.")
    

