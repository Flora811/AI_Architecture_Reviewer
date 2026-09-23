# 🎓 Student Management System

A full-stack Spring Boot web application for managing students, courses, and enrollments through an admin interface.
Built using Spring MVC with Thymeleaf for server-side rendering, Spring Security for authentication, and MySQL for data persistence, following a layered architecture.

**🌐 Live Demo**

Check out the deployed project here: [Student Management System on Render](https://student-management-system-n6j7.onrender.com)

## 🚀 Features

- 🔐 Admin authentication using Spring Security
- 👨‍🎓 Student management (CRUD operations)
- 📚 Course management (CRUD operations)
- 🔗 Student enrollment into courses
- ✅ Input validation and error handling
- 📄 Pagination for large datasets
- 🔄 DTO-based architecture (clean API design)
- 📝 Centralized logging using Logback (console + rolling file logs)

## 🛠 Tech Stack

**Backend**
- Java with Spring Boot
- Spring Security (Authentication & Authorization)
- Spring Data JPA (ORM)

**Frontend**
- Thymeleaf (Server-side rendering)
- HTML, CSS, JS

**Database**
- PostgreSQL

**DevOps & Deployment**
- Docker
- Render

**Version Control**
- Git
- GitHub

**Build Tool**
- Maven


## 📡 API Endpoints

> Base URL: `/`

---

### 🔐 Authentication

| Method | Endpoint | Description       |
| ------ | -------- | ----------------- |
| GET    | `/login` | Render login page |

---

### 🎛 Dashboard

| Method | Endpoint     | Description                                      |
| ------ | ------------ | ------------------------------------------------ |
| GET    | `/dashboard` | View dashboard statistics and recent enrollments |

---

### 👨‍🎓 Students

| Method | Endpoint               | Description                    |
| ------ | ---------------------- | ------------------------------ |
| GET    | `/student/list`        | Get paginated list of students |
| GET    | `/student/new`         | Show create student form       |
| POST   | `/student`             | Create a new student           |
| GET    | `/student/{id}`        | View student details           |
| GET    | `/student/{id}/edit`   | Show edit student form         |
| POST   | `/student/{id}/update` | Update student                 |

---

### 📚 Courses

| Method | Endpoint              | Description                   |
| ------ | --------------------- | ----------------------------- |
| GET    | `/course/list`        | Get paginated list of courses |
| GET    | `/course/new`         | Show create course form       |
| POST   | `/course`             | Create a new course           |
| GET    | `/course/{id}`        | View course details           |
| GET    | `/course/{id}/edit`   | Show edit course form         |
| POST   | `/course/{id}/update` | Update course                 |

---

### 🔗 Enrollments

| Method | Endpoint                              | Description                     |
| ------ | ------------------------------------- | ------------------------------- |
| GET    | `/enrollments/showEnroll`             | Show enrollment form            |
| POST   | `/enrollments/enrollCourse`           | Enroll student in a course      |
| GET    | `/enrollments/enrollmentList`         | Get paginated enrolled students |
| GET    | `/enrollments/enrollmentDetails/{id}` | View enrollment details         |

---

### ⚙️ Query Parameters

| Parameter | Description                             |
| --------- | --------------------------------------- |
| `page`    | Page number (default: 0)                |
| `size`    | Number of records per page (default: 3) |


## 🖼 Screenshots

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=15AD-Qf20KqtPs1Usz-3IXhzNaKTa5sQM" width="45%" />
  <img src="https://drive.google.com/uc?export=view&id=1gESR796guljxrKGwkjUKwIbzyDiIQLUq" width="45%" />
  <img src="https://drive.google.com/uc?export=view&id=1C783FWWD5lmo5ewZYYPgogExw6U3AF2m" width="45%" />
</p>

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1vFNVWNuNtPn4nWG3WhbMycsdk0LzQSwe" width="45%" />
  <img src="https://drive.google.com/uc?export=view&id=11bVINADZNqy-au8BIzde8OtU7U6rSVYf" width="45%" />
  <img src="https://drive.google.com/uc?export=view&id=1UUtlAzGbzKt5ppx_Wd64bmvRA_brME6p" width="45%" />
</p>


## ⚙️ Installation and Setup

**Clone the repository**
```bash
  git clone https://github.com/Flora811/Student-Management-System
```
**Navigate into the project**
```bash
  cd student-management-system
```

**Build the project**
```bash
  mvn clean install
```
*In "application.properties" file, replace the placeholders with actual values (see Environment Variables section)*
- `DATASOURCE_URL`
- `DATASOURCE_USER`
- `DATASOURCE_PASSWORD`

*Run the application (Powershell, GitBash, MacOS, Linux)*
```bash
  ./mvnw spring-boot:run
```
*For windows Command Prompt use:*
```bash
  mvnw.cmd spring-boot:run
```

<details>
  <summary><strong><em>Login Credentials</em></strong></summary>

- **Username:** *admin*
- **Password:** *admin@123*

</details>

## 🔐 Environment Variables

This application uses the following properties for database configuration:

```properties id="v4y8zk"
spring.datasource.url=${DATASOURCE_URL}
spring.datasource.username=${DATASOURCE_USER}
spring.datasource.password=${DATASOURCE_PASSWORD}
```

You can configure these values in one of the following ways:
### Option 1: Define values in `application.properties`

Replace the placeholders with your local database configuration:

```properties id="8m6h2p"
spring.datasource.url=jdbc:mysql://localhost:3306/student_management?createDatabaseIfNotExist=true&serverTimezone=UTC
spring.datasource.username=your_username
spring.datasource.password=your_password
```

### Option 2: Use Environment Variables

Set the following environment variables in your system or IDE:

```env id="kz1d9r"
DATASOURCE_URL=jdbc:mysql://localhost:3306/student_management?createDatabaseIfNotExist=true&serverTimezone=UTC
DATASOURCE_USER=your_username
DATASOURCE_PASSWORD=your_password
```

> If using IntelliJ IDEA, configure these under **Run → Edit Configurations → Environment Variables**



## 🐳Deployment

This application is containerized using Docker and deployed on Render.

Run with Docker

```bash
  docker build -t student-management .
  
  docker run -p 8080:8080 student-management
```


## 🔮 Future improvements

- 👥 Role-based access (Admin, Student, Instructor)
- 🔑 JWT authentication
- 📊 GPA calculation & analytics
- 📅 Course capacity & scheduling logic
- 🧪 Unit & integration testing
- ⚡ Detailed & specific global exception handling
- 🌐 Convert the app to a REST API for multi-device support

## 👤 Author
<p align="center"><strong>✨✨✨ Flora Bhatt ✨✨✨ </strong></p>

<div align="center" style="margin-top: 40px;">
  <strong>🌟 Connect With Me:</strong><br><br>
  <a href="https://www.github.com/Flora811" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white" alt="GitHub"/>
</a>
&nbsp;&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/flora--bhatt" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://flora811.github.io/Portfolio-Website/" target="_blank">
  <img src="https://img.shields.io/badge/Portfolio-FF6B6B?logo=google-chrome&logoColor=white" alt="Portfolio"/>
</a>
</div>
