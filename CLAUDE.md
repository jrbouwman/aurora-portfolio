# Innovatiemanagement - EDIM.21

## Over dit project

Dit is het projectdossier voor het minorvak **Innovatiemanagement (EDIM.21)** van de opleiding Technische Bedrijfskunde, 3e jaar. Docent: Henk Bente Aalbersberg. Semester 2024-2025 S1.

## De casus: Aurora Writing Instruments Group

De casus is **"Beyond Paper"** - een fictieve maar realistische Nederlandse producent van potloden, pennen en tekenmaterialen (vergelijkbaar met Royal Talens) met 125+ jaar historie. De kernvraag: welke rol kan Aurora spelen in een wereld waarin schrijven en tekenen steeds digitaler worden? Het gaat om strategische herpositionering, niet om betere potloden maken.

## Innovatieproces (Design Thinking - Stage/Gate)

```
Discover --> Gate 1 --> Define --> Design --> Gate 2 --> Refine --> Gate 3 --> Deliver
  (BK1-2)              (BK3)     (BK4)              (BK5-6)              (BK7-9)
```

## Toetsing

| Onderdeel | Type | Weging |
|-----------|------|--------|
| 1a - Innovatieportfolio (proces) | Team | 30% |
| 1b - Proof of Value (product) | Team | 30% |
| 2a - Innovatieadvies | Individueel | 20% |
| 2b - Rolontwikkeling | Individueel | 20% |

## Mappenstructuur

```
docs/
  studiehandleiding.md                # Volledige studiewijzer met leerdoelen, toetsing, deadlines
  casus/
    aurora-strategische-casus.md      # Hoofdcasus: strategische context, kernprobleem, opdracht
    aurora-management-samenvatting.md # Executive summary NL + EN
    aurora-bijlagen.md                # Data: marktcijfers, omzetverdeling, surveys, spanningsvelden
  opdrachten/
    opdracht-1a-discover.md           # Opdracht 1a: trends, scenario, empathise, challenges
    opdracht-1b-design-ideate-select.md # Opdracht 1b: innovatieradar, ideate (90 ideeen), gate, 2 denkrichtingen
    opdracht-1c-refine-prototype-test.md # Opdracht 1c: conceptcollection, prototyping, PELV-cyclus, 2 iteraties
    opdracht-1d-proof-of-value.md     # Opdracht 1d: PoV/PoC uitwerken, apart inleveren
    opdracht-2a-innovatieadvies.md    # Opdracht 2a (individueel): adviezen innovatievermogen, video+ppt
    opdracht-2b-rolontwikkeling.md    # Opdracht 2b (individueel): rolprofiel als innovatiemanager, korte video
    werken-met-casussen.md            # Uitleg casus vs. eigen bedrijf
    portfolio-aanwijzingen.md         # Hoe portfolio op te bouwen (structuurdocument + bewijsstukken)
    problem-clarification.md          # AT1 template: probleem vs. non-probleem analyse (Andler 2016)
    discover-challenges-hzwk.md       # Dreams & Gripes -> HZWK-methode voor challenges
    gate0-discussie.md                # Gate 0 discussieformulier: trends scoren en selecteren
  lessen/
    les1-perspectieven-op-innovatie.md # Les 1: definities, VOCA, DESTEP/IBSOTEEP, design thinking intro
    les2-trends-en-immersive-research.md # Les 2: trendsurfing, PLC, BCG, strategieen, immersive research
    voorbereiding-les2.md             # Voorbereidingsopdracht + verplichte literatuur les 2
    trends-tilborgh.md                # IBSOTEEP-analyse uitleg (Van Tilborgh 2022)
    trend-piramide.md                 # Trendpiramide: micro/macro/mega niveaus
    innovatieruimte-rollen.md         # 4 innovatierollen (Derksen 2012): teamsamenstelling
  literatuur/
    van-der-voort-innovatieboek-h1-h2.md # H1: wat is innovatie + H2: waarom innoveren (Van der Voort 2011)
    kastelle-creativity-entrepreneurship-innovation.md # Creativiteit vs. ondernemerschap vs. innovatie
  beoordeling/
    rubric.md                         # Rubric met criteria per niveau (onvoldoende t/m uitmuntend)
```

