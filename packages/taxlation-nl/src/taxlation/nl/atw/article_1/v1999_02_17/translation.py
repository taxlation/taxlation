#import dataclasses module
from dataclasses import dataclass

#import datetime module
from datetime import date, timedelta

#import taxlation
from taxlation.core.result import Result
from taxlation.nl.atw.article_3 import Artikel3

@dataclass
class Artikel1: 
  """
  Dataclass voor Artikel 1 Atw
  """

  @dataclass
  class Lid1:
    """
    Dataclass voor Artikel 1 lid 1 Atw
    """
    wettelijke_termijn: timedelta # een in een wet gestelde termijn
    einddatum_wettelijke_termijn: date # einddatum van een in de wet gestelde termijn

    @property
    def verlenging_wettelijke_termijn(self) -> Result:
      """
      Past de termijn aan zodat de einddatum niet eindigt op zater-, zon- en feestdagen.

      Functie controleert of einddatum op een zater-, zon- of feestdag valt, of in de lijst met feeestdagen voorkomt. 
      Als dat zo is, wordt de termijn met één dag verlengd en wordt de functie opnieuw toegepast.
      
      Geeft terug:
        datetime.date: De eventueel verlengde termijn met inachtneming van artikel 1, lid 1, ATW.
      """

      verlenging_termijn = timedelta(days=0)

      while self.einddatum_verlengde_wettelijke_termijn(verlenging_termijn).weekday() >= 5 or self.einddatum_verlengde_wettelijke_termijn(verlenging_termijn) in Artikel3(jaar=self.einddatum_verlengde_wettelijke_termijn(verlenging_termijn).year).algemeen_erkende_feestdagen:
        verlenging_termijn += timedelta(days=1)
      
      return Result("Artikel 1 lid 1 Atw", verlenging_termijn, "Termijn verlengd tot en met de eerstvolgende dag die niet een zaterdag, zondag of algemeen erkende feestdag is.",)

    def einddatum_verlengde_wettelijke_termijn(self, verlenging_termijn) -> date:
      """
      Berekent de einddatum van de wettelijke termijn met inachtneming van verlenging van de termijn.

      Functie telt de eventuele verlenging op bij de einddatum van de wettelijke termijn.

      Geeft terug:
        datetime.date: De einddatum met inachtneming van de verlenging.
      """
      return self.einddatum_wettelijke_termijn + verlenging_termijn

  @dataclass
  class Lid2:
    """
    Dataclass voor Artikel 1 lid 1 Atw
    """
    lid_1: "Artikel1.Lid1"

    @property
    def vorige_lid_geldt_niet(self) -> Result:
      """
      Deze functie geeft aan wanneer artikel 1 lid 1 Atw ongeldig is.

      Functie controleert of termijn minder dan 0 is.
      Als dat zo is, geeft de functie aan dat het vorige lid ongeldig is.

      Geeft terug:
        bool: True als het vorige lid niet geldt.
      """

      if self.lid_1.wettelijke_termijn < timedelta(0):
        return Result("Artikel 1 lid 2 Atw", True, "Artikel 1 lid 1 geldt niet voor een termijn, bepaald door terugrekening vanaf een tijdstip of gebeurtenis.", (self.lid_1.verlenging_wettelijke_termijn,))
      else:
        return Result("Artikel 1 lid 2 Atw", False, "Artikel 1 lid 2 Atw is niet van toepassing.", (self.lid_1.verlenging_wettelijke_termijn,))
