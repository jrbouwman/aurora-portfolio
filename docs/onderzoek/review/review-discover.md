# Review Discover fase

Scope: homepage + `/aanleiding/` + alle vier discover-pagina's (`trends`, `scenario`, `empathise`, `challenges`). Bron: source in `src/pages/` (server draait op localhost:4321 maar fetchen was geblokkeerd; source is de waarheid). Review gericht op rubric-niveau "uitmuntend" (10) voor 1a-Innovatieportfolio. Drie perspectieven expliciet gescheiden: docent Henk, MT/directie, critical friend.

Overgeslagen zoals afgesproken: onderzoeksplan empathise (1 A4), te magere interviews, structuurdocument, GenAI-verantwoording.

---

## Samenvatting

- **Basis is zeer solide (ruim goed, richting zeer goed).** De Discover-fase heeft alle verplichte ingredienten: IBSOTEEP + Porter + trendpiramide, een 2x2 scenariomatrix met gekozen assen, twee immersive sessies, 5 HZWK-challenges, en 20 gehyperlinkte bronnen. De visuele uitvoering (klikbare overlays, hand-drawn piramide, S-curve) is ver boven het niveau van een standaard portfolio en onderscheidt zich van de meeste teamgenoten.
- **Drie blokkerende zwaktes voor een 10.** (1) Er ontbreekt een expliciete kritische reflectie op de methoden zelf ("waarom deze theorie, wat leverde het wel/niet op?") die de rubric eist voor "uitmuntend". (2) Urgentie + belang voor de directie is verspreid en oppervlakkig onderbouwd, geen getalletjes koppelen aan gevolgen voor Aurora's P&L. (3) Scenario's hebben geen impactbeschrijving per stakeholder (finance/ops/HR) en zijn visueel vrij tekstdicht zonder echt matrix-gevoel.
- **Narratieve samenhang is redelijk, maar mist een rode draad "van trend naar challenge".** De sprong van scenariomatrix naar immersive research naar challenges wordt niet expliciet gemaakt. De scenariokeuze B ("Gouden Kruispunt") op de index wordt niet zichtbaar teruggekoppeld in empathise/challenges.
- **Geen zware AI-tone-incidenten in lopende tekst.** Em-dashes komen uitsluitend voor in page-titles en H2-koppen (zeven incidenten). Een handjevol taglines/pitch-achtige oneliners in scenario.astro en trends.astro. Corporate jargon vrijwel afwezig.
- **Alle bronnen zijn klikbaar.** 20 bronnen, allemaal werkende URLs vanuit `sourceUrls`-map, inclusief de Porter-overlays en trendpiramide. Aurora casusmateriaal is correct gelabeld als intern.

---

## Sterke punten

