import os
import time
import threading
from openai import OpenAI
from PIL import Image
import pytesseract
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=("ENTER_YOUR_KEY_HERE")
)

prompt_template = """Z obrázku s matematickým výrazem rozpoznaným OCR:

{equation}

vytvoř Python kód pro modul `zadani.py`, který obsahuje tyto čtyři proměnné:

- TITLE = "..."
- MAIN_EQ = r"..."
- STEPS = [ r"...", r"...", … ]
- FINAL_RESULT = r"..."

Nepřidávej žádné komentáře ani zpětné apostrofy ``` – pouze čistý Python kód."""

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(image, lang="eng")
    return text.strip()

def ask_openrouter(prompt):
    response = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {"role": "system", "content": "Jsi expert na řešení integrálů a Manim animace."},
        {"role": "user", "content": prompt},
    ],
    temperature=0.2,
)
    return response.choices[0].message.content

def solve_image(image_path):
    print(f"📷 Nový obrázek: {image_path}")
    text = extract_text_from_image(image_path)
    print(f"🧾 OCR výstup: {text}\n")

    print("🧠 Ptám se OpenRouter...")
    prompt = prompt_template.format(equation=text)
    response_text = ask_openrouter(prompt)

    # Uložení bez zpětných apostrofů
    clean_text = response_text.replace("```python", "").replace("```", "").strip()

    with open("zadani.py", "w", encoding="utf-8") as f:
        f.write(clean_text)

    print("📄 Výstup od AI uložen jako zadani.py")
    print("🎬 Spouštím Manim...")

    try:
        subprocess.run(["py", "-m", "manim", "generate_scene.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("❌ Něco se nepovedlo. Zkontroluj chyby výše.")

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.lower().endswith((".png", ".jpg", ".jpeg")):
            time.sleep(1)
            solve_image(event.src_path)

if __name__ == "__main__":
    input_dir = "input"
    os.makedirs(input_dir, exist_ok=True)

    print(f"👁️ Sleduji složku '{input_dir}'... Vlož sem fotku se zadáním.")
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path=input_dir, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
