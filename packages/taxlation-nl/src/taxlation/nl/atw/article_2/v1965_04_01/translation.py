#import dataclasses module
from dataclasses import dataclass

#import datetime module
from datetime import date, timedelta

#import taxlation
from taxlation.core.result import Result
from taxlation.nl.atw.article_3 import Artikel3

@dataclass
class Artikel2:  
  """
  Dataclass voor Art. 2 Algemene termijnenwet
  """
  wettelijke_termijn: timedelta # een in een wet gestelde termijn
  einddatum_wettelijke_termijn: date # einddatum van een in de wet gestelde termijn

  @property
  def verlenging_wettelijke_termijn(self) -> Result:
    """
    Verlengt de termijn in geval de termijn ten minste drie dagen is maar niet bestaat uit twee werkdagen.

    Deze functie controleert of de termijn tenminste drie dagen is. 
    Als dat het geval is, wordt zo nodig de termijn zoveel verlengd dat daarin ten minste twee dagen voorkomen die niet een zaterdag, zonder of algemeen erkende feestdag zijn.
    
    Geeft terug:
     timedelta: De verlenging van de termijn.
    """

    if (self.wettelijke_termijn >= timedelta(days=3)):
      begindatum_wettelijke_termijn = self.einddatum_wettelijke_termijn - self.wettelijke_termijn 
      huidige_datum = begindatum_wettelijke_termijn + timedelta(days=1)
      werkdagen = 0

      while (huidige_datum <= self.einddatum_wettelijke_termijn):
        if huidige_datum.weekday() < 5 and huidige_datum not in Artikel3(jaar=huidige_datum.year).algemeen_erkende_feestdagen:
          werkdagen += 1
        huidige_datum += timedelta(days=1)

      verlenging_termijn = timedelta(days=0)
      while werkdagen < 2:
        verlenging_termijn += timedelta(days=1)
        einddatum_verlengde_termijn= self.einddatum_verlengde_wettelijke_termijn(verlenging_termijn)

        if einddatum_verlengde_termijn.weekday() < 5  and einddatum_verlengde_termijn not in Artikel3(jaar=einddatum_verlengde_termijn.year).algemeen_erkende_feestdagen:
          werkdagen +=1
      
      return Result("Artikel 2 Atw",verlenging_termijn, "Termijn zoveel verlengd dat daarin ten minste twee dagen voorkomen die niet een zaterdag, zondag of algmeen erkende feestdag zijn.")

  def einddatum_verlengde_wettelijke_termijn(self, verlenging_termijn) -> date:
    """
    Berekent de einddatum van de wettelijke termijn met inachtneming van verlenging van de termijn.

    Functie telt de eventuele verlenging op bij de einddatum van de wettelijke termijn.

    Geeft terug:
      date: De einddatum met inachtneming van de verlenging.
    """
    return self.einddatum_wettelijke_termijn + verlenging_termijn