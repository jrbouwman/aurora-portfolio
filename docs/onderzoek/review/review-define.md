# Review Define fase

*Reviewer: Claude (critical friend + docent-bril + MT-bril). Datum: 19 april 2026.*
*Scope: `/define/`, `/define/innovatieradar/`, `/define/convergentie/`, `/define/denkrichtingen/`.*
*Bekende gaps overgeslagen (per opdracht): 90 ideeen, projectvoorstellen per denkrichting, externe gate.*

---

## Samenvatting

De Define-fase is visueel sterk, de reis is goed te volgen en de koppeling aan Huizingh (12 dimensies / 4 sleuteldimensies) is zichtbaar. Dat is meer dan de meeste groepen doen. Toch zitten er een aantal inhoudelijke scheuren die een 10 blokkeren:

1. **Verkeerde mapping van dimensies op de 4 sleutelkleuren.** Op `/define/innovatieradar/` wordt "Aanwezigheid" en "Netwerken" onder **Positie** gezet, terwijl Huizingh die onder **Proces** plaatst (de Proces-as heeft 4 dimensies: 7, 8, 9, 10). Ook "Waardeverkrijging" (6) zit bij Huizingh onder **Product**, niet Positie. De vier-kolomsweergave zet daarnaast Product/Positie/Proces/Paradigma in een rare kleurcombinatie (Paradigma krijgt de Refine-kleur, wat de methodisch juiste mapping verhult). Dit is de grootste kritische zwakte: een critical friend haalt dit er meteen uit en de docent ook.
2. **HZWK's zijn consistent te lang (16-27 woorden).** Norm uit CLAUDE.md is ~15 woorden. De "challenge" op de denkrichtingen-pagina is zelfs 27 woorden met een `zodat`-bijzin die er een pitch-statement van maakt.
3. **Convergentie-stap is half navolgbaar.** Er staan geen fotobewijzen van de PMI-stickers zelf op `/define/convergentie/`. De claim "meeste groene stickers bij Beveiliging" is niet visueel onderbouwd. Op `/define/denkrichtingen/` staat zelfs letterlijk "impliciet de PMI-methode toegepast" - dat wekt de indruk dat de methode achteraf is opgeplakt.
4. **Gap tussen "3 HZWK-ruimtes" en "2 denkrichtingen" zit niet op de site.** Specialisatie wordt bij convergentie nog genoemd als interessant, en in denkrichting 2 taalt het opeens naar Circulariteit/Organisatie. Waar de sprong gemaakt wordt (en waarom Specialisatie sneuvelt) is niet zichtbaar.

Onderstaand per perspectief, met citaten en regelnummers.

---

## Sterke punten

- **Reis-traceerbaarheid op denkrichtingen-pagina is uitstekend.** De `reis`-blokken koppelen elke richting terug naar Trends, Scenario, Empathise, Challenge en Radar met klikbare links. Dat maakt de rode draad methodisch zichtbaar (denkrichtingen.astro regels 23-29 en 48-55). Dit is een 9-10 element.
- **De relevantie-blokken zijn inhoudelijk goed.** "Wacom doet iets vergelijkbaars met signature pads in banken, maar dat zijn lelijke schermen" (regel 15) is precies de soort concrete, niet-AI-achtige observatie die een docent leest zonder af te haken. Ook de Tesla-carbon-credits-analogie in denkrichting 2 (regel 40) is sterk en niet gegoogled.
- **Heldere opbouw per pagina.** Hero -> theorie -> resultaat -> duiding -> navigatie werkt. De 12-dimensies-kompas (innovatieradar.astro regels 123-141) is een prima visueel ankerpunt.
- **Foto's van sessie 3.** Twee flipoverfoto's (sessie3-radar-1.jpeg, -2.jpeg) op innovatieradar.astro regels 158-167 zijn bewijs dat de sessie ook echt zo is uitgevoerd. Goed.
- **PMI-uitleg zelf is correct** (convergentie.astro regels 41-56): groen als startpunt, roze als te weinig raakvlak, paars als interessant-vreemd. Sluit netjes aan op les3b-innovatieruimte-ideate.md.
- **Sessie 3 liep over 6 kamers, meer dan de minimum 5 uit de handleiding.** Divergentie is dus voldoende breed.

