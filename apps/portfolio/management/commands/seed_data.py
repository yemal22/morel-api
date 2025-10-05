"""
Management command to seed the database with sample data.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from datetime import date, datetime, timedelta
from apps.portfolio.models import (
    UserProfile,
    Project,
    Experience,
    Education,
    Skill,
    BlogPost,
)

User = get_user_model()


class Command(BaseCommand):
    help = "Seeds the database with sample portfolio data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing data before seeding",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            self.stdout.write("Clearing existing data...")
            UserProfile.objects.all().delete()
            Project.objects.all().delete()
            Experience.objects.all().delete()
            Education.objects.all().delete()
            Skill.objects.all().delete()
            BlogPost.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()
            self.stdout.write(self.style.SUCCESS("Data cleared!"))

        self.stdout.write("Creating sample data...")

        # Create sample user
        user, created = User.objects.get_or_create(
            username="demo_user", defaults={"email": "demo@example.com", "first_name": "Demo", "last_name": "User"}
        )
        if created:
            user.set_password("demo123")
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created user: {user.username}"))

        # Create user profile
        profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={
                "first_name": "John",
                "last_name": "Doe",
                "bio": "Passionate software developer with expertise in Python, Django, and modern web technologies. "
                "I love building scalable applications and solving complex problems.",
                "email": "john.doe@example.com",
                "phone": "+33 6 12 34 56 78",
                "location": "Paris, France",
                "linkedin_url": "https://linkedin.com/in/johndoe",
                "github_url": "https://github.com/johndoe",
                "twitter_url": "https://twitter.com/johndoe",
                "website_url": "https://johndoe.dev",
                "job_title": "Senior Full-Stack Developer",
                "company": "Tech Innovation Inc.",
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Created user profile"))

        # Create projects
        projects_data = [
            {
                "title": "E-Commerce Platform",
                "slug": "ecommerce-platform",
                "description": "A full-featured e-commerce platform built with Django and React. "
                "Features include product catalog, shopping cart, payment integration, and admin dashboard.",
                "short_description": "Full-featured e-commerce solution",
                "project_url": "https://example-ecommerce.com",
                "github_url": "https://github.com/johndoe/ecommerce",
                "tags": "ecommerce, django, react, stripe",
                "technologies": "Django, React, PostgreSQL, Redis, Stripe",
                "start_date": date(2023, 1, 1),
                "end_date": date(2023, 6, 30),
                "is_featured": True,
                "is_published": True,
                "order": 1,
            },
            {
                "title": "Task Management App",
                "slug": "task-management-app",
                "description": "A collaborative task management application with real-time updates, "
                "team collaboration features, and comprehensive analytics.",
                "short_description": "Collaborative task management tool",
                "project_url": "https://example-tasks.com",
                "github_url": "https://github.com/johndoe/taskmanager",
                "tags": "productivity, websockets, collaboration",
                "technologies": "Django, Vue.js, WebSockets, Celery",
                "start_date": date(2023, 7, 1),
                "is_featured": True,
                "is_published": True,
                "order": 2,
            },
            {
                "title": "Portfolio API",
                "slug": "portfolio-api",
                "description": "RESTful API for managing portfolio content with full CRUD operations, "
                "authentication, and comprehensive documentation.",
                "short_description": "Portfolio management REST API",
                "github_url": "https://github.com/johndoe/portfolio-api",
                "tags": "api, rest, drf, swagger",
                "technologies": "Django REST Framework, PostgreSQL, Docker",
                "start_date": date(2024, 1, 1),
                "is_featured": False,
                "is_published": True,
                "order": 3,
            },
        ]

        for proj_data in projects_data:
            project, created = Project.objects.get_or_create(user=user, slug=proj_data["slug"], defaults=proj_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created project: {project.title}"))

        # Create experiences
        experiences_data = [
            {
                "company": "Tech Innovation Inc.",
                "position": "Senior Full-Stack Developer",
                "location": "Paris, France",
                "description": "Leading development of cloud-based applications. Architecting scalable solutions "
                "and mentoring junior developers. Tech stack: Django, React, AWS.",
                "start_date": date(2021, 3, 1),
                "is_current": True,
                "company_url": "https://techinnovation.example",
                "technologies": "Python, Django, React, PostgreSQL, AWS, Docker",
                "order": 1,
            },
            {
                "company": "StartupXYZ",
                "position": "Full-Stack Developer",
                "location": "Lyon, France",
                "description": "Developed and maintained web applications for various clients. "
                "Implemented RESTful APIs and responsive front-end interfaces.",
                "start_date": date(2019, 1, 1),
                "end_date": date(2021, 2, 28),
                "is_current": False,
                "company_url": "https://startupxyz.example",
                "technologies": "Django, Vue.js, MySQL, Redis",
                "order": 2,
            },
            {
                "company": "WebDev Agency",
                "position": "Junior Developer",
                "location": "Marseille, France",
                "description": "Started career developing websites and small applications. "
                "Gained experience in full-stack web development.",
                "start_date": date(2017, 6, 1),
                "end_date": date(2018, 12, 31),
                "is_current": False,
                "technologies": "Python, Flask, JavaScript, Bootstrap",
                "order": 3,
            },
        ]

        for exp_data in experiences_data:
            experience, created = Experience.objects.get_or_create(
                user=user, company=exp_data["company"], position=exp_data["position"], defaults=exp_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created experience: {experience}"))

        # Create education
        education_data = [
            {
                "institution": "École Polytechnique",
                "degree": "Master of Science",
                "field_of_study": "Computer Science",
                "location": "Palaiseau, France",
                "description": "Specialized in software engineering and distributed systems. "
                "Thesis on microservices architecture.",
                "start_date": date(2015, 9, 1),
                "end_date": date(2017, 6, 30),
                "grade": "Distinction",
                "institution_url": "https://polytechnique.edu",
                "order": 1,
            },
            {
                "institution": "Université Paris-Saclay",
                "degree": "Bachelor of Science",
                "field_of_study": "Computer Science",
                "location": "Paris, France",
                "description": "Foundation in computer science fundamentals, algorithms, and data structures.",
                "start_date": date(2012, 9, 1),
                "end_date": date(2015, 6, 30),
                "grade": "First Class Honours",
                "institution_url": "https://paris-saclay.fr",
                "order": 2,
            },
        ]

        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                user=user, institution=edu_data["institution"], degree=edu_data["degree"], defaults=edu_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created education: {education}"))

        # Create skills
        skills_data = [
            {
                "name": "Python",
                "category": "programming",
                "proficiency": "expert",
                "level": 9,
                "description": "Expert in Python development",
                "years_of_experience": 7.0,
                "icon": "fab fa-python",
                "is_featured": True,
                "order": 1,
            },
            {
                "name": "Django",
                "category": "framework",
                "proficiency": "expert",
                "level": 9,
                "description": "Advanced Django development",
                "years_of_experience": 6.0,
                "icon": "fab fa-python",
                "is_featured": True,
                "order": 2,
            },
            {
                "name": "JavaScript",
                "category": "programming",
                "proficiency": "advanced",
                "level": 8,
                "description": "Proficient in modern JavaScript",
                "years_of_experience": 5.0,
                "icon": "fab fa-js",
                "is_featured": True,
                "order": 3,
            },
            {
                "name": "React",
                "category": "framework",
                "proficiency": "advanced",
                "level": 8,
                "description": "Building modern React applications",
                "years_of_experience": 4.0,
                "icon": "fab fa-react",
                "is_featured": True,
                "order": 4,
            },
            {
                "name": "PostgreSQL",
                "category": "database",
                "proficiency": "advanced",
                "level": 8,
                "description": "Database design and optimization",
                "years_of_experience": 6.0,
                "icon": "fas fa-database",
                "is_featured": True,
                "order": 5,
            },
            {
                "name": "Docker",
                "category": "tool",
                "proficiency": "advanced",
                "level": 8,
                "description": "Container orchestration and deployment",
                "years_of_experience": 5.0,
                "icon": "fab fa-docker",
                "is_featured": True,
                "order": 6,
            },
            {
                "name": "Git",
                "category": "tool",
                "proficiency": "expert",
                "level": 9,
                "description": "Version control and collaboration",
                "years_of_experience": 7.0,
                "icon": "fab fa-git",
                "is_featured": False,
                "order": 7,
            },
            {
                "name": "AWS",
                "category": "tool",
                "proficiency": "intermediate",
                "level": 7,
                "description": "Cloud infrastructure and services",
                "years_of_experience": 3.0,
                "icon": "fab fa-aws",
                "is_featured": False,
                "order": 8,
            },
            {
                "name": "English",
                "category": "language",
                "proficiency": "expert",
                "level": 9,
                "description": "Fluent in technical and business English",
                "years_of_experience": 10.0,
                "is_featured": False,
                "order": 9,
            },
            {
                "name": "French",
                "category": "language",
                "proficiency": "expert",
                "level": 10,
                "description": "Native speaker",
                "years_of_experience": 30.0,
                "is_featured": False,
                "order": 10,
            },
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(user=user, name=skill_data["name"], defaults=skill_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created skill: {skill.name}"))

        # Create blog posts
        blog_posts_data = [
            {
                "title": "Getting Started with Django REST Framework",
                "slug": "getting-started-with-drf",
                "excerpt": "Learn how to build powerful RESTful APIs with Django REST Framework",
                "content": """# Introduction to Django REST Framework

