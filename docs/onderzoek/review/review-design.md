# Review Design fase

Review van `/design/`, `/design/gate/` en `/design/concept-collection/` op de site, tegen opdracht 1b, lessen 3/3b en de rubric. Jr mikt op een 10.

## Samenvatting

De Design-fase vertelt een eerlijk verhaal: gate met twee externe reviewers, DVF-formulieren, value curve, bewuste keuze voor Security Expert ondanks 1 punt lagere score. Dat is op hoofdlijnen prima en de eerlijkheid rond de keuze ("we waren aan het goedpraten", "meer energie") is geloofwaardig. Maar: voor een 10 is het te dun en mist het de theoretische diepgang die de rubric eist.

Drie harde gaten:
1. **DVF is cijferkaal** — alleen totalen 74/73 worden getoond, geen uitsplitsing per D, V en F, geen diagnose van waar Circulair scoorde en waar Security. Daardoor is "1 punt verschil zegt weinig" een hand-waving argument in plaats van een onderbouwde afweging.
2. **Blue Ocean is alleen een plaatje** — de value curve hangt er als foto, maar nergens op de site wordt uitgelegd welke factoren op de as staan, welke lijn welke denkrichting is, wie de concurrentie is en welke ERRC-bewegingen (Eliminate/Reduce/Raise/Create) uit de curve volgen. Het framework wordt genoemd, niet toegepast.
3. **De concept collection is overwegend tekst** — productvormen, authenticatiemethoden en "wilde kruisbestuivingen" staan als lijstjes op de pagina; de 35+ beelden zitten achter een PPTX-download. Dat is precies niet hoe een concept collection volgens de lesstof werkt (visueel verzamelen, kwantiteit als kwaliteit).

De keuze voor Security ondanks lager DVF is nu op gevoel verantwoord, niet op methodiek. Dat is het grootste risico voor de rubric-interpretatie "kritische theorie-toepassing".

Huidige inschatting: **7 tot 7,5**. Met de fixes hieronder: **9**.

## Sterke punten

- **Gate met externen goed gevisualiseerd**: foto's van DVF-formulieren en value curve staan erbij, nette opmaak met hero-image en vermelding van beide Niels'en.
- **Eerlijkheid over keuze**: "we waren bij sommige punten aan het goedpraten" en "desirability was lastig te onderbouwen zonder concreet beeld van de klant" (gate.astro, regel 69-71) zijn zeldzaam eerlijke studentenformuleringen. Niet gladgestreken. Daar zit leervermogen in.
- **Bewuste dump van Concept Collection 2** expliciet benoemd, inclusief motivatie. Niet stiekem laten vallen, maar openlijk verantwoord (concept-collection.astro regel 77-80, 165-169).
- **Divergentie-intentie klopt op conceptueel niveau**: "we hebben ons bewust losgemaakt van de pen. De vraag was niet 'hoe maken we een betere pen' maar 'hoe kan authenticatie eruitzien?'" (concept-collection.astro, regel 94-97). Dat is precies de juiste verschuiving en legt inhoudelijk een kiem voor de latere pivot.
- **Theorie-termen genoemd**: DVF, Blue Ocean, concept collections, Kim & Mauborgne. Het kader wordt wel benoemd.

## Kritische zwaktes

### Docent Henk

Henk beoordeelt op kritische theorie-toepassing en bewijsstukken. Hier zitten de scherpste pijnpunten:

