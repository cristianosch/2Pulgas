# 2Pulgas 🐾

**2Pulgas** is a full-featured blog application built with Django. The project was created for learning and personal development, and includes essential blog features along with third-party authentication.

## 🌟 Features

- User registration and login system
- Social login with Google, Facebook, and GitHub (via Django Allauth)
- Post creation and categorization
- Comment section (only available for registered users)
- Responsive and clean UI
- Admin panel for content management

## 🚀 Technologies Used

- Python
- Django
- Django Allauth
- PostgreSQL (or SQLite)
- Bootstrap or Tailwind CSS (depending on your implementation)

## 🔧 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/2Pulgas.git
   cd 2Pulgas
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the app**:
   Open your browser and go to `http://127.0.0.1:8000/`

## 🔑 Environment Variables

Make sure to set up the following in your `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=your_database_url
SOCIAL_AUTH_GOOGLE_CLIENT_ID=your_google_client_id
SOCIAL_AUTH_GOOGLE_SECRET=your_google_secret
SOCIAL_AUTH_FACEBOOK_KEY=your_facebook_key
SOCIAL_AUTH_FACEBOOK_SECRET=your_facebook_secret
SOCIAL_AUTH_GITHUB_KEY=your_github_key
SOCIAL_AUTH_GITHUB_SECRET=your_github_secret
```

## 📂 Folder Structure

```
2Pulgas/
├── blog/                 # Main blog application
├── users/                # User registration & social auth
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Made with ❤️ by Cristiano Schroeder