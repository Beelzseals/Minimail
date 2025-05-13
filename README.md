# 📬 MailMini – Email Campaign API

A lightweight, scalable backend API for managing and sending email campaigns – inspired by Mailchimp, built with FastAPI, Celery, and PostgreSQL.

---

## 🚀 Features

- ✅ User authentication (JWT)
- 👥 Contact and audience list management
- 📨 Email campaign creation and scheduling
- ⏱ Background sending with Celery + Redis
- 🧩 Templated emails using Jinja2
- 📈 Open and click tracking with analytics
- 🚫 Unsubscribe handling
- 📊 Campaign statistics dashboard
- 📤 CSV/JSON export of campaign data

---

## 🛠️ Tech Stack

| Component     | Tech                           |
| ------------- | ------------------------------ |
| Backend API   | FastAPI                        |
| Database      | PostgreSQL                     |
| Task Queue    | Celery + Redis                 |
| Email Service | SendGrid / SMTP                |
| Auth          | JWT via OAuth2 (FastAPI)       |
| Tracking      | Custom image pixel + redirects |
| Templates     | Jinja2                         |

## ⚙️ Setup Instructions

### 1. Clone and Install

```bash
git clone https://github.com/yourusername/mailmini.git
cd mailmini
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Environment Variables
   Create a .env file:

```ini
DATABASE_URL=postgresql://user:password@localhost/mailmini
SECRET_KEY=your_jwt_secret
EMAIL_HOST=smtp.sendgrid.net
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your_sendgrid_key
EMAIL_FROM=you@example.com
REDIS_BROKER_URL=redis://localhost:6379/0
```

3. Database Setup

```bash
alembic upgrade head  # or use your preferred migration method
```

4. Run the Server

```bash
uvicorn app.main:app --reload
```

5. Start Celery Worker

```bash
celery -A app.services.scheduler worker --loglevel=info
🧪 API Endpoints (Sample)
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/login	Obtain JWT token
POST	/contacts/	Add a new contact
GET	/contacts/	List contacts
POST	/campaigns/	Create a new campaign
POST	/campaigns/send	Trigger/schedule send
GET	/campaigns/stats/	View open/click stats
```