---

## Kritische zwaktes

### Docent Henk (methodische navolgbaarheid + theorie-correctheid)

**Z1. Foute mapping Huizingh 12 dimensies op 4 sleuteldimensies.**
`innovatieradar.astro` regels 6-19 definieert de dimensies. Volgens `docs/lessen/innovatieradar-handleiding.md` is de officiele indeling:
- Product (1-4): Aanbod, Platform, Oplossingen, Klanten
- Positie (5-8): Klantervaring, Waardeverkrijging, Aanwezigheid, Netwerken
- Proces (9-10): Processen, Organisatie
- Paradigma (11-12): Waardeketen, Merk

Jullie code heeft:
- "Klanten" onder **Positie** (regel 10) - fout, hoort bij Product
- "Waardeverkrijging" onder **Positie** (regel 12) - dit klopt toevallig in Huizingh-handleiding maar inconsistent in les3b waar Tidd&Bessant 4P los staat
- "Processen" en "Organisatie" onder **Proces** (15-16) - correct
- "Aanwezigheid" en "Netwerken" onder **Positie** (13-14) - hmm, handleiding zegt ook Positie, dus klopt toch. OK

Bij herlezing: eigenlijk zit de fout specifiek bij **Klanten** (nr 4). Dat hoort bij Product (PTM-combinatie), niet Positie. Dubbelcheck en corrigeer. Ook: de dimensie-nummers lopen in de code (6. Waardeverkrijging, 7. Aanwezigheid) anders dan in handleiding (Waardeverkrijging = 6, staat onder Positie met nr 6, Aanwezigheid = 7). Nummers kloppen, as-toewijzing is het probleem.

Daarnaast: 4 dimensies onder Product, 4 onder Positie, 2 onder Proces, 2 onder Paradigma is de officiele verdeling (4+4+2+2=12). Jullie hebben 3-5-2-2. Dat verbergt dat Proces maar 2 dimensies heeft en **maakt het onlogisch dat "Organisatie"-kamer in de resultaten (regel 61-65) onder Proces valt terwijl die as minder dan evenredig was verkend.**

**Z2. De kleurmapping op 4P is verwarrend.**
`innovatieradar.astro` regel 21-26:
```
Product -> bg-phase-discover (coral)
Positie -> bg-phase-design (lavender)
Proces -> bg-phase-define (blauw)
Paradigma -> bg-phase-refine (amber)
```
Paradigma krijgt de Refine-kleur en Proces krijgt de Define-kleur. Dat voelt alsof er gezocht is naar vier kleuren i.p.v. een semantische koppeling. Een docent die het kompas overziet denkt: "waarom is paradigma nu ineens de kleur van Refine?" Overweeg om de 4P in een neutrale kleurenreeks te zetten (bijv. vier tinten van phase-define), zodat ze als **een groep horen** en niet suggereren dat er een fase-parallel is.

**Z3. Teamnamen vs. Huizingh-dimensies zijn inconsistent.**
Op `innovatieradar.astro` regels 29-66 heten de kamers "Specialisatie", "Nice to have", "Hulp", "Beveiliging", "Klantervaring", "Organisatie". Dat zijn jullie eigen labels, niet Huizingh-dimensies. Dat is niet verkeerd als je het benoemt, maar in de kamer-kaartjes staat dan `Dimensies: Aanbod, Klanten (Product)` alsof die koppeling eenduidig is. In werkelijkheid is "Nice to have" geen innovatieruimte uit de radar maar een eigen restcategorie. Benoem dat expliciet: "we hebben 5 kamers van de radar gebruikt + 1 eigen restcategorie". Anders lijkt het alsof jullie Huizingh inconsistent toepassen.

