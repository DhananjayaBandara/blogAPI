# Blog API - Django REST Framework  

## Overview  
This project is a **Blog API** built using Django REST Framework (DRF) that supports **CRUD (Create, Read, Update, Delete) operations** for blog posts. It includes both **client** and **superuser** pages, ensuring different access levels for managing blog content. The API has been thoroughly tested using **Postman** to verify its functionality.  

## Features  
- **User Authentication:** Secure login and access control for superusers.  
- **Blog Management:** Create, read, update, and delete blog posts.  
- **Superuser Panel:** Admin privileges to manage all blog entries.  
- **Client View:** Users can access published blogs.  
- **RESTful API Endpoints:** Designed to interact smoothly with frontend applications.  
- **Tested with Postman:** Ensured API endpoints work as expected.  

## Technologies Used  
- **Django** - Web framework for Python  
- **Django REST Framework (DRF)** - API development  
- **SQLite/PostgreSQL** - Database for storing blogs  
- **Postman** - API testing  
- **GitHub** - Version control and repository hosting  

## Installation Guide  

### 1. Clone the Repository  
```bash
git clone https://github.com/DhananjayaBandara/blogAPI.git
cd blogAPI
```

### 2. Create and Activate a Virtual Environment  
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations  
```bash
python manage.py migrate
```

### 5. Create a Superuser (for admin access)  
```bash
python manage.py createsuperuser
```

### 6. Run the Server  
```bash
python manage.py runserver
```

## API Endpoints  

### Authentication  
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/token/` | Obtain access and refresh tokens |
| POST | `/api/token/refresh/` | Refresh access token |

### Blog Management  
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/blogs/` | Retrieve all blogs |
| POST | `/api/blogs/` | Create a new blog (Authenticated users) |
| GET | `/api/blogs/{id}/` | Retrieve a specific blog |
| PUT | `/api/blogs/{id}/` | Update an existing blog (Authenticated users) |
| DELETE | `/api/blogs/{id}/` | Delete a blog (Admin only) |

## Testing with Postman  
1. Open Postman and create a new request.  
2. Use the API endpoints above to interact with the blog system.  
3. Include authentication tokens where necessary for protected routes.  

## Future Enhancements  
- Implementing **JWT authentication** for better security.  
- Adding **comments and likes** functionality.  
- Frontend integration with **React/Vue.js** for better UI.  

## Contributions  
Feel free to contribute by forking this repository, making changes, and submitting a pull request!  

---
