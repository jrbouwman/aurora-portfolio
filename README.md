# Aurora Portfolio - Beyond Paper

Portfolio-website voor het minorvak **Innovatiemanagement (EDIM.21)** over de casus Aurora Writing Instruments Group.

## Hoe werkt de site?

De site wordt automatisch gebouwd vanuit **Markdown-bestanden**. Als je een `.md` bestand bewerkt en opslaat (commit), wordt de website binnen 2 minuten automatisch bijgewerkt.

```
Jij bewerkt .md bestand  -->  GitHub Actions bouwt de site  -->  Site is live op GitHub Pages
```

## Welke bestanden mag ik bewerken?

**Alleen bestanden in `src/content/`** - dat is waar onze portfolio-inhoud staat.

```
src/content/
  discover/          <-- Fase 1: Discover
    trends.md        <-- Trendanalyse
    scenario.md      <-- Scenariobouwing
    empathise.md     <-- Immersive Research
    challenges.md    <-- HZWK Challenges
  define/            <-- Fase 2: Define (later)
  design/            <-- Fase 3: Design (later)
  refine/            <-- Fase 4: Refine (later)
  deliver/           <-- Fase 5: Deliver (later)
```

De `docs/` map bevat het cursusmateriaal als referentie - **niet bewerken**.

## Hoe bewerk ik content?

### Via GitHub.com (makkelijkst)

1. Ga naar de repository op GitHub.com
2. Navigeer naar het `.md` bestand dat je wilt bewerken (bijv. `src/content/discover/trends.md`)
3. Klik op het **potlood-icoon** (Edit this file)
4. Pas de tekst aan
5. Klik **"Commit changes"** (groene knop)
6. Binnen ~2 minuten is de site bijgewerkt

### Afbeeldingen toevoegen

1. Ga naar de map `public/images/` op GitHub
2. Klik **"Add file" > "Upload files"**
3. Sleep je afbeelding(en) erin
4. Commit
5. Verwijs in je markdown naar de afbeelding:
   ```markdown
   ![Beschrijving van de foto](/images/mijn-foto.jpg)
   ```

## Markdown Cheatsheet

```markdown
# Grote kop
## Middelgrote kop
### Kleine kop

**Vetgedrukt**
*Cursief*

- Lijstitem 1
- Lijstitem 2

1. Genummerd item
2. Genummerd item

> Dit is een citaat/quote

| Kolom 1 | Kolom 2 |
|---------|---------|
| Data    | Data    |

[Link tekst](https://voorbeeld.nl)
![Alt tekst voor afbeelding](/images/foto.jpg)
```

## Frontmatter

Elk `.md` bestand begint met een blokje YAML tussen `---` streepjes. Dit zijn de metadata van de pagina:

```yaml
---
title: "Titel van je bewijsstuk"
description: "Korte beschrijving (1-2 zinnen)"
order: 1
icon: "📊"
---

# Hier begint je inhoud
```

| Veld | Wat doet het |
|------|-------------|
| `title` | De titel die bovenaan de pagina verschijnt |
| `description` | Korte beschrijving, te zien op de overzichtspagina |
| `order` | Volgorde waarin bewijsstukken worden getoond (1, 2, 3...) |
| `icon` | Emoji-icoon voor visueel onderscheid |

## Template voor een nieuw bewijsstuk

Kopieer dit als basis voor een nieuw `.md` bestand:

```markdown
---
title: "Naam van het bewijsstuk"
description: "Korte beschrijving van wat dit bewijsstuk laat zien"
order: 1
icon: "📄"
---

# Naam van het bewijsstuk

## Wat hebben we gedaan?

Beschrijf hier de activiteit...

## Resultaten

Beschrijf hier de uitkomsten...

## Reflectie

Wat hebben we geleerd?
```

## Lokaal ontwikkelen (optioneel)

Als je de site lokaal wilt draaien (niet nodig voor content-bewerking):

```bash
npm install        # Eenmalig: installeer dependencies
npm run dev        # Start lokale server op localhost:4321
npm run build      # Bouw de productieversie
```
