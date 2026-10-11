#import datackasses module
from dataclasses import dataclass
from taxlation.core.result import Result

@dataclass
class Artikel1:  
  """
  Dataclass voor artikel 1, WBRV
  """
  overdrachtsbelasting: bool # overdrachtsbelasting geregeld in hoofdstuk II WBRV
  assurantiebelasting: bool # assurantiebelasting geregeld in hoofdstuk III WBRV

  @property
  def belasting_van_rechtsverkeer(self):
    """
    Bepaalt of sprake is van een belasting van rechtsverkeer.

    Functie geeft aan dat sprake is van een belasting van rechtsverkeer indien de overdrachtsbelasting of assurantiebelasting van toepassing is.

    Geeft terug:
      bool
    """
    if self.overdrachtsbelasting or self.assurantiebelasting:
      return Result("Art. 1 WBRV", True, "Belasting geheven krachten Wet op belastingen van rechtsverkeer.")
    else:
      return Result("Art. 1 WBRV", False, "Geen belasting geheven krachtens Wet op belastingen van rechtsverkeer.")