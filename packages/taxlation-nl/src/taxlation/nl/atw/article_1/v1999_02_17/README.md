# atw - artikel 1

## Classes
### Artikel1
Slechts container.

#### Lid1
**Fields**
- _wettelijke_termijn_: een in een wet gestelde termijn (timedelta).
- _einddatum_wettelijke_termijn_: einddatum van een in de wet gestelde termijn (date).

**Properties**
- _verlenging_wettelijke_termijn_: verlenging van een in de wet gestelde termijn die op een zaterdag, zondag of algemeen erkende feestdag eindigt tot en met de eerstvolgende dag die niet een zaterdag, zondag of algemeen erkende feestdag is (timedelta).

**Methods**
- _einddatum_verlengde_wettelijke_termijn_: berekent de einddatum van een in de wet gestelde termijn met inachtneming van eventuele verlenging (date).

#### Lid2
**Fields**
- _lid_1_: dataclass Lid1 (dataclass).

**Properties**
- _vorige_lid_geldt_niet_: stelt vast of het vorige lid niet geldt (Result).