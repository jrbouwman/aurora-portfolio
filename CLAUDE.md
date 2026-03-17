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
    voorbereiding-les4-denkrichtingen.md # Voorbereiding BK4: denkrichtingen ordenen, PMI, PowerPoint
  lessen/
    les1-perspectieven-op-innovatie.md # Les 1: definities, VOCA, DESTEP/IBSOTEEP, design thinking intro
    les2-trends-en-immersive-research.md # Les 2: trendsurfing, PLC, BCG, strategieen, immersive research
    les3-define-and-design.md         # Les 3: define, design thinking, 4P innovatieruimte, blue ocean, ERRC
    voorbereiding-les2.md             # Voorbereidingsopdracht + verplichte literatuur les 2
    trends-tilborgh.md                # IBSOTEEP-analyse uitleg (Van Tilborgh 2022)
    trend-piramide.md                 # Trendpiramide: micro/macro/mega niveaus
    innovatieruimte-rollen.md         # 4 innovatierollen (Derksen 2012): teamsamenstelling
    innovatieradar-handleiding.md     # Innovatieradar: 12 dimensies, werkwijze divergeren/convergeren (Huizingh 2019)
  literatuur/
    van-der-voort-innovatieboek-h1-h2.md # H1: wat is innovatie + H2: waarom innoveren (Van der Voort 2011)
    kastelle-creativity-entrepreneurship-innovation.md # Creativiteit vs. ondernemerschap vs. innovatie
  beoordeling/
    rubric.md                         # Rubric met criteria per niveau (onvoldoende t/m uitmuntend)
  onderzoek/
    sessie-notities.md                # Ruwe notities sessie 1 (board) en sessie 3 (innovatieradar)
    03-scenariomatrix.md              # Werkdocument scenariomatrix met 4 scenario's
    bronnen.md                        # Bronnenlijst (26 bronnen)