- **Breedte en diepte van de trendanalyse.** IBSOTEEP met acht letters (inclusief Identiteit en Onderwijs), Porter in plus-vorm met correcte dreiging-scores, trendpiramide met mega/macro/micro-niveaus expliciet gelabeld en een S-curve die de disruptive innovation-theorie illustreert. Dit past methodisch op goed tot zeer goed niveau.
- **Expliciete koppeling aan extra theorie.** Christensen's Innovator's Dilemma is niet zomaar genoemd maar toegepast: "de klanten van morgen groeien op met iPads" en de kernboodschap "luisteren naar bestaande klanten is de valkuil" is correct geparafraseerd. Dat is precies de kritische theorie-toepassing die de rubric op 8+ verwacht.
- **Bronnenhygiene.** `src/pages/discover/trends.astro:5-26` centraliseert alle URLs in een `sourceUrls`-map en hergebruikt ze. Gevolg: elke bronverwijzing heeft een werkende hyperlink, ook in de overlays. Voldoet aan de CLAUDE.md-eis "ELKE bron klikbaar".
- **Interactieve SVG's en overlays.** Porter-kaarten zijn klikbaar met scenario-specifieke detailteksten, IBSOTEEP heeft zelfde patroon. De trendpiramide is een echte SVG, geen stockafbeelding. Disruptive Innovation S-curve is custom. Dit rechtvaardigt het predicaat "originele toepassing" als Jr dit in de reflectie verwoordt.
- **Scenario-assen zijn twee echte onzekerheden.** Tempo digitale adoptie + overheidsregulering zijn goede scenario-assen (onafhankelijk, echt onzeker, strategisch impactvol). Dit is vakkundig; veel teams kiezen hier twee assen die onderling afhankelijk zijn.
- **Early Warning Signals.** `src/pages/discover/scenario.astro:60-103` is een sterk onderdeel dat niet eens verplicht is: zes concrete signalen waar Aurora op kan letten, elk met bron. Dit tilt het scenario-hoofdstuk boven standaard uit.
- **Brief uit 2030.** Visueel krachtig, voldoet aan "schets een mogelijke toekomst als het bedrijf NIET innoveert" uit de opdracht (`docs/opdrachten/opdracht-1a-discover.md:33`).
- **Paradoxblok in aanleiding.** "Schrijven op papier wordt steeds zeldzamer, maar tegelijk steeds waardevoller" is een goede framing die de kernvraag helder maakt en geen tagline-toon heeft.
- **HZWK-formulering is kort en concreet.** `src/pages/discover/challenges.astro:10-44` heeft 5 challenges van elk circa 10-15 woorden, elk met "Basis" (dreams/gripes herkomst) en "Thema". Dat voldoet aan de 15-woorden-eis uit CLAUDE.md en aan Treffinger's HZWK-structuur.

---

## Kritische zwaktes

### Perspectief Docent Henk (rubric-in-hand)

1. **Geen expliciete methode-reflectie.** De rubric stelt voor "goed (8)": theorieen "kritisch beoordeeld op waarde voor het proces". Voor "uitmuntend (10)" wordt verwacht dat de methode-keuze zelf verantwoord wordt. In `discover/index.astro:66-73` staat wel een rijtje "theorie en methode" maar dit is bullet-point-niveau uitleg ("Helpt om..."). Er ontbreekt: wat viel er juist niet onder IBSOTEEP, waarom kozen we Porter EN IBSOTEEP (overlapt), wat deed de trendpiramide dat IBSOTEEP niet deed, en waarom geen VRIO of PESTLE? Dit is waar de 9-10 wordt verdiend.
2. **Aanleiding-pagina reflecteert weinig over het proces.** `src/pages/aanleiding.astro` is mooi maar puur historisch. De koppeling "elke grote verschuiving volgde hetzelfde patroon: nieuwe technologie, gevestigde spelers reageren te laat" (`src/pages/aanleiding.astro:76`) is een goede observatie maar wordt niet methodisch uitgewerkt. De docent zal vragen: welk disruptie-patroon is dat precies, en hoe is dat empirisch onderbouwd per mijlpaal?
3. **Urgentie is aanwezig maar niet directie-klaar.** `scenario.astro:232-245` heeft een "Waarom NU?"-blok met 5 redenen, maar zonder concrete impact op Aurora's omzetmix (24% onderwijs, 31% creatief). De opdracht eist expliciet: "Overtuig de directie van: Urgentie (op welke termijnen kan er wat gebeuren?) Belang (wat is de impact op de organisatie?)" (`docs/opdrachten/opdracht-1a-discover.md:33-36`). De impact-kant is onderbelicht.
4. **Scenariomatrix-pagina is tekstdicht, niet echt een 2x2.** `scenario.astro:170-210` rendert vier cards in een 2x2 grid, maar het leest als vier losse kaarten naast elkaar, niet als een echte as-gebaseerde matrix. De Y-as-label staat roterend in een smalle kolom (`line 182-185`) maar is klein en weinig zichtbaar; de positionering van de kaarten op de assen wordt niet visueel gesuggereerd (geen pijlen, geen kwadrant-nummering die "links=langzaam" duidelijk maakt).
5. **Geen kritische bespreking empathise-methode.** `discover/empathise.astro:100-102`: "Het idee was om niet meteen in oplossingen te denken, maar gewoon te kijken wat er leeft." Dat is goed. Maar er is geen reflectie: werkte dit? Wat hadden we gemist zonder de observaties-sessie? Waarom geen "learn from observation"? Rubric-niveau 8+ vraagt hier expliciet om.
6. **Immersive research: minimaal 1,5 uur wordt niet aangetoond.** De opdracht eist "minimaal 1,5 uur totaal" (`opdracht-1a-discover.md:42`). Op de empathise-pagina staat nergens een tijdsaanduiding. Docent kan dit niet verifieren.
7. **Analyse van Aurora-strategie ontbreekt op de site.** De opdracht eist: "Analyseer de strategie van de organisatie. Beoordeel in welke mate de koers een antwoord geeft op de vragen uit de context" (`opdracht-1a-discover.md:22-25`). Die organisatie-analyse staat niet als aparte component op discover; het zit verspreid (omzetcijfers in IBSOTEEP-Economie). Expliciet missen: wat doet Aurora nu, en waar schiet die strategie tekort?

