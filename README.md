# Task Manager API

A production-grade REST API for managing tasks, built with **Django**, **Django REST Framework**, **PostgreSQL**, and **Docker**.

## Features

- **Authentication**: JWT-based **Email** Registration & Login (Access + Refresh tokens).
- **Task Management**: Create, Read, Update, Delete (CRUD) tasks.
- **Permissions**: Users can only manage their own tasks; Admins can manage all.
- **Documentation**: Auto-generated Swagger UI & OpenAPI schema.
- **Dockerized**: One-command setup with Docker Compose.
- **Database**: PostgreSQL (v15).

## Tech Stack

- **Backend**: Python 3.11, Django 4.2, Django REST Framework
- **Database**: PostgreSQL
- **Auth**: SimpleJWT (Custom User Model)
- **Docs**: drf-spectacular (Swagger)
- **Infrastructure**: Docker & Docker Compose

## Quick Start

### Prerequisites
- Docker & Docker Compose installed.

### Run the Application

1. **Start Database**:
   ```bash
   docker compose up -d
   ```
   This runs PostgreSQL only.

2. **Setup Application & Run Local Server**:

   ```bash
   # Create Virtual Env
   python -m venv venv
   ```

   ```bash
   # Install dependencies (if not done)
   pip install -r requirements.txt

   # Start Server (Auto-migrates on startup)
   python manage.py runserver
   ```
   The application will be available at `http://localhost:8000`.

2. **Access API Documentation**:
   - **Swagger UI**: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
   - **ReDoc**: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

3. **Stop Services**:
   ```bash
   docker compose down
   ```

## Testing

Run the test suite using `pytest`:

```bash
pytest
```

## Project Structure

```
├── apps/               # Django Apps
│   ├── accounts/       # User Authentication
│   └── tasks/          # Task Management
├── config/             # Project Configuration
│   ├── settings/       # Split settings (base, dev, prod)
│   ├── urls.py         # Main URL routing
│   └── wsgi.py
├── docker-compose.yml  # Docker services config
├── Dockerfile          # Python image config
├── manage.py           # Django CLI
├── pytest.ini          # Test configuration
└── requirements.txt    # Python dependencies
```

## Environment Variables

The project uses `.env` file for configuration. Default values are provided for development in the included `.env`.

- `SECRET_KEY`: Django secret key.
- `DEBUG`: Boolean (True/False).
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: Database config.

---

**Production Note**: Ensure to change `SECRET_KEY` and passwords before deploying to production.