- **DVF wordt niet diagnostisch gebruikt**. Totalen 74 en 73 zonder subscores. Hoe scoorde Circulair op D, V en F afzonderlijk? En Security? Juist die uitsplitsing maakt DVF waardevol (je kunt zien "Security is feasibility-sterk maar viability-zwak"). Zonder subscores is het cijferfetisjisme. De opdracht bedoelt DVF als analyse-instrument, niet als stemhokje.
- **Blue Ocean zonder ERRC**. De lesstof (les3 r.90-98, les3b r.83-93) is expliciet: value curve hoort bij het ERRC-framework (Eliminate, Reduce, Raise, Create). Op de site staat nergens welke factoren Aurora Eliminate-t, Reduce-t, Raise-t en Create-t ten opzichte van bestaande schrijfwaren-concurrentie. Het hele punt van Blue Ocean wordt zo gemist. ERRC komt 0 keer voor in `src/pages/design/`.
- **Value curve niet gelezen**. De foto staat erop, maar er is geen tekst die zegt "op de x-as staan de volgende factoren (...), onze curve duikt laag bij X en klimt hoog bij Y, dit is onze blue ocean". Een docent kan de curve niet reviewen zonder die context.
- **"2 van de 4 DVF-formulieren getoond"**. In `public/images/research/gate/` staan `gate-dvf-1.jpg` t/m `gate-dvf-4.jpg`, op de pagina worden alleen 1 en 2 ingeladen (gate.astro r.123, 129). Waarom? Of het zijn beide Niels'en dubbel (dan uitleggen), of er ontbreken 2 (dan toevoegen).
- **"Minimaal 2 anderen" gehaald, goed, maar scope is intern**. Opdracht 1b zegt "minstens 2 anderen", dat is binnen. Maar rubric-uitmuntend vraagt om kritische keuzes; twee medestudenten uit dezelfde klas is de laagste dosis externaliteit. Geen dealbreaker, wel een missed opportunity (er is later nog tijd, of benoem expliciet dat externe gate voor Gate 3 komt).
- **Bewijs van 90 ideeen ontbreekt in Design**. Opdracht 1b: "Bedenk voor de challenges tenminste 30 ideeen per challenge (dus totaal 90!)". Op de designpagina's wordt dit aantal niet genoemd of verantwoord. CLAUDE.md vermeldt dat er 32 ideeen waren; dat is 58 onder de norm en staat niet in de portfolio-verantwoording.

### MT/directie

Een MT-lezer wil snappen "waarom dit, waarom nu, waarom dit team":

- **"Meer potentie" is niet onderbouwd**. Zin: "een punt minder, maar we waren het er met z'n allen over eens: hier zit meer potentie in" (gate.astro r.84-85). MT vraagt: potentie waarin? Marktvraag? Marge? Differentiatie? Zonder concretisering is dit teamgevoel, geen business case.
- **Geen marktplaatsing**. De Security-richting wordt niet gepositioneerd tegenover bestaande handtekeningverificatie (notaris-procedures, PKIsigning, DigiD). Die context wordt pas in de pivot opgebouwd, maar MT wil het nu al weten: "concurreren we met wie?"
- **Concept collection komt over als brainstormlijstje**. Productvormen (ring/smartwatch/handschoen) en kruisbestuivingen (octopus/Banksy/yoga) landen als tekst; voor een MT'er oogt dat als "oppervlakkig ideeenlijstje" zonder visuele onderbouwing. De PPTX-download redt dat niet, een MT'er klikt die niet open.
- **Richting is nog niet concreet**. Na deze fase weet een MT niet waar de richting naartoe gaat, behalve "authenticatie via de pen". Dat is prima voor Design (je moet divergeren), maar benoem dat expliciet: "Refine gaat dit scherp maken, nu bewust open gehouden".

### Critical friend

De vriend die meeleest en scherpe vragen stelt:

- **"Op gevoel gekozen" is methodisch zwak**. Je hebt een scoringsinstrument gebruikt, Circulair wint, daarna gebruik je gevoel om Security te kiezen. Dat is okay mits je het herkadert: de gate-uitkomst was "Circulair lijkt op papier beter, maar bij het invullen merkten we dat onze desirability-score voor Circulair geparkeerde aannames waren. De D-score van Security was lager maar harder onderbouwd." Die herkadering zet je neer als volwassen methodische reflectie in plaats van als bauchgefuhl.
- **Circulair wordt te licht gediskwalificeerd**. "voelde meer als theoretisch verhaal" (r.93-96) is vaag. Wat maakte het theoretisch? Geen concrete klant in zicht? Geen bestaand vraagsignaal? Geen teamcompetentie? Zonder die diagnose mist de critical friend bewijs dat je Circulair echt hebt afgewogen in plaats van weggeduwd.
- **Value curve grafisch check**. Op basis van de foto alleen kan critical friend niet zien of de curve scherp tegen concurrentie is gezet. Dit moet als SVG of uitleg terugkomen op de site.
- **Concept collection: te netjes**. Banksy, yoga en koken staan op de pagina, maar de "maximaal divergerend" belofte vraagt om zichtbare wildheid. In de les: kwantiteit is kwaliteit, de muur moet vol. Nu zijn er 7 kruisbestuivingen keurig in een 3x3-grid. Dat oogt beheerst, niet beheerst-chaotisch. Zet minimaal 15-20 beelden inline met korte caption.
- **Kern-vragen concept collection niet beantwoord**. Lesstof (`concept-collections.md` r.25-30): "Hoe is dit al eens geprobeerd? Waar lijkt dit op? Wie is expert? Hoe zien vergelijkbare oplossingen eruit in andere domeinen?" Geen van deze vragen wordt op de pagina beantwoord of getoond.
- **Kiem voor pivot is latent aanwezig maar niet benoemd**. De zin "we hebben ons bewust losgemaakt van de pen" is precies de kiem. Voeg een vooruitblik-blok toe: "deze losmaking van de pen bleek achteraf cruciaal; in Refine doorlopen we dit tot de pivot naar digitale verificatie". Nu komt de pivot straks uit de lucht vallen.

## AI-toon incidenten

Op AI-toon scoort de Design-fase relatief schoon. Gevonden:

- **Gladde subtitel** in gate-hero: *"Twee denkrichtingen voorgelegd, eentje gekozen. Niet op basis van de score, maar op gevoel en haalbaarheid."* (gate.astro r.26-27). "Niet op X, maar op Y" is een klassieke AI-oneliner-parallel. Echter: Jr mag pitchen, dus borderline. Suggestie: "Twee denkrichtingen voorgelegd, Security gekozen. Het cijfer was een punt lager, de richting voelde concreter." Minder parallel, meer normaal.
- **Marketingy belofte** in concept-collection-hero: *"Alles verzamelen wat ook maar iets te maken heeft met authenticatie en verificatie. Hoe wilder, hoe beter."* (concept-collection.astro r.57-58). "Hoe wilder, hoe beter" is tagline-achtig. Niet fout maar formulerend naar het slogan-randje.
- **Strak-parallelle opsommingen** bij Productvormen en Authenticatiemethoden (concept-collection.astro r.5-25): elk item is 1 strakke regel, allemaal evenlang. Voor een echte concept collection zou de ruwheid (schetsjes, random foto, onuitgewerkt idee) betere geloofwaardigheid geven.
- **Pitch-achtig slot** bij Circulaire kader: *"bij sommige punten aan het 'goedpraten' waren"* is juist goed (spreektaal). Behouden.

Em-dashes in lopende tekst: **geen gevonden**. Alleen in HTML page titles (`title="Gate — Design"`), niet zichtbaar voor lezer.

## Theorie-check (DVF, Blue Ocean/ERRC, concept collections)

**DVF (Desirability, Viability, Feasibility)**
- *Toegepast?* Ja, formulieren ingevuld met 2 reviewers.
- *Kritisch toegepast?* Nee. Alleen totaalscores getoond. Geen per-as-analyse, geen vergelijking "waar scoort X hoger dan Y op welke as", geen reflectie op of het instrument zelf het juiste beeld gaf. De eerlijke opmerking "we waren aan het goedpraten" is goud, maar zou verdiept kunnen worden tot een methodische reflectie over DVF zelf (dat scoring-instrumenten confirmation bias kunnen versterken als invullers al een voorkeur hebben).

**Blue Ocean Strategy / ERRC**
- *Genoemd?* Ja, Kim & Mauborgne expliciet vermeld (index.astro r.33, r.55).
- *Value curve getekend?* Ja, foto aanwezig.
- *Value curve toegelicht?* Nee. Geen asuitleg, geen competitor-benoeming, geen interpretatie.
- *ERRC toegepast?* Nee, nergens genoemd. Dit is de grootste theoretische omissie. ERRC is het werkpaard van Blue Ocean; zonder ERRC heb je Blue Ocean als naam ingevoegd, niet als methode.

