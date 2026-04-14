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
    les3b-innovatieruimte-ideate.md   # Les 3B: innovatieradar, PTM, 4P, PMI convergeren, ERRC/value curves
    les5-rapid-prototyping.md         # Les 5: rapid prototyping, concept collections, PELV-cyclus, forced choice
    les6-concept-collections-prototyping.md # Les 6: concept collections vullen, prototyping, 10 Faces of Innovation (Kelley)
    concept-collections.md            # Uitleg concept collections: divergeren, convergeren, minimale inhoud
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
    testplannen-pelv.md               # PELV-testplannen: pincode, ID-scan, iris (met conclusies)
    herframe-pivot-digitaal.md        # Pivot van analoge pen naar digitale authenticatie
    mckinsey-teamscores.md            # McKinsey innovatiescores Jr/Lianne/Anke
    huiswerk-les3-hzwk-per-ruimte.md  # HZWK's per innovatieruimte (Beveiliging, Hulp, Specialisatie)
public/
  concept-collection-security-expert.pptx # Concept collection moodboard denkrichting 1
  images/moodboard/                   # ~35 Unsplash afbeeldingen voor concept collections
create_moodboard.py                   # Generator script voor concept collection (python-pptx)
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

### TODO: Empathise diepte verbeteren (breedte is goed, diepte mist)
1. **Onderzoeksplan schrijven (verplicht, max 1 A4)** — opdracht eist dit, ontbreekt nu
2. **Interviews verrijken** — Anna & Famke zijn nu alleen bullet points, context/quotes/verhalen toevoegen
3. **Reflectie per sessie** — "wat hadden we niet verwacht", "wat leerde het zelf ervaren ons"
4. **Sessie 1 immersie versterken** — nu meer brainstorm dan onderdompeling, beter beschrijven of extra sessie doen
5. **Observatie-component (learn from observation)** — derde methode, bonus voor diepte
6. **Brug dreams/gripes → challenges expliciteren** — per cluster 1-2 zinnen waarom dit opviel

### Opdracht 1b Define + Design - Status (AFGEROND)
**Define (convergeren):**
- Sessie 3 (Innovatieradar, BK3): flipover met 4P-assen, 6 kamers, 32 ideeen op post-its
  - Kamers: Specialisatie, Nice to have, Hulp, Beveiliging, Klantervaring, Organisatie
  - PMI: groene (plus), roze (min), paarse (interessant) stickers
- Convergentie: HZWK's per innovatieruimte (Beveiliging, Hulp, Specialisatie)
- 2 denkrichtingen: De Analoge Security Expert + De Circulaire Standaard

**Design (divergeren):**
- Gate 1 (18 maart): DVF-formulieren met Niels de Munnik en Niels Verwoerd
  - Scores: Circulair 74, Security 73. Toch Security gekozen (duidelijkere aanleiding)
  - Blue Ocean value curve getekend
  - Foto's: `public/images/research/gate/`
- Concept collection Security Expert: moodboard 35+ afbeeldingen, maximaal divergerend

### Opdracht 1c Refine - Status (IN PROGRESS, pivot gedaan)
- **Conceptcollection Security Expert:** `public/concept-collection-security-expert.pptx`
  - Visuele moodboard, ~35 afbeeldingen (Unsplash + AI-generated)
  - Maximaal divergerend: alle vormen van authenticatie/verificatie
- **PELV iteratie 1 (1 april):**
  - Post-its brainstorm "Analoge Security" met clusters: Out of the Box, Stempel, Data opslag, Papier+Inkt, Pen+Persoonlijke activatie, Biometrische inkt
  - 3 concepten genoteerd: pen met iris-scan, pen met pincode+ID, proces met NFC/ID-scan
  - Paper prototypes: pen-in-kluisje (pincode), pen+ID-scanner (NFC), device met camera+sensoren+LED
  - Testplannen: `docs/onderzoek/testplannen-pelv.md`
  - Foto's: `public/images/research/prototype/postits-*.jpg`, `schets-*.jpg`
- **PELV iteratie 2 (8 april):**
  - Fysiek rapid prototype gebouwd: houten blokken + piepschuim + karton
  - Device met: pen in houder, NFC reader area, LED indicatoren (rood/groen)
  - Paper mockup van telefoonscherm met pincode-invoer
  - Demonstratie: iemand scant telefoon/ID bij device
  - Foto's: `public/images/research/prototype/rapid-prototype-*.jpg`
  - Video's: `public/images/research/prototype/rapid-prototype-*.mp4`
- **Gate/test met vragenlijst (Microsoft Forms, 7 vragen):**
  - Bruikbaarheid, gebruiksvriendelijkheid, haalbaarheid, business value
  - Verbetervoorstellen NFC-scanner en pennenbak-pincode
  - Fraudepreventie
- **Pivot/herframe:**
  - Conclusie uit beide PELV-iteraties: de pen is overbodig, het probleem zit in de handtekening zelf
  - Nieuwe richting: digitale authenticatie/verificatie via ID-bewijs (procesinnovatie)
  - Herframe vastgelegd: `docs/onderzoek/herframe-pivot-digitaal.md`
  - Value: veiliger (moeilijk te vervalsen), efficienter (geen papier), toegankelijker (op afstand)
- **Concept keuze na sparring (13 april):**
  - Digitale verificatieproces via ID-scan + PIN als procesinnovatie
  - Aurora als kennispartij die domeinkennis authenticiteit inbrengt, techpartner zoeken voor uitvoering
  - Stemmen als illustratie (van docent), maar breder toepasbaar (notaris, bank, gemeente)
  - Eerlijk benoemen: dit bestaat al in vormen (DigiD, PKIsigning), Aurora's bijdrage is het inzicht
  - Procesflow SVG gemaakt: `public/images/research/prototype/procesflow-verificatiestation.svg`
