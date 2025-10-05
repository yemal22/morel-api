"""
Views for portfolio app.
"""

from django.db import connection
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import (
    BlogPost,
    Education,
    Experience,
    Project,
    Skill,
    UserProfile,
)
from .serializers import (
    BlogPostListSerializer,
    BlogPostSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProjectListSerializer,
    ProjectSerializer,
    SkillListSerializer,
    SkillSerializer,
    UserProfileListSerializer,
    UserProfileSerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for UserProfile.

    list: Get all user profiles
    retrieve: Get a specific user profile
    create: Create a new user profile
    update: Update a user profile
    destroy: Delete a user profile
    """

    queryset = UserProfile.objects.select_related("user").all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["is_active", "job_title"]
    search_fields = ["first_name", "last_name", "bio", "job_title", "company"]
    ordering_fields = ["created_at", "first_name", "last_name"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserProfileListSerializer
        return UserProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Project.

    list: Get all projects
    retrieve: Get a specific project
    create: Create a new project
    update: Update a project
    destroy: Delete a project
    featured: Get featured projects
    """

    queryset = Project.objects.select_related("user").all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["is_featured", "is_published", "user"]
    search_fields = ["title", "description", "tags", "technologies"]
    ordering_fields = ["created_at", "start_date", "order", "title"]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        return ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Only show published projects to non-authenticated users
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_published=True)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def featured(self, request):
        """Get featured projects."""
        featured_projects = self.get_queryset().filter(is_featured=True, is_published=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Experience.

    list: Get all experiences
    retrieve: Get a specific experience
    create: Create a new experience
    update: Update an experience
    destroy: Delete an experience
    current: Get current experiences
    """

    queryset = Experience.objects.select_related("user").all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["is_current", "company", "user"]
    search_fields = ["company", "position", "description", "technologies"]
    ordering_fields = ["start_date", "end_date", "order"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def current(self, request):
        """Get current experiences."""
        current_experiences = self.get_queryset().filter(is_current=True)
        serializer = self.get_serializer(current_experiences, many=True)
        return Response(serializer.data)


class EducationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Education.

    list: Get all education records
    retrieve: Get a specific education record
    create: Create a new education record
    update: Update an education record
    destroy: Delete an education record
    """

    queryset = Education.objects.select_related("user").all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["institution", "degree", "user"]
    search_fields = ["institution", "degree", "field_of_study", "description"]
    ordering_fields = ["start_date", "end_date", "order"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SkillViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Skill.

    list: Get all skills
    retrieve: Get a specific skill
    create: Create a new skill
    update: Update a skill
    destroy: Delete a skill
    featured: Get featured skills
    by_category: Get skills by category
    """

    queryset = Skill.objects.select_related("user").all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["category", "proficiency", "is_featured", "user"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "level", "order", "years_of_experience"]

    def get_serializer_class(self):
        if self.action == "list":
            return SkillListSerializer
        return SkillSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def featured(self, request):
        """Get featured skills."""
        featured_skills = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(featured_skills, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def by_category(self, request):
        """Get skills grouped by category."""
        categories = {}
        for skill in self.get_queryset():
            category = skill.get_category_display()
            if category not in categories:
                categories[category] = []
            categories[category].append(SkillListSerializer(skill).data)
        return Response(categories)


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for BlogPost.

    list: Get all blog posts
    retrieve: Get a specific blog post
    create: Create a new blog post
    update: Update a blog post
    destroy: Delete a blog post
    featured: Get featured blog posts
    increment_views: Increment views count
    """

    queryset = BlogPost.objects.select_related("author").all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["status", "is_featured", "author"]
    search_fields = ["title", "excerpt", "content", "tags"]
    ordering_fields = ["created_at", "published_at", "views_count", "title"]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return BlogPostListSerializer
        return BlogPostSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Only show published posts to non-authenticated users
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(status="published")
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=["get"])
    def featured(self, request):
        """Get featured blog posts."""
        featured_posts = self.get_queryset().filter(is_featured=True, status="published")
        serializer = self.get_serializer(featured_posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], permission_classes=[AllowAny])
    def increment_views(self, request, slug=None):
        """Increment the views count for a blog post."""
        post = self.get_object()
        post.views_count += 1
        post.save(update_fields=["views_count"])
        return Response({"views_count": post.views_count})


def health_check(request):
    """
    Health check endpoint for monitoring.
    Returns the status of the application and database.
    """
    health_status = {"status": "healthy", "database": "disconnected", "details": {}}

    # Check database connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            health_status["database"] = "connected"
    except Exception as e:
        health_status["status"] = "unhealthy"
        health_status["database"] = "error"
        health_status["details"]["database_error"] = str(e)

    # Add more checks as needed
    health_status["details"]["version"] = "1.0.0"

    status_code = 200 if health_status["status"] == "healthy" else 503
    return JsonResponse(health_status, status=status_code)
