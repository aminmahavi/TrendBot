# phase2.py
import os
from deep_translator import GoogleTranslator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# === Step 1: Read Phase 1 Output ===
INPUT_FILE = "phase1_output.txt"  # نام فایل خروجی فاز ۱
try:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw_text = f.read().strip()
except FileNotFoundError:
    raise FileNotFoundError(f"{INPUT_FILE} not found. Run Phase 1 first.")

# === Step 2: Auto Edit ===
def auto_edit(text):
    """Clean or format the input text."""
    cleaned = " ".join(text.split())  # حذف فاصله‌های اضافی
    return cleaned

edited_text = auto_edit(raw_text)

# === Step 3: Translate to Persian ===
translator = GoogleTranslator(source="en", target="fa")
persian_translation = translator.translate(edited_text)

# === Step 4: Output Prep & Save ===
OUTPUT_FILE = "phase2_output.txt"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("--- English Version ---")
    f.write(edited_text + "")
    f.write("--- Persian Translation ---")
    f.write(persian_translation + "")

print("✅ Phase 2 completed!")
print(f"Results saved to {OUTPUT_FILE}")
