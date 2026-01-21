# Tweet It - Django Twitter Clone

A full-stack Twitter-like social media application built with Django, deployed to production with PostgreSQL and cloud storage.

**🚀 Live Demo**: [https://tweet-django-laer.onrender.com](https://tweet-django-laer.onrender.com)

[![Django](https://img.shields.io/badge/Django-5.2.10-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)](https://www.postgresql.org/)
[![Cloudinary](https://img.shields.io/badge/Cloudinary-Media-blue.svg)](https://cloudinary.com/)

## 🎯 Project Highlights

- ✅ **Production Deployed** on Render with Gunicorn and PostgreSQL
- ✅ **Cloud Storage** integration with Cloudinary for persistent media files
- ✅ **Security Best Practices**: CSRF protection, authorization checks, input validation
- ✅ **Performance Optimized**: Query optimization, pagination, static file compression
- ✅ **Modern Tech Stack**: Django 5.2, Bootstrap 5, WhiteNoise, PostgreSQL

---

## Features

### Core Functionality
- User authentication (register, login, logout)
- Create, read, update, and delete tweets
- Image upload support for tweets
- Paginated tweet feed (10 tweets per page)
- Auto-login after registration

### Security & Authorization
- CSRF protection on all forms
- Login required for creating, editing, and deleting tweets
- Users can only edit/delete their own tweets
- Django's built-in authentication system

### UI/UX
- Modern dark theme using Bootstrap 5
- Twitter-like card-based design
- Responsive navbar with conditional links
- Real-time character counter (280 char limit)
- Image preview in admin panel
- Flash messages for user feedback

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 5.2.10
- **Web Server**: Gunicorn (production)
- **Database**: PostgreSQL (production), SQLite (development)
- **ORM**: Django ORM with query optimization
- **Authentication**: Django built-in authentication system

### Frontend
- **Templates**: Django Template Language (DTL)
- **Styling**: Bootstrap 5 (dark theme)
- **Icons**: Bootstrap Icons
- **JavaScript**: Vanilla JS (character counter)

### Infrastructure & Services
- **Hosting**: Render
- **Media Storage**: Cloudinary (cloud-based, persistent)
- **Static Files**: WhiteNoise (compression & caching)
- **Version Control**: Git & GitHub

### Key Python Packages
```
Django==5.2.10
Pillow==11.0.0
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
dj-database-url==2.1.0
cloudinary==1.41.0
django-cloudinary-storage==0.3.0
```

## Project Structure

```
django_project/
├── manage.py
├── twitter_clone/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tweets/                 # Main app
│   ├── models.py          # Tweet model
│   ├── forms.py           # TweetForm, CustomUserCreationForm
│   ├── views.py           # All function-based views
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Admin configuration
│   └── templates/tweets/
│       ├── base.html
│       ├── feed.html
│       ├── create_tweet.html
│       ├── edit_tweet.html
│       ├── delete_tweet.html
│       ├── login.html
│       └── register.html
├── media/                  # User-uploaded images
└── static/                 # Static files
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Pillow (for image handling)

### Step 1: Install Dependencies

```bash
# Install Django (if not already installed)
pip install django

# Install Pillow for image handling
pip install Pillow
```

### Step 2: Create Database & Apply Migrations

```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Admin Superuser

```bash
# Create an admin account to access /admin
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email (optional)
- Password

### Step 4: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## Usage Guide

### For Regular Users

1. **Register an Account**
   - Visit `/register` or click "Register" in the navbar
   - Fill in username, email, and password
   - You'll be automatically logged in after registration

2. **Login**
   - Visit `/login` or click "Login" in the navbar
   - Enter your credentials

3. **Create a Tweet**
   - Click "Create Tweet" in the navbar (only visible when logged in)
   - Enter tweet text (max 280 characters)
   - Optionally upload an image (JPG, PNG, GIF - max 5MB)
   - Click "Post Tweet"

4. **Edit Your Tweet**
   - Click the edit icon (pencil) on your own tweets
   - Modify the text or image
   - Click "Update Tweet"

5. **Delete Your Tweet**
   - Click the delete icon (trash) on your own tweets
   - Confirm deletion

6. **View Feed**
   - Homepage shows all tweets from all users
   - Tweets are ordered by most recent first
   - Navigate through pages using pagination

### For Administrators

Access the admin panel at: **http://127.0.0.1:8000/admin**

Admin features:
- View all tweets with filters and search
- Edit or delete any tweet
- View user accounts
- See image previews
- Filter by date, author

## Key Files Explained

### Models ([tweets/models.py](tweets/models.py))
- `Tweet` model with fields: author, text, image, created_at, updated_at
- Includes file validation for image uploads
- Ordered by creation date (newest first)

### Forms ([tweets/forms.py](tweets/forms.py))
- `TweetForm`: ModelForm for creating/editing tweets
- `CustomUserCreationForm`: Enhanced registration form with email
- Includes image size validation (max 5MB)

### Views ([tweets/views.py](tweets/views.py))
All function-based views with proper authentication:
- `feed()`: Display paginated tweets
- `create_tweet()`: Create new tweet (login required)
- `edit_tweet()`: Edit tweet (author only)
- `delete_tweet()`: Delete tweet (author only)
- `user_login()`: Handle user login
- `user_register()`: Handle registration with auto-login
- `user_logout()`: Handle logout

### Templates
- **base.html**: Base template with navbar, Bootstrap, and dark theme
- **feed.html**: Display tweets with pagination and conditional buttons
- **create_tweet.html**: Form to create new tweet with character counter
- **edit_tweet.html**: Form to edit existing tweet
- **delete_tweet.html**: Confirmation page for deletion
- **login.html**: Login form
- **register.html**: Registration form with password requirements

## Security Features

1. **CSRF Protection**: All forms include `{% csrf_token %}`
2. **Authentication**: `@login_required` decorator on protected views
3. **Authorization**: Permission checks ensure users can only edit/delete their own tweets
4. **File Validation**:
   - Allowed extensions: JPG, JPEG, PNG, GIF
   - Max file size: 5MB
   - Proper error handling
5. **Password Requirements**: Django's built-in password validators

## Access Control Rules

| Action | Authenticated User | Unauthenticated User |
|--------|-------------------|---------------------|
| View tweets | ✅ Yes | ✅ Yes |
| Create tweet | ✅ Yes | ❌ No |
| Edit own tweet | ✅ Yes | ❌ No |
| Edit other's tweet | ❌ No | ❌ No |
| Delete own tweet | ✅ Yes | ❌ No |
| Delete other's tweet | ❌ No | ❌ No |

## Customization

### Change Theme Colors
Edit the CSS variables in [tweets/templates/tweets/base.html](tweets/templates/tweets/base.html:14-17):
```css
:root {
    --twitter-blue: #1da1f2;
    --twitter-dark: #15202b;
    --twitter-darker: #0f1419;
}
```

### Change Pagination
Edit [tweets/views.py](tweets/views.py:15):
```python
paginator = Paginator(tweets_list, 10)  # Change 10 to desired number
```

### Change Tweet Character Limit
Edit [tweets/models.py](tweets/models.py:9):
```python
text = models.TextField(max_length=280)  # Change 280 to desired limit
```

## Common Commands

```bash
# Run development server
python manage.py runserver

# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic

# Run tests (if you add them)
python manage.py test
```

## Troubleshooting

### Issue: Images not displaying
**Solution**: Ensure you're running the development server and that `MEDIA_URL` and `MEDIA_ROOT` are configured in [twitter_clone/settings.py](twitter_clone/settings.py:122-124)

### Issue: "Pillow not installed" error
**Solution**: Install Pillow:
```bash
pip install Pillow
```

### Issue: Static files not loading
**Solution**: Run:
```bash
python manage.py collectstatic
```

### Issue: Permission denied when editing/deleting
**Solution**: Ensure you're logged in and trying to edit/delete your own tweets

## 📊 Technical Achievements

### Database Optimization
- Implemented `select_related()` to prevent N+1 query problems
- Reduced feed query from O(n) to O(1) database calls
- Database connection pooling with `conn_max_age=600`

### Security Implementation
- CSRF protection on all forms
- Authorization middleware (users can only edit/delete own tweets)
- File upload validation (type, size, extension)
- Environment-based configuration (SECRET_KEY, DEBUG, DATABASE_URL)
- Password hashing with PBKDF2

### Production Deployment
- Configured for production with Gunicorn WSGI server
- PostgreSQL database with automated migrations
- Cloudinary integration for persistent media storage (ephemeral filesystem workaround)
- WhiteNoise for efficient static file serving with compression
- Environment variable management for secure configuration

### Code Quality
- Clean separation of concerns (Models, Views, Forms)
- DRY principle with template inheritance
- Proper error handling with messages framework
- Input validation at both form and model level

## 📈 Learning Outcomes

This project demonstrates proficiency in:
- Full-stack web development with Django
- RESTful CRUD operations
- User authentication and authorization
- Database design and ORM usage
- Cloud deployment and DevOps basics
- Third-party API integration (Cloudinary)
- Production best practices and security

## 🚀 Future Enhancements

Potential features to add:
- [ ] REST API with Django REST Framework
- [ ] Real-time updates with Django Channels and WebSockets
- [ ] User profiles with bio and avatars
- [ ] Social features: likes, retweets, comments
- [ ] Follow/unfollow system
- [ ] Hashtag support and trending topics
- [ ] Full-text search functionality
- [ ] Email verification and password reset
- [ ] Rate limiting and spam protection
- [ ] Unit and integration tests
- [ ] CI/CD pipeline

## 📖 Documentation

- **[Interview Preparation Guide](INTERVIEW_PREP.md)**: Comprehensive Q&A for technical interviews
- **[Quick Reference](QUICK_REFERENCE.md)**: Cheat sheet for key concepts and code snippets

## 🤝 Contributing

This is a portfolio project, but suggestions and feedback are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is for educational and portfolio purposes.

## 👤 Author

**Janvi**

Built with Django following industry best practices and deployed to production. This project showcases full-stack development skills, from database design to cloud deployment.

---

**Note for Recruiters**: This is a fully functional, production-deployed application. Live demo available at [tweet-django-laer.onrender.com](https://tweet-django-laer.onrender.com). See [INTERVIEW_PREP.md](INTERVIEW_PREP.md) for detailed technical documentation.
