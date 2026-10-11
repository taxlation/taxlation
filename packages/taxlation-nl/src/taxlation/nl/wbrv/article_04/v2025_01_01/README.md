# Art. 4 WBRV

## Classes

### Artikel4
Slechts container en omvat dus geen properties of methods.

#### Lid1
**Properties**'
_onderdeel_a_: Dataclass onderdeelA (dataclass).
_fictieve_onroerende_zaken_: Of het fictieve onroerende zaken betreft (bool).

##### OnderdeelA
**Properties**
_aandelen_rechtspersoon_: Of het aandelen in een rechtspersoon betreft (bool).
_waarde_onroerende_zaken_: De waarde van de onroerende zaken (int).
_waarde_onroerende_zaken_nl_: De waarde van in Nederland gelegen onroerende zaken (int).
_waarde_onroerende_zaken_vve_: De waarde van de onroerende zaken dienstbaar aan het verkrijgen, vervreemden of exploiteren van onroerende zaken (int).
_waarde_bezittingen_: De waarde van de bezittingen (int).
_onroerendezaakrechtspersoon_: Of sprake is van een onroerendezaakrechtspersoon (bool).

**Methods**
_bezitseis_: berekent of de bezitting voor meer dan 50% bestaan uit onroerende zaken en tegelijkertijd ten minste 30% van de bezittingen bestaan uit in Nederland gelegen onroerende zaken (bool).
_doeleis_: berekent of de onroerende zaken als geheel genoemen voor 70% of meer dienstbaar zijn of waren aan het verkrijgen, vervreemden of exploiteren van die onroerende zaken (bool).
