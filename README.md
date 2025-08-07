# 📽️ Integral Agent – Automatický řešitel a animátor integrálů

Tento nástroj automaticky rozpozná matematický výraz z obrázku, vyřeší ho krok po kroku pomocí LLM (např. `deepseek-r1`) a vygeneruje vizuální animaci výpočtu pomocí Manim.

---

## 🚀 Funkce

- 🧠 Rozpoznání integrálu z obrázku pomocí OCR
- 🗣️ Výpočet krok po kroku přes OpenRouter API (LLM model `deepseek-r1:free`)
- 📦 Automatické vygenerování Python modulu `zadani.py` se všemi kroky
- 🎞️ Vizuální animace řešení v Manim (včetně zvýraznění kroků)
- ♻️ Plně automatizovaný workflow – stačí vložit obrázek do složky `input/`

---

## 🛠️ Požadavky

- Python 3.10+
- Manim CE (doporučeno nainstalovat přes pip)
- Tesseract OCR  
  (Windows: nainstaluj z [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract))
- OpenRouter API účet + platný API klíč
- Git + VS Code (volitelně)

---

## 📦 Instalace

1. Naklonuj repozitář:

```bash
git clone https://github.com/tvoje-jmeno/integral-agent.git
cd integral-agent
```

2. Nainstaluj požadavky:

```bash
pip install -r requirements.txt
```

3. Ujisti se, že máš nainstalovaný Tesseract  
   (např. `C:\Program Files\Tesseract-OCR\tesseract.exe`)

4. Vlož svůj OpenRouter API klíč do `agent.py`:

```python
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-..."  # ← sem vlož svůj klíč
)
```

---

## ▶️ Použití

1. Spusť agenta:

```bash
python agent.py
```

2. Vlož obrázek se zadáním (např. fotku integrálu) do složky `input/`.

3. Automaticky se:
   - spustí OCR a LLM,
   - vytvoří soubor `zadani.py`,
   - spustí `generate_scene.py` přes Manim a vygeneruje animaci.

4. Výsledné video najdeš ve složce `media/videos/`.

---

## 📁 Struktura složek

```
📁 integral-agent/
├── agent.py              # Hlavní skript – sleduje složku a spouští proces
├── zadani.py             # Vygenerovaný modul s TITLE, MAIN_EQ, STEPS, FINAL_RESULT
├── generate_scene.py     # Manim animace řešení
├── input/                # Sem vkládej obrázky se zadáním
├── media/                # Výstupní video složka (Manim)
```

---

## ⚠️ Upozornění k API klíči

🔐 Nikdy nesdílej svůj API klíč veřejně (ani na GitHub).  
Pokud jsi ho omylem zveřejnil, okamžitě ho regeneruj na [https://openrouter.ai](https://openrouter.ai).

---

## 🧠 Použitý LLM model

- [DeepSeek Math](https://openrouter.ai/chat/deepseek/deepseek-math) (`deepseek-r1:free`)
- Prompt je optimalizovaný pro přesné krokové řešení a validní Python výstup.

---

## 📜 Licence

MIT License


