from dataclasses import dataclass

from datetime import date, timedelta

from taxlation.core.result import Result

@dataclass
class Artikel6_9:
  """
  Dataclass voor artikel 6:9 Awb
  """

  @dataclass
  class Lid1:
    """
    Dataclass voor artikel 6:9 lid 1 Awb
    """

    einddatum_indieningstermijn: date # einddatum van de indieningstermijn
    ontvangstdatum_bezwaar_beroepschrift: date # ontvangstdatum bezwaar- of beroepschrift
    
    @property
    def bezwaar_beroepschrift_tijdig(self):
      """
      Geeft aan of een bezwaar- of beroepschrift tijdig is ingediend.

      Functie vergelijkt de ontvangstdatum van het bezwaar- of beroepschrift met het het einde van de indieningstermijn.

      Geeft terug:
        bool: of het een bezwaar- of beroepschrift tijdig is ingediend.
      """

      if self.ontvangstdatum_bezwaar_beroepschrift <= self.einddatum_indieningstermijn:
        return Result("Artikel 6:9 lid 1 Awb", True, "Bezwaar- of beroepschrift is tijdig ingediend.")
      else:
        return Result("Artikel 6:9 lid 2 Awb", False, "Bezwaar- of beroepschrift is niet tijdig ingediend.")

  @dataclass
  class Lid2:
    """
    Dataclass voor artikel 6:9 lid 2 Awb
    """
    einddatum_indieningstermijn: date # einddatum van de indieningstermijn
    ontvangstdatum_bezwaar_beroepschrift: date # ontvangstdatum bezwaar- of beroepschrift
    verzending_per_post: bool # indien bezwaar- of beroepschrift per post is verzonden
    datum_terpostbezorging_bezwaar_beroepschrift: date # datum ter post bezorgd van bezwaar- of beroepschrift

    @property
    def bezwaar_beroepschrift_tijdig(self):
      """
      Geeft aan of een bezwaar- of beroepschrift tijdig is ingediend bij verzending per post.

      Functie controleert of verzending per post heeft plaatsgevonden, vergelijkt de datum terpostbezorging met de einddatum van de indieningstermijn en vergelijkt
      
      vergelijkt de ontvangstdatum van het bezwaar- of beroepschrift met het het einde van de indieningstermijn.

      Geeft terug:
        bool: of het een bezwaar- of beroepschrift tijdig is ingediend.
      """

      if self.verzending_per_post:
        if self.datum_terpostbezorging_bezwaar_beroepschrift <= self.einddatum_indieningstermijn:
          if self.ontvangstdatum_bezwaar_beroepschrift <= (self.einddatum_indieningstermijn + timedelta(weeks=1)):
            return Result("Artikel 6:9 lid 2 Awb", True, "Bezwaar- of beroepschrift tijdig ingediend.")
          else:
            return Result("Artikel 6:9 lid 2 Awb", False, "Bezwaar- of beroepschrift niet tijdig ontvangen.")
        else:
          return Result("Artikel 6:9 lid 2 Awb", False, "Bezwaar- of beroepschrift niet tijdig verzonden.")
      else:
        return Result("Artikel 6:9 lid 2 Awb", False, "Bezwaar- of beroepschrift niet ter post bezorgd.")
        







    