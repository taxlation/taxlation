# awb - artikel 7:10

## Classes

### Artikel7_10
Slechts container en omvat dus geen properties of methods.

#### Lid1
**Properties**
- _datum_einde_bezwaartermijn_: Datum waarop de termijn voor het indienen van een bezwaarschrift is verstreken (date).
- _commissie_ingesteld_: Indien een commissie als bedoeld in artikel 7:13 is ingesteld (bool).
- _termijn_beslissing_bezwaar_: Termijn voor de beslissing op bezwaar (Result).

#### Lid2
**Properties**
- _datum_einde_bezwaartermijn_: Datum waarop de termijn voor het indienen van een bezwaarschrift is verstreken (date).
- _datum_verzoek_verzuim_: Datum waarop de indiender is verzocht een verzuim als bedoeld in artikel 6:6 Awb te herstellen (date).
- _termijn_verzoek_verzuim_: Termijn voor het herstel van het verzuim (timedelta)
- _datum_herstel_verzuim_: Datum waarop het verzuim is hersteld (date).
- _termijn_opgeschort: Nieuw te berekenen termijn van het opschorten van de beslistermijn (Result).

#### Lid3
**Properties**
- _termijn_verdagen_: Gewenste termijn van het verdagen van de beslistermijn (timedelta).
- _termijn_verdaagd_: Nieuw te berekenen maximale termijn van het verdagen van de beslistermijn (Result).

#### Lid4
**Properties**
- _onderdeel_a_: dataclass van OnderdeelA (dataclass).
- _onderdeel_b_: dataclass van OnderdeelB (dataclass).
- _onderdeel_c_: dataclass van OnderdeelC (dataclass).
- _termijn_verder_uitstel_: Gewenste termijn verder uitstel (timedelta).
- _termijn_verder_uitgesteld_: Nieuw te berekenen maximale termijn van het uitstellen van de beslistermijn (Result).

##### OnderdeelA
**Properties**
- _instemming_alle_belanghebbenden_: Of alle belanghebbende met verder uitstel instemmen (bool).

##### OnderdeelB
**Properties**
- _instemming_indiender_: Of de indiener met verder uitstel instemt (bool).
- _andere_belanghebbende_niet_geschaad_: Of andere belanghebbende dan de indiender door verder uitstel niet in hun belangen kunnen worden geschaad.

##### OnderdeelC
**Properties**
- _naleving_wettelijke_procedurevoorschriften_: Of verder uitstel nodig is in verband met de naleving van wettelijke procedurevoorschriften.
