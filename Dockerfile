# استخدم صورة Python الرسمية
FROM python:3.9-slim

# تحديد مسار العمل داخل الحاوية
WORKDIR /app

# نسخ متطلبات المشروع (ملف التطبيق) إلى الحاوية
COPY . /app

# تثبيت Flask
RUN pip install flask

# تعريف المنفذ الذي سيعمل عليه التطبيق
EXPOSE 5000

# تشغيل التطبيق
CMD ["python", "assli.py"]