### Perspectief MT/directie (leest blind)

1. **"Wat wil je van mij?"-antwoord ontbreekt.** De pagina's zijn leerzaam, maar eindigen niet met een heldere aanbeveling aan de directie. Na empathise verwacht een directielid: "dus... dit betekent dat we X moeten doen". In plaats daarvan leidt de navigatie door naar "Challenges". Dat is logisch voor het design thinking-proces, niet voor een directielezer.
2. **Urgentie komt niet scherp binnen.** `scenario.astro:232-245` "Waarom NU?" voelt als losse claims. "Merk heeft nog waarde, over 5 jaar misschien niet" (reden 5) heeft geen bron of signaal eronder. Een directielid wil: op welk scenario zitten we nu waarschijnlijk, en welke early warnings zijn al geactiveerd?
3. **De Brief uit 2030 werkt, maar staat te geisoleerd.** `scenario.astro:214-224` is een prima narratieve hook, maar wordt niet opgevolgd met een concrete "als we niets doen, gebeurt dit in 2027, 2029, 2030"-tijdlijn. Docent-feedback op andere teams is vaak: een directie wil een tijdlijn zien, niet alleen een toekomstbeeld.
4. **Cijfers zijn er, maar worden niet gebundeld.** De euro-bedragen en groeicijfers liggen verspreid (IBSOTEEP-Economie, trendpiramide, Porter-substituten). Een directie wil op EEN plek: wereldwijde schrijfmarkt X, premium segment Y, onze (Aurora) omzet daalt van A naar B, de analoge-vs-digitale verhouding kantelt in jaar Z. Die executive summary mist op scenario of trends.
5. **De scenario-implicatie per scenario is zeer kort.** `scenario.astro:16, 29, 42, 55` geeft voor elk scenario een enkele zin "implication". Voor scenario B (Gouden Kruispunt): "Grootste kans voor Aurora: combineer erfgoed met innovatie en profiteer van regelgeving." Een directie vraagt: combineer hoe, welke regelgeving, met welke investeringen, op welke termijn?
6. **Discover/index.astro "wat viel op" is informeel en niet-sturend.** `src/pages/discover/index.astro:51-57`. Het cijfer "~20% in 10 jaar" wordt genoemd, maar direct erna volgt een informele zin "mensen missen niet per se betere pennen, ze waarderen juist het gevoel van schrijven". Dat laatste is een inzicht, maar niet iets waar de directie op kan sturen.

### Perspectief Critical friend / medestudent (theorie-check + narratief)

