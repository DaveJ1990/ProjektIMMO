import streamlit as st
from openai import OpenAI

# Neuen OpenAI-Client initialisieren
client = OpenAI()

# Streamlit-Seite konfigurieren
st.set_page_config(page_title="KI Mieteranfragen-Analysator", layout="centered")
st.title("📑 KI Mieteranfragen-Analysator")

# Texteingabe
anfrage = st.text_area("🔑 Mieteranfrage eingeben", height=200)

if st.button("Analyse starten"):
    if anfrage.strip() == "":
        st.warning("Bitte eine Anfrage eingeben.")
    else:
        prompt = f'''
Analysiere folgende Mieteranfrage:

"{anfrage}"

1) Extrahiere:
  - Anzahl Personen
  - Alter der Kinder
  - Beruf & Einkommen (falls vorhanden)
  - Haustiere
  - Einzugsdatum (falls vorhanden)
2) Bewerte, ob alle Infos vorhanden sind (Ja/Nein).
3) Gib eine Empfehlung: (a) Besichtigung vorschlagen, (b) Rückfrage stellen, (c) Absagen.
4) Gib einen Score von 0 bis 100.
5) Erstelle eine formelle Antwort-E-Mail passend zur Empfehlung.

Antwort im Format:
Personen:
Alter Kinder:
Beruf/Einkommen:
Haustiere:
Einzugsdatum:
Empfehlung:
Score:
Antwort:
'''

        # Neuer Aufruf mit aktuellem Client
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        ergebnis = response.choices[0].message.content
        st.success("✅ Analyse abgeschlossen")
        st.code(ergebnis, language="markdown")
