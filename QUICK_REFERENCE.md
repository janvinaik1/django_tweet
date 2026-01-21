# Django Twitter Clone - Quick Reference Cheat Sheet

## 🎯 Project Elevator Pitch (30 seconds)
"I built a Twitter-like social media platform with Django featuring user authentication, tweet CRUD operations with image uploads, and deployed it to production on Render using PostgreSQL and Cloudinary for persistent storage. Implemented security best practices, query optimization, and pagination for better performance."

---

## 📊 Key Statistics
- **Lines of Code**: ~500
- **Models**: 1 (Tweet)
- **Views**: 7 (feed, create, edit, delete, login, register, logout)
- **Forms**: 2 (TweetForm, CustomUserCreationForm)
- **Deployment**: Render (Gunicorn + PostgreSQL + Cloudinary)

---

## 🏗️ Architecture Overview

```
User Request → Gunicorn → Django (WSGI) → View → Model → PostgreSQL
                                      ↓
                                  Template → Response
                                      ↓
                            Static: WhiteNoise
                            Media: Cloudinary
```

---

## 💾 Database Schema

```
User (Django built-in)
├── id (PK)
├── username
├── email
└── password (hashed)

Tweet
├── id (PK)
├── author_id (FK → User)
├── text (max 280 chars)
├── image (optional)
├── created_at
└── updated_at
```

**Relationship**: One User → Many Tweets (ForeignKey)

---

## 🔑 Key Code Snippets

### Model Definition
```python
class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text = models.TextField(max_length=280)
    image = models.ImageField(upload_to='tweet_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Newest first
```

### Optimized Query (N+1 Prevention)
```python
tweets = Tweet.objects.select_related('author').all()
# JOIN instead of separate queries for each author
```

### Authorization Check
```python
if tweet.author != request.user:
    return HttpResponseForbidden()
```

### Form Validation
```python
def clean_image(self):
    image = self.cleaned_data.get('image')
    if image and image.size > 5 * 1024 * 1024:  # 5MB
        raise forms.ValidationError('Image must be under 5MB')
    return image
```

### Pagination
```python
paginator = Paginator(tweets_list, 10)
page_number = request.GET.get('page')
tweets = paginator.get_page(page_number)
```

---

## 🛡️ Security Features Implemented

✅ CSRF Protection (`{% csrf_token %}`)
✅ Password Hashing (PBKDF2)
✅ Authorization Checks (own tweets only)
✅ File Upload Validation (type + size)
✅ SQL Injection Prevention (ORM)
✅ XSS Prevention (auto-escaping)
✅ HTTPS in Production
✅ Environment Variables (SECRET_KEY, DATABASE_URL)
✅ DEBUG=False in Production
✅ ALLOWED_HOSTS Restriction

---

## 🚀 Deployment Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Platform | Render | Cloud hosting |
| Web Server | Gunicorn | WSGI server |
| Database | PostgreSQL | Production DB |
| Media Storage | Cloudinary | Persistent file storage |
| Static Files | WhiteNoise | Serve CSS/JS |
| Version Control | Git/GitHub | Code management |

---

## 📝 Common Interview Questions - Quick Answers

**Q: What's the difference between `blank=True` and `null=True`?**
- `blank=True`: Form validation (can be empty)
- `null=True`: Database constraint (can be NULL)

**Q: Why `commit=False` in `form.save(commit=False)`?**
To modify the object before saving (e.g., set author)

**Q: What's N+1 query problem?**
Making N separate queries in a loop. Solved with `select_related()`

**Q: Why PostgreSQL instead of SQLite?**
SQLite = single file, no concurrency. PostgreSQL = production-ready, multi-user, ACID compliant

**Q: What's CSRF?**
Cross-Site Request Forgery. Django prevents with tokens in forms

**Q: `redirect()` vs `render()`?**
- `redirect()`: New HTTP request (POST → GET pattern)
- `render()`: Same request, return template

**Q: What's Gunicorn?**
Production WSGI server (runserver is dev-only)

**Q: Why Cloudinary?**
Render's filesystem is ephemeral (files deleted on redeploy)

**Q: What's `@login_required`?**
Decorator that redirects unauthenticated users to login

**Q: What's `related_name='tweets'`?**
Reverse lookup: `user.tweets.all()` instead of `user.tweet_set.all()`

---

## 🎓 Django Concepts Used

### Models & Database
- ForeignKey relationships
- on_delete behaviors
- Model Meta options
- auto_now vs auto_now_add
- FileExtensionValidator

### Views
- Function-based views (FBV)
- @login_required decorator
- get_object_or_404
- Form handling (POST/GET)
- Post-Redirect-Get pattern