1. **IBSOTEEP-toepassing is correct, maar de 'I' is dun.** `trends.astro:36-42` heeft voor Identiteit drie bullets, waarvan twee over bullet journaling en digital detox. Dat is prima, maar Aurora's eigen identiteit (125 jaar, Nederlands, erfgoed) wordt niet bij 'I' geplaatst. Strikte IBSOTEEP-lezer zou Identiteit splitsen in "ideologisch klimaat buitenwereld" EN "identiteit organisatie". De O ("Omgeving") is nu hertaald naar Onderwijs, dat is op zich verdedigbaar maar wijkt af van Van Tilborgh.
2. **Porter is correct maar "substituten zeer hoog, rivaliteit hoog" is een standaard vaktaal-verhaal.** Goede kritiek zou zijn: hoe reageren gevestigde partijen (Faber-Castell, Staedtler) op digitale disruptie, concreet? Staan er al overnames, zijn er tech-partnerships? De Porter-overlays geven dit niet.
3. **Scenariomatrix-keuze voor B ("Gouden Kruispunt") wordt niet terug-gekoppeld naar de rest van Discover.** De index zegt "scenario B lijkt de meest realistische toekomst voor Aurora" (`discover/index.astro:54`), maar op `scenario.astro` wordt scenario B niet aangewezen als gekozen/meest waarschijnlijk. De empathise en challenges-pagina's verwijzen nergens terug naar dit scenario. Dat breekt de narratieve keten.
4. **HZWK-challenge #5 loopt vooruit op de pivot.** `challenges.astro:38-45`: "Hoe zouden we een pen kunnen beveiligen zodat je handtekening niet te vervalsen is?" is prima als challenge, maar de basis ("Dream: beveiligde pen met vingerafdrukherkenning") is NIET een cluster in empathise — daar staat het als een losse entry onder cluster "Beveiliging" met slechts 1 item (`empathise.astro:23-26`). Een critical friend ziet hier: HZWK #5 is backwards gepland vanuit de latere richting die jullie gekozen hebben. Dat kan, maar het ondermijnt de "divergeren"-claim van Discover.
5. **HZWK-formulering: #1 is prima open, #4 is te oplossings-gestuurd.** Challenge 4: "Hoe zouden we kunnen voorkomen dat pennen uitdrogen, lekken of kapotgaan?" is eigenlijk drie problemen in een zin en stuurt naar betrouwbaarheidsoplossingen. Volgens Treffinger moet de HZWK breed genoeg zijn voor creatieve oplossingen. Beter: "hoe zouden we schrijfgerei betrouwbaarder kunnen maken?"
6. **Dreams en gripes: alleen 1 item onder "Welzijn" en "Beveiliging" maakt de cluster zwak.** `empathise.astro:23-30`. Clusters met 1-2 items zijn geen clusters, dat zijn losse observaties. Beter samenvoegen of accepteren als "overige observaties".
7. **Observaties worden nu gepresenteerd als "niet dream, niet gripe" maar worden niet geanalyseerd.** `empathise.astro:54-66` lijst 11 observaties in de vorm "analoog vs digitaal", maar er is geen conclusie wat dit betekent voor de challenges. Gemiste kans.
8. **Trendpiramide: mooie SVG, maar mega/macro/micro-claims niet allemaal onderbouwd op de pagina zelf.** Op `trends.astro:529` staat onder micro: "Zweden: ~$45 mln/jaar in handschrift op scholen". Dat is eigenlijk politiek beleid (macro of zelfs mega), niet een microtrend. Microtrends horen 1-3 jaar te zijn. Critical friend-check: wat in deze piramide is echt 1-3 jaar oud, vs 10+ jaar?
9. **"Hybride tijdperk" in aanleiding-pagina (2020-nu) is conceptueel correct, maar wordt niet teruggekoppeld aan Aurora's positionering.** `src/pages/aanleiding.astro:24` benoemt het, maar de conclusie "dus Aurora zit in het hybride tijdperk" wordt niet getrokken.

---

## AI-toon incidenten (met citaat + pagina)

De lat is scherp: docent haakt af op AI-toon. Onderstaande incidenten zijn niet allemaal even erg, maar ze wegen op in een 10-oordeel. Alles staat in source; indien niet gefixt voor de deadline zijn ze zichtbaar op de site.

### Em-dashes (—) in lopende tekst

