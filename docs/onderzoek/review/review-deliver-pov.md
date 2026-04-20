# Review Deliver + Proof of Value

**Scope:** `/deliver/`, `/deliver/proof-of-value/`, `/deliver/roadmap/`
**Gewicht:** 1b PoV = 30% van eindcijfer (zwaarste onderdeel naast 1a proces)
**Reviewdatum:** 19 april 2026
**Reviewer-perspectieven:** Docent Henk (rubric), MT/directie (blind), critical friend (theorie), skeptische investeerder (business)

---

## Samenvatting

De Deliver-fase leest coherent en vriendelijk, maar schiet op drie plekken te kort voor een 10: (1) de PoV is **niet zelfstandig leesbaar op MT-niveau** omdat driver/aanleiding, prototype-uitkomsten en ontwikkelfasen-status ("waar staan we nu, wat moet er nog") ontbreken of alleen elders beschikbaar zijn, (2) het **financieel model is kwalitatief, geen cijfer erin** (geen prijsaannames, geen TAM/SAM, geen kosten), en (3) de **waardeproposities zijn generiek** (geen meetbare cijfers: hoeveel uur bespaart, hoeveel euro fraudepreventie, hoeveel aktes per dag). Rogers 5 factoren en ambidexteriteit zijn netjes toegepast, maar DVF scoort gemiddeld en waarde-uitwerking per sector blijft oppervlakkig. AI-toon is overwegend goed beheerst, met enkele incidenten (o.a. "juridisch waterdichte audittrail", "naadloze beleving" in lesmateriaal terecht, perfect parallelle drievouden in stakeholder-kaarten, taglines zoals "Aurora weet als geen ander wat ondertekenen betekent"). Grootste blinde vlek voor investeerder: geen concurrentie-analyse van DocuSign/PKIsigning/itsme/iDIN/Yivi met feitelijke vergelijking, geen cijfers op marktomvang, geen claim op "deze innovatie is nieuw" onderbouwd. De roadmap is logisch maar mist randvoorwaarden, budgetaannames en feedbackmomenten. Cijferinschatting: **huidige staat 6,5/10**, na blokkerende fixes **8/10**, met uitmuntendheidstoevoegingen **9,5–10/10**. Concrete verbetervoorstellen staan onderaan, prioriteit 1 eerst.

---

## Checklist 1d-eisen

