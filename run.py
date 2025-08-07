import os
import shutil
from pathlib import Path

# Cesty a názvy
scene_file = "generate_scene.py"
scene_class = "IntegralScene"
media_dir = Path("media/videos")

# Smazání starých videí
if media_dir.exists():
    print("Mažu staré video soubory...")
    shutil.rmtree(media_dir)

# Spuštění manim v rozlišení 1080x1920 (vertikální video)
command = f'py -m manim -pqh -r 1080,1920 {scene_file} {scene_class}'
print("Spouštím manim...")
exit_code = os.system(command)

if exit_code == 0:
    print("\n✅ Hotovo! Nové video je v adresáři media/videos/")
else:
    print("\n❌ Něco se nepovedlo. Zkontroluj chyby výše.")