Geen directe incidenten in lopende zinnen. De gevonden em-dashes staan uitsluitend in page-titles en H2-koppen:
- `src/pages/discover/empathise.astro:69` `<BaseLayout title="Immersive Research — Discover">` (tab-titel, acceptabel)
- `src/pages/discover/empathise.astro:130` `<h2>Sessie 1 — Learn from Experience</h2>` (kop, net acceptabel; vervangen door ":" of "·" is veiliger)
- `src/pages/discover/empathise.astro:173` idem voor Sessie 2
- `src/pages/discover/challenges.astro:49` `title="Challenges — Discover"`
- `src/pages/discover/scenario.astro:106` idem
- `src/pages/discover/trends.astro:167` idem
- `src/pages/discover/empathise.astro:149` alt-text "Sessie 1 — brainstorm resultaten"

Verdict: alleen de H2-koppen voelen AI-achtig. Docent leest niet tab-titels. Advies: H2-koppen vervangen door "Sessie 1: Learn from Experience" (dubbele punt) of weghalen van de em-dash.

### Taglines / oneliners (pitch-deck-toon)

- **`src/pages/discover/trends.astro:317`** in Porter key insight: *"De grootste bedreiging komt niet van andere pennenmakers, maar van tech-bedrijven die schrijven helemaal opnieuw definiëren."* Dit is een pitch-quote. Docent-alarm. Suggestie: vervang door een platte conclusie zonder aanhalingstekens en zonder de "niet X maar Y"-structuur.
- **`src/pages/discover/scenario.astro:42`** voor scenario C: *"Meest verraderlijke scenario: het lijkt veilig, maar is het niet."* Typische tagline-structuur.
- **`src/pages/discover/scenario.astro:55`** voor scenario D: *"Existentiële crisis: overleving alleen door radicale transformatie."* Dramatisch-essayistisch, AI-achtig.
- **`src/pages/aanleiding.astro:44`** *"Van kleitabletten tot tablets."* Bekende tagline-structuur ("van X tot Y") die in tech-journalistiek veel gebruikt wordt. In combinatie met de "5000 jaar schrijven" hero is dit op het randje.
- **`src/pages/discover/index.astro:71`** *"De formulering 'Hoe zouden we kunnen...' houdt het open."* Uitleg is prima, maar de zin zelf heeft een tagline-ritme.
- **`src/pages/index.astro:94`** hero *"Hoe kan Aurora Writing Instruments Group relevant blijven in een wereld waarin schrijven en tekenen steeds digitaler worden?"* Als kernvraag legitiem, maar "relevant blijven in een wereld waarin..." is erg LinkedIn-post-toon.

### Perfect parallelle opsommingen (te glad)

- **`src/pages/discover/trends.astro:648-661`** "De disruptor / De blinde vlek / De oplossing" 3-tile-layout met drie even lange omschrijvingen. Dit leest exact als een consultant slide. Suggestie: asymmetrisch maken (1 langere + 2 kortere), of een minder "deck"-achtige framing kiezen.
- **`src/pages/discover/scenario.astro:233-238`** "Waarom NU?"-blok met vijf genummerde cards van elk 1 korte zin. Te gepolijst voor een studentenportfolio. Het is geen fout, maar in combinatie met de rest maakt het een pitch-deck-gevoel.

### Corporate jargon

- **`src/pages/discover/trends.astro:659`** *"richt een aparte eenheid op voor hybride innovatie, los van de kernbusiness"*. "Kernbusiness" is mild-corporate; "aparte eenheid" is ambidexteriteit-taal. Niet fout, maar flag.
- Geen "competitive moat", "paradigmashift", "synergieen" o.i.d. gevonden. Dit is OK.

### Samenvatting AI-toon

Geen disqualifiers, maar circa 5-6 incidenten die samen de indruk van "gemaakt met AI" kunnen versterken. Individueel niet erg, gecombineerd in de hero-quotes en bij implications wel. **Als Jr een 10 wil: fix de drie scenario-implications (`scenario.astro:16,29,42,55`), de Porter quote (`trends.astro:317`) en de drie H2-em-dashes.**

---

## Theorie-check (per theorie)

