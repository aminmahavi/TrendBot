# TrendBot

**TrendBot** یک ربات تولید محتوای ویدیویی هوش‌مصنوعی برای یوتیوب است که ترندهای روز را شناسایی کرده، نسخه Creative Commons آنها را دانلود، ترجمه و پردازش می‌کند و نسخه آماده انتشار تولید می‌کند.

---

## 🚀 ویژگی‌ها
- دریافت لیست ترند یوتیوب و فیلتر Creative Commons  
- ترجمه عنوان‌ها به فارسی با `deep-translator`  
- دانلود ویدئوهای CC با `pytube`  
- بک‌اند سبک و سریع با **FastAPI**  
- ساختار ماژولار برای توسعه در فازهای بعدی  

---

## 📂 ساختار پروژه

app/

├── main.py

├── trend_finder.py

└── utils/

downloads/

tests/

requirements.txt


---

## ⚙️ نصب و اجرا
```bash
# ساخت و فعال‌سازی محیط مجازی
python -m venv venv
.\venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرا
uvicorn app.main:app --reload
🛠 تکنولوژی‌ها
Python 3.11+
FastAPI
deep-translator
pytube
📅 برنامه توسعه (Roadmap)
Phase 1 ✅: شناسایی و دانلود ویدئو CC
Phase 2 ⏳: ادیت خودکار، ترجمه کامل و تولید خروجی
Phase 3 ⏳: آپلود خودکار به یوتیوب، سئو و گزارش
📄 لایسنس
این پروژه تحت لایسنس MIT منتشر شده است.