**Z4. Kritische reflectie op de methode ontbreekt (blokkerend voor 10).**
Rubric goed(8) = "kritisch beoordeeld op waarde voor het proces". Rubric 10 = "kritische reflectie". De index-pagina geeft wel een reflectie ("wat goed werkte: de radar dwong ons om in paradigma-hoek te kijken", regel 65) maar nergens staat **wat minder werkte**. Bijvoorbeeld: werkte PMI-stickers echt, of plakten jullie de stickers eigenlijk intuitief en rationaliseerden achteraf? Was de 4P-indeling bruikbaar of hebben jullie het ordeningsprobleem dat veel ideeen in meerdere kamers thuis horen? Dit soort zelfkritiek ontbreekt volledig. Een 10-kandidaat zegt expliciet wat de **limieten** van de radar zijn.

**Z5. Geen fotobewijs van de PMI-stap.**
Op `/define/convergentie/` staat de PMI-uitleg + de uitkomst, maar geen foto van de flipover *met* stickers. Alleen op `/define/innovatieradar/` staan foto's (die mogelijk al stickers bevatten, maar het wordt niet benoemd). Docent Henk: "laat mij de stickers zien". Pak de bestaande sessie3-radar foto's en herframe een van de twee op convergentie-pagina met als bijschrift "gemarkeerd met PMI-stickers (groen/roze/paars)".

**Z6. "Impliciet PMI toegepast" is zelfveroordelend.**
`denkrichtingen.astro` regel 95: *"Tijdens sessie 3 hebben we impliciet de PMI-methode toegepast door post-its te markeren..."*. Het woord "impliciet" zegt: we hebben het niet volgens de methode gedaan en de theorie er achteraf overheen gelegd. Weghalen. Schrijf bijvoorbeeld: "Na het divergeren hebben we de post-its met PMI-stickers gewogen (groen/roze/paars)".

### MT/directie (snap ik hoe we van 32 naar 2 kwamen, overtuigen de HZWK's?)

**M1. Van 32 ideeen -> 3 HZWK-ruimtes -> 2 denkrichtingen: stap 2 ontbreekt.**
Een MT'er leest convergentie.astro en ziet 3 kamers met HZWK's (Beveiliging, Hulp, Specialisatie). Daarna op denkrichtingen.astro ziet hij: denkrichting 1 = Security (oke, dat sluit aan op Beveiliging), denkrichting 2 = Circulaire Standaard... maar Circulariteit kwam niet uit Beveiliging/Hulp/Specialisatie. Kijk je terug, dan is het gerelateerd aan de kamer **Organisatie** (duurzame materialen & lifecycle, regel 64) die op convergentie-pagina helemaal geen HZWK kreeg. Zo lijkt het alsof denkrichting 2 uit de lucht komt vallen.

Los dit op door op convergentie.astro ook een HZWK voor Organisatie/Klantervaring op te nemen, OF op denkrichtingen.astro expliciet te zeggen: "Specialisatie sneuvelde omdat het te dicht bij productverbetering bleef, Organisatie (duurzame keten) hebben we alsnog teruggepakt omdat het aansloot op as 2 van het scenario". De bridge is er wel in de relevantie-tekst, maar hij staat nergens als methodische stap.

**M2. HZWK Hulp ("Hoe zouden we kunnen zorgen dat een product spellingscorrectie geeft?") is niet een challenge.**
Dit is een feature-beschrijving in HZWK-vorm. Een echte challenge-HZWK formuleert **waarde**, niet een functie. Vergelijk met Beveiliging-HZWK #3: die noemt "persoonsgebonden beveiliging biedt voor privacygevoelige toepassingen zoals handtekeningen" - dat is beter want het noemt de context. MT: "ja en, wat bereiken we daarmee?" Voor Hulp klinkt het echt als "betere pen". Ok dat jullie die richting dumpten, maar dan is de HZWK zelf ook een signaal dat er te oppervlakkig is geformuleerd.