Django REST Framework (DRF) is a powerful toolkit for building Web APIs. In this article, we'll explore the basics of DRF and how to create a simple API.

## Why Django REST Framework?

- Powerful serialization
- Authentication and permissions
- Browsable API
- Extensive documentation

## Getting Started

First, install DRF:

```bash
pip install djangorestframework
```

Then add it to your INSTALLED_APPS...
""",
                "status": "published",
                "published_at": datetime.now() - timedelta(days=30),
                "tags": "django, drf, python, api",
                "read_time": 8,
                "is_featured": True,
                "meta_description": "Complete guide to getting started with Django REST Framework",
                "meta_keywords": "django, rest framework, api, python",
            },
            {
                "title": "Docker Best Practices for Python Applications",
                "slug": "docker-best-practices-python",
                "excerpt": "Essential Docker best practices for deploying Python applications",
                "content": """# Docker Best Practices for Python

Containerization is essential for modern application deployment. Here are some best practices for Dockerizing Python applications.

## Multi-stage Builds

Use multi-stage builds to keep your images small...

## Security Considerations

Always run as a non-root user...
""",
                "status": "published",
                "published_at": datetime.now() - timedelta(days=15),
                "tags": "docker, python, devops, deployment",
                "read_time": 10,
                "is_featured": True,
                "meta_description": "Learn Docker best practices for Python applications",
                "meta_keywords": "docker, python, containers, devops",
            },
            {
                "title": "Building Scalable APIs with Django",
                "slug": "building-scalable-apis-django",
                "excerpt": "Techniques for building scalable and performant APIs with Django",
                "content": """# Scaling Django APIs

As your API grows, you need to consider scalability. This article covers key techniques...

## Database Optimization

- Use select_related and prefetch_related
- Add proper indexes
- Use database connection pooling

## Caching Strategies

Redis and Memcached can dramatically improve performance...
""",
                "status": "published",
                "published_at": datetime.now() - timedelta(days=5),
                "tags": "django, scalability, performance, optimization",
                "read_time": 12,
                "is_featured": False,
                "meta_description": "Learn how to build scalable Django APIs",
                "meta_keywords": "django, api, scalability, performance",
            },
        ]

        for post_data in blog_posts_data:
            blog_post, created = BlogPost.objects.get_or_create(author=user, slug=post_data["slug"], defaults=post_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created blog post: {blog_post.title}"))

        self.stdout.write(self.style.SUCCESS("\n=== Database seeded successfully! ==="))
        self.stdout.write(self.style.SUCCESS("Demo user credentials:"))
        self.stdout.write(self.style.SUCCESS("  Username: demo_user"))
        self.stdout.write(self.style.SUCCESS("  Password: demo123"))