**Concept Collections**
- *Begrip goed uitgelegd?* Ja, uitlegblok op `/design/concept-collection/` r.72-76 klopt conceptueel.
- *Volgens de methode uitgevoerd?* Gedeeltelijk. De bronverzameling (35+ beelden) bestaat als PPTX, maar de pagina toont die beelden niet inline. Kwantiteit is kwaliteit: een pagina met 7 kruisbestuivingen en 2 lijstjes laat de verzamelwoede niet zien.
- *Convergentiefase zichtbaar?* Nauwelijks. Lesstof: "Neem de tijd om samen verbanden te leggen" en "leg de ontwikkeling vast in prototypes". De site springt direct naar divergentie-lijstjes en daarna naar download. Welke verbanden legden jullie? Dat ontbreekt.

## Verantwoording keuze Security (kritisch)

De inhoudelijke keuze is prima (pivot achteraf bewijst dat Security een rijker spoor was). De verantwoording op de site is nu:

1. "1 punt verschil zegt weinig" (OK, hand-waving)
2. "duidelijkere aanleiding" (OK, plausibel maar niet uitgediept)
3. "meer concrete beelden" (OK, subjectief maar eerlijk)
4. "bij Circulair waren we aan het goedpraten" (sterk, dit is het echte argument)

Dit werkt voor een 7-8. Voor een 10 moet de keuze methodisch worden:

**Wat ontbreekt:**
- DVF-subscores per richting per as → laat zien dat Security op Feasibility en Viability gelijk of hoger scoorde, en dat Circulair's D-voorsprong gebaseerd was op "theoretische wenselijkheid bij een denkbeeldige klant" versus Security's D gebaseerd op "bestaande klant (notaris, bank) met zichtbare pijn".
- Afweging per criterium uit opdracht 1b — opdracht noemt "criteria om ideeen/denkrichtingen door te laten": welke criteria zijn eigenlijk toegepast in de gate? Staan nergens.
- Reflectie op het instrument DVF zelf: stel dat jullie niet DVF maar bijvoorbeeld een confidence-weighted-score hadden gebruikt, had Circulair dan nog gewonnen? Dit toont dat je het framework kritisch hebt doordacht (rubric 8-10: "kritisch beoordeeld op waarde").
- Teamcompetenties meegewogen? McKinsey-scores uit CLAUDE.md laten zien dat het team sterker is in Generating/Pioneering/Networking dan in Tabulating. Circulair-innovatie vraagt veel tabulating (regelgeving, LCA, certificering); Security is meer pioneering-terrein. Dat is een legitiem teamargument dat nu ontbreekt en dat kritisch-zelfbewust zou staan.

**Suggestie voor herformulering op de pagina** (kort):

> "We kozen Security ondanks het punt verschil. Onze uitgesplitste DVF-scores lieten zien dat Circulair's voorsprong volledig in Desirability zat, terwijl we juist daar aan het goedpraten waren: we bedachten een klant in plaats van er een te hebben. Bij Security was de klant concreet (notaris, bank, overheidsorganisaties met handtekeningfraude). Op Feasibility en Viability scoorden de richtingen gelijk. We concludeerden dat het instrument DVF ons op het verkeerde been kon zetten als we niet kritisch naar onze eigen invulling keken."

Dit is geen AI-toon, dit is kritische methodische reflectie. Exact wat de rubric 8-10 vraagt.

## Concrete verbeteringen

### Blokkerend voor 8+