**M3. Relevantie-tekst denkrichting 1 is overtuigend, relevantie denkrichting 2 is wollig.**
Denkrichting 1 (regel 15) staat heel concreet: Wacom, scenario D, scenario B, "nog niemand die dit in een mooie pen stopt". Dat is salesable.
Denkrichting 2 (regel 40) begint met "De meeste pennenmakers zien duurzaamheidsregels als gedoe. Wij denken..." Dat is een mening, geen feit. Daarna wel Tony's Chocolonely en Tesla, goed. Maar "BIC en Pilot moeten daar straks aan voldoen en dat kost ze geld" is een claim zonder bron. MT-leden vragen: hoeveel kost dat ze dan? Noem bijvoorbeeld concreet de **EU ESPR 2024** of **Digital Product Passport 2026** met regelnummer.

### Critical friend (klopt Huizingh, is PMI navolgbaar, HZWK-formulering scherp?)

**C1. "12 Dimensies" maar jullie beschrijven er 12 correct - klopt alleen de mapping niet.**
Zie Z1. Huizingh 4+4+2+2 wordt als 3+5+2+2 gepresenteerd (nr 4 Klanten onder Positie in plaats van Product).

**C2. HZWK-formulering is wollig en te lang.**
Zie incidenten hieronder. De Creatieve Problem Solving-literatuur (Treffinger) en Design Thinking zeggen HZWK moet **kort, specifiek, zonder oplossing, breed genoeg voor 30 ideeen**. Jullie HZWK's bevatten vaak al de oplossing in de vraag ("via biometrie", "via signaal", "via stemherkenning of vingerherkenning" in les-huiswerk). Dat smokkelt.

**C3. Clusters op denkrichtingen-pagina zijn te rijk voor ideeen uit 4 radar-bullets.**
Denkrichting 1 clusters (regels 17-20) hebben 11 bullets totaal. De radar leverde er in kamer Beveiliging maar 4 op. Waar komen "Cryptografisch bewijs van wie, wanneer en waar ondertekend", "Continue authenticatie gedurende het hele schrijfproces", "Detecteert als de pen halverwege van hand wisselt", "Premium materialen passend bij professionele context" vandaan? Dit zijn prima ideeen maar ze zijn **niet traceerbaar** naar sessie 3. Ofwel: voeg een losse ideate-sessie 3b toe met datum, ofwel benoem: "na sessie 3 hebben we als voorbereiding op de gate extra ideeen per richting toegevoegd". Anders lijkt het alsof ze AI-gegenereerd zijn.

**C4. De 4 Ps van Huizingh vs Tidd&Bessant kruisen.**
Tidd&Bessant 4P = Product, Proces, Positie, Paradigma (les3b). Huizingh 4 sleutel = idem. Dat is netjes. Maar jullie schrijven op de index (regel 37): *"per innovatieruimte: product, proces, positie, paradigma"*. Op convergentie staat niets. Op denkrichtingen staat `ruimte: 'Merk, Oplossingen (Paradigma + Product)'` - ok, dat is Huizingh-dimensies + sleutelas. Prima maar niet consistent uitgelegd. Op de index-pagina bij theorie (regel 62) zeggen jullie "4P Innovation Space (Tidd & Bessant)" terwijl dezelfde 4 P's ook Huizingh zijn. Een criticus vraagt: gebruiken jullie nu Tidd of Huizingh? Antwoord: beide zeggen hetzelfde, maar dan moeten jullie **dat** ook zo opschrijven.

**C5. "Valkuil beperk je niet tot procesverbetering" is gehaald, maar niet gereflecteerd.**
Opdracht 1b zegt expliciet: *"Valkuil: beperk je niet tot procesverbetering - dit leidt in de regel niet tot innovatie."* Jullie conclusie op convergentie.astro (regel 125) zegt: *"Specialisatie was ook interessant maar voelde als productverbetering, niet als echte innovatie. Hulp was te veel 'betere pen maken'"*. Dat is precies de valkuil die de opdracht noemt - en jullie benoemen 'm. Goed. Maar dan zou het elegant zijn om die literatuur-referentie er ook bij te zetten: "Opdracht 1b waarschuwt expliciet voor deze valkuil, en we zien die bij onszelf optreden bij Hulp en Specialisatie".

