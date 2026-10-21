# atw - artikel 4

## Classes

### Artikel4
**Fields**
- _onderdeel_a: dataclass OnderdeelA (dataclass).

**Property**
- _wet_geldt_niet_: bepaalt of de Algemene termijnenwet niet van toepassing is (Result).

#### OnderdeelA
**Fields**
- _wettelijke_termijn_: een in een wet gestelde termijn (timedelta).
- _einddatum_wettelijke_termijn_: einddatum van een in de wet gestelde termijn (date).
- _omschrijving_wettelijke_termijn_: de enkelvoudige omschrijving van de in een wet gestelde termijn (str = [uur, dag, week, maand, jaar]).

**Properties**
- _uitgezonderde_termijn_omschrijving_: geeft aan wanneer de termijn is omschreven in uren, in meer dan 90 dagen, in meer dan twaalf weken, in meer dan drie maanden, of in een of meer jaren, of de termijn betreft de bekendmaking, inwerkingtreding of buitenwerkingtreding van wettellijke voorschriften, of de termijn betreft de termijn van vrijheidsbeneming.