1. **Voeg DVF-subscores toe op `/design/gate/`**. Maak een kleine tabel: Circulair D/V/F en Security D/V/F met totalen. Visueel: staafdiagram of gewoon een nette HTML-tabel. Zonder dit is DVF niet kritisch toegepast.
2. **Pas ERRC toe en toon op `/design/gate/`**. Vier blokjes: Eliminate / Reduce / Raise / Create, per blok 2-3 concrete punten voor Aurora's Security-richting ten opzichte van de bestaande handtekeningverificatie-wereld. Zonder ERRC is Blue Ocean enkel een foto.
3. **Value curve toelichten**. Onder de curve-foto: welke factoren op de x-as, welke lijnen zijn wat, wie is de concurrentie (bijvoorbeeld: traditioneel pen, PKIsigning, fysieke DigiD, notariele controle). Liefst als SVG zodat het scherp leesbaar wordt.
4. **Herformuleer Security-keuze methodisch** (zie zin hierboven bij "Verantwoording"). Behoud de eerlijkheid, voeg methodische laag toe.
5. **Concept collection moet visueel worden op de pagina**. Minimaal 12-20 beelden uit de PPTX inline, grid met captions. De PPTX-download mag blijven als extra, maar de pagina moet de verzamelwoede zelf tonen.
6. **Maak bewijs compleet**: toon alle 4 DVF-formulieren (gate-dvf-3.jpg en -4.jpg missen), of leg uit waarom 2 voldoende is.
7. **Benoem aantal ideeen en verantwoord**. "We kwamen tot 32 ideeen in plaats van de gevraagde 90. Reden: we hebben bewust diepte boven breedte gekozen door per kamer tot sterke denkrichtingen te convergeren." Of compenseer alsnog. Niet verzwijgen.

### Nice-to-have voor 10

8. **Reflectie op DVF als instrument**. Eén alinea: "DVF zet scores op iets wat moeilijk te meten is. Wij merkten dat..." Laat zien dat je het gereedschap zelf bevraagt. Dit is rubric-10-niveau.
9. **Concept collection convergentie-reflectie**. Welke verbanden ontdekten jullie tijdens het verzamelen? Welk beeld bracht jullie dichter bij de pivot-kiem? "De octopus-associatie (meerdere verificatiemethoden tegelijk) was achteraf het zaadje voor de gedachte dat authenticatie niet aan de pen hoefde te hangen." Dat soort expliciete doorverwijzingen maakt de rode draad sterk.
10. **Teamcompetentie-argument toevoegen**. Kort blokje: "Ook keken we naar onze team-sterktes. McKinsey-scan toonde Pioneering en Generating als sterk; Security past daar beter bij dan Circulair (dat veel Tabulating vraagt: certificering, LCA, regelgeving)." Dit is zeldzame zelfreflectie en wordt in de rubric beloond.
11. **Externe gate-moment benoemen voor later**. "Voor Gate 3 willen we een reviewer van buiten school" — laat zien dat je de kwaliteit van externaliteit zelf monitort.
12. **Pivot-kiem expliciet markeren**. Klein blok onder concept collection: "Wat we toen niet wisten: dit losmaken van de pen werd in Refine onze pivot. Zie `/refine/pivot/`." Maakt de reis traceerbaar.
13. **Kern-vragen concept collection beantwoorden** (uit `concept-collections.md`): "Hoe is dit al eens geprobeerd?" (DigiD, PKIsigning, notariele ID-check) en "Wie is expert?" (BKR, Logius, security-researchers). Laat zien dat je de concept collection methodisch hebt gevoerd, niet alleen associatief.
14. **AI-toon micro-fix**: "Hoe wilder, hoe beter" vervangen door iets normalers zoals "We zochten expres ver weg van de pen". En "Niet op basis van de score, maar op gevoel en haalbaarheid" vervangen door "Security scoorde een punt lager maar voelde concreter" (geen "niet X maar Y").

## Cijferinschatting (nu / na fix)

| Dimensie | Nu | Na blokkerende fixes (1-7) | Na ook nice-to-haves (8-14) |
|---|---|---|---|
| Theorie-toepassing (DVF/Blue Ocean/CC) | 6,5 | 8,5 | 9,5 |
| Verantwoording Security-keuze | 7 | 8,5 | 9,5 |
| Bewijsstukken compleetheid | 7,5 | 8,5 | 9 |
| Concept collection als divergentie | 6 | 8 | 9,5 |
| Rode draad naar pivot | 6,5 | 8 | 9,5 |
| AI-toon | 8 | 8,5 | 9 |
| **Overall Design-fase** | **7** | **8,5** | **9,5** |

Een glatte 10 voor Design alleen is lastig zonder substantieel meer ideeen (90-eis) en een externe gate. Realistisch eindpunt voor deze fase is 9-9,5, en dat is genoeg voor een 10 op het portfolio als andere fases meedoen.
