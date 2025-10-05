"""
Unit tests for portfolio serializers.
"""

import pytest

from apps.portfolio.serializers import (
    BlogPostSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    SkillSerializer,
    UserProfileSerializer,
)


@pytest.mark.django_db
@pytest.mark.unit
class TestUserProfileSerializer:
    """Test UserProfileSerializer."""

    def test_user_profile_serialization(self, user_profile):
        """Test serializing a user profile."""
        serializer = UserProfileSerializer(user_profile)
        data = serializer.data

        assert data["first_name"] == "John"
        assert data["last_name"] == "Doe"
        assert data["full_name"] == "John Doe"
        assert data["email"] == "john@example.com"
        assert data["job_title"] == "Software Engineer"


@pytest.mark.django_db
@pytest.mark.unit
class TestProjectSerializer:
    """Test ProjectSerializer."""

    def test_project_serialization(self, project):
        """Test serializing a project."""
        serializer = ProjectSerializer(project)
        data = serializer.data

        assert data["title"] == "Test Project"
        assert data["slug"] == "test-project"
        assert data["is_featured"] is True
        assert data["tag_list"] == ["python", "django", "rest"]
        assert data["technology_list"] == ["Django", "PostgreSQL", "Docker"]

    def test_project_deserialization(self, user):
        """Test deserializing a project."""
        data = {
            "user": user.id,
            "title": "New Project",
            "slug": "NEW-PROJECT",  # Test slug validation
            "description": "Description",
            "tags": "tag1, tag2",
            "technologies": "tech1, tech2",
            "is_published": True,
        }
        serializer = ProjectSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data["slug"] == "new-project"  # Should be lowercase


@pytest.mark.django_db
@pytest.mark.unit
class TestExperienceSerializer:
    """Test ExperienceSerializer."""

    def test_experience_serialization(self, experience):
        """Test serializing an experience."""
        serializer = ExperienceSerializer(experience)
        data = serializer.data

        assert data["company"] == "Tech Corp"
        assert data["position"] == "Software Engineer"
        assert data["is_current"] is True
        assert data["technology_list"] == ["Python", "Django", "React"]

    def test_experience_validation_dates(self, user):
        """Test experience date validation."""
        data = {
            "user": user.id,
            "company": "Company",
            "position": "Position",
            "description": "Description",
            "start_date": "2020-01-01",
            "end_date": "2019-01-01",  # Before start_date
        }
        serializer = ExperienceSerializer(data=data)
        assert not serializer.is_valid()
        assert "non_field_errors" in serializer.errors

    def test_experience_current_with_end_date(self, user):
        """Test validation: current position cannot have end_date."""
        data = {
            "user": user.id,
            "company": "Company",
            "position": "Position",
            "description": "Description",
            "start_date": "2020-01-01",
            "end_date": "2021-01-01",
            "is_current": True,  # Contradiction
        }
        serializer = ExperienceSerializer(data=data)
        assert not serializer.is_valid()


@pytest.mark.django_db
@pytest.mark.unit
class TestEducationSerializer:
    """Test EducationSerializer."""

    def test_education_serialization(self, education):
        """Test serializing an education record."""
        serializer = EducationSerializer(education)
        data = serializer.data

        assert data["institution"] == "University of Technology"
        assert data["degree"] == "Master of Science"
        assert data["field_of_study"] == "Computer Science"

    def test_education_validation_dates(self, user):
        """Test education date validation."""
        data = {
            "user": user.id,
            "institution": "University",
            "degree": "Master",
            "field_of_study": "CS",
            "start_date": "2020-01-01",
            "end_date": "2019-01-01",  # Before start_date
        }
        serializer = EducationSerializer(data=data)
        assert not serializer.is_valid()


@pytest.mark.django_db
@pytest.mark.unit
class TestSkillSerializer:
    """Test SkillSerializer."""

    def test_skill_serialization(self, skill):
        """Test serializing a skill."""
        serializer = SkillSerializer(skill)
        data = serializer.data

        assert data["name"] == "Python"
        assert data["category"] == "programming"
        assert data["proficiency"] == "expert"
        assert data["level"] == 9
        assert data["is_featured"] is True

    def test_skill_level_validation(self, user):
        """Test skill level validation."""
        # Invalid level (too high)
        data = {
            "user": user.id,
            "name": "JavaScript",
            "category": "programming",
            "proficiency": "expert",
            "level": 11,  # Invalid
        }
        serializer = SkillSerializer(data=data)
        assert not serializer.is_valid()
        assert "level" in serializer.errors


@pytest.mark.django_db
@pytest.mark.unit
class TestBlogPostSerializer:
    """Test BlogPostSerializer."""

    def test_blog_post_serialization(self, blog_post):
        """Test serializing a blog post."""
        serializer = BlogPostSerializer(blog_post)
        data = serializer.data

        assert data["title"] == "Test Blog Post"
        assert data["slug"] == "test-blog-post"
        assert data["status"] == "published"
        assert data["tag_list"] == ["testing", "django", "python"]

    def test_blog_post_slug_validation(self, user):
        """Test blog post slug validation."""
        data = {
            "author": user.id,
            "title": "Test Post",
            "slug": "TEST-POST",  # Should be lowercase
            "content": "Content",
            "status": "draft",
        }
        serializer = BlogPostSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data["slug"] == "test-post"
