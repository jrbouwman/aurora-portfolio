# Review Refine fase

*Review uitgevoerd op basis van `/refine/`, `/refine/prototyping/`, `/refine/pivot/` en de onderliggende source + werkdocumenten. Rubric-mikpunt: 10. Toon: scherp, eerlijk, constructief.*

---

## Samenvatting

De Refine-fase staat er solide. PELV-cyclus is expliciet per iteratie in labels zichtbaar (P/E/L/V blokjes), er zijn twee iteraties met foto's, schetsen en een fysiek prototype, en de pivot is inhoudelijk goed onderbouwd vanuit de test. Het procesflow-werk en het VPC geven MT-niveau kwaliteit aan de Refine-output.

Wat het cijfer nu remt: (1) de testresultaten van iteratie 2 zijn niet zichtbaar op de pagina — alleen de vragenlijst staat er, geen antwoorden, geen N, geen bevindingen; zonder die data is "cyclisch getest op meerwaarde" niet aantoonbaar. (2) De pivot wordt op twee plekken net te glad gebracht ("Niet meer de maker van de pen, maar...", "Je moet durven om je eigen product in vraag te stellen", hero "de pen is overbodig" als tagline). (3) Eerlijkheid over DocuSign/PKIsigning staat er wel, maar wordt direct weer ingehaald door claims over Aurora's 125+ jaar die niet onderbouwd zijn met een bron of interview. (4) De opdracht vraagt 2 presentabele concepten + externe gate — beide ontbreken en worden op de site niet benoemd als gat.

Inschatting nu: **7,5**. Met fixes haalbaar op **9**.

---

## Sterke punten

- **PELV-labels expliciet zichtbaar per iteratie** (`prototyping.astro` regels 100-117 en 224-241). Dit is een docent-vriend: Henk kan in één oogopslag zien dat de methode is gevolgd. Veel teams laten dit impliciet.
- **Concrete hands-on prototypes**: post-its, schetsen, fysiek rapid prototype in hout/piepschuim/karton, paper mockup. Dit is echt "innoveren met je handen" zoals les 5 voorschrijft.
- **Pivot is inhoudelijk logisch onderbouwd**. Beide iteraties leverden dezelfde conclusie, en de "van-naar" vraagverschuiving op pivot-pagina (regels 48-55) is precies hoe design thinking pivot hoort te werken.
- **Procesflow in huisstijl (3 varianten: hoogover, uitgebreid, voorbeeld)** met lightbox-modals — dit tilt het visuele niveau naar MT-niveau.
- **Value Proposition Canvas** volgens BMI-template (vierkant Value Map + ovaal Customer Profile) — inhoudelijk goed ingevuld per beide partijen (Aurora+techpartner en notaris/bank/verzekeraar).
- **Eerlijk-verhaal sectie** op pivot-pagina benoemt expliciet DocuSign en PKIsigning — dat voorkomt dat het te claim-achtig wordt.
- **Navigatie-flow**: breadcrumbs, vorige/volgende, "Refine afgerond, door naar Deliver" — portfolio voelt als reis, niet als losse pagina's.

---

## Kritische zwaktes

### Docent Henk

1. **PELV iteratie 2 mist de L (Learn) bewijsdata.** De Learn-stap claimt "Concept is duidelijk. Maar: de pen in het device voegt niks toe." (regel 235). Maar waar komt dat uit? De vragenlijst staat er wel (regels 304-309), de **antwoorden niet**. Hoeveel testers, welke antwoorden, welke verdeling? Voor "cyclisch getest op meerwaarde" (rubric 1b Goed=8) heb je de *data* nodig, niet alleen de vraagstelling.
2. **Verbeter-loop van iteratie 1 → iteratie 2 is niet scherp navolgbaar.** Waar iteratie 1's "V — Verbeter" zegt "fysiek device met ID-scan en PIN. Dat werd iteratie 2", ontbreekt wat er concreet verbeterd is *tov* iteratie 1. De lezer ziet twee parallelle iteraties, geen echte iteratie waarin prototype 2 voortbouwt op het leerrendement van 1.
3. **De derde PELV-stap (testen met externen) ontbreekt en wordt niet benoemd.** Opdracht 1c regel 48: "Organiseer een gate waarin je anderen (buiten school) betrekt bij door-selectie". Op de site staat "getest met medestudenten". Benoem dit gat expliciet (critical reflection hoort bij uitmuntend).
4. **"Minimaal 2, maximaal 4 presentabele concepten" ontbreekt.** De opdracht (regel 47) vraagt presentabele concepten aan het einde van Refine. De pagina noemt 3 concepten in iteratie 1 (iris/pincode/NFC), maar daarna is iris afgevallen en zijn de andere twee samengesmolten in de pivot. Er wordt niet expliciet gezegd: "dit zijn onze 2 presentabele concepten en zo verhouden ze zich tot elkaar". Nu lijkt het of er 1 concept uit komt.
5. **Kritische reflectie op eigen proces ontbreekt.** Voor "uitmuntend (10)" op rubric 1a wil Henk kritische beoordeling van de theorie op eigen situatie. Er staat niet: "wat werkte niet aan PELV voor ons", "waarom kostte iteratie 2 ons een week", "wat zou je achteraf anders doen". Dat is precies het niveau-verschil tussen 8 en 10.