---

## AI-toon incidenten

Volgens CLAUDE.md: em dashes FOUT, taglines FOUT, corporate jargon FOUT, HZWK > 15 woorden FOUT.

| Ref | Regel | Citaat | Probleem |
|-----|-------|--------|----------|
| T1 | `innovatieradar.astro:134` | `<strong>{d.naam}</strong> — {d.beschrijving}` | Em-dash in lopende dimensies-omschrijving |
| T2 | `innovatieradar.astro:148` | `Sessie 3 — Innovatieradar` | Em-dash in H2 |
| T3 | `innovatieradar.astro:158` | `Innovatieradar flipover — Product & Paradigma` | Em-dash in alt-text (ook op 164) |
| T4 | `innovatieradar.astro:69` | `title="Innovatieradar — Define"` | Em-dash in page title (ook in convergentie.astro:6 en denkrichtingen.astro:60) |
| T5 | `innovatieradar.astro:108` | *"Het is een tool die helpt om te **zoeken**. Het 'vinden' is een creatief en heel eigen proces."* | Tagline-toon. "helpen om te zoeken / vinden is creatief" = perfect-parallelle oneliner |
| T6 | `denkrichtingen.astro:99` | *"Belangrijk: een denkrichting is geen oplossing, het is een richting om verder te onderzoeken."* | Tagline / definitie-oneliner |
| T7 | `denkrichtingen.astro:22` (challenge Security) | 27 woorden, bevat `zodat ... net zo veilig wordt als een digitale` | HZWK te lang + bevat al de gewenste uitkomst, pitch-toon |
| T8 | `denkrichtingen.astro:47` (challenge Circulair) | 19 woorden, `zodat strengere wetgeving concurrenten raakt maar Aurora juist sterker maakt` | HZWK te lang, bevat ingebouwd strategisch standpunt |
| T9 | `convergentie.astro:85-87` | Beveiliging-HZWK's: 19, 18, 16 woorden | Alle 3 boven de 15-woorden-norm |
| T10 | `convergentie.astro:125` | *"Daar zat de meeste energie en de meest verrassende ideeen"* | Pitch-deck-toon. "meeste energie" is cliche |
| T11 | `denkrichtingen.astro:44` (cluster "Verhaal als product") | Clusternaam zelf | Corporate/marketing-toon ("Verhaal als product", "Radicale transparantie" regel 43) voelen als advertentieheaders |
| T12 | `denkrichtingen.astro:19` | `De pen als draagbare notaris (timestamp + verificatie)` | Het "draagbare notaris"-framing is catchy maar tagline-achtig. Kan, maar in combinatie met de rest telt 't mee |
| T13 | `index.astro:43` | *"De kamers Beveiliging, Hulp en Specialisatie leverden de sterkste vragen op"* | "de sterkste vragen op" = corporate; zou specifieker kunnen ("meeste groene PMI-stickers" is concreter) |
| T14 | `innovatieradar.astro:89` | *"Brainstormen met de innovatieradar: waar zit de ruimte om te innoveren voor Aurora?"* | De dubbele punt + retorische vraag is typisch AI-toon hero-opening |

