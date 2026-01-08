# Scripturient ✍️  
*A Dedicated Platform for Creative Writers*

## 📌 Project Overview
**Scripturient** is a creative writing and blogging platform designed exclusively for writers and readers.  
The name *Scripturient* comes from Latin, meaning *having a strong urge to write*, and the platform truly embodies this spirit by offering a focused, distraction-free environment for literary expression.

Unlike generic social media platforms, Scripturient prioritizes meaningful content, constructive feedback, and visibility for both aspiring and established writers.

---

## 🎯 Problem Statement
- Lack of **dedicated communities** for creative writers  
- High-quality writing often gets **lost in noise** on general platforms  
- **Beginner writers** struggle to gain visibility  
- Minimal **constructive feedback and engagement**  

**Scripturient addresses these gaps** by offering a platform built solely for writing, reading, and thoughtful interaction.

---

## 🚀 Features
- 🔐 **Secure User Authentication**
  - User registration and login
  - Password protection and session handling  

- ✍️ **Create, Edit & Publish Content**
  - Blogs, poems, stories, and articles
  - Draft management and updates anytime  

- ❤️ **Engagement System**
  - Like posts
  - Comment and reply
  - Follow favorite writers  

- 👤 **User Profile Management**
  - View personal posts
  - Edit profile details  

- 📊 **Author Dashboard**
  - Post statistics (views, likes, comments)
  - Draft and published post management  

- 🛡️ **Admin Dashboard**
  - User moderation
  - Content moderation
  - Analytics and engagement tracking  

---

## 🏗️ System Architecture
Scripturient follows a **client-server architecture** with a RESTful backend and a dynamic frontend.

### Frontend
- **React.js**
- **Tailwind CSS**
- Responsive UI for desktop & mobile
- Search, filter, and interactive dashboards

### Backend
- **Django REST Framework (DRF)**
- REST APIs for users, posts, comments
- JWT / OAuth based authentication
- Media handling and analytics

### Database
- **PostgreSQL** (Relational)  
  *(MongoDB can be used alternatively)*

### Storage
- **Cloudinary / AWS S3**
- Stores images and media files

### Optional Services
- Redis (Caching)
- Celery (Background tasks & notifications)
- ElasticSearch (Advanced full-text search)
- AI modules (content suggestions, toxicity detection)

---

## 🖥️ User Interface Highlights
- **Landing Page** – Featured posts & latest content
- **Post Detail Page** – Rich text, comments, likes, tags
- **Author Dashboard** – Post management & insights
- **Admin Dashboard** – Analytics & moderation tools
- **Comment System** – Nested replies and engagement

---

## 🔄 Sample Workflow (Post Creation)
1. User writes content in frontend editor
2. React sends POST request to backend API
3. Backend validates and stores data
4. Media uploaded to Cloudinary (if any)
5. Post published successfully
6. Followers notified asynchronously

---

## 🛠️ Tech Stack
**Frontend:**  
- React.js  
- Tailwind CSS  

**Backend:**  
- Django REST Framework  

**Database:**  
- PostgreSQL  

**Storage & Services:**  
- Cloudinary / AWS S3  
- Redis, Celery (optional)

<img width="1865" height="1009" alt="image" src="https://github.com/user-attachments/assets/01dd008f-eae0-4fa7-b2a4-ea5f66aefa64" />
