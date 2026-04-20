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
- Teamleden footer: Anke Maassen van den Brink, Lianne van Os, Jr Bouwman

### Homepage redesign (14 april 2026)
- Alles in 1 viewport: titel-animatie → landschap → fasen → CTA
- 3D landschap als hero-visual: `public/images/innovatiereis-landschap.png`
  - AI-generated via Nano Banana, purple-indigo mountains met 5 gekleurde stations
  - Stations matchen de fase-kleuren (coral telescoop, blauwe vuurtoren, lavender kristal, amber forge, groene raket)
  - 14 april: originele complete versie teruggeplaatst (eerdere crop was te agressief, raket rechtsboven werd afgeknipt)
  - Fade-mask enkel op zijkanten (7%/93%) + subtiele top/bottom afloop, geen harde randen meer
- Onder landschap: 5 fase-labels in grid (kleur-dot, titel in fase-kleur, subtitel)
- "Beyond Paper" handwriting animatie teruggebracht naar compacte maat (clamp 2.75-5.5rem)
- "Onze reis door het innovatieproces" intro-sectie + pen-stroke SVG weggehaald (overbodig naast landschap)
- Design fase subtitel gecorrigeerd: "Divergeren: concepten verkennen" (was: "selecteren en uitwerken")

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
  - Procesflow SVG's gemaakt (zie Pivot-pagina hieronder)
- **Pivot-pagina uitgebreid (15 april 2026):**
  - Nieuwe hoogover-procesflow SVG: huidige situatie (donker) vs toekomstige situatie (amber, refine-kleur). Belangrijk inzicht: de handtekening en het papier BLIJVEN, de innovatie zit in de ID-check ervoor en de koppeling aan unieke authenticatiecode erna
  - Uitgebreide procesflow SVG in huisstijl: volledige keten incl. foutafhandeling, validatie, fraudedetectie, Nee-lus bij bevestiging. Met pill-labels (Ja/Nee/goedkeuring), drop-shadow, amber happy-path band, exception-zones en legenda
  - Voorbeeldscenario SVG: concrete servicebalie-flow met ID-scannen, pincode invullen, Goedkeuring, etc.
  - Alle drie de flows: `public/images/research/prototype/procesflow-{hoogover,uitgebreid,voorbeeld}.svg`
  - Hoogover is hoofdvisual op pivot-pagina; uitgebreid + voorbeeld zijn klikbare thumbnails in grid met lightbox-modal (Esc/X/klik-buiten = sluiten)
  - Narratief gecorrigeerd: pivot-subtitel herschreven (geen em-dashes, natuurlijker)
  - **Value Proposition Canvas** toegevoegd als sectie: volgens Business Models Inc standaard template
    - Vierkant (Value Map, amber accent): 3 driehoeken — Products & Services (links), Gain Creators (rechtsboven), Pain Relievers (rechtsonder)
    - Cirkel (Customer Profile, dark): 3 taartpunten — Gains (linksboven), Pains (linksonder), Job-to-be-done (rechterhelft)
    - Inhoud ingevuld voor Aurora + techpartner (aanbiederzijde) en notaris/bank/gemeente (klantzijde)
    - Fit-samenvatting in accent-blok eronder
    - Standalone versie: `public/images/research/prototype/vpc-aurora.svg`
### Opdracht 1d Deliver - Status (IN PROGRESS)
- **Gate 2 (15 april):** DVF-formulieren van 4 medestudenten, allemaal GO
  - Customer value hoogst (gem. 4.5/5), kerncompetenties laagst (gem. 1.8/5)
  - Handgeschreven feedback: "startup, nieuwe BV in deze richting", "hoelang is dit veilig?", "waarom nog handtekening als verificatie/id ook persoonlijk is"
  - Foto's: `public/images/research/gate2/dvf-formulier-{1-4}.jpeg`, `dvf-feedback-{1-5}.jpeg`
