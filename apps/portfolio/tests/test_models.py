"""
Unit tests for portfolio models.
"""
import pytest
from django.contrib.auth import get_user_model
from datetime import date
from apps.portfolio.models import (
    UserProfile,
    Project,
    Experience,
    Education,
    Skill,
    BlogPost,
)

User = get_user_model()


@pytest.mark.django_db
@pytest.mark.unit
class TestUserProfile:
    """Test UserProfile model."""

    def test_create_user_profile(self, user):
        """Test creating a user profile."""
        profile = UserProfile.objects.create(
            user=user,
            first_name='Jane',
            last_name='Smith',
            bio='Test bio',
            email='jane@example.com'
        )
        assert profile.first_name == 'Jane'
        assert profile.last_name == 'Smith'
        assert profile.full_name == 'Jane Smith'
        assert str(profile) == 'Jane Smith'

    def test_user_profile_full_name(self, user_profile):
        """Test full_name property."""
        assert user_profile.full_name == 'John Doe'


@pytest.mark.django_db
@pytest.mark.unit
class TestProject:
    """Test Project model."""

    def test_create_project(self, user):
        """Test creating a project."""
        project = Project.objects.create(
            user=user,
            title='New Project',
            slug='new-project',
            description='Description',
            tags='tag1, tag2, tag3',
            technologies='tech1, tech2'
        )
        assert project.title == 'New Project'
        assert project.slug == 'new-project'
        assert str(project) == 'New Project'

    def test_project_tag_list(self, project):
        """Test tag_list property."""
        assert project.tag_list == ['python', 'django', 'rest']

    def test_project_technology_list(self, project):
        """Test technology_list property."""
        assert project.technology_list == ['Django', 'PostgreSQL', 'Docker']

    def test_project_ordering(self, user):
        """Test project ordering."""
        project1 = Project.objects.create(
            user=user,
            title='Project 1',
            slug='project-1',
            description='Desc',
            tags='tag1',
            technologies='tech1',
            is_featured=False,
            order=2
        )
        project2 = Project.objects.create(
            user=user,
            title='Project 2',
            slug='project-2',
            description='Desc',
            tags='tag1',
            technologies='tech1',
            is_featured=True,
            order=1
        )
        projects = list(Project.objects.all())
        assert projects[0] == project2  # Featured first
        assert projects[1] == project1


@pytest.mark.django_db
@pytest.mark.unit
class TestExperience:
    """Test Experience model."""

    def test_create_experience(self, user):
        """Test creating an experience."""
        exp = Experience.objects.create(
            user=user,
            company='Company',
            position='Developer',
            description='Description',
            start_date=date(2020, 1, 1),
            is_current=True,
            technologies='Python, Django'
        )
        assert exp.company == 'Company'
        assert exp.position == 'Developer'
        assert str(exp) == 'Developer at Company'

    def test_experience_technology_list(self, experience):
        """Test technology_list property."""
        assert experience.technology_list == ['Python', 'Django', 'React']


@pytest.mark.django_db
@pytest.mark.unit
class TestEducation:
    """Test Education model."""

    def test_create_education(self, user):
        """Test creating an education record."""
        edu = Education.objects.create(
            user=user,
            institution='University',
            degree='Bachelor',
            field_of_study='CS',
            start_date=date(2015, 9, 1),
            end_date=date(2019, 6, 30)
        )
        assert edu.institution == 'University'
        assert edu.degree == 'Bachelor'
        assert 'Bachelor in CS from University' in str(edu)


@pytest.mark.django_db
@pytest.mark.unit
class TestSkill:
    """Test Skill model."""

    def test_create_skill(self, user):
        """Test creating a skill."""
        skill = Skill.objects.create(
            user=user,
            name='JavaScript',
            category='programming',
            proficiency='advanced',
            level=8
        )
        assert skill.name == 'JavaScript'
        assert skill.category == 'programming'
        assert skill.level == 8
        assert 'JavaScript' in str(skill)

    def test_skill_unique_constraint(self, user, skill):
        """Test that user cannot have duplicate skill names."""
        with pytest.raises(Exception):
            Skill.objects.create(
                user=user,
                name='Python',  # Same as fixture
                category='programming',
                proficiency='expert',
                level=9
            )


@pytest.mark.django_db
@pytest.mark.unit
class TestBlogPost:
    """Test BlogPost model."""

    def test_create_blog_post(self, user):
        """Test creating a blog post."""
        post = BlogPost.objects.create(
            author=user,
            title='Test Post',
            slug='test-post',
            content='Content here',
            status='draft',
            tags='tag1, tag2'
        )
        assert post.title == 'Test Post'
        assert post.slug == 'test-post'
        assert str(post) == 'Test Post'

    def test_blog_post_tag_list(self, blog_post):
        """Test tag_list property."""
        assert blog_post.tag_list == ['testing', 'django', 'python']

    def test_blog_post_views_default(self, blog_post):
        """Test default views count."""
        assert blog_post.views_count == 0
