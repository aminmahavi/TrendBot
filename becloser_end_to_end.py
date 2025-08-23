# becloser_end_to_end.py
from deep_translator import GoogleTranslator
from trend_finder_new import get_trending_videos  # استفاده از نسخه جدید با کلید API جدید

# ----------------
# مرحله ۱: Phase 1
# ----------------
def phase1_process():
    # گرفتن لیست ویدیوهای ترند به همراه ترجمه فارسی و ذخیره احتمالی Creative Commons
    return get_trending_videos(region_code="US", max_results=5)

# ----------------
# مرحله ۲: Auto Edit
# ----------------
def auto_edit(text_list):
    # اگر ورودی لیست باشه، به رشته تبدیلش می‌کنیم
    if isinstance(text_list, list):
        text = "".join(text_list)
    else:
        text = str(text_list)
    edited_text = text.strip().replace("  ", " ")
    return edited_text

# ----------------
# مرحله ۳: Translate
# ----------------
def translate_to_persian(text):
    # متن رو اگر انگلیسی بود به فارسی ترجمه می‌کنیم
    translator = GoogleTranslator(source="auto", target="fa")
    return translator.translate(text)

# ----------------
# مرحله ۴: Output Prep
# ----------------
def output_prep(translated_text):
    final_output = "*** خروجی نهایی ***" + translated_text + ""
    return final_output

# ----------------
# اجرای کل فرآیند
# ----------------
def main():
    # گام ۱: فاز ۱
    phase1_output = phase1_process()
    print("[Phase 1] Raw output:", phase1_output)

    # گام ۲: Auto Edit
    edited = auto_edit(phase1_output)
    print("[Phase 2 - Step 1] Edited output:", edited)

    # گام ۳: Translate (اختیاری اگر لازم باشه دوباره ترجمه شه)
    translated = translate_to_persian(edited)
    print("[Phase 2 - Step 2] Translated output:", translated)

    # گام ۴: Output Prep
    final_output = output_prep(translated)

    # ذخیره در فایل
    with open("final_output.txt", "w", encoding="utf-8") as f:
        f.write(final_output)

    print("[DONE] Final output saved to final_output.txt")

if __name__ == "__main__":
    main()
