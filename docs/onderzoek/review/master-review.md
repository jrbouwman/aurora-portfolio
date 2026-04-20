---
name: Master Review Aurora Portfolio
datum: 2026-04-19
reviewer: 6 Claude-agents, aggregatie door Claude
scope: 1a Portfolio (30%) + 1b Proof of Value (30%). Individueel werk 2a/2b niet meegenomen.
mikpunt: cijfer 10 (uitmuntend)
bekende gaps overgeslagen: onderzoeksplan empathise, 90 ideeen, concept collection 2, projectvoorstellen per denkrichting, externe gate, structuurdocument, GenAI-formulier
---

# Master-review Aurora portfolio

Deze aggregatie bundelt zes deelrapporten in `docs/onderzoek/review/`. Elk deelrapport bevat de volledige detailanalyse per fase, met drie perspectieven (docent Henk, MT/directie, critical friend), citaten met regelnummers en fase-specifieke verbeterlijsten.

## Cijferinschatting per fase

| Fase | Bestand | Nu | Na prio-1 | Uitmuntend-potentieel |
|---|---|---|---|---|
| Discover | `review-discover.md` | 7.5 | 8.5 | 9 - 9.5 |
| Define | `review-define.md` | 7.0 - 7.5 | 8.0 - 8.5 | 9 - 9.5 (10 vraagt eigen methode-aanpassing) |
| Design | `review-design.md` | 7.0 | 8.5 | 9.5 |
| Refine | `review-refine.md` | 7.5 | 8.0 - 8.5 | 9.0 (10 vraagt externe gate) |
| Deliver / PoV | `review-deliver-pov.md` | **6.5** | 8.0 | 9.5 - 10 |
| Holistisch | `review-holistic.md` | 7.5 | 8.5 | 9 - 9.5 |

**Gewogen prognose team-werk (1a + 1b, elk 30%):**
- Nu: ongeveer **7.0** (ruim voldoende, onder goed)
- Na prio-1 fixes: ongeveer **8.2** (goed)
- Uitmuntend-scenario: ongeveer **9.3** (zeer goed, richting uitmuntend)

De grootste hefboom zit in **Deliver + PoV** (weegt 30% en staat laagst). Tweede hefboom is de site-brede **AI-toon en kritische reflectie op theorieen**.

## Cross-cutting patterns (overal terug)

### 1. Kritische reflectie op theorieen ontbreekt

Rubric-10 vraagt: "theorieen kritisch beoordeeld op waarde voor het proces". Nergens op de site staat "wat IBSOTEEP/DVF/PELV/VPC wel en niet oploste voor ons". Dit is de grootste en tegelijk makkelijkst te fixen gap. Eén alinea per theorie per fase tilt dit van 8 naar 9.

### 2. AI-toon incidenten (docent haakt hierop af)

