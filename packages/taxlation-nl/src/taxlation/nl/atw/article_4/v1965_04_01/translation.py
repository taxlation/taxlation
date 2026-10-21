#import dataclasses module
from dataclasses import dataclass

#import datetime module
from datetime import date, timedelta

#import relativedelta module
from dateutil.relativedelta import relativedelta

#import taxlation
from taxlation.core.result import Result

@dataclass
class Artikel4: 
  """
  Dataclass voor Art. 4 Algemene termijnenwet
  """

  @dataclass
  class OnderdeelA:
    wettelijke_termijn: timedelta # in een wet gestelde termijn
    einddatum_wettelijke_termijn: date # einddatum van een in de wet gestelde termijn
    omschrijving_wettelijke_termijn: str # eenheid van de in een wet gestelde termijn (uur, dag, week, maand, jaar)

    @property
    def uitgezonderde_termijn_omschrijving(self) -> Result:
      """
      Onderdeel is van toepassing indien de wettelijke termijn specifiek is geformuleerd.
      
      Geeft terug:
        bool: True als onderdeel van toepassing is.
      """
      begindatum_wettelijke_termijn = self.einddatum_wettelijke_termijn - self.wettelijke_termijn
      if ((self.omschrijving_wettelijke_termijn == 'uur') or
        (self.wettelijke_termijn > timedelta(days=90) and self.omschrijving_wettelijke_termijn == 'dag') or
        (self.wettelijke_termijn > timedelta(weeks=12) and self.omschrijving_wettelijke_termijn == 'week') or
        (self.wettelijke_termijn > (begindatum_wettelijke_termijn + relativedelta(months=3) - begindatum_wettelijke_termijn) and self.omschrijving_wettelijke_termijn == 'maand') or
        (self.wettelijke_termijn >= (begindatum_wettelijke_termijn + relativedelta(year=1) - begindatum_wettelijke_termijn) and self.omschrijving_wettelijke_termijn == 'jaar')
      ):
        return Result( "Artikel 4 onderdeel a Atw", True, "Termijn omschrijving uitgezonderd voor de Algemene termijnenwet.")
      else:
        return Result("Artikel 4 onderdeel a Atw", False, "Termijn omschrijving is niet uitgezonderd voor de Algemene termijnenwet.")

  onderdeel_a: OnderdeelA = None # dataclass OnderdeelA

  @property   
  def wet_geldt_niet(self) -> Result:
    """
      Laat verlengde termijnen niet van toepassing zijn indien onderdeel a van toepassing is.

      Geeft terug:
        bool: True als wet niet geldt voor de termijn.
      """
    if (self.onderdeel_a.uitgezonderde_termijn_omschrijving.result == True):
      return Result("Artikel 4 Atw", True, "De Algemene termijnenwet geldt niet voor het termijn.", (self.onderdeel_a.uitgezonderde_termijn_omschrijving,))
    else:
      return Result("Artikel 4 Atw", False, "De Algemene termijnenwet geldt voor het termijn.", (self.onderdeel_a.uitgezonderde_termijn_omschrijving,))