| # | Eis | Status | Toelichting |
|---|---|---|---|
| 1 | Zelfstandig leesbaar op MT/directieniveau | PARTIAL | `proof-of-value.astro` opent direct met "De natte handtekening is achterhaald" zonder context over Aurora, de pivot of de voorgaande reis. MT-lezer weet niet waar dit vandaan komt. |
| 2 | Challenge helder beschreven | JA | Challenge-blok regel 43-48 is scherp. |
| 3 | Driver/aanleiding terug te vinden | NEE | Aurora's strategische context (pennenmaker, digitaliseringsdruk, pivot van pen naar proces) staat NIET op PoV-pagina. Alleen indirect: "125+ jaar expertise". |
| 4 | Prototypes + uitkomsten in PoV samengevat | NEE | Geen enkele verwijzing naar PELV 1, PELV 2, testresultaten, of wat prototypes hebben geleerd. De Forms-vragenlijst en conclusies ontbreken volledig. |
| 5 | Waardepropositie per stakeholder meetbaar + kwalitatief | PARTIAL | Notaris/bank/verzekeraar genoemd, maar uitsluitend kwalitatief (geen uren, euro's, percentages). |
| 6 | Roadmap met fasen, mijlpalen, randvoorwaarden | PARTIAL | Fasen + tijdlijn + tags aanwezig. Randvoorwaarden (budget, techpartner-profiel, certificeringsinstantie) ontbreken. Feedbackmomenten tussen fasen niet benoemd. |
| 7 | Financieel model / kosten-baten onderbouwing | NEE | Drie inkomstenstromen genoemd, maar **nul cijfers**. Geen prijsaannames, geen marktomvang, geen breakeven. |
| 8 | Ontwikkelfasen "waar zijn we nu, wat moet nog" | NEE | Niet expliciet. Impliciet leesbaar uit roadmap (fase 1-4), maar het ankerpunt "hier staan we NU" ontbreekt. |
| 9 | Validatie-methode verantwoord | PARTIAL | Gate 2 met DVF wordt genoemd op index, maar de validatie van het concept (PELV-iteraties) komt niet terug op PoV. |
| 10 | Conclusie / call-to-action | NEE | PoV-pagina eindigt met financieel model en dan navigatie. Geen concluderende "daarom GO, dit is wat we vragen"-blok. |
| 11 | Rogers 5 adoptiefactoren toegepast | JA | Netjes toegepast op roadmap-pagina met score per factor. |
| 12 | Ambidexteriteit-argument voor aparte BV onderbouwd | JA | O'Reilly & Tushman 2013 correct aangehaald, exploit/explore-uitleg klopt. |
| 13 | Diffusie-strategie per sector | PARTIAL | Notarissen → banken → verzekeraars/accountants. Rogers-categorieën zijn echter verkeerd toegepast (zie critical-friend-sectie). |

**Score tegen 1d-eisen: 7/13 volledig, 5/13 partial, 1/13 volledig ontbrekend = ongeveer 60% compleet.**

---

## Sterke punten

1. **Ambidexteriteit-toepassing** (`roadmap.astro` regel 40-50): helder, correct, goed gekoppeld aan eigen casus. "Een pennenmaker die digitale verificatiesoftware gaat bouwen" is een sterk beeld.
2. **Eerlijk-verhaal-blok** (`proof-of-value.astro` regel 216-226): credibiliteit boost dat DocuSign/PKIsigning worden erkend in plaats van weggeschreven.
3. **Procesflow-visual** (SVG) is geïntegreerd en geeft MT-lezer houvast.
4. **Gate 2 DVF-scores-grid** (index regel 46-63): compacte dashboardvorm, direct leesbaar.
5. **Rogers 5 factoren met score** (roadmap regel 262-313): methodisch toegepast met duidelijke hoog/midden/laag-labeling.
6. **Risico's en mitigatie-blok** (roadmap regel 318-355): 4 risico's met tegenmaatregelen, incl. gate-feedback-quote ("Hoelang is dit veilig?").
7. **Spin-off-argument** (roadmap regel 46-50) citeert gate-feedback letterlijk — sterk bewijs dat de keuze gedragen wordt.
8. **Hybride positionering** als USP tegen volledig-digitale concurrenten is defensief onderbouwd.

---

## Kritische zwaktes

### Docent Henk (rubric)

**Rubric 1b Goed (8) = "methodisch ontwikkeld en cyclisch getest op meerwaarde, zeer gedetailleerd, aantoonbaar praktisch toepasbaar".** Hier gaat het mis:

- **Cyclisch getest op meerwaarde ontbreekt op PoV-pagina.** De twee PELV-iteraties hebben plaatsgevonden, maar op PoV staat geen woord over wat ze opleverden, wat is aangepast, of welke aannames zijn gefalsifieerd. Docent kan niet vinken dat er **cyclisch** getest is zonder elders te klikken.
- **"Zeer gedetailleerd" mist**: fysieke vorm wordt op abstract-conceptueel niveau beschreven ("compact apparaat", "NFC-reader", "LED-indicatoren"). Geen afmetingen, geen doorlooptijd per verificatie, geen error-rate, geen batterijduur, geen typen ID's die werken (Nederlands paspoort, rijbewijs, verblijfsvergunning?).
- **"Aantoonbaar praktisch toepasbaar":** er is géén gesimuleerde klantreis met cijfers. De procesflow-SVG is er, maar ontbreekt "zo gaat het voelen op dinsdagochtend bij notaris X".
- **Waardecreatie-vragen les 8 (Waar in de keten? Voor wie? Wat voor waarde? Hoe groot vs. kosten?) worden niet systematisch beantwoord.** Vraag 4 (hoe groot is de waarde t.o.v. de kosten?) wordt NIET beantwoord — en dat is precies wat MT wil weten.
- **Suggested outline afgevinkt:** Introduction (impliciet via hero) - Current Scenario (ontbreekt, direct naar challenge zonder huidige-situatie-analyse) - Solution Overview (ja) - Detailed Value Proposition met pains/gains (VPC staat op pivot-pagina, niet hier) - Roadmap (ja, aparte pagina) - Conclusion (ontbreekt). **3/6 outline-punten gedekt.**

### MT/directie (zelfstandig leesbaar — BLINDE TEST)

**Ik ben directielid. Ik krijg een link naar /deliver/proof-of-value/. Ik klik nergens anders. Wat snap ik?**

- **Wat is Aurora?** Onbekend. "Aurora levert het kennismodel: 125+ jaar expertise over ondertekenen" — dus Aurora is een bedrijf. Wat doet het? Pennen? Schrijfwaren? Digitaal? Onduidelijk. MT-lezer die de casus niet kent, weet niet waarom Aurora relevant is hier.
- **Waar komt deze innovatie vandaan?** Geen verwijzing naar onderzoek, trends, of voorgaande iteraties. Lijkt uit de lucht te vallen.
- **Welk probleem los ik op voor MIJN organisatie?** Als ik directeur van een notariskantoor ben: oké, ID-verificatie + PIN. Wat kost het me? Hoeveel minuten per akte? Wat levert het op in euro's of uren? Geen antwoord.
- **Waarom zou ik Aurora kiezen en niet DocuSign?** Eerlijk-verhaal-blok geeft antwoord ("hybride"), maar dat is nog steeds zachte claim — geen vergelijkingstabel, geen feature-matrix, geen prijsvergelijking.
- **Wat is de STATUS?** Werkt het al? Is er een prototype? Pilot gestart? Staat in de roadmap dat het nog gebouwd moet worden, maar op PoV-pagina lijkt het alsof het product bestaat.
- **Wie investeert?** Ambidexteriteit-argument staat op roadmap, niet PoV. Ik snap niet dat Aurora dit niet zelf bouwt.
- **Call to action?** Niet aanwezig. Na "Training & consultancy" scroll ik door naar navigatie. Geen "neem contact op", "volgende gate", "pilot-aanvraag".

**Conclusie MT-test: zakt. Zou géén go-besluit kunnen nemen op basis van alleen deze pagina.**

### Critical friend (theorie-check)

**Rogers-toepassing bevat een fout:**

- In `roadmap.astro` regel 187-204 worden notarissen "early adopters", banken "early majority" en verzekeraars "late majority" genoemd. Dit is een **verkeerde toepassing van Rogers' adopter-categorieën**. Die categorieën gelden per **individuele adopter binnen een sociaal systeem**, niet per sector. Een bank kan in Rogers-termen best een early adopter zijn en een notariskantoor een laggard. De juiste framing is: "notarissen zijn onze **eerste doelgroep** omdat ze de beste mix van urgentie en bereikbaarheid hebben", niet "notarissen ZIJN early adopters".
- **5 adoptiefactoren toepassing klopt** (regel 262-313), maar is te mild voor zichzelf. "Compatibiliteit: gemiddeld" — is het niet **laag**? Conservatieve notariaatwetgeving, certificering, fysiek apparaat erbij? "Probeerbaarheid: gemiddeld" — voor een notariskantoor is een pilot-investering van enkele tienduizenden euro's geen kleine drempel. Hier wordt naar het eigen concept toegekeurd.

**Ambidexteriteit correct toegepast**, maar mist nuance: O'Reilly & Tushman onderscheiden **structurele** vs **contextuele** ambidexteriteit. Hier wordt gekozen voor structureel (aparte BV), maar er wordt niet benoemd dat dit de meest extreme variant is en andere opties (interne incubator, joint venture) niet zijn afgewogen.

**DVF-scores zijn inconsistent:**
- Op index staat Gate 2 gemiddelden: 4.5 / 3.8 / 3.4 / 1.8 (dit zijn 4 DVF-dimensies van het gate-formulier?).
- Op PoV staat DVF 4.5 / 2.5 / 3.8 (Desirability/Feasibility/Viability). Maar 2.5 en 3.8 komen niet uit de gate-scores. Waar komen die vandaan? Eigen inschatting? Niet toegelicht.

**Blue Ocean / Porter ontbreekt volledig in Deliver**, terwijl de concurrentiepositie cruciaal is. Op design-pagina's stond een value curve — die wordt in Deliver niet hergebruikt om te claimen dat de positionering nog steeds blue ocean is na pivot.

**Waardecreatie-vragen les 8 systematisch doorlopen:**
- "Waar in de keten?" — niet expliciet beantwoord (het moment van ondertekenen? de archivering?)
- "Voor wie?" — stakeholder-kaarten, oké
- "Wat voor waarde?" — alleen rechtsgeldigheid/fraudepreventie/efficiency. Waar blijft de **merkwaarde voor Aurora** zelf? Medewerkerswaarde? Maatschappelijke waarde (minder fraude)?
- "Hoe groot vs kosten?" — NIET beantwoord.

### Skeptische investeerder (businessmodel)

**Zou ik hierin investeren? Stevige NEE met huidige stand. Gaten:**

1. **Geen cijfers nergens.** "Per organisatie, per jaar" — hoeveel euro? Licentie €500/jaar? €50.000/jaar? Factor 100 verschil. "Hardware-omzet" — €800 per station of €8.000? "Marktomvang" — ca. 800 notariskantoren in NL wordt genoemd, maar hoeveel van die 800 is realistisch binnen 5 jaar? Wat is de ARR-doelstelling?
2. **Geen concurrentie-matrix.** DocuSign wordt genoemd, PKIsigning éénmaal. Ontbreekt: **itsme, iDIN, Yivi (DigiD-alternatief), AdobeSign, Signicat, Notarisnet (Frans), Onfido, Veriff, Jumio.** Een investeerder vraagt: waarom kan Signicat dit niet morgen bouwen? Wat is het vertragingselement voor nieuwe toetreders (moat)?
3. **Aurora's claim op authenticiteitskennis** is zacht. "125+ jaar expertise over ondertekenen" — concreet: welke unieke kennis? Onderzoeksrapporten? Patenten? Gepubliceerde methodes? Een investeerder ziet dit als narrative, niet als asset.
4. **Techpartner = grootste single point of failure.** Wie? Profiel? Wat als partner bailout? Vendor lock-in? Geen contingency.
5. **Compliance/certificering kosten** worden genoemd ("certificering starten" in fase 2) maar niet begroot. EIDAS-certificering voor qualified electronic signatures = tientallen duizenden euro's + 6-18 maanden.
6. **Eenheidsprijs van een verificatie** — mist. €0,10 per verificatie? €1? €10? Bepaalt of banken überhaupt instappen.
7. **Exit-scenario / waardering** — voor een startup onbesproken. Strategische koper?
8. **"125+ jaar vertrouwen" als merkwaarde voor digitale verificatie** is een zwak argument. Een notaris die kiest tussen Aurora-spin-off en Signicat kiest op security-certificering en referenties, niet op "leuk merk".
9. **Adoptietijd "lange adoptietijd door compliance-eisen"** wordt genoemd als viability-risico — maar wat betekent dat voor runway? Hoe lang kan de startup zonder inkomsten door?

---

## AI-toon incidenten

Jr's schrijfstijl is dit keer overwegend beheerst, maar er zijn duidelijke glijders richting pitch-deck:

| # | Locatie | Citaat | Probleem |
|---|---|---|---|
| 1 | `proof-of-value.astro` regel 140 | "Juridisch waterdichte audittrail" | Corporate jargon / pitchdeck-woord. Alternatief: "elke ondertekening traceerbaar: wie, wanneer, welk document". |
| 2 | `proof-of-value.astro` regel 38-40 | "Ze bewijst niet wie er getekend heeft, is makkelijk na te maken en past niet meer in een digitale wereld." | Perfect parallelle drievoud (3 claims, zelfde structuur). Docent-AI-flag. |
| 3 | `proof-of-value.astro` regel 62-64 | "identificeren (ID-bewijs scannen), authenticeren (persoonlijke PIN invoeren) en koppelen (identiteit vastleggen bij het document)" | Drievoudige parallel weer. Te netjes. Rommeliger maken: "Drie stappen: eerst scannen we je ID-bewijs, dan vul je een PIN in, en die combinatie koppelen we aan het document". |
| 4 | `proof-of-value.astro` regel 106-108 | "Aurora levert het kennismodel: 125+ jaar expertise over ondertekenen, wat het betekent, wanneer het telt en hoe mensen het ervaren." | Drievoud ("wat/wanneer/hoe") + corporate "kennismodel". Pitchdeck-toon. |
| 5 | `proof-of-value.astro` regel 222 | "Aurora weet als geen ander wat ondertekenen betekent. Die kennis is waardevoller dan de pen." | **Tagline-alert.** Exacte oneliner-structuur. Docent zal dit rood omcirkelen. |
| 6 | `proof-of-value.astro` regel 218-221 | "volledig digitaal. Ons concept vult een andere plek in: de situaties waar papier en fysieke aanwezigheid nog steeds de norm zijn" | "Vult een andere plek in" = gladde positionering-taal. |
| 7 | `proof-of-value.astro` regel 77-79 | "Vergelijkbaar met een pinautomaat, maar dan voor ondertekening." | Deze is juist goed: concreet beeld, geen jargon. Behouden. |
| 8 | `proof-of-value.astro` regel 131-145 | Notaris/Bank/Verzekeraar bullets | Alle drie stakeholders 3 bullets, identieke structuur. Extreme parallellie. Varieer: één krijgt 4, één krijgt 2 met langere uitleg. |
| 9 | `roadmap.astro` regel 35-39 | "een compleet andere manier van werken, andere mensen, andere processen" | Drievoud + retorische opbouw. Pitchdeck. |
| 10 | `roadmap.astro` regel 62 | "Nieuwe markt, nieuwe technologie, nieuwe klanten." | **Extreme parallellie** (drievoud "nieuwe X"). Docent-vlag. |
| 11 | `roadmap.astro` regel 176-178 | "De fax werd uitgevonden in 1843 maar brak pas door in 1964. ABS bestond al in 1959 maar werd pas standaard in 1978." | Te netjes parallel. Eén voorbeeld met bron en jaartal is sterker dan twee parallelle. |
| 12 | `roadmap.astro` regel 151 | "uitrollen naar meer notariskantoren, dan banken" | "Uitrollen" = corporate. Alternatief: "meer kantoren toevoegen". |
| 13 | `index.astro` regel 91 | "Klein volume, hoge urgentie, makkelijk bereikbaar." | Drievoudig ritme, staccato pitch-deck stijl. |
| 14 | `index.astro` regel 30-32 | "digitale verificatie van ondertekening via ID-scan en PIN. De pen was overbodig gebleken, het probleem zat in de handtekening zelf." | "De pen was overbodig gebleken" = storytelling, sterk. Behouden. |
| 15 | `roadmap.astro` regel 336 | "duidelijke afspraken, milestone-based betaling" | "Milestone-based" = corporate. |
| 16 | `proof-of-value.astro` regel 105 | "Aurora brengt het merk en het vertrouwen." | Taglineachtig. Een docent die dit in een studentenportfolio leest, hoort AI. |

**Geen em-dashes gevonden — goed gedaan.**

**Samenvatting AI-toon:** 16 vlaggen, waarvan ~5 kritisch (taglines/oneliners/extreme parallellie) en ~11 mild (corporate jargon, drievoudsopbouw). Gemiddeld acceptabel, maar met name `proof-of-value.astro` hero/challenge/eerlijk-verhaal en `roadmap.astro` waarom-startup moeten rommeliger.

---

## Theorie-check

### DVF (Desirability / Feasibility / Viability)

- **Goed:** Expliciete DVF-sectie op PoV (regel 184-213) met score per dimensie en toelichting.
- **Zwak:** Scores 4.5 / 2.5 / 3.8 zijn niet herleidbaar. Op index staat dat Gate 2 medestudenten 4.5 / 3.8 / 3.4 / 1.8 gaven (4 dimensies?). Die mismatch + afwezigheid van "hoe zijn deze getallen berekend" ondergraaft de geloofwaardigheid.
- **Advies:** Expliciteer: "Gate 2 scores van medestudenten vertaald naar DVF: Desirability = gemiddelde customer value (4.5), Feasibility = eigen inschatting gebaseerd op kerncompetenties-score (1.8 gate-score → 2.5 na techpartner-correctie), Viability = financiële kansen (3.8)".

### Rogers (5 adoptiefactoren + diffusie)

- **Goed:** Alle 5 factoren doorlopen met score (relatief voordeel, compatibiliteit, complexiteit, probeerbaarheid, observeerbaarheid).
- **Fout:** Adopter-categorieën (early adopter / early majority / late majority) toegewezen per **sector**, terwijl Rogers die per **individu in een sociaal systeem** definieert.
- **Zwak:** Zelfbeoordeling te mild (vooral compatibiliteit scoort te hoog).
- **Diffusievoorbeelden fax/ABS** zijn correct aangehaald uit les 8.

### Ambidexteriteit (O'Reilly & Tushman 2013)

- **Goed:** Correcte explore/exploit-dichotomie, link naar casus scherp.
- **Zwak:** Structurele ambidexteriteit (spin-off) gekozen zonder contextuele/sequentiele alternatieven te noemen of af te wegen. Docent Henk zou vragen: waarom niet interne business unit? Waarom geen joint venture?

### Waardecreatie-vragen (les 8)

| Vraag | Beantwoord? |
|---|---|
| Waar in de keten? | Impliciet (bij de balie / op afstand). Niet expliciet. |
| Voor wie? | Ja, notaris/bank/verzekeraar. |
| Wat voor waarde? | Ja, kwalitatief. Mist merkwaarde voor Aurora zelf, medewerker-waarde, maatschappelijke waarde. |
| Hoe groot vs kosten? | **NEE.** Ernstigste gat. |

### Blue Ocean / Porter / concurrentie

- **Blue Ocean:** niet aangehaald in Deliver. Value curve uit Design komt niet terug. Gemiste kans om "we blijven blue ocean na pivot" te bewijzen.
- **Porter 5 krachten:** ontbreekt voor de nieuwe markt (digitale identiteitsverificatie). Rivaliteit met DocuSign/Signicat, toetredingsbarrières (certificering), onderhandelingsmacht notarissen, substituten (itsme/DigiD), leveranciersmacht (techpartner) — allemaal relevant en niet benoemd.

### Ontbrekende theorie die docent kan verwachten

- **Lean Startup / MVP-denken** (les 8: "Vroegtijdig marktvraag en product testen → lean startup"): fase 2 roadmap noemt MVP, maar link naar Lean Startup-framework (Build-Measure-Learn, pivot-or-persevere) ontbreekt.
- **Crowdfunding / supply chain finance** (les 8 alternatieven): geen woord over alternatieve financiering voor de startup.
- **Open innovatie** (les 8): Aurora + techpartner IS open innovatie, maar wordt niet als zodanig benoemd.

---

## Financieel model & waardepropositie (scherp!)

### Financieel model: ONVOLDOENDE VOOR MT-NIVEAU

Huidig: 3 boxjes met tekst "Per organisatie, per jaar. Inclusief updates en certificering." **Nul cijfers.**

**Minimaal nodig voor voldoende (8-niveau):**
1. **Prijsaannames met bandbreedte**: licentie €X.000-€X.000/jaar, hardware €X.000 per station, training €X.000 per implementatie.
2. **Marktomvang**: 800 notariskantoren × gem. 5 balies × licentie/balie = € potentieel bij 100% penetratie.
3. **Kostprijs per verificatie** (de unit economics): hardware afschrijving + software cost + support = € per verificatie.
4. **Breakeven-aanname**: bij X klanten X werkplekken = break-even na Y maanden.
5. **Investeringsbehoefte**: hoeveel kapitaal moet Aurora inbrengen? €X00.000 – €X.000.000?
6. **Kostenoverzicht startup eerste 3 jaar**: salarissen, techpartner-fee, certificering, marketing, overhead.

**Al zijn de cijfers aannames met expliciete unzekerheidsband, dan nog laat het zien dat er ORDE VAN GROOTTE over is nagedacht.**

### Waardepropositie: ONVOLDOENDE CONCREET

Huidig per stakeholder 3 bullets, alle kwalitatief. **Herschrijf met cijfers:**

- **Notaris:** "Gemiddeld 20 min/akte aan ID-verificatie en dossieropbouw. Met ons: <5 min. Bij 1000 aktes/jaar = 250 uur terug = ~€25.000/jaar aan junior-tijd (€100/u tarief). Licentie €X = X-voudige ROI."
- **Bank:** "Fraudeschade Nederlandse banken ~€40M/jaar (bron), waarvan X% via handtekeningvervalsing op contracten. Onze verificatie sluit die route af. 1 grote fraudezaak voorkomen = licentie voor 10 jaar terugverdiend."
- **Verzekeraar:** ...

**Dit zijn aannames, maar orders of magnitude tellen. Nu staat er: "Minder tijd aan administratie per akte". Dat is geen waardepropositie, dat is een wens.**

---

## Zelfstandige leesbaarheid (MT-test)

**Wat begrijpt een MT'er die ALLEEN deze 3 pagina's leest, in volgorde (index → PoV → roadmap)?**

| Aspect | Wel begrepen | Niet begrepen |
|---|---|---|
| Wat is het concept? | Ja | - |
| Welk probleem lost het op? | Ja, generiek | Nee, specifiek per sector |
| Waar komt het vandaan (driver)? | - | Nee, Aurora's situatie onbekend |
| Wat zijn bewijsstukken? | Gate 2 GO's | Prototypes/iteraties onzichtbaar |
| Hoe ziet het eruit fysiek? | Grof beeld | Geen afmetingen/UX |
| Wat kost het? | - | Nee |
| Wat levert het op? | Generiek kwalitatief | Nee, cijfers |
| Wie is de concurrent? | DocuSign genoemd | Verder niets |
| Hoe gaat implementatie? | 4 fasen, tags | Randvoorwaarden, budget |
| Waar staan we NU? | - | Niet expliciet |
| Wat wordt gevraagd? | - | Geen CTA |

**MT-test uitslag: 5/11 = onvoldoende voor zelfstandige leesbaarheid op directieniveau.**

---

## Concrete verbeteringen

### Blokkerend voor 8+

1. **Voeg "Context" sectie toe bovenaan PoV (vóór challenge):** Wat is Aurora, waarom dit concept, waar in de innovatiereis staan we. Max 120 woorden. MT moet niet hoeven klikken.
2. **Voeg "Prototype-uitkomsten" sectie toe op PoV:** PELV 1 + PELV 2 in twee alinea's samenvatten, inclusief belangrijkste leerervaring en aanpassingen. Bewijst "cyclisch getest op meerwaarde" (rubric 8+).
3. **Voeg "Waar staan we nu" statusblok toe:** expliciet 1-regel-per-component: concept (validated), prototype (paper + rapid, getest), technologie (techpartner nog niet geselecteerd), klanten (0 pilots), financiering (0).
4. **Voeg cijfers toe aan financieel model:** minimaal prijsbandbreedte per inkomstenstroom + marktomvang-berekening notarissen + investeringsbehoefte startup. Mag expliciet "aanname" heten.
5. **Voeg cijfers toe aan waardepropositie per stakeholder:** uren bespaard, euro's fraude voorkomen, doorlooptijdreductie. Met bron of "aanname"-label.
6. **Voeg conclusie / CTA toe onderaan PoV:** 3-regel-samenvatting + concrete vraag ("Wij vragen een investeringsbesluit voor de oprichtingsfase: €X en 6 maanden runway om techpartner te selecteren en MVP te starten").
7. **Herzie Rogers-sectortoewijzing:** gebruik niet "early adopter/early majority/late majority" per sector, maar "eerste doelgroep / volgende segment / latere segment" en motiveer op urgentie + bereikbaarheid + investeringsruimte.
8. **Voeg beknopte concurrentie-matrix toe:** 1 tabel op PoV met minimaal 5 concurrenten (DocuSign, Signicat, itsme, iDIN, Jumio) en 3 vergelijkingscriteria (hybride ja/nee, ID-chip-based ja/nee, certificeringsniveau).

### Nice-to-have voor 10

9. **Link naar en embed Value Proposition Canvas** uit pivot-pagina. Werk VPC-pains/gains sectie-voor-sectie uit op PoV zelf (pains/gains per stakeholder).
10. **Financieel model met scenario's:** conservatief / realistisch / optimistisch. 3 kolommen, jaar 1/3/5 revenue.
11. **Randvoorwaarden per roadmap-fase:** techpartner-profiel (Fase 1), certificeringsinstantie (Fase 2), pilot-investering bedrag (Fase 3), licentiestructuur (Fase 4). Feedbackmoment per fase.
12. **Expliciete validatie-ladder:** "wij hebben gevalideerd dat X (wijze van validatie). Nog te valideren: Y (in fase Z)". Maakt wetenschappelijke rigueur zichtbaar.
13. **Voeg merkwaarde-voor-Aurora sectie toe:** wat wint Aurora zelf? Strategische positie, merkassociatie, toekomstige acquisitiekansen. Antwoord op waardecreatie-vraag "voor wie".
14. **Hergebruik Blue Ocean value curve** uit Design, maar dan voor de gepivoteerde dienst. Bewijst continuïteit theorie-toepassing.
15. **Porter 5 krachten-mini op de startupmarkt** in risico's-sectie uitwerken.
16. **AI-toon fixes:** alle 16 incidenten adresseren, vooral taglines 1, 5, 6 verwijderen of herschrijven.

### Uitmuntend-niveau (wat maakt het een 10?)

17. **Meervoudige validatie:** niet alleen Gate 2 studenten, maar ook simulatie-interview met een echte notaris of bank-contactpersoon (telefonisch, LinkedIn, docent-netwerk). Zelfs één outreach + citaat maakt het "echt".
18. **Commerciële onderbouwing:** letter of intent/ interesse-citaat van een potentiële pilotklant, of een Google-search-onderbouwd marktpotentieel met bron (CBS, KNB).
19. **Scherpe roadmap met gates**: iedere fase eindigt met een go/no-go gate, inclusief criterium (omzetcurve, klantaantal, technische milestone). Investeerderstaal.
20. **Originele value-positionering:** nu is de positionering "hybride papier-digitaal". Onderzoek of een sterkere frame beschikbaar is: "authenticatie-as-a-service in momenten van juridische zwaarte" of "de enige oplossing die fysieke aanwezigheid behoudt". Een zin die blijft hangen zonder tagline-toon.
21. **Ethische reflectie:** wat als onze technologie gebruikt wordt voor surveillance? Hoe waarborgen we privacy? AVG-analyse. Laat ethisch bewustzijn zien — telt bij deze docent.
22. **Expliciete reflectie op het leerproces:** in een apart blokje "Wat we onderweg hebben geleerd over waarde". Maakt eigenaarschap zichtbaar.

---

## Cijferinschatting

- **Nu: 6,5/10 voor 1b PoV (30%).**
  - Voldoet aan 6 (basisniveau), maar mist cyclische validatie-bewijs en zelfstandige leesbaarheid. Score dichterbij 7 dan 6, maar net niet 8 vanwege 7 partial/1 missing van 13 checks en zwakke financieel model.
- **Na prioriteit-1 fixes (verbeteringen 1-8): 8/10.**
  - Driver, prototype-uitkomsten, status-nu, cijfers, CTA, Rogers-herzieningen en concurrentiematrix tillen het naar rubric-niveau "Goed": methodisch ontwikkeld, cyclisch getest op meerwaarde, zeer gedetailleerd, aantoonbaar praktisch toepasbaar.
- **Na uitmuntend-niveau (verbeteringen 1-22): 9,5-10/10.**
  - Meervoudige validatie (externe stem), commerciële onderbouwing, scherpe roadmap met gates, originele positionering. Zou maken dat deze PoV door een echte MT gelezen kan worden zonder verdere aanvullingen.

**Advies voor Jr:** prioriteer verbeteringen 1-6 (driver, prototypes, status-nu, cijfers-financieel, cijfers-waarde, CTA). Die zijn binnen een dag of twee te doen en tillen het cijfer met ruim 1,5 punt. Daarna AI-toon-fixes (low effort, hoge return). Uitmuntend-niveau items zijn ambitieus maar een echte notaris bellen voor 1 citaat is binnen een week haalbaar en verhoogt het cijfer significant.