- 28 em-dashes verdeeld over 13 bestanden. Grootste concentratie: `refine/prototyping.astro` (8 in PELV-labels `P — Plan`), `empathise.astro`, `innovatieradar.astro`, alle page-titles.
- "Niet X, maar Y"-constructies op `pivot.astro:211`, `pivot.astro:212-213`, `proof-of-value.astro:222`. Jr heeft dit expliciet in eigen feedback-memory staan als te vermijden.
- "Als geen ander" op `pivot.astro:212` en `proof-of-value.astro:222` (dezelfde frase, twee plekken).
- "Paradigmashift!" op `innovatieradar.astro:13` (staat letterlijk op Jr's eigen blacklist).
- Parallel-template op alle 5 fase-indexen: identieke kopvolgorde "Wat hebben we gedaan / Wat viel op / Bewijsstukken / Theorie en methode". Oogt als AI-sjabloon.
- Strak-parallelle drievouden: Notaris/Bank/Verzekeraar-stakeholder-blokken (3x 3 bullets), Veiliger/Efficienter/Toegankelijker op pivot, 5 Rogers-factoren in identieke structuur op roadmap.

### 3. Bewijs ontbreekt waar het methodisch moet

- **PELV 2 testantwoorden** ontbreken op `refine/prototyping.astro`. Vragenlijst staat er, antwoorden niet. Zonder data is "cyclisch getest op meerwaarde" (rubric 1b=8) niet aantoonbaar.
- **PMI-stickerfoto's** ontbreken op `convergentie.astro`. Het woord "impliciet" op `denkrichtingen.astro:95` veroordeelt zichzelf.
- **DVF-subscores** ontbreken op `gate.astro`. Alleen totalen 74/73 zonder D/V/F-uitsplitsing. ERRC-framework wordt 0 keer genoemd, Blue Ocean alleen als foto.
- **Financieel model** op PoV: drie inkomstenstromen, **nul cijfers**. Geen prijs, geen TAM, geen investeringsbehoefte.
- **Waardeproposities** per stakeholder: uitsluitend kwalitatief ("minder tijd aan administratie"), geen uren, geen euro's.

### 4. Concrete fouten (hard te fixen, levert punten op)

- **Huizingh-mapping fout** op `innovatieradar.astro:6-19`. "Klanten" staat onder Positie, hoort bij Product. Jullie tonen 3+5+2+2 ipv officiele 4+4+2+2. Critical friend haalt dit er direct uit.
- **Breadcrumb bug** op `denkrichtingen.astro:72`: label "Design" ipv "Define".
- **Rogers adopter-categorieen fout toegepast** op `roadmap.astro:187-204`: early adopter/majority/late hoort per individu binnen een sociaal systeem, niet per sector. Framing moet worden: "eerste doelgroep / volgende segment" met motivering op urgentie + bereikbaarheid.
- **DVF-scores niet herleidbaar**: gate 2 gemiddelden 4.5/3.8/3.4/1.8 (4 dimensies) matchen niet met PoV 4.5/2.5/3.8 (3 dimensies).
- **PELV-attributie aan Boehm twijfelachtig** op `refine/index.astro:50`. Boehm = spiraalmodel, PELV is eerder actieleren/Kolb. Check of dit klopt.

### 5. Theorie-breedte is mager

Op de site ~9 theorieen toegepast (Christensen, Porter, IBSOTEEP, Treffinger, Huizingh, Tidd&Bessant, Kim&Mauborgne, O'Reilly&Tushman, Rogers). CLAUDE.md noemt 20+. Structureel afwezig: **Bossink, Van der Voort, Kastelle, Derksen (teamrollen), Dodgson (4 strategieen), Snowden (Cynefin), BCG, Suzuki, Kelley (10 Faces), Andler (problem clarification), Zomer, Mueller-Roterberg**. Kiezen of delen: 3-5 ervan alsnog 1 paragraaf toevoegen aan relevante fase.

### 6. Bronnen niet consequent klikbaar

Discover is netjes (20+ links via `sourceUrls` in trends.astro). Vanaf Define gaat het mis. Platte tekst zonder link: Treffinger (challenges), Huizingh (innovatieradar + denkrichtingen), De Bono PMI (convergentie), DVF (design), Boehm PELV (refine), O'Reilly & Tushman (deliver), Rogers (deliver), 70%-productlanceringen-faalt (roadmap, verwijst naar les ipv bron). CLAUDE.md eist expliciet dat elke bron klikbaar is.

### 7. Zelfstandige leesbaarheid PoV op MT-niveau faalt

Opdracht 1d eist expliciet: "PoV is zelfstandig leesbaar door MT en directie". MT-blindtest uit de Deliver-review geeft 5/11 begrepen. Ontbreekt op PoV-pagina: context over Aurora, driver/aanleiding, prototype-uitkomsten, status-nu, concurrentievergelijking, call to action, cijfers. Alles elders aanwezig, maar MT klikt niet door.

## Geprioriteerde actielijst

Elke actie: waarom, waar, impact op cijfer.

### Blokkerend voor 8 (doe deze week)

**Deliver / PoV (zwaarste gewicht, laagste cijfer)**

1. **Voeg "Context"-blok toe bovenaan PoV** voor de challenge-sectie. Max 120 woorden: Aurora, de pivot, waar in de reis. Impact: tilt zelfstandige leesbaarheid van 5/11 naar 8/11. (`proof-of-value.astro`)
2. **Voeg "Prototype-uitkomsten"-sectie toe op PoV.** PELV 1 + PELV 2 in 2 alineas met belangrijkste leerervaring en wat is aangepast. Bewijst "cyclisch getest op meerwaarde". (`proof-of-value.astro`)
3. **Voeg "Waar staan we nu"-statusblok toe:** per component 1 regel (concept validated, prototype paper+rapid, techpartner niet geselecteerd, 0 pilots, 0 financiering). (`proof-of-value.astro`)
4. **Cijfers in financieel model.** Minimaal: prijsbandbreedte per inkomstenstroom, marktomvang 800 notariskantoren x gem. licentie, investeringsbehoefte startup, breakeven-aanname. Mag expliciet "aanname" heten. (`proof-of-value.astro`)
5. **Cijfers in waardepropositie per stakeholder.** Notaris: uren bespaard per akte x tarief = euros. Bank: fraudeschade-getal met bron. Verzekeraar: idem. (`proof-of-value.astro:129-181`)
6. **Conclusie + CTA onderaan PoV.** 3-regel-samenvatting + concrete investeringsvraag. (`proof-of-value.astro`)
7. **Herzie Rogers adopter-categorieen** op roadmap: "eerste doelgroep / volgende segment / latere segment" met argumentatie op urgentie + bereikbaarheid + investeringsruimte, niet early-adopter/majority/late. (`roadmap.astro:187-204`)
8. **Concurrentie-matrix op PoV:** tabel met minimaal DocuSign, Signicat, itsme, iDIN, Jumio op 3 criteria (hybride ja/nee, ID-chip, certificering). (`proof-of-value.astro`)

**Refine**

9. **PELV 2 testresultaten zichtbaar maken:** N, antwoorden per vraag, 2-3 letterlijke citaten. Zonder dit is rubric-Goed-eis "cyclisch getest op meerwaarde" niet aantoonbaar. (`prototyping.astro` iteratie 2 L-blok)
10. **Verbeterloop iteratie 1 naar 2 expliciet maken.** Minimaal 3 concrete aanpassingen met reden.
11. **Benoem de 2 presentabele concepten expliciet voor de pivot** (opdracht 1c: 2-4 concepten). Nu lijkt het of er 1 uitkomt.
12. **Benoem externe gate als gat** in 1 eerlijke zin. Voorkomt dat docent hierop struikelt.

**Define**

13. **Fix Huizingh-mapping** op `innovatieradar.astro:6-19`. "Klanten" onder Product, verdeling 4+4+2+2 herstellen. (Ook de kleur-mapping herzien, zie review-define.md Z2.)
14. **Voeg fotobewijs PMI toe** aan `convergentie.astro`. Crop uit `sessie3-radar-2.jpeg` met bijschrift dat stickers noemt. Haal "impliciet" weg op `denkrichtingen.astro:95`.
15. **Herschrijf HZWK's naar <15 woorden zonder oplossing in de vraag.** Met name `denkrichtingen.astro:22` (27 woorden, bevat "via biometrie") en `:47` (21 woorden, bevat strategisch standpunt).
16. **Bridge van 3 HZWK-kamers naar 2 denkrichtingen.** Mini-beslismatrix: waarom sneuvelde Specialisatie, waarom kwam Organisatie terug als Circulair.

**Design**

17. **DVF-subscores tonen** op `gate.astro`: Circulair D/V/F en Security D/V/F met totalen. Zonder subscores is DVF geen diagnose-instrument.
18. **Pas ERRC toe en toon op `gate.astro`.** Vier blokjes Eliminate/Reduce/Raise/Create voor de Security-richting. Zonder ERRC is Blue Ocean alleen een foto.
19. **Value curve toelichten** onder de foto: x-as-factoren, lijnen-legenda, wie de concurrentie is.
20. **Concept collection visueel maken** op de pagina. 12-20 beelden inline in grid met captions. Pptx-download mag blijven als extra.
21. **Herformuleer Security-keuze methodisch.** Niet "meer potentie op gevoel", wel: DVF-subscores lieten zien dat Circulair's voorsprong alleen in Desirability zat, bij Circulair was klant bedacht, bij Security concreet. Suggestie-tekst staat in review-design.md.

**Discover**

22. **Voeg methode-reflectie toe op `discover/index.astro`.** Per methode 2-3 zinnen: waarom deze, wat leverde het op, wat was de beperking. Bottleneck voor elk cijfer boven 7.
23. **Wijs expliciet gekozen scenario aan** op `scenario.astro`. Nu staat alleen op index dat scenario B waarschijnlijk is. Maak een "Ons gekozen scenario"-blok met 3-5 argumenten en actieve early warnings.
24. **Aurora-strategie-analyse als eigen blok.** Wat is Aurora's huidige strategie, waar schiet die tekort. Opdracht-eis die nu verspreid is.
25. **Documenteer tijdsbesteding immersive research** (minimaal 1,5 uur eis uit opdracht 1a). Een zin volstaat.

**Cross-cutting**

26. **AI-toon sweep**. Em-dashes weg uit zichtbare content (PELV-labels, Sessie-headings, alt-teksten). Zoek-en-vervang `—` door `:` of `-`. Herschrijf "Niet X, maar Y" constructies op pivot.astro en proof-of-value.astro. "Paradigmashift!" eruit.
27. **Klikbare bronnen overal.** Treffinger, Huizingh, De Bono PMI, DVF, Boehm PELV, O'Reilly, Rogers. Minstens 8 ontbrekende links.
28. **Breadcrumb-bug** `denkrichtingen.astro:72`: "Design" wordt "Define".
29. **PELV-attributie checken.** Boehm = spiraalmodel. Als PELV uit Zwolse lesmateriaal komt, attribueer daar aan of verwijder de attributie.
30. **Parallel-template van fase-indexen doorbreken.** Minstens 2 van de 5 krijgen een andere kopvolgorde of persoonlijke opening.

### Nice-to-have voor 9 (doe volgende week als tijd)

31. **Kritische reflectie per theorie.** Per fase 1 blokje "Wat deze theorie WEL en NIET oploste voor ons". Direct rubric-10-niveau. Voorbeelden in review-holistic.md sectie Theorie.
32. **Team-dynamiek zichtbaar.** McKinsey-rollen uit `docs/onderzoek/mckinsey-teamscores.md` inbrengen op een fase (bv. Define): Lianne netwerkt, Anke motiveert, Jr genereert. Niet pas bij 2b.
33. **Interviews verrijken.** Anna en Famke met letterlijke quote + context-zin.
34. **Aanleiding koppelen aan Discover/Trends.** Link vanuit trends naar de tijdlijn.
35. **Bronnen-sectie per pagina** (collapsible details, zoals op trends.astro) ook op define/design/refine/deliver.
36. **Theorie-breedte uitbreiden.** Kies 3-5 uit: Bossink, Derksen (teamrollen past op Define/Deliver), Dodgson (4 strategieen past op Discover), Snowden/Cynefin (past op Scenario), BCG (past op Aurora-portfolio in aanleiding), Andler (past op pivot als problem clarification). Elk 2-3 paragrafen.
37. **Gate-quotes van Niels en Niels** letterlijk op `gate.astro`.
38. **"Wat hebben we NIET gedaan"-blok** op Deliver of Discover. Eerlijk benoemen: 90 ideeen niet gehaald, concept collection 2 niet gedaan, geen externe gate. Versterkt leerervaring-oordeel.
39. **Pen-business impact-zin** op pivot: wat betekent dit voor Aurora's bestaande penproductie.
40. **Splits VPC per klanttype** (notaris/bank/verzekeraar). Nu geaggregeerd, per segment ondiep.
41. **AVG / ethische reflectie** op PoV. Wat als dit voor surveillance gebruikt wordt. Past bij deze docent.

### Stretch: originele zetten voor 10

42. **"Onze twijfels"-uitklapblok per fase.** 2-3 zinnen waar je vastliep. Hardste reis-verslag-signaal.
43. **Time-capsule terugblik.** "Als we opnieuw zouden beginnen"-blok per fase. Past bij rubric-criterium reflectie op leerproces.
44. **Eigen methode-aanpassing claimen.** Bv. 5e sleuteldimensie Technologie aan Huizingh toegevoegd. Of DVF uitgebreid met team-competentie-weging. Methodisch origineel = rubric 10.
45. **Externe gate alsnog organiseren.** Interview 1 notaris of bankmedewerker, laat prototype + VPC zien, documenteer reactie. Dit is het enige blokkerende gat tussen 9 en 10 op Refine + Deliver.
46. **Team-verhaal op aparte "Over ons"-pagina of in aanleiding.** Teamfoto, McKinsey-rollen, wie deed wat, waar zat spanning.
47. **Scoring-transparantie op Deliver.** 4 individuele DVF-scores tonen ipv gemiddelden, met spreiding. Laat zien dat je meetfouten incalculeert.
48. **Moodboard als interactieve grid** op concept collection. 35+ afbeeldingen scrollbaar met hover-tags (productvorm/authenticatie/kruisbestuiving).

## Samenvatting per fase (links naar deelrapporten)

### Discover → `review-discover.md`
Sterk op theorie-breedte (IBSOTEEP, Porter, trendpiramide, scenariomatrix, Christensen). Bronnen klikbaar. Pijnpunten: geen methode-reflectie, urgentie voor directie niet gebundeld, Aurora-strategie-analyse ontbreekt als eigen blok, narratieve break tussen scenario-keuze en challenges, HZWK #5 loopt vooruit op pivot. AI-toon beperkt tot H2-em-dashes en 5 taglines. **Scenario B is niet expliciet aangewezen op scenario.astro zelf.**

### Define → `review-define.md`
Reis-traceerbaarheid op denkrichtingen.astro is een 9-10 element. Maar Huizingh-mapping is fout (3+5+2+2), "impliciet PMI toegepast" is zelfveroordelend, HZWK's 16-27 woorden met oplossing in de vraag, brug van 3 HZWK-kamers naar 2 denkrichtingen ontbreekt, fotobewijs PMI mist.

### Design → `review-design.md`
Eerlijk verhaal over keuze ondanks lager DVF, bewuste dump CC2 verantwoord. Maar DVF alleen totalen zonder subscores, Blue Ocean alleen als foto (geen ERRC, geen value-curve-uitleg), concept collection is tekst ipv beeld, pivot-kiem "losmaken van de pen" aanwezig maar niet expliciet gemarkeerd. 2 van de 4 DVF-foto's niet getoond.

### Refine → `review-refine.md`
PELV-labels expliciet per iteratie, fysiek prototype, procesflow + VPC op MT-niveau. Maar **PELV 2 testresultaten ontbreken op pagina** (#1 blokker voor rubric-8). Verbeterloop 1 naar 2 dun. Pivot-narratief 4-5 keer te glad ("Niet X, maar Y"-taglines, "als geen ander", paradox-trope). VPC geaggregeerd over klanttypes, bevat corporate jargon. 2-concepten-eis niet afgehandeld. Externe gate niet gedaan en niet benoemd.

### Deliver / PoV → `review-deliver-pov.md`
**Zwaarste en laagste: 6.5 nu.** 7 van 13 1d-eisen volledig, 5 partial, 1 ontbrekend. PoV niet zelfstandig leesbaar op MT-niveau. Financieel model zonder cijfers. Waardeproposities generiek. Rogers-adopter-categorieen fout per sector toegepast. DVF-scores niet herleidbaar tussen gate-2-gemiddelden en PoV. Concurrentie-matrix ontbreekt (DocuSign/Signicat/itsme/iDIN/Jumio). Ambidexteriteit goed, maar structureel-vs-contextueel niet afgewogen. 16 AI-toon incidenten, 5 kritisch.

### Holistisch → `review-holistic.md`
Reis-narratief werkt (landschap-hero, fase-dots, breadcrumbs, forward-knoppen). Maar theorie-breedte schraal (9 van 20+), kritische reflectie ontbreekt volledig, 28 em-dashes, parallel-template op fase-indexen oogt als AI-sjabloon, Deliver leest als pitch-deck terwijl Refine/Pivot echt reis-toon hebben. Team-dynamiek niet zichtbaar. Breadcrumb-bug op denkrichtingen.astro:72.

## Realistisch pad naar 10

Gezien de weging 1a + 1b beide 30%:

- **Deze week prio-1 (acties 1-30):** haalbaar in 2-3 dagen werk voor 3-persoons-team. Tilt site van gemiddeld 7.0 naar 8.2. Rubric-niveau "goed" is dan bereikt.
- **Volgende week prio-2 (acties 31-41):** nog eens 2-3 dagen. Tilt naar 8.8 - 9.2. Zit dan op "zeer goed", randje uitmuntend.
- **Stretch 42-48:** haalbaarheid hangt af van externe gate. Zonder gate met notaris/bank is 10 op Refine + Deliver structureel buiten bereik, want rubric-uitmuntend op 1b vraagt meervoudige validatie. Eén LinkedIn-bericht naar een notaris, 15 minuten bellen, 1 citaat: haalbaar.

**Advies:** begin bij Deliver/PoV (zwaarste gewicht, grootste hefboom). Daarna AI-toon-sweep (lage effort, zichtbaar resultaat). Dan Refine PELV 2 data. Pas daarna de kleinere fixes op Discover/Define/Design.

Een cijfer 10 is niet gegarandeerd, maar **9 is realistisch haalbaar** met prio-1 + prio-2 binnen 2 weken. Voor de sprong naar 10 is één externe stem nodig (notaris, bank) plus originele methodische zetten (bv. eigen aanpassing aan Huizingh of DVF).