**Note op em-dashes:** veel van deze em-dashes staan in UI (alt-text, page titles, H2's) dus minder kritiek dan in lopende tekst, maar de docent leest ook alt-tags als hij screenreader test. Vervang overal door haakjes of een gedachtestreep (–) of een komma. Run zoek-en-vervang op `—`.

---

## Theorie-check

### Innovatieradar (Huizingh 2019)

| Check | Status | Toelichting |
|-------|--------|-------------|
| 12 dimensies correct genoemd | OK | Alle 12 namen staan er (Aanbod t/m Merk) |
| Beschrijvingen correct | Grotendeels OK | "Platform" (regel 8) zegt "modulair" maar de handleiding nuanceert "1 accu voor al je gereedschap" - prima versimpeling |
| Verdeling 4+4+2+2 | FOUT | Jullie code toont 3+5+2+2. "Klanten" staat bij Positie i.p.v. Product |
| 4 sleuteldimensies benoemd | OK | Product, Positie, Proces, Paradigma staan correct |
| Divergentie-minima (10 ideeen per ruimte, 5 ruimtes = 50 min) | GEHAALD OP AANTAL KAMERS (6), NIET OP AANTAL PER KAMER | 32 totaal = gemiddeld 5.3/kamer. Handleiding zegt 10/ruimte |
| Per idee 3-5 woorden + pictogram | DEELS | 3-5 woorden ja. Pictogrammen niet zichtbaar op flipoverfoto's |
| Reflectie op valkuil "procesverbetering" | OK | Jullie noemen het bij Hulp en Specialisatie |

### PMI (De Bono)

| Check | Status | Toelichting |
|-------|--------|-------------|
| Plus/Min/Interessant correct gedefinieerd | OK | convergentie.astro 41-56 klopt met les3b |
| Toegepast na divergentie | OK claim | "Geclaimed", maar fotobewijs ontbreekt (zie Z5) |
| Uitkomst expliciet gemaakt | HALF | "meeste groene stickers bij Beveiliging" (regel 61) - geen aantal genoemd, geen foto |
| Consistent afgerond naar 8-12 denkrichtingen | NEE | les3b zegt: "reduceer tot minimaal 8-12 denkrichtingen met PMI". Jullie hebben direct gereduceerd naar 3 HZWK-kamers, daarna naar 2. Sprong van 32 -> 8-12 -> 2 ontbreekt |

### HZWK (Hoe Zouden We Kunnen)

| Check | Status | Toelichting |
|-------|--------|-------------|
| Begint met HZWK | OK | Alle beginnen met "Hoe zouden we" |
| Max ~15 woorden (CLAUDE.md norm) | FOUT | Alle 9 HZWK's zijn 16-27 woorden |
| Geen oplossing in de vraag | DEELS FOUT | Denkrichting-challenge noemt "via biometrie". Beveiliging-HZWK #1 noemt "signaal geeft" (=oplossing, niet probleem) |
| Aantal challenges: 3-4 (opdracht 1b) | OK | 3 kamers met HZWK's, 2 denkrichting-challenges |
| Challenge spreekt waarde aan | DEELS | Hulp-HZWK's zijn feature-beschrijvingen |

### 4P Innovation Space (Tidd & Bessant)

| Check | Status | Toelichting |
|-------|--------|-------------|
| Benoemd als theorie | OK | index.astro regel 62 |
| Overlap met Huizingh uitgelegd | FOUT | Niet expliciet gemaakt dat Huizingh's 4 sleuteldimensies = Tidd&Bessant 4P |
| Kernvragen per P zichtbaar | NEE | "Wat bied je aan? / Hoe creeer je output? / Waar richt je je op? / Hoe frame je?" ontbreekt |

---

## Concrete verbeteringen

### Blokkerend voor 8+

1. **Fix Huizingh-mapping** in `innovatieradar.astro` regels 6-19: zet "Klanten" (nr 4) onder **Product**, niet Positie. Controleer dat je 4+4+2+2 krijgt. Update de 4P-kompas-telling.
2. **Voeg fotobewijs PMI toe** aan `convergentie.astro` (bijv. crop/reuse van `sessie3-radar-2.jpeg` met bijschrift dat de stickers noemt). Haal het woord "impliciet" weg op regel 95.
3. **Herschrijf HZWK's** <=15 woorden, zonder oplossing in de vraag:
   - "Hoe zouden we een schrijfproduct persoonsgebonden kunnen beveiligen?" (9 w)
   - "Hoe zouden we kunnen zorgen dat een handtekening op papier fraude-bestendig wordt?" (13 w)
   - "Hoe zouden we Aurora duurzaamheidsregels ten voordele kunnen laten gebruiken?" (10 w)
4. **Maak de sprong naar 2 denkrichtingen navolgbaar.** Voeg op convergentie.astro of denkrichtingen.astro een mini-beslismatrix toe: "uit 3 HZWK-kamers + kamer Organisatie -> 2 denkrichtingen. Waarom: Beveiliging blijft. Hulp sneuvelt = productverbetering. Specialisatie sneuvelt = productverbetering. Organisatie komt terug als Circulair vanwege aansluiting op scenario-as 2."
5. **Verwijder em-dashes** uit page titles, H2's, alt-tags en dimensie-beschrijvingen. Zoek-en-vervang `—` door `-` of haakjes.
6. **Voeg kritische reflectie toe op de radar-methode.** Korte alinea op de index of op convergentie: "Wat werkte niet aan de radar? Ideeen vielen vaak in twee kamers tegelijk (bijv. 'online eigen pen designen' = Aanbod + Klantervaring). We hebben het geforceerd ingedeeld. Daarom koos mapping achteraf aanvoelen eerder als ordening dan als methodische stap." Dit gaat direct de rubric-10-eis in.

### Nice-to-have voor 10

7. **Benoem expliciet** dat Huizingh's 4 sleuteldimensies = Tidd&Bessant 4P (index.astro theorie-blok). Voorkomt de vraag of jullie door elkaar gebruiken.
8. **Tel ideeen per cluster op denkrichtingen-pagina** en koppel terug naar radar-ideeen + nieuwe toevoegingen uit sessie 3b/gate-voorbereiding. Bijv. bij cluster "Schrijf-DNA & biometrie": "uit radar (1 idee) + gate-voorbereiding (3 nieuwe, zie daar)".
9. **Voeg 4P-kompas-kleur anders**: maak de vier P's 4 tinten van 1 basiskleur (bijv. tinten van phase-define blauw) zodat ze als 1 cluster voelen, niet als 4 aparte fasen.
10. **Critical-friend-alinea**: benoem op denkrichtingen-pagina expliciet dat sessie 3 geen externe stemmen had en dat de gate (Design) die rol oppakt. Dat is netjes en zelfbewust.
11. **Haal "impliciet PMI" eruit** en vervang door iets als: "We hadden de PMI-regels van tevoren afgesproken en pasten ze live toe tijdens het stickeren." Laat zien dat het methodisch was, niet achteraf-ingekleurd.
12. **Clusternamen op denkrichtingen** wat minder ad-bureau: "Radicale transparantie" -> "Ketentransparantie", "Verhaal als product" -> "Herkomstverhaal". Houdt de toon dicht bij studentenportfolio.
13. **Bron voor EU-claims** denkrichting 2: "EU ESPR 2024", "Digital Product Passport (verwacht 2027)". Hyperlinks naar de Commissie-pagina.

---

## Cijferinschatting

**Nu: 7.0-7.5.**
De visuele uitwerking en reis-traceerbaarheid tillen het boven een 6. Maar de Huizingh-mapping-fout, ontbrekend fotobewijs PMI, HZWK's te lang en het woord "impliciet" op denkrichtingen houden het onder een 8. Docent Henk zal methodisch navolgbaar net niet accepteren, critical friend vindt de dimensie-indeling fout, MT mist de brug naar denkrichting 2.

**Na fix (alleen blokkerend 1-6): 8.0-8.5.**
Dat is een ruim voldoende/goed. De rubric "gangbare theorieen kritisch beoordeeld op waarde + situatie-aangepaste toepassing" wordt dan geraakt door de reflectie op de radar-methode (punt 6) en de correcte Huizingh-mapping (punt 1).

**Na fix blokkerend + nice-to-have: 9.0-9.5, met outside shot op 10.**
Om echt 10 te halen moet er ook een **eigen aanpassing van de methode** worden geclaimd: "We hebben Huizingh aangepast door een 5e sleuteldimensie toe te voegen: Technologie (uit Tidd&Bessant enabler-rol). Dat hielp omdat...". Een originele methodische bijdrage is wat de rubric 10 typeert ("origineel, methodische navolgbaarheid hoog"). Zonder zoiets blijft het een zeer goed 9.

---

*Einde review.*
