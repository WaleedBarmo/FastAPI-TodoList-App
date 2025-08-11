FastAPI To-Do App with PostgreSQL
نظرة عامة على المشروع (Project Overview)
تطبيق قائمة مهام متكامل (Full-stack) مصمم لمساعدة المستخدمين على إدارة مهامهم الشخصية بكفاءة. يجمع المشروع بين قوة الأداء والمرونة باستخدام إطار عمل FastAPI للواجهة الخلفية وقاعدة بيانات PostgreSQL الموثوقة.

A full-stack To-Do list application designed to help users manage their personal tasks efficiently. The project combines the high performance of the FastAPI framework for the backend with the reliability of a PostgreSQL database.

الميزات الرئيسية (Key Features)
إدارة المهام (Task Management):

إنشاء، قراءة، تحديث، وحذف المهام (CRUD).

نظام تراتبية للمهام يسمح بنقل المهام بين الحالات: "قيد الإنجاز" (To-Do)، "قيد التقدم" (In-Progress)، "تم" (Done). هذه الميزة تتيح للمستخدمين تتبع تقدم المهام وإعادتها للمراجعة.

توثيق المستخدمين (User Authentication):

نظام آمن لتسجيل الدخول وتسجيل المستخدمين الجدد باستخدام رموز JWT.

API من نوع RESTful:

واجهة برمجية نظيفة ومنظمة تم بناؤها باستخدام FastAPI، مع توثيق تفاعلي تلقائي عبر Swagger UI.

تخزين البيانات (Data Storage):

يتم تخزين جميع بيانات المهام والمستخدمين في قاعدة بيانات PostgreSQL.

التقنيات المستخدمة (Technologies Used)
الواجهة الخلفية (Backend): Python, FastAPI, Pydantic, Uvicorn, SQLAlchemy.

قاعدة البيانات (Database): PostgreSQL.

المصادقة (Authentication): JWT (PyJWT).

الواجهة الأمامية (Frontend): HTML, CSS, JavaScript.

كيفية التشغيل (How to Run the Project)
لضمان عمل المشروع بشكل صحيح، اتبع هذه الخطوات بدقة:

1. إعداد بيئة العمل (Setup Environment)
# استنسخ المستودع (Clone the Repository)
git clone https://github.com/WaleedBarmo/FastAPI-TodoList-App.git

# انتقل إلى مجلد المشروع (Navigate into the project directory)
cd FastAPI-TodoList-App

# إعداد البيئة الافتراضية (Create a Virtual Environment)
python -m venv venv

# تفعيل البيئة (Activate the Virtual Environment)
# على أنظمة macOS / Linux
source venv/bin/activate
# على أنظمة Windows
.\venv\Scripts\activate

# تثبيت المكتبات المطلوبة (Install required packages)
pip install -r requirements.txt

2. إعداد قاعدة بيانات PostgreSQL (Setup PostgreSQL Database)
أنشئ قاعدة بيانات PostgreSQL جديدة (يمكنك استخدام خدمات مثل Railway أو تشغيلها محلياً).

ستحتاج إلى رابط الاتصال (Database URL). سيكون شكله كالتالي:
postgresql://<username>:<password>@<host>:<port>/<database_name>

إذا كنت تستخدم Railway، يمكنك الحصول على رابط الاتصال كما في الصورة

3. إعداد الواجهة الخلفية (Backend Setup)
# انتقل إلى مجلد الـ backend
cd backend

# أنشئ ملفاً جديداً باسم .env
touch .env

# افتح الملف وأضف المفتاح السري ورابط قاعدة البيانات
# استبدل القيم الخاصة بك هنا
SECRET_KEY="your-secret-key-goes-here"
DATABASE_URL="postgresql://user:password@host:port/database"

4. تشغيل المشروع (Run the Application)
# في مجلد backend، شغل الخادم باستخدام Uvicorn
uvicorn main:app --reload

# يجب أن يعمل الخادم الآن على http://127.0.0.1:8000

5. استخدام التطبيق (Using the App)
بعد تشغيل الخادم، افتح ملف frontend/index.html في متصفح الويب الخاص بك. يمكنك الآن التسجيل، تسجيل الدخول، وإدارة المهام.