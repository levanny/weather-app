A FastAPI-based weather application that fetches real-time weather data from an external API, stores it in PostgreSQL, and exposes it via REST endpoints.

---

## 🚀 Features
- FastAPI backend with async support
- PostgreSQL database (via SQLAlchemy & Alembic)
- Background scheduler to fetch weather every 15 minutes
- Dockerized for easy deployment
- Database migrations with Alembic
- Configurable city list via environment variables

---

## 🛠️ Setup

### Prerequisites
- Docker & Docker Compose
- Python 3.12+
- uv (dependency manager)

1. Clone the repository
```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app

2. Create .env file
POSTGRES_USER=postgres
POSTGRES_PASSWORD=FantasticFox
POSTGRES_DB=weather
POSTGRES_HOST=db
POSTGRES_PORT=5432

# List of cities (comma-separated)
CITIES=London,Paris,Tbilisi

3. Start services
docker-compose up -d

4. Run database migrations
docker-compose exec app alembic upgrade head

🌐 API Endpoints
Fetch & store weather
POST /weather/fetch → fetches weather for all cities and stores in DB
Example request: curl -X POST http://localhost:8000/weather/fetch


📦 Project Structure

app/
 ├── core/           # Configurations
 ├── db/             # Database models, migrations, session
 ├── services/       # Weather fetching logic
 ├── main.py         # FastAPI entrypoint
alembic/             # Migration files
docker-compose.yml
README.md





