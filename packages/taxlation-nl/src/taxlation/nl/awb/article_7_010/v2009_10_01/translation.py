#import dataclasses module
from dataclasses import dataclass

#import datetime module
from datetime import date, timedelta

from taxlation.core.result import Result

@dataclass
class Artikel7_10:
  """
  Dataclass voor artikel 7:10 Awb
  """

  @dataclass
  class Lid1:
    """
    Dataclass voor artikel 7:10 lid 1 Awb
    """
    datum_einde_bezwaartermijn: date # datum waarop de bezwaartermijn is verstreken 
    commissie_ingesteld: bool # commissie ingesteld als bedoeld in artikel 7:13

    @property
    def termijn_beslissing_bezwaar(self):
      """
      Bepaalt aan de hand van of een adviescommissie is ingesteld of de beslistermijn van zes werken of twaalf weken van toepassing is.
      
      Geeft terug:
        timedelta: De termijn van een beslissing op een bezwaar.
      """
      if (self.commissie_ingesteld):
        termijn_beslissing_bezwaar = timedelta(weeks=12)
      else:
        termijn_beslissing_bezwaar = timedelta(weeks=6)

      return Result("Artikel 7:10 lid 1 Awb", termijn_beslissing_bezwaar, "Termijn beslissing op bezwaar",)

  @dataclass
  class Lid2:
    """
    Dataclass voor artikel 7:10 lid 2 Awb
    """ 
    datum_einde_bezwaartermijn: date # datum waarop de bezwaartermijn is verstreken  
    datum_verzoek_verzuim: date = None # de dag waarop de indiener is verzocht een verzuim als bedoeld in artikel 6:6 te herstellen
    termijn_verzoek_verzuim: timedelta = timedelta(days=0) # de voor het herstel van het verzuim gestelde termijn
    datum_herstel_verzuim: date = None # de dag waarop het verzuim is hersteld

    @property
    def termijn_opgeschort(self):
      """
      Schort de beslistermijn op in geval de indiener van het bezwaarschrift wordt verzocht een verzuim als bedoeld in artikel 6:6 te herstellen en hiervoor een termijn wordt meegegeven.

      Opschorting kan niet eerder plaatsvinden dan de einddatum van de bezwaartermijn (ECLI:NL:CRVB:2016:4204). 
      
      De termijn wordt opgeschort tot de eerstvolgende dag waarop het verzuim is hersteld of de daarvoor gestelde termijn ongebruikt is verstreken.

      Geeft terug:
        timedelta: De termijn van het opschorten van de beslistermijn.
      """
      termijn_opgeschort = timedelta(days=0)

      if (self.datum_verzoek_verzuim and self.termijn_verzoek_verzuim > timedelta(days=0)):
        
        datum_einde_verzoek_verzuim = self.datum_verzoek_verzuim + self.termijn_verzoek_verzuim
        datum_start_opschorten = max(self.datum_verzoek_verzuim, self.datum_einde_bezwaartermijn)

        if (self.datum_herstel_verzuim == None):
          termijn_opgeschort = datum_einde_verzoek_verzuim - datum_start_opschorten
        else:
          termijn_opgeschort = min(self.datum_herstel_verzuim, datum_einde_verzoek_verzuim) - datum_start_opschorten

      return Result("Artikel 7:10 lid 2 Awb", termijn_opgeschort, "Termijn opschorting",)
    
  @dataclass
  class Lid3:
    """
    Dataclass voor artikel 7:10 lid 3 Awb
    """
    termijn_verdagen: timedelta = timedelta(days=0) # de termijn voor het verdagen

    @property
    def termijn_verdaagd(self):
      """
      Verdaagt de beslistermijn met ten hoogste zes weken.
      
      Geeft terug:
        timedelta: De termijn van het verdagen van de beslistermijn.
      """
      termijn_verdaagd = min(self.termijn_verdagen, timedelta(weeks=6))
      return Result("Artikel 7:10 lid 3 Awb", termijn_verdaagd, "Termijn verdaging",)

  @dataclass
  class Lid4:
    """
    Dataclass voor artikel 7:10 lid 4 Awb
    """

    @dataclass
    class OnderdeelA:
      """
      Dataclass voor artikel 7:10 lid 4 onderdeel a Awb
      """
      instemming_alle_belanghebbenden: bool = None # alle belanghebbende stemmen in met verder uitstel

    @dataclass
    class OnderdeelB:
      """
      Dataclass voor artikel 7:10 lid 4 onderdeel b Awb
      """   
      instemming_indiener: bool = None # de indiener van het bezwaarschrift stemt in met verder uitstel
      andere_belanghebbende_niet_geschaad: bool = None # andere belanghebbende worden door verder uitstel niet in hun belangen geschaad

    @dataclass
    class OnderdeelC:  
      """
      Dataclass voor artikel 7:10 lid 4 onderdeel c Awb
      """    
      naleving_wettelijke_procedurevoorschriften: bool = None # verder uitstel is nodig in verband met de nalevign van wettelijke procedurevoorschriften

    onderdeel_a: OnderdeelA
    onderdeel_b: OnderdeelB
    onderdeel_c: OnderdeelC
    termijn_verder_uitstel: timedelta = timedelta(days=0)

    @property
    def termijn_verder_uitgesteld(self):
      """
      Stelt de beslistermijn uit zodra aan de voorwaarden van onderdeel a, b of c wordt voldaan.
      
      Geeft terug:
        timedelta: Het verdere uitstel van de beslistermijn.
      """
      if (self.onderdeel_a.instemming_alle_belanghebbenden or (self.onderdeel_b.instemming_indiener and self.onderdeel_b.andere_belanghebbende_niet_geschaad) or self.onderdeel_c.naleving_wettelijke_procedurevoorschriften):
        termijn_verder_uitgesteld = self.termijn_mogelijk_verder_uitstel
      elif (self.onderdeel_a.instemming_alle_belanghebbenden is False and  (self.onderdeel_b.instemming_indiener and self.onderdeel_b.andere_belanghebbende_niet_geschaad) is False and  self.onderdeel_c.naleving_wettelijke_procedurevoorschriften is False):
        termijn_verder_uitgesteld = timedelta(days=0)
      return Result("Artikel 7:10 lid 4 Awb", termijn_verder_uitgesteld, "Termijn verder uitstel",)
