#!/usr/bin/env python3
"""Pivot presentatie: hoogover + strategische/financiële toelichting. Max 3 slides, weinig tekst."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Huisstijl
DARK = RGBColor(0x2D, 0x29, 0x38)
BG = RGBColor(0x0F, 0x0E, 0x1A)
BG_SLIDE = RGBColor(0xF8, 0xF5, 0xEF)  # cream
REFINE = RGBColor(0xF5, 0x9E, 0x0B)
REFINE_LIGHT = RGBColor(0xFE, 0xF3, 0xE7)
TEXT = RGBColor(0x2D, 0x29, 0x38)
MUTED = RGBColor(0x6B, 0x61, 0x73)
CORAL = RGBColor(0xF4, 0x72, 0x64)
BG_RISK = RGBColor(0xFD, 0xEC, 0xEA)

HOOGOVER_PNG = "/tmp/hoogover-export.png"

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height


def add_bg(slide, color=BG_SLIDE):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    bg.line.fill.background()
    bg.fill.solid(); bg.fill.fore_color.rgb = color
    slide.shapes._spTree.remove(bg._element); slide.shapes._spTree.insert(2, bg._element)
    return bg


def add_text(slide, left, top, width, height, text, *, size=14, bold=False, color=TEXT, align=PP_ALIGN.LEFT, font="Calibri"):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(0); tf.margin_right = Emu(0); tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
    lines = text.split("\n") if isinstance(text, str) else text
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        run = p.add_run(); run.text = line
        run.font.size = Pt(size); run.font.bold = bold
        run.font.color.rgb = color; run.font.name = font
    return tb


def add_accent_bar(slide, left, top, width=Inches(0.6), height=Inches(0.08), color=REFINE):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    bar.line.fill.background()
    bar.fill.solid(); bar.fill.fore_color.rgb = color


def add_card(slide, left, top, width, height, title, bullets, *, accent=REFINE, bg_color=None, text_color=TEXT):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.adjustments[0] = 0.08
    card.line.color.rgb = accent
    card.line.width = Pt(1.5)
    card.fill.solid(); card.fill.fore_color.rgb = bg_color if bg_color else RGBColor(0xFF, 0xFF, 0xFF)

    # Accent bar
    add_accent_bar(slide, left + Inches(0.25), top + Inches(0.25), width=Inches(0.35), height=Inches(0.05), color=accent)

    # Title
    add_text(slide, left + Inches(0.25), top + Inches(0.35), width - Inches(0.5), Inches(0.35),
             title, size=13, bold=True, color=text_color, font="Calibri")

    # Bullets
    tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.8), width - Inches(0.5), height - Inches(0.9))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(0); tf.margin_right = Emu(0); tf.margin_top = Emu(0); tf.margin_bottom = Emu(0)
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(4)
        run = p.add_run(); run.text = "•  " + b
        run.font.size = Pt(10.5); run.font.color.rgb = MUTED; run.font.name = "Calibri"


# ============ SLIDE 1: Hoogover flowchart ============
s1 = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s1, BG_SLIDE)

# Tag
add_accent_bar(s1, Inches(0.6), Inches(0.45), width=Inches(0.3), height=Inches(0.04))
add_text(s1, Inches(1.0), Inches(0.38), Inches(6), Inches(0.3),
         "PIVOT · AURORA", size=9, bold=True, color=REFINE)

# Title
add_text(s1, Inches(0.6), Inches(0.62), Inches(11), Inches(0.9),
         "Van natte handtekening naar gekoppelde identiteit",
         size=28, bold=True, color=TEXT)

add_text(s1, Inches(0.6), Inches(1.35), Inches(11), Inches(0.4),
         "Het papier en de pen blijven. Het bewijs verschuift.",
         size=13, color=MUTED)

# Hoogover image
img_left = Inches(0.6)
img_top = Inches(1.95)
img_w = Inches(12.1)
s1.shapes.add_picture(HOOGOVER_PNG, img_left, img_top, width=img_w)

# Footer
add_text(s1, Inches(0.6), Inches(7.1), Inches(8), Inches(0.25),
         "Anke · Lianne · Jr  ·  EDIM.21", size=9, color=MUTED)


# ============ SLIDE 2: Strategisch + technisch ============
s2 = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s2, BG_SLIDE)

add_accent_bar(s2, Inches(0.6), Inches(0.45), width=Inches(0.3), height=Inches(0.04))
add_text(s2, Inches(1.0), Inches(0.38), Inches(6), Inches(0.3),
         "ANALYSE · DEEL 1", size=9, bold=True, color=REFINE)

add_text(s2, Inches(0.6), Inches(0.62), Inches(11), Inches(0.6),
         "Strategisch & technisch", size=26, bold=True, color=TEXT)

# 2x2 cards
card_w = Inches(6.0)
card_h = Inches(2.7)
col1, col2 = Inches(0.6), Inches(6.75)
row1, row2 = Inches(1.55), Inches(4.4)

add_card(s2, col1, row1, card_w, card_h,
         "Strategische fit",
         ["125+ jaar autoriteit rond ondertekenen",
          "Betekeniswereld (vertrouwen, gezag) blijft",
          "Verschuiving: van tool naar proces"])

add_card(s2, col2, row1, card_w, card_h,
         "Kerncompetenties",
         ["Domeinkennis: hoe mensen tekenen",
          "Merkautoriteit bij notaris en bank",
          "Bestaand distributienetwerk",
          "Niet in huis: tech-engineering → partner"])

add_card(s2, col1, row2, card_w, card_h,
         "Technische fit",
         ["Aurora levert kennismodel + merk",
          "Techpartner levert infrastructuur",
          "Hergebruik: ID-scan, NFC, PIN",
          "Protocol koppelt handtekening aan code"])

add_card(s2, col2, row2, card_w, card_h,
         "Concurrentievoordeel — nieuwe markt",
         ["DocuSign/PKI: 100% digitaal",
          "DigiD: overheidsgebonden",
          "Witte plek: hybride papier + digitaal bewijs",
          "Aurora als eerste geloofwaardig in die combinatie"])


# ============ SLIDE 3: Customer value + financieel ============
s3 = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(s3, BG_SLIDE)

add_accent_bar(s3, Inches(0.6), Inches(0.45), width=Inches(0.3), height=Inches(0.04))
add_text(s3, Inches(1.0), Inches(0.38), Inches(6), Inches(0.3),
         "ANALYSE · DEEL 2", size=9, bold=True, color=REFINE)

add_text(s3, Inches(0.6), Inches(0.62), Inches(11), Inches(0.6),
         "Waarde & financieel", size=26, bold=True, color=TEXT)

# 3 columns
card_w3 = Inches(4.0)
card_h3 = Inches(5.3)
gap = Inches(0.15)
col_a = Inches(0.6)
col_b = col_a + card_w3 + gap
col_c = col_b + card_w3 + gap
row_y = Inches(1.55)

add_card(s3, col_a, row_y, card_w3, card_h3,
         "Customer value",
         ["Notaris: rechtsgeldigheid zonder extra stap",
          "Bank: fraudepreventie bij contracten",
          "Gemeente: schaalbare ondertekening",
          "Eindgebruiker: vertrouwde handtekening met bewijsbare identiteit"])

add_card(s3, col_b, row_y, card_w3, card_h3,
         "Financiële kansen",
         ["Licentiemodel kennismodel (recurring)",
          "Hardware-omzet verificatiestations",
          "Training en consultancy bij uitrol",
          "NL-markt: ~3.000 notarissen, banken, 340 gemeenten, zakelijk",
          "Merkextensie zonder kannibalisatie bestaande lijn"])

add_card(s3, col_c, row_y, card_w3, card_h3,
         "Financiële risico's",
         ["Ontwikkelkosten techpartner buiten onze grip",
          "Adoptietijd lang (compliance, juridisch)",
          "Afhankelijkheid van één techpartner",
          "Fully-digital concurrentie drukt marges",
          "Risico cannibalisatie pen-lijn bij brede uitrol"],
         accent=CORAL, bg_color=BG_RISK)


# Save
output = "/Users/jr/Library/CloudStorage/OneDrive-Zonneplan/School/Innovatiemanagement/public/presentatie-pivot.pptx"
prs.save(output)
print(f"Saved: {output}")