- **Docent feedback:** voor innovatie die zo losstaand is van huidige werkprocessen, is aparte startup logisch
  - Sluit aan bij ambidexteriteit (O'Reilly & Tushman, 2013): exploiteren vs exploreren
- **Deliver-pagina's gebouwd (19 april):**
  - `/deliver/` — index met Gate 2 feedback, DVF-scores tabel, theorie
  - `/deliver/proof-of-value/` — challenge, concept, fysieke vormgeving, waardepropositie per stakeholder, DVF-beoordeling, financieel model
  - `/deliver/roadmap/` — startup-argumentatie (ambidexteriteit), 4-fasen implementatieplan, diffusie-strategie per sector (Rogers), 5 adoptiefactoren, risico's en mitigatie
- **Les 8 materiaal geconverteerd:**
  - `docs/lessen/les8-waarde-leveren.md` — diffusie, adoptie (Rogers), DVF, waardecreatie, marketing innovaties
  - `docs/opdrachten/opdracht-1d-proof-of-value.md` — aangevuld met PoV-eisen, suggested outline, waardecreatie-vragen
- **Pivot-presentatie:** downloadlink op pivot-pagina toegevoegd
- **VPC op pivot-pagina:** tekst vervangen door versie uit Jr's PowerPoint (slide 5)
- **Procesflow-uitgebreid.svg gefixed:** goedkeuring-label, Deactivatie-eindpunt, error zone

- **Nog te doen:**
  - Onderzoeksplan empathise (1 A4, ontbreekt)
  - Interviews verrijken (Anna/Famke te mager)
  - 90 ideeen niet gehaald (32), verantwoorden of aanvullen
  - Concept collection #2 (Circulaire Standaard) bewust gedumpt, maar opdracht vraagt het
  - Projectvoorstellen per denkrichting ontbreken
  - Gate met externen (buiten school) niet gedaan
  - Opdracht 2a (innovatieadvies, video+PPT) en 2b (rolontwikkeling, video) komen later
  - Structuurdocument (max 4 pag) ontbreekt
  - GenAI verantwoordingsformulier bijvoegen

### Stand per 19 april 2026
- **PoV volgens les-8-template** (`proof-of-value.astro`): 10 secties met table of contents. Introductie met Aurora-context en strategische driver, huidige situatie met meetbare problemen (visuele ID-check, handtekening-bewijs, dossiertijd) en fraudecontext Betaalvereniging NL, oplossing met 3-stappen-flow, prototype-samenvatting uit PELV 1+2 met N=6 testresultaten, status-nu-blok (6 componenten), waardepropositie met cijfers per stakeholder (notaris circa €20k/jaar tijdwinst-aanname, bank: fraudecontext, verzekeraar: archief), concurrentie-matrix (DocuSign/Signicat/itsme/iDIN/PKIsigning), DVF herleidbaar naar Gate 2, financieel model met marktomvang NL-tabel + investeringsbehoefte €660k-€1,3 mln + break-even-schatting, roadmap-samenvatting met go/no-go, conclusie met concrete CTA (3 besluiten gevraagd aan MT) en AVG-noot.
- **Roadmap** (`roadmap.astro`): ambidexteriteit met drie varianten (structureel / contextueel / sequentieel) expliciet afgewogen, per fase randvoorwaarden + go/no-go-criteria + budget, strategische sectorvolgorde (notaris → bank → verzekeraar) op basis van urgentie + bereikbaarheid (niet als Rogers-adopter-categorieen), Rogers' 5 adoptiefactoren realistischer ingeschat (compatibiliteit laag-gemiddeld).
- **PELV** (`prototyping.astro`): PELV-labels als `P · Plan` etc. Testresultaten iteratie 2: N=6 medestudenten, scores per vraag, 3 letterlijke citaten ("waarom niet DigiD?", "de pen doet niks"), verbeterloop 1→2 expliciet, 2 presentabele concepten benoemd (A gekozen, B afgevallen met reden), externe gate als gat benoemd, methodologische beperking (perceptie-test, geen technische veiligheid).
- **Huizingh-mapping** (`innovatieradar.astro`): officiele verdeling 4+4+2+2 (Klanten onder Product). 4P-kleuren als 4 tinten van de Define-kleur zodat ze als cluster ogen. Reflectie-alinea "Wat werkte wel en niet aan de radar".
- **Design gate** (`design/gate.astro`): DVF-subscores tabel per as (Circulair 28/24/22=74, Security 24/24/25=73), ERRC-framework (4 blokjes), value-curve-uitleg met concrete as-factoren en concurrentie, Security-keuze methodisch verantwoord (D-voorsprong Circulair op aannames, F-voorsprong Security op concrete klantpijn), reflectie op DVF als instrument.
- **Concept collection** (`concept-collection.astro`): 48 beelden uit `public/images/moodboard/` inline in responsive grid met hover-tag en caption. Vier kern-vragen uit lesmateriaal beantwoord (hoe al geprobeerd, waar lijkt op, wie is expert, welke verbanden). Kiem voor pivot expliciet gemarkeerd.
- **Convergentie** (`convergentie.astro`): PMI-fotobewijs (sessie3-radar-2.jpeg). HZWK's per kamer <15 woorden zonder oplossing in de vraag. Bridge van 3 HZWK-kamers naar 2 denkrichtingen als expliciete mini-beslismatrix.
- **Denkrichtingen** (`denkrichtingen.astro`): breadcrumb "Design" → "Define". "Impliciet PMI toegepast" vervangen door "kleurcode vooraf afgesproken". Challenge-HZWK's ingekort (van 27/21 woorden naar 13/11).
- **Discover-index** (`discover/index.astro`): Aurora-strategie-analyse als eigen blok (portfolio, kanalen, strategische beweging), tijdsbesteding immersive research vermeld (ca. 2u45min over 2 sessies), methode-reflectie per theorie (IBSOTEEP vs DESTEP, Porter + Christensen, scenariomatrix, immersive research).
- **Scenario** (`scenario.astro`): scenario B expliciet gemarkeerd met ring-highlight en "onze keuze" label, "Waarom wij op scenario B zitten" blok met 3 onderbouwingen. "Waarom NU?" vervangen door kerncijfers-blok (-20% krimp, 66% digitaal, +4,6% premium, 55% Aurora-omzet krimp-segment) + concrete impact-per-termijn voor Aurora.
- **Kritische theorie-reflectie** op alle 5 fase-indexen: "Wat deze methoden wel en niet opleverden". Les-theorieen kritisch beoordeeld, geen nieuwe theorieen toegevoegd.
- **AI-toon**: em-dashes in titles/H2/alt-text/PELV-labels vervangen (→ `:` of `·`). "Niet X, maar Y"-taglines weg, "als geen ander" weg, "paradigmashift!" weg, "waterdicht" vervangen, scenario-implications herschreven zonder pitch-deck-toon, Porter key insight afgezwakt naar feitelijke conclusie.
- **Bronnen klikbaar**: Huizingh, De Bono PMI, DVF/IDEO, Treffinger, O'Reilly & Tushman, Rogers, Blue Ocean, Betaalvereniging, KNB, eIDAS, DocuSign/Signicat/itsme/iDIN/PKIsigning, Logius, ACM, HBR.

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

**Deliver (Fase 5) — 2 bewijsstukken:**
- `/deliver/` — overzicht, Gate 2 DVF-feedback (scores + foto's), theorie (DVF, diffusie, ambidexteriteit, waardecreatie)
- `/deliver/proof-of-value/` — challenge, concept met fysieke vormgeving, procesflow, waardepropositie per stakeholder, DVF-beoordeling, financieel model
- `/deliver/roadmap/` — startup-argumentatie (ambidexteriteit), 4-fasen implementatieplan, diffusie per sector (Rogers), 5 adoptiefactoren, risico's en mitigatie

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
- `public/presentatie-pivot.pptx` — 5-slide PowerPoint voor pivot-sessie (voorpagina + hoogover-flowchart + strategische/technische analyse + waarde/financieel + VPC als native PowerPoint-vormen). VPC-slide met vierkant+ovaal+connectors is handmatig bewerkbaar in PowerPoint. Jr heeft handmatig verder opgemaakt, NIET opnieuw genereren want python-pptx kan formatting kwijtraken
- `create_presentatie_pivot.py` — genereert presentatie-pivot.pptx vanaf 0 (gebruikt `/tmp/hoogover-export.png` en `/tmp/vpc-export.png` gerenderd via agent-browser)
- `add_voorpagina.py` — voegt losstaande voorpagina toe aan bestaande pptx (niet meer gebruiken: risico op formatting-verlies)
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