## Werkwijze

### Mappenstructuur uitbreidingen
- `docs/onderzoek/` — Werkdocumenten en uitwerkingen per opdracht (bespreek eerst in groep, daarna naar website)
- `src/utils/base.ts` — Helper functie `url()` voor correcte base path in alle links

### Aanpassingen website (maart 2025)
- Nieuw design: donker thema, felle fase-kleuren, Space Grotesk font, scroll-animaties
- Geinspireerd op stockdutchdesign.com — reis/storytelling door het project
- Alle interne links gebruiken `url()` helper uit `src/utils/base.ts` voor correcte base path

### Opdracht 1a Discover - Status
- Werkdocumenten in `docs/onderzoek/` — alle met bronverwijzingen (genummerd, met URLs)
- Trendanalyse (IBSOTEEP + Porter + piramide): v2 met 19+ bronnen
- Scenariomatrix: concept met 4 scenario's + 3 alternatieve opties voor as 2
- Aanleiding (geschiedenis schrijfwaren + tijdlijn): v2 met drivers per mijlpaal en 16 bronnen
- Bronnenlijst: `docs/onderzoek/bronnen.md` — 26 bronnen
- Extra theorie gekozen: Christensen's Disruptive Innovation (1997)
- Klasdiscussie genoteerd: duurzaamheid, goedkope arbeid lage-lonenlanden, ethische productie
- As 2 scenario: nog te kiezen door groep (3 alternatieven voorgesteld)

## Rol van Claude

Claude helpt als **studieassistent en sparringpartner** bij het uitwerken van dit innovatieproject:

- **Analyseren:** Helpen met DESTEP/IBSOTEEP-analyses, Porter's 5 Forces, trendherkenning voor Aurora
- **Structureren:** Portfolio opbouwen volgens de stage/gate structuur, bewijsstukken ordenen
- **Schrijven:** Scenario's onderbouwen, Proof of Value uitwerken, innovatieadvies formuleren
- **Theorie toepassen:** Bossink, VOCA/VUCA, design thinking, Creative Problem Solving koppelen aan de casus
- **Kwaliteit bewaken:** Werk toetsen aan de rubric-criteria (docs/beoordeling/rubric.md)

### Belangrijke richtlijnen
- GenAI-gebruik is toegestaan maar moet verantwoord; het werk moet eigen leerproces reflecteren
- Het betreft een **simulatie** - geen echt product nodig, wel een overtuigende Proof of Value
- Focus op het perspectief van een **manager van innovaties**, niet puur technisch
- Portfolio = reisverslag met structuurdocument (max 4 pag) + bewijsstukken
- **ELKE bron moet een klikbare hyperlink zijn** naar de originele bron (geen platte tekst)
- **Zo veel mogelijk illustraties en afbeeldingen** gebruiken — SVG-illustraties waar mogelijk, foto's als illustratie niet voldoet

## Kernliteratuur & referenties

- Bossink (2018) - Innovatiemanagement, basaal innovatiemodel
- Van der Voort & Ormondt (2011) - Het Innovatieboek (H1+H2 beschikbaar als markdown)
- Kastelle - Creativity, Entrepreneurship & Innovation (beschikbaar als markdown)
- Van Tilborgh (2022) - IBSOTEEP, trends op verschillende niveaus
- Derksen (2012) - Innovatieruimte en rollen in teams
- Dodgson et al. (2008) - 4 innovatiestrategieen (proactive/active/reactief/passief)
- O'Reilly & Tushman (2013) - Ambidexteriteit (exploiteren vs. exploreren)
- Suzuki (2020) - Beginners mind
- Zomer (2021), Mueller-Roterberg (2018) - Design Thinking
- Treffinger (1995) - Creative Problem Solving
- Andler (2016) - Problem clarification
- Snowden (2005) - Cynefin, paradigmashift
- BCG (Henderson) - Growth-Share Matrix