media/                                # Originele bronbestanden (niet op de website)
```

## Werkwijze

### Mappenstructuur uitbreidingen
- `docs/onderzoek/` — Werkdocumenten en uitwerkingen per opdracht (bespreek eerst in groep, daarna naar website)
- `src/utils/base.ts` — Helper functie `url()` voor correcte base path in alle links

### Aanpassingen website (maart 2026)
- Nieuw design: donker thema, felle fase-kleuren, scroll-animaties
- Geinspireerd op stockdutchdesign.com — reis/storytelling door het project
- Alle interne links gebruiken `url()` helper uit `src/utils/base.ts` voor correcte base path
- Fonts: Patrick Hand (display/koppen), Kalam (body/UI — licht handgeschreven maar leesbaar)
- Pen-stroke SVG visual in hero (`public/images/pen-stroke.svg`)
- Teamleden footer: Anke Maassen van den Brink, Lianne van Os, Jr Bouwman

### Opdracht 1a Discover - Status (AFGEROND)
- Werkdocumenten in `docs/onderzoek/` — alle met bronverwijzingen (genummerd, met URLs)
- Trendanalyse (IBSOTEEP + Porter + piramide): v2 met 19+ bronnen
- Scenariomatrix: 4 scenario's op 2 assen:
  - X-as: Tempo digitale adoptie (langzaam ↔ snel)
  - Y-as: Overheidsregulering (actief beleid ↔ laissez-faire)
  - Scenario's: A. Analoge Renaissance, B. Gouden Kruispunt, C. Stille Status Quo, D. Digitale Dominantie
- Aanleiding (geschiedenis schrijfwaren + tijdlijn): v2 met drivers per mijlpaal en 16 bronnen
- Bronnenlijst: `docs/onderzoek/bronnen.md` — 26 bronnen
- Extra theorie gekozen: Christensen's Disruptive Innovation (1997)
- Klasdiscussie (Gate 0): duurzaamheid, goedkope arbeid lage-lonenlanden, ethische productie
- Empathise: sessie 1 (learn from experience) + sessie 2 (learn from users)
- Dreams (6 clusters) en Gripes (4 clusters), HZWK op challenges-pagina (5 challenges)
- HZWK staat ALLEEN op challenges-pagina, NIET op empathise

### Immersive Research - Status
- Pagina: `src/pages/discover/empathise.astro`
- Sessie 1 (Learn from Experience): brainstorm eigen ervaringen, timelapse + foto
  - Niet alle punten gelabeld als dream/gripe, sommige zijn observaties (analoog vs. digitaal)
- Sessie 2 (Learn from Users): interviews Anna & Famke
- Dreams geclusterd in 6 thema's, Gripes in 4 thema's (compact, zonder HZWK)
- Media: `public/images/research/` (sessie1-timelapse.mp4, sessie1-foto.jpeg, dreams-gripes.jpeg)

### Opdracht 1b Define - Status (IN PROGRESS)
- Sessie 3 (Innovatieradar, BK3): flipover met 4P-assen, 6 kamers, 32 ideeën op post-its
  - Kamers: Specialisatie, Nice to have, Hulp, Beveiliging, Klantervaring, Organisatie
  - PMI impliciet toegepast: groene (plus), roze (min), paarse (interessant) stickers
  - Foto's: `public/images/research/sessie3-radar-1.jpeg`, `sessie3-radar-2.jpeg`
- Innovatieradar: Huizingh (2019), 12 dimensies over 4 sleuteldimensies (Product, Positie, Proces, Paradigma)
  - Handleiding: `docs/lessen/innovatieradar-handleiding.md`
  - PDF en DOCX bronbestanden in projectroot
- 2 denkrichtingen geconvergeerd:
  1. **De Analoge Security Expert** (Merk + Oplossingen = Paradigma + Product): pen bewijst wie er geschreven heeft via schrijf-DNA (druk, snelheid, hoek, ritme). Robuust in alle scenario's.
  2. **De Circulaire Standaard** (Platform + Merk = Product + Paradigma): regelgeving als wapen (Tesla/Tony's model), EU Digital Product Passport, cradle-to-cradle, radicale ketentransparantie. Sterkst in scenario B.
- Elke denkrichting heeft "Hoe zijn we hier gekomen?" traceerbaarheid: trends → scenario → empathise → challenge → radar
- Voorbereiding BK4: `docs/opdrachten/voorbereiding-les4-denkrichtingen.md` (PowerPoint 7 slides, gate)
- **Nog te doen:** Gate (BK4) — selectie van 2 denkrichtingen met minimaal 2 anderen

### Website structuur (actueel)
**Discover (opdracht 1a):**
- `/discover/` — overzicht met 4 bewijsstukken
- `/discover/trends/` — trendanalyse
- `/discover/scenario/` — scenariomatrix met 4 scenario's
- `/discover/empathise/` — sessie 1+2, dreams & gripes (zonder HZWK)
- `/discover/challenges/` — 5 HZWK-challenges uit dreams/gripes

**Define (opdracht 1b):**
- `/define/` — overzicht met 2 bewijsstukken
- `/define/innovatieradar/` — sessie 3, 12 dimensies, 32 ideeën per kamer
- `/define/denkrichtingen/` — 2 richtingen met clusters, challenges, reis-traceerbaarheid

### Media
- `media/` — originele bronbestanden (WhatsApp foto's, AI-generated images, sessie-originelen)
- `public/images/research/` — gebruiksklare images voor de website:
  - challenges-hero.jpeg, dreams-gripes.jpeg (AI)
  - denkrichting1-security-expert.jpeg (AI, biometrische pen bij ondertekening)
  - denkrichting2-circulaire-standaard.jpeg (AI, gedemonteerde pen met recycling)
  - innovatieradar-hero.jpeg, brief-2030.jpeg (AI)
  - sessie1-foto.jpeg, sessie1-timelapse.mp4 (eigen)
  - sessie3-radar-1.jpeg, sessie3-radar-2.jpeg (eigen)
- `public/presentatie-define.html` — 8-slide presentatie voor Gate BK4 (standalone HTML, pijltjestoetsen)

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
- **Zo veel mogelijk illustraties en afbeeldingen** gebruiken, SVG-illustraties waar mogelijk, foto's als illustratie niet voldoet

### AI-toon vermijden (BELANGRIJK)
De docent moet niet afhaken op AI-toon. Vermijd daarom:
- **Em dashes (—)** in lopende tekst. Gebruik komma's, punten, of "en"/"of"
- **Taglines en oneliners** zoals "Niet oplossen, maar ontdekken" of "De juiste vraag stellen is halve werk"
- **Perfect parallelle opsommingen** die te netjes zijn voor een studentenportfolio
- **Corporate jargon** zoals "competitive moat", "paradigmashift", "convergeren naar" (behalve als het theorie-termen zijn)
- **Pitch deck-toon**: te glad, te overtuigend, te veel als verkooppraatje
- **Te lange HZWK's**: houd ze kort en direct (~15 woorden), niet 40 woorden met bijzinnen
- Schrijf in **wij-vorm** en gewone spreektaal: "We vroegen ons af...", "Daar kwamen we op door..."
- Het mag best een beetje rommelig of onaf klinken, dat is geloofwaardiger

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
- Huizingh (2019) - Innovatieradar, 12 dimensies binnen 4P (Product, Positie, Proces, Paradigma)
- Tidd & Bessant - 4P Innovation Space (product, process, position, paradigm)
- Kim & Mauborgne - Blue Ocean Strategy, ERRC framework, value curves
