# Holistische Review Portfolio

Datum: 19 april 2026. Reviewer-perspectieven: docent Henk (rubric), MT/directie (overtuigingskracht), critical friend (houdbaarheid verhaal).

## Samenvatting (belangrijkste bevindingen)

De site is visueel sterk, met een duidelijke fase-kleurcodering, consistente layout en veel bewijsstukken. De reis Discover→Deliver is logisch opgebouwd met breadcrumbs en "verder naar X"-links op bijna elke pagina. De navigatieflow werkt als een Polarsteps-variant.

Maar: voor een 10 is dit nog niet scherp genoeg op drie fronten.

1. **Theorie-breedte is mager voor een uitmuntend-oordeel.** CLAUDE.md noemt 20+ kernbronnen, maar op de site staan er ongeveer 6 (Christensen, Porter, IBSOTEEP/Tilborgh, Treffinger, Huizingh, Tidd/Bessant, Kim/Mauborgne, O'Reilly/Tushman, Rogers). Grote afwezigen: Bossink, Van der Voort, Kastelle, Derksen, Dodgson, Snowden/Cynefin, BCG, Suzuki, Zomer/Mueller-Roterberg, Andler, Kelley. Kritische reflectie op theorieen ontbreekt volledig.
2. **AI-toon incidenten, voornamelijk em-dashes.** 28 em-dashes in 13 paginas, plus enkele "Niet X, maar Y"-constructies, "als geen ander", "paradigmashift", "competitive moat"-achtig jargon (gering) en "De pen blijft bestaan, maar het bewijs verschuift" in de VPC-fit. Docent-risico.
3. **Leerervaring vs. succes.** De pivot is het sterkste leerpunt, mooi geexpliciteerd. Maar het algehele verhaal leunt nog richting pitch (vooral op Deliver-paginas). Twijfels, mislukkingen, team-dynamiek, interpersoonlijke spanning of teamrollen (McKinsey) komen niet aan bod.

Een kleine bug: breadcrumb op `/define/denkrichtingen/` zegt "Design" in plaats van "Define". De spin-off `src/pages/refine/[slug].astro` en `src/pages/design/[slug].astro` en `src/pages/define/[slug].astro` zijn dynamische routes die mogelijk 404-gedrag opleveren (bekijk of ze nog nut hebben).

Portfolio nu: **7.5/10**. Met prio-1 fixes: **8.5/10**. Uitmuntend-potentieel: **9-9.5/10** (hard werken aan kritische reflectie + theorie-breedte).

---

## Reisnarratief-check (Polarsteps-eis)

De site voelt inderdaad als een reis. Vijf fase-stations met een gekleurde dot, een landschap-hero op home, breadcrumbs per pagina, "Verder naar X"-knoppen onderaan. De rode draad Discover→Define→Design→Refine→Deliver is visueel helder (fase-kleuren in navigatie, knoppen, linten).

**Wat voelt als reis:**
- Homepage met landschap, fase-stations en "Start de reis"-CTA (`src/pages/index.astro:129-136`).
- Elke subpagina heeft forward+backward-navigatie (bijv. `scenario.astro:277-285`, `pivot.astro:356-370`).
- Traceerbaarheids-blokken op `denkrichtingen.astro`: "Hoe zijn we hier gekomen?" met stappen linkt naar Trends/Scenario/Empathise/Challenge/Radar (`denkrichtingen.astro:166-190`). Dit is het mooiste reis-element van de hele site.

**Wat toch rapport-achtig voelt:**
- `proof-of-value.astro` en `roadmap.astro` leunen richting consultancyrapport: strak geordend in blokken zoals "Het concept", "Waardepropositie", "Financieel model", "Risico's en mitigatie". Feitelijk, maar weinig "we dachten eerst... toen...". Zie prio-2.
- `refine/pivot.astro` doet het goed ("Dat was even schrikken") maar is een uitzondering.
- De fase-indexen (`discover/index.astro`, `define/index.astro` etc.) werken met standaard-koppen "Wat hebben we gedaan?" / "Wat viel op?" / "Theorie en methode". Dat hergebruik oogt parallel en AI-achtig (zie AI-sweep).

**Verder naar X check (compleet):**
- `discover/index.astro:76-78`: Verder naar Define (OK).
- `define/index.astro:68-71`: Verder naar Design (OK).
- `design/index.astro:62-65`: Verder naar Refine (OK).
- `refine/index.astro:57-60`: Verder naar Deliver (OK).
- `deliver/index.astro`: **geen Verder-knop**, eindigt met ul met 3 bullets. Dat klopt (einde reis), maar een "Einde van de reis — terug naar home" afsluiter hoort er wel bij. Nu gaat de reader op roadmap.astro `einde van de reis` zien.

---

## Navigatie & rode draad

**Navigatiebalk** (`Navigation.astro`): fixed, backdrop-blur, logo + 5 tab-dots. Active state via `currentPath.startsWith(phase.href)` is simpel en werkt. Aanleiding ontbreekt in de hoofdnav (alleen via home-CTA bereikbaar).

**Breadcrumbs:**
- Per subpagina aanwezig, netjes "Home / Discover / Trendanalyse" pattern.
- **BUG**: `denkrichtingen.astro:72` heeft `<a href={url('/define/')} class="...">Design</a>` — label is "Design" maar link gaat naar /define/. De breadcrumb voor deze pagina hoort "Home / Define / Denkrichtingen" te zijn. Fix.

**Forward/backward koppeling:**
- Bijna elke pagina heeft beiden. Goed.
- `discover/trends.astro`: eindigt met "Volgende bewijsstuk" + scenariobouwing, maar geen link terug naar `/discover/`. Alleen via breadcrumb.
- `design/concept-collection.astro:176-184`: gaat naar /refine/ zonder tussenstap, OK.

**Dead ends / suspect routes:**
- `src/pages/refine/[slug].astro`, `design/[slug].astro`, `define/[slug].astro` zijn dynamische routes. Bestaan er content-collecties die hiermee corresponderen? Zo niet, dan zijn dit potentiele 404's of onbedoelde URLs. Check of je ze kunt verwijderen.
- `src/pages/deliver/[slug].astro` is verwijderd (git status: `D`), `src/content/deliver/placeholder.md` idem. Goed.

**Aanleiding-integratie:** `aanleiding.astro` wordt alleen bereikt via de "Start de reis"-knop op home. Er is geen link vanuit Discover terug naar Aanleiding. De tijdlijn (5000 jaar schrijven) is waardevolle context — overweeg vanuit `discover/trends.astro` een link naar `/aanleiding/` om historische drivers te koppelen aan huidige trends.

---

## Theorie-rode-draad (cruciaal voor 10)

**Wat ingezet op welke pagina:**

| Theorie / bron | Locatie | Niveau |
|---|---|---|
| IBSOTEEP (Van Tilborgh 2022) | `discover/trends.astro` + `discover/index.astro` | Toegepast, kernpunten per dimensie met kritische bronnen. Geen kritische reflectie op theorie zelf. |
| Porter's 5 Forces | `discover/trends.astro` | Toegepast met scores, overlays, conclusie "grootste dreiging is tech, niet pennenmakers". Goed. |
| Trendpiramide (Macro/Mega/Micro) | `discover/trends.astro` | Visueel mooi, maar geen expliciete bron. Mee oppassen. |
| Christensen Disruptive Innovation | `discover/trends.astro` (eigen sectie) | Uitgebreid met S-curve, valkuil, toepassing op Aurora. Sterkst toegepaste theorie. |
| Scenariomatrix 2x2 | `discover/scenario.astro` + `discover/index.astro` | Toegepast. Theorie-attributie ontbreekt (Peter Schwartz / Shell? GBN?). |
| HZWK / CPS (Treffinger 1995) | `discover/challenges.astro` + `discover/empathise.astro` | Genoemd, maar oppervlakkig. Alleen als "How Might We"-techniek. |
| Innovatieradar 12 dimensies (Huizingh 2019) | `define/innovatieradar.astro` + `define/index.astro` | Sterk toegepast: tabel met 12 dimensies + eigen resultaten gemapped. |
| 4P Innovation Space (Tidd & Bessant) | `define/index.astro`, `define/innovatieradar.astro` | Alleen kort vermeld. |
| PMI-methode (De Bono) | `define/convergentie.astro`, `define/index.astro` | Toegepast met stickers-materiaalkoppeling. OK. |
| DVF (Desirability/Viability/Feasibility) | `design/gate.astro` + `deliver/index.astro` + `deliver/proof-of-value.astro` | Toegepast maar geen bronvermelding. Herkomst: IDEO? Zonder attributie zwak. |
| Blue Ocean / Value Curve (Kim & Mauborgne) | `design/gate.astro`, `design/index.astro` | Genoemd en foto, maar de value curve zelf niet doorgekauwd. ERRC framework wordt niet genoemd. |
| Concept Collections | `design/concept-collection.astro` + `design/index.astro` | Toegepast, maar methodische bron ontbreekt. Herkomst (college-onderwerp) maakt het bibliografisch zwak. |
| PELV-cyclus (Boehm) | `refine/prototyping.astro`, `refine/index.astro` | Toegepast als 4-stappen grid per iteratie. Expliciete PELV-labels staan er. Attributie aan Boehm is echter twijfelachtig (Boehm = spiraalmodel; PELV lijkt een Zwolse-lesterm). Check deze claim. |
| Rapid Prototyping (Tom Chi) | `refine/index.astro:50` | Slechts 1x genoemd. |
| Design Thinking (algemeen) | Door de site heen impliciet | Nooit expliciet via Zomer 2021 / Mueller-Roterberg 2018 attributie. |
| Ambidexteriteit (O'Reilly & Tushman 2013) | `deliver/roadmap.astro:41-65` + `deliver/index.astro` | Goed toegepast in startup-argumentatie. |
| Diffusie (Rogers 1962) | `deliver/roadmap.astro` (diffusie-sectie, 5 adoptiefactoren) | Sterkst toegepast op deliver. |
| Value Proposition Canvas | `refine/pivot.astro:219-353` | Toegepast met eigen invulling, bronnen BMI/Osterwalder ontbreken. |

**Ontbrekende theorieen uit CLAUDE.md (belangrijk):**
- **Bossink** (innovatiemodel) — nergens.
- **Van der Voort** (H1+H2 innovatie) — nergens.
- **Kastelle** (creativiteit vs. ondernemerschap) — nergens.
- **Derksen (2012)** (innovatieruimte, teamrollen) — nergens. Was specifiek genoemd als interessant voor teamsamenstelling.
- **Dodgson et al. (2008)** (proactive/active/reactive/passive strategies) — nergens.
- **Snowden (Cynefin)** — nergens. Was in casus relevant geweest bij scenariowerk.
- **BCG Growth-Share Matrix** — nergens, terwijl Aurora's portfolio bij uitstek hier voor zou roepen.
- **Suzuki (beginners mind)**, **Zomer (2021)**, **Mueller-Roterberg (2018)** — nergens.
- **Treffinger CPS** — alleen als HZWK-label. De bredere Creative Problem Solving-cyclus wordt niet gebruikt.
- **Andler (2016)** (problem clarification) — nergens, hoewel de pivot er om schreeuwde.
- **Kelley — 10 Faces of Innovation** — nergens.

**Kritische reflectie op theorie (uitmuntend-niveau):** nergens beoordeel je een theorie op tekortkomingen. Uitmuntend vereist "kritisch beoordeeld op waarde voor het proces". Voorbeelden die zouden werken:
- "IBSOTEEP dwong breder kijken, maar maakte het vooral bibliografisch, weinig inzicht in hoe de acht dimensies samenhangen."
- "Huizingh's innovatieradar is een zoeklamp, niet een ordener. Bij het brainstormen bleek dat ideeen naar meerdere dimensies tegelijk vallen."
- "DVF is een checklist die suggereert objectiviteit waar die er niet is. Wij kozen uiteindelijk op gevoel (Security Expert scoorde 73, Circulair 74)."

Dit type zin is nu nergens aanwezig.

**Overlap/dubbelingen:** HZWK staat zowel op `discover/challenges.astro` (5 challenges) als op `define/convergentie.astro` (HZWK per innovatieruimte). Opzettelijk (verschillende fases), maar dat is nergens expliciet gemaakt.

---

## Bewijsstukken-inventarisatie

**Discover**
- Trends: IBSOTEEP-kaarten, Porter-kaarten, trendpiramide-SVG, S-curve-SVG, Christensen-sectie, klasdiscussie-notitie. Sterk.
- Scenario: 2x2 matrix, Brief uit 2030 (AI-image), Early warning signals. Voldoende.
- Empathise: timelapse-video sessie 1, whiteboard-foto, observaties, dreams/gripes clusters, 2 interviews. Thin op interviews (zie CLAUDE.md TODO), maar wel aanwezig.
- Challenges: 5 HZWK-kaarten, hero-image. Compact.

**Define**
- Innovatieradar: 12 dimensies-tabel, 2 foto's van sessie 3 (flipover), 32 ideeen per kamer. Goed.
- Convergentie: PMI-uitleg + 3 HZWK-blokken per ruimte. **Geen foto's van PMI-stickers.** Gemiste kans, want CLAUDE.md vermeldt die wel.
- Denkrichtingen: AI-images per richting, clusters, challenge, traceerbaarheid. Mooi.

**Design**
- Gate: value curve-foto, 2 DVF-foto's, score-blokken. Prima, kon rijker (bijv. quotes van Niels en Niels, wat zeiden ze precies?).
- Concept Collection: downloadbare pptx, lijstjes productvormen/authenticatiemethoden/kruisbestuivingen. Visueel zwak op de site zelf — de 35+ afbeeldingen zitten achter een download. **Grote gemiste kans:** toon bijvoorbeeld een 6-grid thumbnail van de moodboard inline op de pagina.

**Refine**
- Prototyping: 2 PELV-iteraties expliciet, foto's postits (2x), schetsen (3x), rapid prototype (3x), paper mockups (2x), vragenlijst. Zeer sterk.
- Pivot: tekst, 3 procesflow-SVGs (1 inline, 2 in lightbox), huidig-vs-nieuw vergelijking, VPC, pptx-download. Sterk.

**Deliver**
- Index: Gate 2 DVF-scores (4 getalblokken), 4 DVF-formulier-foto's in details-tag. Goed.
- Proof of Value: challenge, concept, 4 vorm-blokken, procesflow, waardepropositie-3-kolommen, DVF-beoordeling, eerlijk-verhaal, 3 inkomstenstromen. Inhoudsrijk maar consultancy-aangevoeld.
- Roadmap: Ambidexteriteit, 4-fasen timeline, diffusie per sector, adoptie 5-factoren, risico-mitigatie. Inhoudsrijk.

**Missende bewijsstukken (t.o.v. CLAUDE.md en opdracht):**
- Foto's van PMI-stickers tijdens convergentie.
- Originele flipover/post-it-foto's van sessie 1 immersive research zijn er wel (`sessie1-foto.jpeg`), maar geen foto's van sessie 2 met users — wel de dreams/gripes AI-image. De interviews voelen daarom secundair.
- **Geen teamfoto, geen procesverslag-stuk waarin Anke, Lianne, Jr ook echt als personen zichtbaar zijn**, behalve in de footer.

---

## Bronnen & hyperlinks

**Waar het goed gaat:**
- `discover/trends.astro`: 20+ bronnen, allemaal als klikbare Wikipedia/URL-linkjes en nummerverwijzingen naar `sourceUrls`-map. Mooi uitgewerkt.
- `discover/scenario.astro`: early warning signals met elk een klikbare source. Alleen "Aurora casusmateriaal EDIM.21" is terecht niet-klikbaar.

**Waar het misgaat:**
- `discover/challenges.astro:88`: "Treffinger (1995), Creative Problem Solving" — **platte tekst**, geen URL.
- `define/convergentie.astro:33-65`: "PMI-methode" — **geen bron**. De Bono wordt nergens genoemd, niet klikbaar.
- `define/innovatieradar.astro:104-108`: Huizingh (2019) genoemd, maar **geen klikbare bron**.
- `define/denkrichtingen.astro:102`: "Huizingh (2019)" platte tekst.
- `design/gate.astro`: DVF nergens geattribueerd (IDEO?) — geen bron.
- `design/index.astro:54-56`: DVF, Blue Ocean, Concept Collections allemaal zonder link.
- `refine/index.astro:49-51`: Boehm, Tom Chi — **geen bronnen, geen links**. Bovendien is "PELV-cyclus (Boehm)" twijfelachtig qua attributie (Boehm = spiraalmodel, niet PELV).
- `deliver/index.astro` & `deliver/roadmap.astro`: O'Reilly & Tushman (2013), Rogers (1962) — beide zonder URL.
- `deliver/roadmap.astro:324`: "70% van productlanceringen faalt (les 8)" — verwijst naar een les, **geen externe bron**. Docent verwacht een marketingonderzoek.

**Impact:** CLAUDE.md eist "ELKE bron moet klikbare hyperlink zijn". Op Discover is dat goed; op Define/Design/Refine/Deliver niet. Grofweg 15+ bronverwijzingen mist hyperlink.

---

## AI-TOON SWEEP (uitputtend per pagina)

### Em-dashes in lopende tekst/UI
28 incidenten in 13 bestanden. Een flink aantal zit in `<title>`-strings ("Trendanalyse — Discover"). Dat valt buiten zichtbare body maar staat wel in tab-titel en is nog steeds zichtbaar.

**Zichtbaar in body/content:**
- `discover/empathise.astro:130`: `Sessie 1 — Learn from Experience` (heading).
- `discover/empathise.astro:149`: alt-tekst `Sessie 1 — brainstorm resultaten op whiteboard`.
- `discover/empathise.astro:173`: `Sessie 2 — Learn from Users`.
- `define/innovatieradar.astro:134`: lijst-item `{d.naam} — {d.beschrijving}`.
- `define/innovatieradar.astro:148`: `Sessie 3 — Innovatieradar`.
- `define/innovatieradar.astro:158`: alt `Innovatieradar flipover — Product & Paradigma kwadranten met post-its`.
- `define/innovatieradar.astro:164`: alt `... — alle zes kamers met post-its`.
- `refine/prototyping.astro:102/106/110/114/226/230/234/238`: 8 em-dashes in `P — Plan` / `E — Experiment` / `L — Learn` / `V — Verbeter` blokjes. Zeer zichtbaar.
- Page-titel em-dashes op 11 paginas ("Challenges — Discover" etc.).

**Aanpak:** vervang door en-dash (–), dubbele punt, gewone punt of komma. Voor PELV-labels bijvoorbeeld `P — Plan` naar `P: Plan` of `P - Plan`.

### Taglines, oneliners, te netjes parallel
- `discover/scenario.astro:217`: "Wat als Aurora NIET innoveert?" — tagline.
- `discover/scenario.astro:229`: "Waarom NU?" — tagline-cadence, met "Vijf redenen waarom Aurora niet kan wachten" eronder (pitch-toon).
- `discover/trends.astro:317`: quote in italic "De grootste bedreiging komt niet van andere pennenmakers, maar van tech-bedrijven die schrijven helemaal opnieuw definieren." — **klassieke "Niet X, maar Y"-constructie die Jr heeft aangegeven te willen vermijden.**
- `design/concept-collection.astro:59`: "Alles verzamelen wat ook maar iets te maken heeft met authenticatie en verificatie. Hoe wilder, hoe beter." — goed, natuurlijk, hoeft niet weg.
- `design/concept-collection.astro:90-91`: "Maximaal divergeren / Weg van de pen, alle kanten op" — lichte tagline-toon.
- `refine/pivot.astro:211`: "Niet meer de maker van de pen, maar de expert op het gebied van ondertekenen." — **Niet-X-maar-Y-constructie, opnieuw.**
- `refine/pivot.astro:212`: "Aurora weet als geen ander wat een handtekening betekent, hoe mensen ondertekenen en waarom dat belangrijk is. Die expertise is de echte waarde, niet het schrijfgereedschap." — "als geen ander" is een reclamefrase. "De echte waarde is X, niet Y" is weer de inverse-formule.
- `refine/pivot.astro:349-350`: "De pen blijft bestaan, maar het bewijs verschuift van de krul op papier naar de koppeling tussen ID, moment en handeling." — te gestileerd voor een reisverslag. Klinkt als pitch-deck.
- `deliver/proof-of-value.astro:222-225`: "Aurora weet als geen ander wat ondertekenen betekent. Die kennis is waardevoller dan de pen." — dezelfde frase tweemaal op de site.
- `deliver/proof-of-value.astro:21`: "Wat is de aantoonbare meerwaarde van deze innovatie? En hoe ziet het er in de praktijk uit?" — rhetorische vraag, tv-reclame-ritme.

### Corporate jargon / theorie-termen waar Jr alert op wou zijn
- `define/innovatieradar.astro:13`: "Kan een complete **paradigmashift** zijn!" — dit woord stond expliciet op Jr's AI-tone-blacklist.
- `define/denkrichtingen.astro` (meerdere): "convergeren", "divergeren" worden in uitleg gebruikt — OK als theorie-term, mits consistent gelabeld.
- `deliver/roadmap.astro:41-43`: "ambidexteriteit (O'Reilly & Tushman, 2013): de mate waarin een organisatie in staat is om tegelijk te optimaliseren ... en te verkennen" — dit is theorie, prima.

### Perfect parallelle opsommingen (AI-tell)
- `refine/pivot.astro:76-99`: Drie blokken "Veiliger / Efficienter / Toegankelijker" met elk exact 2-zin-paragraaf, ~zelfde lengte, ~zelfde structuur. **Klassieke AI-opsomming.**
- `deliver/proof-of-value.astro:129-181`: "Notaris / Bank / Verzekeraar-accountant" met elk 3 bullets, exact parallel qua structuur.
- `deliver/roadmap.astro:82-161`: 4 fasen (Oprichting, Ontwikkeling, Pilot, Opschaling) met elk "titel + tijdsindicatie + 1 paragraaf + 3 tags". Te strak.
- `deliver/roadmap.astro:263-313`: 5 Rogers-adoptiefactoren met **allemaal dezelfde structuur** "Score: X. [zin] [zin]." Dit schreeuwt AI.
- `deliver/roadmap.astro:329-354`: 4 risico-blokken: "Risico / Mitigatie" — OK voor leesbaarheid, maar bevestigt het patroon.

### Parallel-patroon op fase-indexpaginas
Alle 5 fase-indexen (`discover/index`, `define/index`, `design/index`, `refine/index`, `deliver/index`) hebben identieke koppen: "Wat hebben we gedaan?" → "Wat viel op?" → "Bewijsstukken" → "Theorie en methode". Dit is bibliotheek-sjabloonwerk, niet reis-schrijven. Docent zal dit herkennen als template.

### HZWK-lengte
- `define/convergentie.astro:85-87`: "Hoe zouden we een analoog product kunnen voorzien van slimme beveiligingsfuncties die passen bij privacy en persoonlijk gebruik?" — 18 woorden. Net onder de grens.
- `define/convergentie.astro:87`: "Hoe zouden we kunnen zorgen dat een product persoonsgebonden beveiliging biedt voor privacygevoelige toepassingen zoals handtekeningen?" — 16 woorden, maar klinkt als ambtelijk Nederlands door "persoonsgebonden ... privacygevoelige".
- `define/denkrichtingen.astro:22`: "Hoe zouden we een pen kunnen ontwikkelen die via biometrie bewijst wie er geschreven heeft, zodat een handtekening op papier net zo veilig wordt als een digitale?" — 27 woorden, **te lang**.
- `define/denkrichtingen.astro:47`: "Hoe zouden we Aurora kunnen laten voorlopen op duurzaamheidsregels, zodat strengere wetgeving concurrenten raakt maar Aurora juist sterker maakt?" — 21 woorden, te lang.

### Eerlijk-verhaal-secties (positief)
- `refine/pivot.astro:187-216`: "Eerlijk verhaal"-sectie erkent concurrenten (DocuSign/PKIsigning) en dat Aurora's bijdrage het inzicht is. **Goed.** Dit is reis-toon.
- `deliver/proof-of-value.astro:217-226`: "Eerlijk verhaal"-blok herhaalt hetzelfde, minder sterk omdat het al gezegd is.

---

## Visuele samenhang

**Sterk:**
- Fase-kleuren consistent door de hele site gebruikt (Discover coral, Define blue, Design lavender, Refine amber, Deliver green). Navigatie-dots matchen landschap-stations.
- Hero-sectie-patroon vast: bg-bg-primary + backdrop-blurbol + breadcrumb + titel met gradient-text + subtekst + gekleurd lintje.
- Patrick Hand (display/koppen) en Kalam (body) consequent via `--font-display` en `--font-sans`.
- Kaart-hover-animaties (hover:scale-[1.02]) en reveal-animaties (scroll-observer in BaseLayout) zitten overal.
- SVG-gebruik waar het telt: trendpiramide, S-curve Christensen, procesflows (hoogover/uitgebreid/voorbeeld), VPC. Zelfs de emoji-iconen (🔬, 🎨, 🔧) staan in .astro-props. Aurora-logo in SVG.

**Zwak / aandachtspunten:**
- Emoji-iconen inline (🚪, 🎨, 🔧, 🔄, 🚀, 🗺️): mix met SVG's geeft lichte inconsistentie. Werkt visueel maar kan strakker.
- `pivot.astro:104` Procesflow-SVG rendert op witte achtergrond binnen donker thema (`bg-white` class). Dat is bewust (SVG is voor witte ondergrond gemaakt) maar creeert een visueel breuk. Overweeg SVG-invert of donkere variant.
- **Moodboard-visualisatie op `concept-collection.astro` ontbreekt.** 35+ afbeeldingen staan in de pptx maar de pagina zelf toont geen enkele afbeelding uit de moodboard. Dat is een gemiste kans — Jr's feedback "visueel eerst" zegt precies dit. Zou een 6-12 grid thumbnail sterk maken.
- De "tabs" in de navigatie tonen op mobile alleen dots (label hidden md:inline). Op smaller schermen is de navigatie kryptisch.

**Afbeeldingen per fase:**
- Discover: dreams-gripes (AI), challenges-hero (AI), brief-2030 (AI), sessie1-foto, sessie1-timelapse, sessie3-radar (2x). Sterk.
- Define: innovatieradar-hero, sessie3-radar x2, denkrichting1-security-expert, denkrichting2-circulaire-standaard. Goed.
- Design: gate-value-curve, gate-dvf-1/2. Matig (maar 3 foto's bestaan op disk, niet alle 5). Zie CLAUDE.md vermeldt 5 gate-foto's.
- Refine: 7+ foto's, 2 video's, 3 SVG-procesflows. Zeer sterk.
- Deliver: 4 DVF-formulier-foto's (in collapsed details), procesflow-SVG (hergebruikt). Schraal. Geen foto van team, geen schets van het Proof-of-Value device.

---

## Leerervaring-zichtbaarheid

**Sterk (leerervaring zichtbaar):**
- `refine/pivot.astro:34-45`: "Dat was even schrikken, want we waren al een tijdje bezig met 'de analoge security expert'. Maar achteraf gezien was het logisch..." — dit is wat de opdracht bedoelt met reisverslag.
- `refine/prototyping.astro:326-328`: "Dat was het moment dat we dachten: wacht even, we lossen het verkeerde probleem op." — idem.
- `design/gate.astro:92-96`: "We hadden meteen concrete beelden ... bij de Circulaire Standaard voelde het meer als een theoretisch verhaal. Interessant, maar we konden ons er minder goed in vastbijten." — nuchter, natuurlijk.

**Zwak (successtory-toon):**
- Deliver-paginas lezen als pitch naar een MT. Geen "we twijfelden", "we wilden eerst X", "dit vonden we lastig".
- Team-dynamiek komt niet aan bod. McKinsey-teamrollen (Jr: Generating/Pioneering/Tabulating; Lianne: Networking/Pioneering; Anke: Motivating/Absorbing) zijn bewust gedocumenteerd in `docs/onderzoek/mckinsey-teamscores.md` maar worden nergens op de site gedeeld. Dat is een gemiste kans. Bij opdracht 2b (rolontwikkeling) hoort dit, maar voor een reisverslag zou je best mogen laten zien dat Jr veel tabulating doet, Lianne aan netwerken, Anke aan motiveren.
- `discover/empathise.astro`: CLAUDE.md's TODO "diepte empathise" is zichtbaar: interviews zijn nog bullet points zonder quotes. Dat komt over als netjes, maar niet als immersie.
- Fouten: de Circulaire Standaard is "bewust laten vallen na de gate" (`design/concept-collection.astro:167`). Dat is eerlijk, maar zou sterker zijn met een reflectie "we wisten nog niet of dat goed was".

**Conclusie:** De leerervaring is er, maar ongelijk verdeeld. Refine + Pivot staan als leerreis; Deliver leest als eindpresentatie.

---

## Technische hygiene

**Onderzocht via source (geen agent-browser gebruikt, review-taak):**

- Alle `url()` helper-aanroepen zien er correct uit; base-path wordt consistent toegepast.
- Alt-tags: decoratieve hero-backgrounds gebruiken `alt=""` (semantisch correct voor puur visueel). Content-afbeeldingen hebben beschrijvende alt-teksten. Accessibility-basics ok.
- Scroll reveal-observer in BaseLayout geldt voor alle `.reveal`-elementen. Werkt.
- Lightbox-modals op pivot-pagina hebben Esc/close/klik-buiten handlers (`pivot.astro:372-396`). Goed.
- Porter + IBSOTEEP overlays werken identiek via data-attributes + JS. Goed.

**Potentiele issues:**
- `src/pages/refine/[slug].astro`, `define/[slug].astro`, `design/[slug].astro` zijn dynamische routes. Check wat er gebeurt als je naar `/refine/foo` gaat. Zo niet gebruikt, verwijder.
- `public/presentatie-pivot.pptx` en `public/concept-collection-security-expert.pptx` zijn downloadlinks. Check of paden kloppen met `url()`-helper bij deployed base path. `concept-collection.astro:159` gebruikt `url('/concept-collection-security-expert.pptx')`, klopt.
- `refine/pivot.astro:335`: downloadlink naar `presentatie-pivot.pptx` OK.
- Breadcrumb-bug op `denkrichtingen.astro:72`.
- Deliver-index eindigt abrupt zonder verder-knop.

**Mobile responsive:**
- Grids gebruiken `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`-patroon: OK.
- Navigation-labels verstoppen onder md: alleen dot zichtbaar.
- VPC-SVG op `pivot.astro` heeft `min-w-[900px]` + overflow-x-auto. Werkt, maar geeft horizontaal scrollen op mobile.
- 2x2 matrix `scenario.astro:180-208`: op md+ werkt het, mobile wordt 1-kolom. OK maar verliest de 2x2-visual.
- Homepage-landschap (max-w-5xl) + 5-kolom fase-grid (`grid-cols-5`): op mobile worden 5 kolommen krap. Text wordt erg klein.

---

## Concrete verbeteringen

### Blokkerend voor 8+

1. **Em-dashes wegwerken.** Minstens uit zichtbare content: `refine/prototyping.astro` (8x in PELV-labels), `empathise.astro`, `innovatieradar.astro` (Sessie 3 heading + alt-tekst), `title`-strings. Vervang door `:` of `-`.
2. **Breadcrumb-bug fixen** op `denkrichtingen.astro:72` (Design → Define).
3. **"Als geen ander" + "Niet X, maar Y"-constructies herschrijven** op `refine/pivot.astro:211-213` en `deliver/proof-of-value.astro:222`. Jr's eigen feedback-instructies benoemen dit expliciet.
4. **"Paradigmashift!" uit `define/innovatieradar.astro:13`** verwijderen. Vervang door "Kan een echte kentering zijn" of "Raakt het hart van hoe Aurora zich positioneert".
5. **Bronnen klikbaar maken waar ze platte tekst zijn:** Treffinger (challenges), Huizingh (innovatieradar + denkrichtingen), De Bono PMI (convergentie), DVF (design), Boehm PELV (refine), O'Reilly & Tushman (deliver), Rogers (deliver). Minstens 8 ontbrekende links.
6. **PELV-attributie checken.** Boehm is spiraalmodel, niet PELV. PELV komt eerder uit action-learning-literatuur (Kolb-cyclus achtig). Liever niet een foutieve attributie houden — docent zal het opvallen.
7. **Deliver-index "Verder/Einde"-knop toevoegen.** "Einde van de reis — terug naar home" of naar roadmap.
8. **Parallel-template van fase-indexen doorbreken.** Op minstens 2 van de 5 fase-indexen: andere kop, andere volgorde, een persoonlijke opening ("We gingen Discover in met het idee dat..."). Voorkomt AI-tell.

### Nice-to-have voor 10

9. **Concept-collection-pagina visueel maken.** Minstens 6-12 thumbnails uit de moodboard inline tonen, niet alleen pptx-download.
10. **Interviews (Anna, Famke) verrijken met quotes en context.** Een zin per persoon die ze letterlijk zei, onderschrift over wie ze zijn.
11. **Kritische reflectie op theorieen toevoegen.** Per fase 1 blokje "Wat deze theorie WEL en NIET oploste voor ons". Voorbeelden in de Theorie-sectie hierboven.
12. **Missende theorieen uit CLAUDE.md alsnog aanraken:** minstens Bossink, Derksen (teamrollen), Dodgson (strategieen), Snowden (Cynefin bij scenario), BCG (Aurora's portfolio). 2-3 paragrafen elk.
13. **Teamdynamiek zichtbaar maken.** Een kleine sectie met de McKinsey-teamrollen op bijv. Define of Deliver: "Lianne hield het netwerkt levend, Anke zorgde voor motivatie, Jr...". Niet bij 2b wachten.
14. **Aanleiding-link vanuit Discover/Trends.** De tijdlijn blijft nu geisoleerd.
15. **Foto's van PMI-stickers** toevoegen aan convergentie-pagina. Als ze bestaan in `docs/onderzoek/` of teams-map.
16. **Gate-pagina: quotes van Niels en Niels**, wat zeiden ze letterlijk toen ze scoorden?
17. **"Wat hebben we NIET gedaan"-paragraaf op Discover of Deliver.** CLAUDE.md heeft een lijstje (90 ideeen niet gehaald, concept collection 2 niet gedaan, geen externe gate). Eerlijk benoemen versterkt uitmuntend-oordeel voor leerervaring.
18. **Bronnen-sectie per pagina** zoals die op `trends.astro` staat (collapsible details), ook op andere paginas.

### Originele zetten die een 10 kunnen pakken

19. **"Onze twijfels"-knop per fase.** Klein uitklapbaar blok met 2-3 zinnen "waar we vast zaten". Maakt reisverslag.
20. **Gedeelde concept-collection-grid.** Toon de 35+ afbeeldingen als scrollbaar grid met on-hover tags (productvorm/authenticatie/kruisbestuiving). Is divergeren zichtbaar maken.
21. **Een "laat je zien hoe je hiertoe kwam"-animatie bij de pivot.** De procesflow-SVG kan een kleine fade-in-stagger krijgen om de verschuiving te tonen: eerst pen, dan doorgestreept, dan ID+PIN. Design Thinking in beeld.
22. **Scoring-transparantie.** Hoe zijn de DVF-scores (4.5, 3.8, 3.4, 1.8 op Deliver) tot stand gekomen? Geef een kleine matrix met de individuele scores van 4 beoordelaars zichtbaar — dan zie je ook spreiding.
23. **Time-capsule terugblik per fase.** Kleine "Als we opnieuw zouden beginnen"-blok per fase. Past bij rubric-criterium "reflectie op eigen leerproces".
24. **Team-story op aanleiding of een aparte "Over ons"-pagina.** Team-foto, McKinsey-rollen, wie deed wat, waar zat de spanning. Docent wil dit zien.

---

## Cijferinschatting

- **Portfolio als geheel nu: 7.5/10.** Tussen "Voldoende (6)" en "Goed (8)". De bewijsstukken zijn compleet per fase, theorieen zijn basaal-naar-redelijk toegepast, navigatie is in orde, pivot toont leerervaring. Maar theorie-breedte is schraal, kritische reflectie ontbreekt, AI-toon incidenten geven een synthetische afwerking, en Deliver voelt als pitch-deck.
- **Na prio-1 fixes: 8.5/10.** Als em-dashes weg zijn, bronnen klikbaar, breadcrumb gefixed, PELV-attributie gecheckt, parallel-template doorbroken en een paar "als geen ander"-formuleringen herschreven, staat de site op goed niveau "Gangbare theorieen worden kritisch beoordeeld op waarde voor het proces en op eigen (situatie-aangepaste) wijze toegepast".
- **Uitmuntend-potentieel: 9-9.5/10.** Haalbaar met nice-to-haves 9-14: kritische reflectie per theorie, team-dynamiek zichtbaar, interviews verrijkt, theorie-breedte vergroot (Bossink/Derksen/Dodgson/Snowden/BCG), aanleiding-integratie, concept-collection-visueel. De 10 komt alleen met de originele zetten 19-24 (twijfels-blokken, time-capsules, team-story, zichtbaar maken van convergeer/divergeer-dynamiek). Die zijn ambitieus, maar leveren precies wat de rubric bij "Uitmuntend" omschrijft: eigen toepassing, diepgaand/breed inzicht, navolgbaarheid, reflectie op eigen leerproces.
