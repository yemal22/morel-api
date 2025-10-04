"""
Pytest configuration and fixtures.
"""
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.portfolio.models import (
    UserProfile,
    Project,
    Experience,
    Education,
    Skill,
    BlogPost,
)

User = get_user_model()


@pytest.fixture
def api_client():
    """Return an API client."""
    return APIClient()


@pytest.fixture
def user(db):
    """Create and return a test user."""
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )


@pytest.fixture
def authenticated_client(api_client, user):
    """Return an authenticated API client."""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def user_profile(user):
    """Create and return a user profile."""
    return UserProfile.objects.create(
        user=user,
        first_name='John',
        last_name='Doe',
        bio='Test bio',
        email='john@example.com',
        phone='+1234567890',
        location='Paris, France',
        linkedin_url='https://linkedin.com/in/johndoe',
        github_url='https://github.com/johndoe',
        job_title='Software Engineer',
        company='Tech Corp'
    )


@pytest.fixture
def project(user):
    """Create and return a project."""
    return Project.objects.create(
        user=user,
        title='Test Project',
        slug='test-project',
        description='This is a test project description.',
        short_description='Test project',
        project_url='https://example.com',
        github_url='https://github.com/test/project',
        tags='python, django, rest',
        technologies='Django, PostgreSQL, Docker',
        is_featured=True,
        is_published=True,
        order=1
    )


@pytest.fixture
def experience(user):
    """Create and return an experience."""
    from datetime import date
    return Experience.objects.create(
        user=user,
        company='Tech Corp',
        position='Software Engineer',
        location='Paris, France',
        description='Working on awesome projects',
        start_date=date(2020, 1, 1),
        is_current=True,
        company_url='https://techcorp.com',
        technologies='Python, Django, React',
        order=1
    )


@pytest.fixture
def education(user):
    """Create and return an education record."""
    from datetime import date
    return Education.objects.create(
        user=user,
        institution='University of Technology',
        degree='Master of Science',
        field_of_study='Computer Science',
        location='Paris, France',
        description='Studied advanced computer science topics',
        start_date=date(2015, 9, 1),
        end_date=date(2017, 6, 30),
        grade='Distinction',
        institution_url='https://university.edu',
        order=1
    )


@pytest.fixture
def skill(user):
    """Create and return a skill."""
    return Skill.objects.create(
        user=user,
        name='Python',
        category='programming',
        proficiency='expert',
        level=9,
        description='Expert in Python programming',
        years_of_experience=5.0,
        icon='fa-python',
        is_featured=True,
        order=1
    )


@pytest.fixture
def blog_post(user):
    """Create and return a blog post."""
    from datetime import datetime
    return BlogPost.objects.create(
        author=user,
        title='Test Blog Post',
        slug='test-blog-post',
        excerpt='This is a test excerpt',
        content='This is the full content of the test blog post.',
        status='published',
        published_at=datetime.now(),
        tags='testing, django, python',
        read_time=5,
        is_featured=True,
        meta_description='Test blog post for unit testing',
        meta_keywords='test, blog, django'
    )
