#import dataclasses module
from dataclasses import dataclass
from taxlation.core.result import Result

@dataclass
class Artikel4:
  """
  Class voor artikel 4 WBRV
  """

  @dataclass
  class Lid1:
    """
    Class voor artikel 4 lid 1 WBRV
    """

    @dataclass (kw_only= True)
    class OnderdeelA:  
      """
      Dataclass voor voor artikel 4 lid 1 onderdeel a WBRV
      """
      aandelen_rechtspersoon: bool # WAAR bij de aanwezigheid van aandelen in een rechtspersoon en ONWAAR indien anders
      waarde_onroerende_zaken: int # waarde in het economische verkeer van de onroerende zaken
      waarde_onroerende_zaken_nl: int # waarde in het economische verkeer van in Nederland gelegen onroerende zaken
      waarde_onroerende_zaken_vve: int # waarde in het economische verkeer van onroerende zaken dienstbaar aan verkrijgen, vervreemden of exploiteren
      waarde_bezittingen: int # waarde in het economische verkeer van alle bezittingen

      def bezitseis(self):
            if (self.waarde_onroerende_zaken / (self.waarde_bezittingen)) > 0.5 and (self.waarde_onroerende_zaken_nl / self.waarde_bezittingen) >= 0.3:
              return True
            else:
              return False
      
      def doeleis(self):
            if (self.waarde_onroerende_zaken_vve / self.waarde_onroerende_zaken) >= 0.7:
              return True
            else:
              return False

      @property
      def onroerendezaakrechtspersoon(self):
        if self.aandelen_rechtspersoon and self.bezitseis() and self.doeleis():
          return Result("Artikel 4 lid 1 onderdeel a WBRV", True, "Aangemerkt als fictieve onroerende zaak.")
        else:
          return Result("Artikel 4 lid 1 onderdeel a WBRV", False,"Niet aangemerkt als fictieve onroerende zaak.")

    onderdeel_a: OnderdeelA

    @property
    def fictieve_onroerende_zaken(self) -> Result:
      if self.onderdeel_a.onroerendezaakrechtspersoon:
         return Result("Artikel 4 lid 1 WBRV", True, "Mede aangemerkt als zaken als bedoeld in artikel 2.")
      else:
         return Result("Artikel 4 lid 1 WBRV", False, "Niet mede aangemerkt als zaken als bedoeld in artikel 2.")