- **Nog te doen:**
  - PoV/PoC uitwerking (opdracht 1d, 30% van cijfer)
  - Onderzoeksplan empathise (1 A4, ontbreekt)
  - Interviews verrijken (Anna/Famke te mager)
  - 90 ideeen niet gehaald (32), verantwoorden of aanvullen
  - Concept collection #2 (Circulaire Standaard) bewust gedumpt, maar opdracht vraagt het
  - Projectvoorstellen per denkrichting ontbreken
  - Gate met externen (buiten school) niet gedaan
  - Opdracht 2a (innovatieadvies, video+PPT) en 2b (rolontwikkeling, video) komen later
  - Structuurdocument (max 4 pag) ontbreekt
  - GenAI verantwoordingsformulier bijvoegen

### McKinsey Teamscores
- Jr: Generating(4), Pioneering(4), Tabulating(4)
- Lianne: Networking(5), Pioneering(5)
- Anke: Motivating(5), Absorbing(5)
- Gaten in team: Motivating(Jr:2), Networking(Jr:2), Tabulating(Lianne:1), Pioneering(Anke:2)
- Details: `docs/onderzoek/mckinsey-teamscores.md`

### Website structuur (actueel, april 2026)
**Double diamond: Discover (div) → Define (conv) → Design (div) → Refine (conv) → Deliver**

**Discover (Fase 1, divergeren) — 4 bewijsstukken:**
- `/discover/` — overzicht, theorie (IBSOTEEP, Porter, scenariomatrix, immersive research, HZWK)
- `/discover/trends/` — trendanalyse
- `/discover/scenario/` — scenariomatrix met 4 scenario's
- `/discover/empathise/` — sessie 1+2, dreams & gripes
- `/discover/challenges/` — 5 HZWK-challenges

**Define (Fase 2, convergeren) — 3 bewijsstukken:**
- `/define/` — overzicht, theorie (innovatieradar, PMI, 4P)
- `/define/innovatieradar/` — sessie 3, 12 dimensies, 32 ideeen, 6 kamers
- `/define/convergentie/` — PMI-methode (groen/roze/paars), HZWK per ruimte (Beveiliging, Hulp, Specialisatie)
- `/define/denkrichtingen/` — 2 richtingen met clusters, challenges, reis-traceerbaarheid → linkt door naar gate

**Design (Fase 3, divergeren) — 2 bewijsstukken:**
- `/design/` — overzicht, theorie (DVF, Blue Ocean, concept collections)
- `/design/gate/` — DVF-formulieren + value curve, keuze Security Expert, foto's
- `/design/concept-collection/` — moodboard 35+ afbeeldingen, productvormen, authenticatie, kruisbestuivingen

**Refine (Fase 4, convergeren) — 2 bewijsstukken:**
- `/refine/` — overzicht, theorie (PELV, rapid prototyping, design thinking pivot)
- `/refine/prototyping/` — PELV 1 (brainstorm, schetsen, testplannen) + PELV 2 (rapid prototype, vragenlijst), expliciet P-E-L-V labels
- `/refine/pivot/` — herframe pen→digitaal, procesflow SVG, vergelijking oud/nieuw

**Deliver (Fase 5) — placeholder:**
- `/deliver/` — nog leeg, wacht op les 7+

**Overig:**
- `/aanleiding/` — geschiedenis schrijfwaren + tijdlijn

### Navigatieflow (rode draad)
Homepage → Aanleiding → Discover → (trends → scenario → empathise → challenges) → Define → (innovatieradar → convergentie → denkrichtingen) → Design → (gate → concept collection) → Refine → (prototyping → pivot) → Deliver
Elke fase-index heeft "Verder naar X →" link onderaan.

### Media
- `media/` — originele bronbestanden (WhatsApp foto's, AI-generated images, sessie-originelen)
- `public/images/research/` — gebruiksklare images voor de website:
  - challenges-hero.jpeg, dreams-gripes.jpeg (AI)
  - denkrichting1-security-expert.jpeg, denkrichting1-intelligente-pen.jpeg (AI)
  - denkrichting2-circulaire-standaard.jpeg (AI)
  - innovatieradar-hero.jpeg, brief-2030.jpeg (AI)
  - sessie1-foto.jpeg, sessie1-timelapse.mp4 (eigen)
  - sessie3-radar-1.jpeg, sessie3-radar-2.jpeg (eigen)
  - `gate/` — 5 foto's gate 1 DVF-formulieren + value curve (18 maart)
  - `prototype/` — 12 foto's + 2 video's prototyping (1+8 april)
  - `brainstorm/` — 3 whiteboardfoto's immersive research (10 maart)
- `public/presentatie-define.html` — 8-slide presentatie voor Gate BK4
- `public/concept-collection-security-expert.pptx` — Concept collection moodboard
- `public/images/moodboard/` — ~35 Unsplash afbeeldingen

### Teams-map (extern, niet in repo)
Pad: `/Users/jr/Library/CloudStorage/OneDrive-Gedeeldebibliotheken-WindesheimOffice365/O365-Innovatiemanagement - General/`
- `Fotos/` — alle originele foto's (brainstorm, gate, prototype, persoonlijk)
- `Huiswerk/` — les 2, les 3, les 7 PowerPoints, McKinsey Excel, immersive research docx
- `Opdrachten/` — testplannen (pincode/id/iris), gate0, HZWK pdf
- `Verslagen/Verslag.docx` — (leeg/onbekend)

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
