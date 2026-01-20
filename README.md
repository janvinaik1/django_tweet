# Twitter Clone - Django Web Application

A modern, Twitter-style web application built with Django, featuring a dark theme UI and full CRUD functionality for tweets/posts.

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

## Tech Stack

- **Backend**: Django 5.1.3
- **Templates**: Django Templates (Jinja-style syntax)
- **Forms**: Django Forms & ModelForms
- **Styling**: Bootstrap 5 (dark theme)
- **Database**: SQLite (default, can be changed)
- **Icons**: Bootstrap Icons

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

## Future Enhancements (Optional)

- [ ] User profiles with bio and avatar
- [ ] Follow/unfollow users
- [ ] Like/favorite tweets
- [ ] Comment/reply functionality
- [ ] Hashtag support
- [ ] Search functionality
- [ ] Notifications
- [ ] Direct messaging
- [ ] Email verification
- [ ] Password reset
- [ ] Tweet analytics

## License

This project is for educational purposes.

## Author

Built with Django following best practices for clean, maintainable code.