| Theorie | Toegepast? | Kritiek |
|---|---|---|
| **IBSOTEEP (Van Tilborgh, 2022)** | Ja, alle 8 letters ingevuld. | Correct. Zwakte: 'I' gaat over identiteit buitenwereld, niet Aurora's eigen identiteit; 'O' is hertaald van Omgeving naar Onderwijs (verdedigbaar maar wijkt af). Geen expliciete onderlinge weging — welke factoren zijn het belangrijkst? |
| **Porter's 5 Forces** | Ja, alle 5 krachten met dreigingsscores. | Goed uitgewerkt met overlays. Substituten is Zeer hoog, dat is verdedigbaar maar niet hard onderbouwd met cijfers in de overlay (geen % marktaandeel tablet-gebruik). De rivaliteit-analyse noemt wel namen (Faber-Castell etc.) maar geen marktaandelen. |
| **Trendpiramide (micro/macro/mega)** | Ja, visueel sterk. | Classificatie deels discutabel: "Zweden $45 mln/jaar" zit onder micro maar is beleidsmatig macro. Geen expliciete tijdshorizon per item. |
| **Scenariomatrix (2x2)** | Ja, twee scenario-assen gekozen met onderbouwing. | Assen zijn onafhankelijk en onzeker = goed. Matrix-visualisatie is echter meer een "grid van 4 cards" dan een echt coordinatenstelsel. Geen driving forces-analyse voorafgaand; waarom deze 2 assen en niet bv AI-adoptie vs vergrijzing? |
| **Disruptive Innovation (Christensen, 1997)** | Ja, expliciet als extra theorie. | Correct toegepast: "luisteren naar bestaande klanten = valkuil". S-curve visueel goed. Zwakte: de "oplossing" wordt opgesomd (aparte eenheid) zonder kritische vraag of Aurora dat kan. |
| **Immersive Research / Design Thinking** | Gedeeltelijk. Learn from experience + learn from users gedaan. | "Learn from observation" ontbreekt. Minimale 1,5 uur niet aangetoond. Geen onderzoeksplan (bekende gap). Methode-reflectie ontbreekt. |
| **HZWK / Creative Problem Solving (Treffinger, 1995)** | Ja, 5 challenges. | Formulering deels te oplossingsgericht (#4). #5 loopt vooruit op pivot. Verder prima. |
| **BCG / PLC / Dodgson's strategieen** | Niet toegepast op Discover. | Niet verplicht voor 1a, maar Dodgson's 4 strategieen zouden de "analyse bedrijfsstrategie" (rubric-eis) kunnen onderbouwen. Gemiste kans. |
| **VRIO / interne analyse Aurora** | Niet aanwezig. | De opdracht eist een analyse van Aurora's huidige strategie. Die staat niet expliciet op de site; moet nog. |

---

## Concrete verbeteringen

### Blokkerend voor een 8+ (moet echt gebeuren)

1. **Voeg een methode-reflectie toe aan `discover/index.astro`** (of als aparte sectie op elke pagina). Per methode 2-3 zinnen: waarom deze, wat leverde het op, wat was de beperking. Dit is de bottleneck voor elk cijfer boven de 7.
2. **Scenario.astro: wijs expliciet aan welk scenario het team als meest waarschijnlijk ziet en waarom.** Nu staat dit alleen in discover/index in een losse bullet. Maak een "Ons gekozen scenario: B — Gouden Kruispunt" blok met 3-5 argumenten + welke early warnings al actief zijn.
3. **Maak een Aurora-strategie-analyse-blok.** Ergens in discover (of aanleiding): wat is Aurora's huidige strategie (generiek qua portfolio, B2B via retail, geen D2C, geen digitale producten), waar schiet die tekort (uit omzetverschuiving). Dit is een expliciete rubric-eis die nu verspreid is.
4. **Fix de taglines/pitch-zinnen genoemd onder AI-toon.** Met name: Porter key insight (trends.astro:317), de vier scenario-implications (scenario.astro), "Waarom NU?"-blok afzwakken.
5. **Bundel de kerncijfers voor directie** op een plek (executive summary-blok op scenario-pagina of homepage): wereldwijde markt X, premium +Y%, Aurora's mix verschuift A→B over jaar Z, 5 early warnings.
6. **Documenteer tijdsbesteding immersive research** (minstens een zin: "sessie 1: 1u10min, sessie 2: 55 min, totaal 2u05min"). De opdracht eist 1,5 uur minimum, anders kan docent dit bewijsstuk afwijzen.
7. **Vervang em-dashes in H2-koppen** door ":" of "·". Voorkomt AI-vlag.

### Nice-to-have voor een 10

8. **Een derde immersive-methode (learn from observation).** Bijvoorbeeld een winkel bezoeken, 30 minuten observeren wie welke pen koopt. Korte fotomontage + 5 bullets.
9. **Reflectie per empathise-sessie** ("wat hadden we niet verwacht / wat verbaasde ons"). 3-4 zinnen per sessie.
10. **Koppel challenges expliciet aan de dreams/gripes-clusters** met klikbare verwijzing of pijl. Nu staat "Basis" als platte tekst; maak dit visueel traceerbaar.
11. **Verbeter HZWK #4** naar een bredere formulering ("hoe zouden we schrijfgerei betrouwbaarder kunnen maken").
12. **Scenario-pagina: voeg een tijdlijn toe onder de Brief uit 2030** ("2027: onderwijscontract verloren, 2028: marktaandeel -15%, 2029: Aurora als overnamekandidaat"). Maakt urgentie concreet.
13. **Trendpiramide: fix de Zweden-claim** (verplaatsen naar macro of anders inkleuren). Critical friend/docent zal hier puntjes op i zetten.
14. **Voeg een "driving forces"-analyse toe** aan scenariopagina: waarom deze 2 assen en niet andere (AI, demografie, supply-chain)? Korte 4-5 zin argumentatie.
15. **Methode-verantwoording IBSOTEEP vs DESTEP** (waarom IBSOTEEP, wat voegt 'I' en 'O' toe). Dit is precies het "eigen methode-keuzes verantwoord" uit rubric-niveau 10.
16. **Scenario B uitdiepen met stakeholder-impact**: wat betekent dit scenario voor finance, sales, productie, R&D van Aurora?
17. **Toevoegen van minimaal een korte reflectie op de Porter-analyse**: past Porter uberhaupt nog bij disruptieve markten (Christensen-kritiek)? Dit is precies wat "kritisch beoordeeld op waarde" betekent.

---

## Cijferinschatting

**Nu: 7.5 / 10** (ruim voldoende, richting goed)

Onderbouwing:
- Plus: alle bewijsstukken aanwezig, visueel professioneel, bronnen zijn klikbaar en goed onderbouwd, extra theorie (Christensen) correct toegepast, HZWK-methode gevolgd, scenario-assen goed gekozen.
- Min: methode-reflectie ontbreekt (kost 1 punt), urgentie/belang voor directie niet geconsolideerd (kost 0.5), Aurora-strategie-analyse ontbreekt als expliciet onderdeel (kost 0.5), licht AI-toon in implications/taglines (kost 0.5), narratieve koppeling scenario-keuze → challenges mist (kost 0.5).

**Na prio-1 fixes (punten 1-7 hierboven): 8.5 / 10** (goed)

Haalbaar in ~6-8 uur werk. Met fix 1 (methode-reflectie) + fix 2-3 (gekozen scenario + Aurora-strategie) + fix 4 (AI-toon) zit je op "goed (8)" volgens de rubric: theorieen worden kritisch beoordeeld op waarde en op eigen situatie-aangepaste wijze toegepast.

**Na nice-to-haves (punten 8-17): 9 - 9.5 / 10** (zeer goed, op het randje van uitmuntend)

Een echte 10 vereist dan nog: aantoonbaar originele toepassing (bijvoorbeeld IBSOTEEP kritisch vergelijken met DESTEP en beargumenteren welke beter past bij schrijfwaren), en een methodologisch weerwoord (bijvoorbeeld "Porter heeft als beperking X bij disruptieve markten, daarom hebben we ook Christensen gebruikt"). Die kritische reflectie op de waarde van de methoden zelf is het verschil tussen 9 en 10. Zonder aanvullend advies van de docent is 10 lastig te garanderen; 9 is realistisch haalbaar.