### Forms
- ModelForm
- Custom validation (clean_image)
- Form widgets
- cleaned_data

### ORM
- select_related() (JOIN)
- filter(), all(), get()
- QuerySets (lazy evaluation)

### Templates
- Template inheritance (extends/block)
- Template tags ({% url %})
- Template variables ({{ }})
- CSRF token

### Authentication
- Django's User model
- login(), logout(), authenticate()
- Session management
- Password hashing

### Other
- Pagination
- Messages framework
- Static files (collectstatic)
- Media files
- Migrations

---

## 🔧 Terminal Commands You Should Know

```bash
# Development
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell

# Production
python manage.py collectstatic --no-input
gunicorn twitter_clone.wsgi
pip freeze > requirements.txt

# Git
git add .
git commit -m "message"
git push origin main
```

---

## 📦 Dependencies Explained

```
Django==5.2.10              # Web framework
Pillow==11.0.0              # Image processing
gunicorn==21.2.0            # WSGI server
whitenoise==6.6.0           # Static files
psycopg2-binary==2.9.9      # PostgreSQL adapter
dj-database-url==2.1.0      # Parse DATABASE_URL
cloudinary==1.41.0          # Cloud storage SDK
django-cloudinary-storage   # Django integration
```

---

## 🎯 What Makes Your Project Stand Out

1. **Production-Ready**: Not just localhost, actually deployed
2. **Best Practices**: Environment variables, proper security
3. **Performance**: Query optimization, pagination, caching headers
4. **Cloud Services**: Cloudinary for scalable media storage
5. **Complete CRUD**: Full create/read/update/delete functionality
6. **Authorization**: User-specific permissions
7. **Real Database**: PostgreSQL, not SQLite
8. **Professional Deployment**: Gunicorn, not runserver

---

## 💡 How to Answer "What challenges did you face?"

**Good answer:**
"One challenge was handling media files in production. Initially, images weren't showing because Render has an ephemeral filesystem - files get deleted on redeploy. I researched solutions and integrated Cloudinary for persistent cloud storage. This taught me about stateless deployments and cloud architecture.

Another challenge was the N+1 query problem. The feed was making hundreds of database queries. I profiled it, identified the issue, and used `select_related()` to reduce it to a single JOIN query, significantly improving performance."

---

## 🚀 How to Answer "How would you improve this?"

**Strong answer:**
"Several directions:

1. **Add REST API** with Django REST Framework for mobile apps
2. **Implement caching** with Redis for frequently accessed data
3. **Add real-time features** using Django Channels and WebSockets
4. **Social features**: likes, retweets, comments, follow system
5. **Search functionality** with full-text search
6. **Testing**: Unit tests, integration tests, coverage reports
7. **Monitoring**: Error tracking (Sentry), performance monitoring
8. **CI/CD**: Automated testing and deployment pipeline
9. **Rate limiting**: Prevent spam and abuse
10. **Email verification**: More secure user registration"

---

## 📈 Technical Growth Story

"This project taught me:
- How Django's ORM translates Python to SQL
- The importance of query optimization and database indexing
- Difference between development and production environments
- How to use environment variables for configuration
- Cloud architecture and stateless deployments
- Security considerations in web applications
- The value of proper error handling and user feedback"

---

## 🎤 Practice Questions to Drill

1. Explain your project in 60 seconds
2. Walk through the code for creating a tweet
3. How does authentication work?
4. What happens when a user clicks "Delete Tweet"?
5. How did you deploy to production?
6. What security measures did you implement?
7. How would you add a "like" feature?
8. Explain the database schema
9. What's the difference between your dev and prod setup?
10. How do you prevent unauthorized users from editing tweets?

---

## 🔗 Your Project URLs

- **Live Site**: https://tweet-django-laer.onrender.com
- **GitHub**: [Your repo URL]
- **Code Walkthrough**: Prepared to share screen and walk through:
  - [tweets/models.py](tweets/models.py) - Data models
  - [tweets/views.py](tweets/views.py) - Business logic
  - [tweets/forms.py](tweets/forms.py) - Form validation
  - [twitter_clone/settings.py](twitter_clone/settings.py) - Configuration

---

## ⏰ Last Minute Prep (5 minutes before interview)

1. ✅ Run through elevator pitch
2. ✅ Review security features
3. ✅ Know your deployment stack
4. ✅ Remember: select_related() for N+1 problem
5. ✅ Know the difference between authentication and authorization
6. ✅ Breathe! You built a real production app 🚀

---

**Remember**: You didn't just follow a tutorial. You:
- Deployed to production
- Handled real-world challenges (media storage, database choice)
- Implemented security best practices
- Optimized for performance

This is **production experience**, not just a classroom project! 💪
