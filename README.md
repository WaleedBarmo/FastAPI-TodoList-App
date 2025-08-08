# FastAPI To-Do App with PostgreSQL

تطبيق قائمة مهام متكامل (Full-stack) يسمح للمستخدمين بتسجيل الدخول وإدارة مهامهم الشخصية.

## الميزات
- **توثيق المستخدمين:** نظام تسجيل وتسجيل دخول آمن باستخدام رموز JWT (JSON Web Tokens).
- **إدارة المهام:** يمكن للمستخدمين إضافة، تعديل، وحذف مهامهم.
- **تخزين البيانات:** يتم تخزين المهام وبيانات المستخدم في قاعدة بيانات **PostgreSQL**.
- **API من نوع RESTful:** واجهة برمجية نظيفة ومنظمة تم بناؤها باستخدام FastAPI.

## التقنيات المستخدمة
- **الواجهة الخلفية (Backend):** Python, FastAPI, Pydantic, Uvicorn, SQLAlchemy
- **الواجهة الأمامية (Frontend):** HTML, CSS, JavaScript
- **قاعدة البيانات:** PostgreSQL
- **المصادقة (Authentication):** JWT (PyJWT)

---

## كيفية التشغيل
لضمان عمل المشروع بشكل صحيح، اتبع هذه الخطوات بدقة:

### 1. إعداد بيئة العمل
1.  **استنسخ المستودع (Clone the Repository):**
    ```bash
    git clone [https://github.com/WaleedBarmo/FastAPI-TodoList-App.git](https://github.com/WaleedBarmo/FastAPI-TodoList-App.git)
    cd FastAPI-TodoList-App
    ```
2.  **إعداد البيئة الافتراضية:**
    ```bash
    python -m venv venv
    # تفعيل البيئة (Windows)
    .\venv\Scripts\activate
    # تفعيل البيئة (macOS / Linux)
    source venv/bin/activate
    ```
3.  **تثبيت المكتبات:**
    ```bash
    pip install -r requirements.txt
    ```

---

### 2. إعداد الواجهة الخلفية (Backend)
1.  **انتقل إلى مجلد الـ `backend`:**
    ```bash
    cd backend
    ```
2.  **إعداد قاعدة بيانات PostgreSQL:**
    * أنشئ قاعدة بيانات PostgreSQL جديدة (على Railway أو محلياً).
    * احصل على **رابط الاتصال (Database URL)** الخاص بها.
3.  **إنشاء ملف `env.`:**
    * في مجلد `backend`، أنشئ ملفاً جديداً باسم `.env`.
    * أضف المفتاح السري ورابط قاعدة البيانات بهذا الشكل (مع استبدال القيم الخاصة بك):
    ```env
    SECRET_KEY="your-secret-key-goes-here"
    DATABASE_URL="postgresql://user:password@host:port/database"
    ```
4.  **تشغيل الخادم:**
    ```bash
    uvicorn main:app --reload
    ```
    يجب أن يعمل الخادم الآن بدون أي أخطاء.

---

### 3. إعداد الواجهة الأمامية (Frontend)
1.  **افتح الواجهة الأمامية:**
    * بعد تشغيل الخادم الخلفي، افتح ملف `frontend/index.html` في متصفح الويب الخاص بك.
    * يمكنك الآن التسجيل، تسجيل الدخول، وإدارة المهام.
