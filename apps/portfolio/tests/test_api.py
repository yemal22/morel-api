"""
API tests for portfolio endpoints.
"""

from django.urls import reverse

from rest_framework import status

import pytest


@pytest.mark.django_db
@pytest.mark.api
class TestUserProfileAPI:
    """Test UserProfile API endpoints."""

    def test_list_user_profiles(self, api_client, user_profile):
        """Test listing user profiles."""
        url = reverse("portfolio:profile-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) >= 1

    def test_retrieve_user_profile(self, api_client, user_profile):
        """Test retrieving a specific user profile."""
        url = reverse("portfolio:profile-detail", kwargs={"pk": user_profile.pk})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["first_name"] == "John"

    def test_create_user_profile_authenticated(self, authenticated_client):
        """Test creating a user profile when authenticated."""
        url = reverse("portfolio:profile-list")
        data = {"first_name": "Jane", "last_name": "Smith", "email": "jane@example.com", "bio": "Test bio"}
        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["first_name"] == "Jane"


@pytest.mark.django_db
@pytest.mark.api
class TestProjectAPI:
    """Test Project API endpoints."""

    def test_list_projects(self, api_client, project):
        """Test listing projects."""
        url = reverse("portfolio:project-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) >= 1

    def test_retrieve_project_by_slug(self, api_client, project):
        """Test retrieving a project by slug."""
        url = reverse("portfolio:project-detail", kwargs={"slug": project.slug})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Test Project"

    def test_create_project_authenticated(self, authenticated_client):
        """Test creating a project when authenticated."""
        url = reverse("portfolio:project-list")
        data = {
            "title": "New Project",
            "slug": "new-project",
            "description": "A new test project",
            "tags": "python, django",
            "technologies": "Django, PostgreSQL",
            "is_published": True,
        }
        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["title"] == "New Project"

    def test_featured_projects(self, api_client, project):
        """Test getting featured projects."""
        url = reverse("portfolio:project-featured")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1
        assert response.data[0]["is_featured"] is True

    def test_search_projects(self, api_client, project):
        """Test searching projects."""
        url = reverse("portfolio:project-list")
        response = api_client.get(url, {"search": "Test"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) >= 1

    def test_filter_published_projects(self, api_client, project):
        """Test filtering published projects."""
        url = reverse("portfolio:project-list")
        response = api_client.get(url, {"is_published": "true"})

        assert response.status_code == status.HTTP_200_OK
        for item in response.data["results"]:
            assert item["is_published"] is True


@pytest.mark.django_db
@pytest.mark.api
class TestExperienceAPI:
    """Test Experience API endpoints."""

    def test_list_experiences(self, api_client, experience):
        """Test listing experiences."""
        url = reverse("portfolio:experience-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) >= 1

    def test_current_experiences(self, api_client, experience):
        """Test getting current experiences."""
        url = reverse("portfolio:experience-current")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1
        assert response.data[0]["is_current"] is True


@pytest.mark.django_db
@pytest.mark.api
class TestEducationAPI:
    """Test Education API endpoints."""

    def test_list_education(self, api_client, education):
        """Test listing education records."""
        url = reverse("portfolio:education-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) >= 1

    def test_create_education_authenticated(self, authenticated_client):
        """Test creating an education record when authenticated."""
        url = reverse("portfolio:education-list")
        data = {
            "institution": "New University",
            "degree": "Bachelor",
            "field_of_study": "Engineering",
            "start_date": "2020-09-01",
            "end_date": "2024-06-30",
        }
        response = authenticated_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["institution"] == "New University"


@pytest.mark.django_db
@pytest.mark.api
class TestSkillAPI:
    """Test Skill API endpoints."""

    def test_list_skills(self, api_client, skill):
        """Test listing skills."""
        url = reverse("portfolio:skill-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) >= 1

    def test_featured_skills(self, api_client, skill):
        """Test getting featured skills."""
        url = reverse("portfolio:skill-featured")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1

    def test_skills_by_category(self, api_client, skill):
        """Test getting skills grouped by category."""
        url = reverse("portfolio:skill-by-category")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, dict)

    def test_filter_skills_by_category(self, api_client, skill):
        """Test filtering skills by category."""
        url = reverse("portfolio:skill-list")
        response = api_client.get(url, {"category": "programming"})

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
@pytest.mark.api
class TestBlogPostAPI:
    """Test BlogPost API endpoints."""

    def test_list_blog_posts(self, api_client, blog_post):
        """Test listing blog posts."""
        url = reverse("portfolio:blogpost-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) >= 1

    def test_retrieve_blog_post_by_slug(self, api_client, blog_post):
        """Test retrieving a blog post by slug."""
        url = reverse("portfolio:blogpost-detail", kwargs={"slug": blog_post.slug})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == "Test Blog Post"

    def test_featured_blog_posts(self, api_client, blog_post):
        """Test getting featured blog posts."""
        url = reverse("portfolio:blogpost-featured")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1

    def test_increment_views(self, api_client, blog_post):
        """Test incrementing views count."""
        initial_views = blog_post.views_count
        url = reverse("portfolio:blogpost-increment-views", kwargs={"slug": blog_post.slug})
        response = api_client.post(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["views_count"] == initial_views + 1

    def test_only_published_posts_for_anonymous(self, api_client, user):
        """Test that anonymous users only see published posts."""
        from apps.portfolio.models import BlogPost

        # Create a draft post
        BlogPost.objects.create(
            author=user, title="Draft Post", slug="draft-post", content="Draft content", status="draft"
        )

        url = reverse("portfolio:blogpost-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        slugs = [item["slug"] for item in response.data["results"]]
        assert "draft-post" not in slugs


@pytest.mark.django_db
@pytest.mark.integration
class TestHealthCheck:
    """Test health check endpoint."""

    def test_health_check(self, api_client):
        """Test health check endpoint."""
        response = api_client.get("/health/")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["status"] == "healthy"
        assert response.json()["database"] == "connected"
