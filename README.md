FastAPI To-Do App with PostgreSQL
In English
Project Overview
This is a full-stack To-Do list application that allows users to sign in and manage their personal tasks efficiently. The project combines the high performance of the FastAPI framework for the backend with the reliability of a PostgreSQL database.

Key Features
Task Management: A status-based system that allows users to move tasks between "To-Do," "In-Progress," and "Done" states. This feature enables users to track progress and revert tasks for review.

User Authentication: A secure system for user registration and login using JWT (JSON Web Tokens).

RESTful API: A clean and organized API built with FastAPI, featuring automatic interactive documentation via Swagger UI.

Data Storage: All task and user data are stored in a PostgreSQL database.

Technologies Used
Backend: Python, FastAPI, Pydantic, Uvicorn, SQLAlchemy.

Database: PostgreSQL.

Authentication: JWT (PyJWT).

Frontend: HTML, CSS, JavaScript.

How to Run the Project
To ensure the project runs correctly, follow these steps:

Setup Environment:

git clone https://github.com/WaleedBarmo/FastAPI-TodoList-App.git
cd FastAPI-TodoList-App
python -m venv venv
# Activate the virtual environment on macOS / Linux
source venv/bin/activate
# Activate the virtual environment on Windows
.\venv\Scripts\activate
pip install -r requirements.txt

Setup PostgreSQL Database:

Create a new PostgreSQL database (you can use services like Railway or run it locally).

Get your Database URL, which will look like this:
postgresql://<username>:<password>@<host>:<port>/<database_name>

If you're using Railway, you can find the connection URL as shown in the image

Backend Setup:

cd backend
touch .env
# Add your secret key and database URL to the .env file
SECRET_KEY="your-secret-key-goes-here"
DATABASE_URL="postgresql://user:password@host:port/database"

Run the Application:

uvicorn main:app --reload

The server should now be running at http://127.0.0.1:8000.

Using the App:
After the backend server is running, open the frontend/index.html file in your web browser. You can now register, log in, and manage your tasks.

باللغة العربية
نظرة عامة على المشروع
تطبيق قائمة مهام متكامل (Full-stack) يسمح للمستخدمين بتسجيل الدخول وإدارة مهامهم الشخصية بكفاءة. يجمع المشروع بين قوة الأداء والمرونة باستخدام إطار عمل FastAPI للواجهة الخلفية وقاعدة بيانات PostgreSQL الموثوقة.

الميزات الرئيسية
إدارة المهام: نظام تراتبية يسمح بتتبع المهام ونقلها بين الحالات: "قيد الإنجاز" (To-Do)، "قيد التقدم" (In-Progress)، "تم" (Done).

توثيق المستخدمين: نظام آمن لتسجيل الدخول وتسجيل المستخدمين الجدد باستخدام رموز JWT.

API من نوع RESTful: واجهة برمجية منظمة مع توثيق تفاعلي تلقائي عبر Swagger UI.

تخزين البيانات: يتم تخزين جميع البيانات في قاعدة بيانات PostgreSQL.

التقنيات المستخدمة
الواجهة الخلفية: Python, FastAPI, Pydantic, Uvicorn, SQLAlchemy.

قاعدة البيانات: PostgreSQL.

المصادقة: JWT (PyJWT).

الواجهة الأمامية: HTML, CSS, JavaScript.

كيفية التشغيل
لضمان عمل المشروع بشكل صحيح، اتبع هذه الخطوات:

إعداد بيئة العمل:

git clone https://github.com/WaleedBarmo/FastAPI-TodoList-App.git
cd FastAPI-TodoList-App
python -m venv venv
# تفعيل البيئة (Windows)
.\venv\Scripts\activate
# تفعيل البيئة (macOS / Linux)
source venv/bin/activate
pip install -r requirements.txt

إعداد قاعدة بيانات PostgreSQL:

أنشئ قاعدة بيانات PostgreSQL جديدة.

احصل على رابط الاتصال (Database URL) الخاص بها.

إذا كنت تستخدم Railway، يمكنك الحصول على رابط الاتصال

إعداد الواجهة الخلفية:

cd backend
touch .env
# أضف المفتاح السري ورابط قاعدة البيانات
SECRET_KEY="your-secret-key-goes-here"
DATABASE_URL="postgresql://user:password@host:port/database"

تشغيل المشروع:

uvicorn main:app --reload

الخادم سيعمل على http://127.0.0.1:8000.

استخدام التطبيق:
افتح ملف frontend/index.html في متصفح الويب.