#import datackasses module
from dataclasses import dataclass
from taxlation.core.result import Result

@dataclass
class Artikel2:  
  """
  Dataclass voor artikel 2 WBRV
  """

  @dataclass
  class Lid1:
    """
    Dataclass voor artikel 15, lid 1, WBRV
    """
    verkrijging: bool # True indien sprake is van een verkrijging.
    in_nederland_gelegen: bool # True indien sprake is van een in Nederland gelegen onroerende zaak.
    onroerende_zaken: bool # True indien sprake is van een onroerende zaken.
    rechten_onroerende_zaken_onderworpen: bool # True indien sprake is van een recht waaraan een onroerende zaak is onderworpen.

    @property
    def overdrachtsbelasting(self) -> bool:
      """
      Bepaalt of overdrachtsbelasting wordt geheven.

      Functie geeft aan of overdrachtsbelasting wordt geheven.

      Geeft terug:
        bool
      """
      if self.verkrijging and self.in_nederland_gelegen and (self.onroerende_zaken or self.rechten_onroerende_zaken_onderworpen):
        return Result("Art. 2 lid 1 WBRV", True, "Overdrachtsbelasting wordt geheven.")
      else:
        return Result("Art. 2 lid 1 WBRV", False, "Geen overdrachtsbelasting wordt geheven.")