### MT/directie

1. **"Waarom de pen sneuvelde" overtuigt inhoudelijk wel, maar de financiële/strategische consequentie niet.** MT leest "we stoppen met ons kernproduct in dit spoor" — waar is de impactanalyse? (Hoort bij Deliver, maar op pivot-pagina mag één zin staan over wat dit voor Aurora's pen-business betekent.)
2. **Procesflow is visueel sterk, maar claim "Aurora als kennispartij" wordt niet gevalideerd.** De VPC zegt "Domeinkennis geeft gezag" (regel 263) maar er is geen interview met notaris/bank, geen tests met die klantgroep, geen markt-onderbouwing. Voor MT voelt dit als een aanname, niet als onderbouwing.
3. **"125+ jaar ervaring met schrijfgerei en ondertekening"** (pivot regel 198) — ervaring met *schrijfgerei* is niet hetzelfde als ervaring met *ondertekening als juridische handeling*. Dit glijdt iets te makkelijk.
4. **Pivot-risico niet benoemd.** Waarom zou Aurora niet gewoon klant zijn van DocuSign? Wat is de specifieke reden dat een pennenmaker hier de kennispartij is en niet een consultancy of notaris zelf? MT zal dit vragen.

### Critical friend

1. **PELV-labels staan er, maar de inhoud van L en V in iteratie 2 is dun.** L zegt één conclusie, V zegt "pivot". Waar zijn de 5 verbeterpunten die les 5 (regel 54) voorschrijft? 
2. **Prototypes zijn technisch niet echt testbaar voor anderen.** Het rapid prototype (hout + piepschuim) demonstreert het idee maar kan niks. De vereiste uit les 5 is "testbaar en tastbaar voor anderen". Dit is tastbaar ✓, maar testbaar is het niet — een tester kan geen ID echt scannen, geen PIN echt invoeren. Dat had met Wizard-of-Oz beter gemoeten (iemand achter het gordijn simuleert de response). Benoem dat als beperking.
3. **Vragenlijst methodologisch dun.** 7 vragen zoals "Voorkomt het daadwerkelijk fraude?" vragen een inschatting van een medestudent die geen security-expert is. "Is het technisch haalbaar om te bouwen?" — hoe kan een testperson dat weten na 10 min? De vragenlijst test perceptie, niet meerwaarde. Dat is OK als je dat benoemt.
4. **Pivot-narratief: "de pen is overbodig" als herhaalde tagline.** Hero subtitel regel 82, PELV-conclusie regel 321, index regel 14 en 36 — steeds dezelfde zin. Voelt gecureerd, minder als spontane realisatie en meer als pitch.
5. **"Eerlijk verhaal" sectie blijft toch een beetje glad.** Het benoemt DocuSign en PKIsigning (goed), maar spint daarna meteen door naar "onze bijdrage is het inzicht" en "Aurora als kennispartij" — dat is precies de gladde move waar de critical friend op let. Waar is de *tegen*-argumentatie? Waarom is "inzicht" een verdedigbaar product? Is dit geen consultancy-klus van 3 maanden die elk adviesbureau ook kan leveren?
6. **"Niet meer de maker van de pen, maar de expert op het gebied van ondertekenen"** (regel 211) — klassieke tagline-structuur (niet X, maar Y). Dit is precies de AI-toon die vermeden moet worden.

---

## AI-toon incidenten

Gescand op em dashes, taglines, corporate jargon, pitch-structuren.

| # | Waar | Citaat | Type |
|---|------|--------|------|
| 1 | `pivot.astro` regel 211 | "Niet meer de maker van de pen, maar de expert op het gebied van ondertekenen." | Tagline-structuur "niet X, maar Y". Vermijd. |
| 2 | `pivot.astro` regel 205 | "Je moet durven om je eigen product in vraag te stellen." | Innovatie-tagline/oneliner. Glad. |
| 3 | `pivot.astro` regel 203-204 | "Het is een beetje paradoxaal: een pennenmaker die concludeert dat de pen overbodig is. Maar dat is precies wat innovatie soms vraagt." | Paradox-trope, pitch-toon. |
| 4 | `pivot.astro` regel 212-213 | "Die expertise is de echte waarde, niet het schrijfgereedschap." | Tagline, niet X maar Y opnieuw. |
| 5 | `prototyping.astro` regel 82 | "Twee iteraties, drie concepten, en een conclusie die we niet hadden verwacht: de pen is overbodig." | Hero-subtitel leest als pitch deck opener. Driedelig ritme + cliffhanger. |
| 6 | `refine/index.astro` regel 36-39 | "Wat we niet hadden zien aankomen: beide prototypes lieten zien dat de pen eigenlijk overbodig is." | Marketing-reveal. Lichter dan #5 maar zelfde patroon. |
| 7 | `pivot.astro` regel 348-350 | "De pen blijft bestaan, maar het bewijs verschuift van de krul op papier naar de koppeling tussen ID, moment en handeling." | "De krul op papier" is poetisch, corporate-copy toon. Drieslag op het eind (ID, moment, handeling). |
| 8 | `pivot.astro` regel 23-24 | "Tijdens het testen kwamen we erachter dat de pen overbodig is. Het probleem zit in de handtekening zelf, en daar hebben we onze richting op aangepast." | Hero, nette AI-zin. Zet er bijv. een echt moment in: "Op 8 april, tijdens het derde testmoment met X, zei iemand: ..." |
| 9 | `pivot.astro` regel 199-200 | "Die kennis over hoe mensen ondertekenen, wanneer ze dat doen en wat het voor ze betekent" | Drieslag + abstractie. Typisch AI-ritme. |
| 10 | `pivot.astro` regel 344-346 (Fit) | "raken vooral aan ondertekeningsprocessen waar identiteit telt" | Corporate abstractie. |

Geen em-dashes in lopende tekst gespot — de em-dashes in "P — Plan" zijn labelscheidingstekens, prima.

Geen harde corporate-woorden als "naadloze beleving", "waarde-bril", "competitive moat" — dat is goed.

**Oordeel AI-toon:** bovengemiddeld qua discipline, maar de pivot-pagina heeft een cluster van 4-5 tagline-achtige zinnen in het "Eerlijk verhaal" + "rol van Aurora" blok. Dat moet rauwer.

---

## PELV-cyclus beoordeling

### Iteratie 1 (1 april)

| Stap | Zichtbaar op site? | Kwaliteit | Opmerkingen |
|------|---|---|---|
| **P — Plan** | Ja, label + 1 zin | Dun | "Wat willen we weten" is breed ("UX en technische werking"), geen meetbare hypothese. Les 5 vraagt "wat wil je weten" — antwoord moet specifieker. |
| **E — Experiment** | Ja, foto's + 3 concepten + schetsen | Goed | Brainstorm-foto's, schetsen, 2 testplannen. Testplannen staan in `docs/onderzoek/testplannen-pelv.md`, niet direct op pagina gelinkt — link dit. |
| **L — Learn** | Ja, testresultaten-tabel met bevindingen | Redelijk | Bevindingen staan er, maar wie heeft getest? Aantal testers? Citaten? "Online schrijven is beter" staat als opmerking maar is vaag. |
| **V — Verbeter** | Ja, label + 1 zin | Dun | "Weg van de pen. Naar fysiek device..." — dit is geen verbeterplan maar al bijna de pivot. Tussenstap ontbreekt. |

### Iteratie 2 (8 april)

| Stap | Zichtbaar op site? | Kwaliteit | Opmerkingen |
|------|---|---|---|
| **P — Plan** | Ja, label | Redelijk | "Is een fysiek device met ID-scan begrijpelijk? Snappen mensen het concept zonder uitleg?" Dit is een testbare vraag, goed. |
| **E — Experiment** | Ja, 5 foto's (device + mockup) | Goed | Fysiek prototype, paper mockup, vragenlijst. |
| **L — Learn** | **DEFICIENT** | Laag | Label zegt "Concept is duidelijk. Maar: de pen voegt niks toe." Maar: **nergens zie je de vragenlijst-antwoorden.** Geen grafieken, geen citaten, geen N. Dit is het grootste methodische gat. |
| **V — Verbeter** | Ja, label | Dun | "Pivot: laat de pen los." — springt direct naar pivot, geen tussenstap. |

**Algemeen oordeel PELV**: labels zijn expliciet aanwezig (punt verdiend bij Henk), maar de *inhoud* per label is vaak 1-2 zinnen. Voor rubric "methodisch ontwikkeld en cyclisch getest op meerwaarde" (PoC=Goed/8) moet de L per iteratie rijker — testresultaten, citaten, aantallen, liefst een mini-dashboard van de Forms-output.

---

## Pivot-verantwoording (eerlijk of glad?)

**Conclusie: gemengd. De inhoudelijke onderbouwing is eerlijk, het narratief eromheen is te glad.**

### Wat eerlijk is
- Expliciet genoemd: DocuSign, PKIsigning als bestaande oplossingen (regel 192-195).
- "Het is niet alsof we hier iets compleet nieuws hebben bedacht" — goed, dat is precies de eerlijkheid die Jr's feedback in CLAUDE.md vraagt.
- De pivot-reden komt logisch uit de PELV-conclusie (pen zelf voegt niks toe). Dat is verdedigbaar.
- Huidig-vs-nieuw proces tabel (regels 161-179) legt duidelijk uit wat er verandert.

### Wat glad is
- Meteen na de eerlijkheid volgt: "Onze bijdrage zit in het inzicht dat Aurora als kennispartij kan bijdragen". Deze zin is de klassieke "ja maar toch wij" move. Critical friend moet hier oppakken: *wat is dat inzicht precies?* Eén zin concreet graag — niet "domeinkennis over hoe mensen ondertekenen" in het abstracte.
- "Aurora heeft 125+ jaar ervaring met schrijfgerei en ondertekening" — Aurora (fictief) heeft ervaring met schrijfgerei *maken*, niet met ondertekeningsprocessen ontwerpen. Dit is een sprong.
- Het paradox-frame ("een pennenmaker die concludeert dat de pen overbodig is") is prachtig verteld — maar dat is het probleem. Te mooi. De eerlijke versie zou zijn: "Eigenlijk zitten we nu in een spoor waar Aurora *niet* de natuurlijke speler is. We moeten verantwoorden waarom juist wij dit zouden doen." Die twijfel staat er niet.
- VPC-fit paragraaf (regel 344-350) leest als slotwoord van een pitch. Woord "schaalbaarheid" + "juridische zekerheid" + "digitale rechtsgeldigheid" — klinkt als consultancy-slide. 

### Risico dat je door Henk wordt gepakt
Henk zal vragen: "jullie hebben gepivot van een product-innovatie (pen) naar een proces-innovatie (digitaal verificatieproces). Hoe rechtvaardigt dat het werk dat jullie daarvóór deden? Is de Discover/Define-fase retroactief een andere challenge geworden?" Antwoord hierop staat nergens. Eén paragraaf die de pivot in het licht van de *oorspronkelijke challenge* plaatst, zou dit afvangen.

---

## VPC-beoordeling

De VPC staat inline als SVG op de pivot-pagina (regel 228-331) en volgens BMI-template: vierkant Value Map links (Products & Services + Gain Creators + Pain Relievers als driehoeken), ovaal Customer Profile rechts (Gains + Pains + Job-to-be-done als taartpunten).

### Vorm: goed

- Vierkant + ovaal: ✓ conform BMI.
- Amber accent voor Value Map, donker voor Customer Profile: ✓ visuele hiërarchie.
- Driehoeken in vierkant, taartpunten in ovaal: ✓.
- Labels in hoeken (PRODUCTS & SERVICES, GAIN CREATORS, PAIN RELIEVERS, GAINS, PAINS, JOB-TO-BE-DONE): ✓.
- Subtiel: "Aurora + techpartner" en "Notaris, bank, verzekeraar" als italic: ✓.

### Inhoud: redelijk tot goed, maar niet scherp

**Products & Services (Aurora-kant):**
- "Kennismodel voor authenticiteit" — vaag. Wat is een kennismodel? Een document? Een training?
- "Verificatiestation: ID + PIN" — concreet ✓
- "Koppeling handtekening ↔ code" — concreet ✓
- "Implementatie-ondersteuning" — OK maar vaag

**Gain Creators:**
- "Juridisch waterdichte audittrail" — claim zonder bewijs, "waterdicht" is te sterk
- "Schaalbaar over transacties" — corporate jargon
- "Compliance-klaar" — buzzword
- "Domeinkennis geeft gezag" — dit is meer een *reden waarom* Aurora gain-creator is, niet een gain

**Pain Relievers:**
- "Objectieve ID-check" ✓
- "Gescande handtekening rechtsgeldig" — twijfelachtige claim, zou eHerkenning/eIDAS-conform moeten zijn
- "Fraudesignalen direct zichtbaar" ✓
- "Digitaal doorzoekbaar archief" ✓

**Gains (klant):**
- Juridische zekerheid, sneller proces, minder administratie, vertrouwen eindklant — generiek. Mist specificiteit per segment. Een notaris heeft andere gains dan een bank.

**Pains (klant):**
- Vervalsing lastig bewijsbaar ✓
- Visuele ID-check foutgevoelig ✓
- Scan niet rechtsgeldig ✓
- Fraude komt laat aan licht ✓  → deze sectie is het sterkst.

**Job-to-be-done:**
- Rechtsgeldig laten ondertekenen, juiste persoon tekent, audittrail voor compliance, klanten snel bedienen — goed, 4 concrete jobs.

### Fit-conclusie
De VPC toont fit op pains (goed) en op jobs (goed). Maar de gain creators zitten vol corporate taal ("schaalbaar", "compliance-klaar") die niet naar een echte gain herleidt.

**Aanbeveling**: 
1. Maak per klanttype (notaris, bank, verzekeraar) een mini-VPC zodat je ziet dat je in elk segment de fit aantoont. Nu is het geaggregeerd en dus ondiep.
2. Vervang "Domeinkennis geeft gezag" als gain creator; zet dit bij Products & Services of in de Fit-paragraaf. Het is geen klantgain.
3. "Juridisch waterdichte audittrail" → "Audittrail die voldoet aan eIDAS/Wwft" (concreter en toetsbaar).

---

## Concrete verbeteringen

### Blokkerend voor 8+

1. **Voeg testresultaten iteratie 2 toe op de pagina.** De Microsoft Forms vragenlijst staat er, de antwoorden niet. Minimaal: N-getal, antwoorden per vraag (grafiek of tabel), 2-3 letterlijke citaten. Zonder dit is "cyclisch getest op meerwaarde" niet aantoonbaar. Dit is de #1 fix.
2. **Maak verbeterloop iteratie 1 → 2 navolgbaar.** Voeg een expliciet blokje toe: "Wat hebben we aangepast tov iteratie 1?" Minimaal 3 concrete aanpassingen met reden.
3. **Benoem de 2 presentabele concepten expliciet.** Voordat je de pivot introduceert: "Dit zijn onze 2 concepten aan het eind van Refine: [A] en [B]". Dan pas de pivot-sectie. Opdracht 1c vraagt 2-4 concepten.
4. **Benoem externe gate als gat.** Één eerlijke zin: "We hebben dit alleen met medestudenten getest, niet met een notaris of bank. Dat is een beperking." Dan val je niet door de mand bij Henk.
5. **Herschrijf "Eerlijk verhaal" sectie naar echte rauwheid.** Nu leest het nog steeds als pitch. Voorbeeld-herformulering: "Eerlijk: we zitten hier op een terrein waar al tientallen spelers zitten. Waarom wij? Omdat — en dat is wat we denken, niet wat we hebben aangetoond — de ervaring van een pennenmaker met hoe mensen tekenen iets kan toevoegen aan het *ontwerp* van het proces. Of dat klopt, weten we nog niet. We zouden een notaris moeten interviewen."
6. **Fix de AI-toon taglines** (incidenten #1, #2, #4, #5, #6 uit de tabel). Ruil "Niet X, maar Y"-constructies in voor concrete zinnen.

### Nice-to-have voor 10

7. **Voeg kritische reflectie op PELV-methode toe.** Eén paragraaf: "Wat werkte niet aan PELV voor ons." Bijvoorbeeld: "De V-stap liep bij ons meer als een sprong dan als een verfijning. Achteraf zou een derde iteratie waar we de pivot écht getest hadden met een klant, krachtiger zijn geweest."
8. **Geef prototype-vragenlijst methodologische nuance.** Eén regel: "We vroegen mensen naar fraudepreventie terwijl ze geen security-expert zijn. We testten vooral perceptie, niet technische veiligheid."
9. **Splits VPC per klanttype** (notaris, bank, verzekeraar). Nu is het geaggregeerd, dus per segment ondiep.
10. **Wizard-of-Oz benoemen.** Leg uit dat het rapid prototype niet testbaar was op functionaliteit (een medestudent kon niet echt zijn ID scannen), en hoe je dat met Wizard-of-Oz had kunnen oplossen in iteratie 3. Dat is precies het soort meta-reflectie dat Henk bij "uitmuntend (10)" zoekt.
11. **Link testplannen-pelv.md als bewijsstuk** direct vanaf de pagina (downloadknop of interne link). Dat versterkt het dossier-karakter.
12. **Eén zin over de pen-business-impact.** MT wil weten: "als jullie dit doen, wat betekent dat voor Aurora's huidige pen-productie?" Antwoord hoort in Deliver, maar een haakje op pivot-pagina is goed.
13. **Citaten uit de tests.** Ten minste 3 letterlijke citaten ("dit snapte ik meteen", "waarom niet gewoon DigiD?", etc.) — die maken het echt. Nu is alles geparafraseerd.

---

## Cijferinschatting

| Scenario | Cijfer | Onderbouwing |
|---|---|---|
| **Nu** | **7,5** | PELV-labels expliciet ✓, 2 iteraties ✓, fysiek prototype ✓, pivot onderbouwd ✓, procesflow + VPC op MT-niveau ✓. Tegen: testresultaten iteratie 2 niet zichtbaar, verbeterloop dun, 2-concepten-eis niet expliciet afgehandeld, externe gate ontbreekt en niet benoemd, pivot-narratief 4-5x te glad, VPC generiek. |
| **Na blokkerende fixes 1-6** | **8 - 8,5** | Methodisch verantwoord, pivot eerlijk, data toonbaar. Goed (8) op rubric 1b = "methodisch ontwikkeld en cyclisch getest op meerwaarde, zeer gedetailleerd, aantoonbaar praktisch toepasbaar" — dan haal je dat. |
| **Na alle fixes inclusief 7-13** | **9** | Kritische reflectie + per-segment VPC + meta-methodiek + citaten maken het uitmuntend-waardig — maar voor 10 heeft Henk écht externe validatie nodig (gate met notaris of bank). Zonder die externe gate is 10 op rubric 1a/1b structureel buiten bereik, want "rigoureuze methodiek met meervoudige validatie" staat of valt met externe testing. |
| **Voor 10** | nodig: externe gate | Interview minimaal 1 notaris of bankmedewerker, laat diegene het prototype/VPC zien, documenteer reactie. Dan pas is "aantoonbaar praktisch toepasbaar" volledig waargemaakt. |

---

*Review door Claude, 19 april 2026. Gebaseerd op source van `src/pages/refine/*.astro`, `docs/onderzoek/testplannen-pelv.md`, `docs/onderzoek/herframe-pivot-digitaal.md`, `docs/opdrachten/opdracht-1c-refine-prototype-test.md`, `docs/lessen/les5-rapid-prototyping.md`, `docs/lessen/les6-concept-collections-prototyping.md`, `docs/beoordeling/rubric.md`.*
