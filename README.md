# FastAPI To-Do App

A full-stack to-do list application that allows users to register, log in, and manage their personal tasks.

## Features
- **User Authentication:** Secure signup and login using JWT (JSON Web Tokens).
- **Task Management:** Users can add, edit, and delete their tasks.
- **Data Persistence:** Tasks and user data are stored in a MongoDB database.
- **RESTful API:** A clean and well-structured API built with FastAPI.

## Technologies Used
- **Backend:** Python, FastAPI, Pydantic, Uvicorn
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MongoDB
- **Authentication:** JWT (PyJWT)

## How to Run
1. **Clone the Repository:**
    ```bash
    git clone [https://github.com/WaleedBarmo/FastAPI-TodoList-App.git](https://github.com/WaleedBarmo/FastAPI-TodoList-App.git)
    cd FastAPI-TodoList-App
    ```
2. **Setup the Backend:**
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
3. **Open the Frontend:**
    Open the `frontend/index.html` file in your web browser.

---

# تطبيق قائمة المهام بـ FastAPI

تطبيق قائمة مهام متكامل (Full-stack) يسمح للمستخدمين بتسجيل الدخول وإدارة مهامهم الشخصية.

## الميزات
- **توثيق المستخدمين:** نظام تسجيل وتسجيل دخول آمن باستخدام رموز JWT (JSON Web Tokens).
- **إدارة المهام:** يمكن للمستخدمين إضافة، تعديل، وحذف مهامهم.
- **تخزين البيانات:** يتم تخزين المهام وبيانات المستخدم في قاعدة بيانات MongoDB.
- **API من نوع RESTful:** واجهة برمجية نظيفة ومنظمة تم بناؤها باستخدام FastAPI.

## التقنيات المستخدمة
- **الواجهة الخلفية (Backend):** Python, FastAPI, Pydantic, Uvicorn
- **الواجهة الأمامية (Frontend):** HTML, CSS, JavaScript
- **قاعدة البيانات:** MongoDB
- **المصادقة (Authentication):** JWT (PyJWT)

## كيفية التشغيل
1. **استنسخ المستودع (Clone the Repository):**
    ```bash
    git clone [https://github.com/WaleedBarmo/FastAPI-TodoList-App.git](https://github.com/WaleedBarmo/FastAPI-TodoList-App.git)
    cd FastAPI-TodoList-App
    ```
2. **إعداد الواجهة الخلفية (Backend):**
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
3. **افتح الواجهة الأمامية (Frontend):**
    افتح ملف `frontend/index.html` في متصفح الويب الخاص بك.
