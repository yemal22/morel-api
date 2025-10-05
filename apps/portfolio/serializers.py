"""
Serializers for portfolio app.
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    UserProfile,
    Project,
    Experience,
    Education,
    Skill,
    BlogPost,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class UserProfileSerializer(serializers.ModelSerializer):
    """User profile serializer."""
    full_name = serializers.ReadOnlyField()
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'full_name',
            'bio',
            'profile_photo',
            'email',
            'phone',
            'location',
            'linkedin_url',
            'github_url',
            'twitter_url',
            'website_url',
            'job_title',
            'company',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'full_name']


class UserProfileListSerializer(serializers.ModelSerializer):
    """Simplified user profile serializer for list views."""
    full_name = serializers.ReadOnlyField()
    
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'full_name',
            'bio',
            'profile_photo',
            'job_title',
            'company',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    """Project serializer."""
    tag_list = serializers.ReadOnlyField()
    technology_list = serializers.ReadOnlyField()
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'short_description',
            'image',
            'project_url',
            'github_url',
            'demo_url',
            'tags',
            'tag_list',
            'technologies',
            'technology_list',
            'start_date',
            'end_date',
            'is_featured',
            'is_published',
            'order',
            'user',
            'user_name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'tag_list', 'technology_list', 'user']

    def validate_slug(self, value):
        """Ensure slug is lowercase and valid."""
        return value.lower()


class ProjectListSerializer(serializers.ModelSerializer):
    """Simplified project serializer for list views."""
    tag_list = serializers.ReadOnlyField()
    technology_list = serializers.ReadOnlyField()
    
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'slug',
            'short_description',
            'image',
            'tag_list',
            'technology_list',
            'is_featured',
            'is_published',
            'start_date',
            'created_at',
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    """Experience serializer."""
    technology_list = serializers.ReadOnlyField()
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Experience
        fields = [
            'id',
            'company',
            'position',
            'location',
            'description',
            'start_date',
            'end_date',
            'is_current',
            'company_url',
            'technologies',
            'technology_list',
            'order',
            'user',
            'user_name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'technology_list']

    def validate(self, data):
        """Validate that end_date is after start_date if provided."""
        if data.get('end_date') and data.get('start_date'):
            if data['end_date'] < data['start_date']:
                raise serializers.ValidationError(
                    "End date must be after start date."
                )
        
        # If is_current is True, end_date should be None
        if data.get('is_current') and data.get('end_date'):
            raise serializers.ValidationError(
                "Current positions cannot have an end date."
            )
        
        return data


class EducationSerializer(serializers.ModelSerializer):
    """Education serializer."""
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Education
        fields = [
            'id',
            'institution',
            'degree',
            'field_of_study',
            'location',
            'description',
            'start_date',
            'end_date',
            'grade',
            'institution_url',
            'order',
            'user',
            'user_name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    def validate(self, data):
        """Validate that end_date is after start_date if provided."""
        if data.get('end_date') and data.get('start_date'):
            if data['end_date'] < data['start_date']:
                raise serializers.ValidationError(
                    "End date must be after start date."
                )
        return data


class SkillSerializer(serializers.ModelSerializer):
    """Skill serializer."""
    user_name = serializers.CharField(source='user.username', read_only=True)
    proficiency_display = serializers.CharField(source='get_proficiency_display', read_only=True)
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    class Meta:
        model = Skill
        fields = [
            'id',
            'name',
            'category',
            'category_display',
            'proficiency',
            'proficiency_display',
            'level',
            'description',
            'years_of_experience',
            'icon',
            'order',
            'is_featured',
            'user',
            'user_name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_level(self, value):
        """Ensure level is between 1 and 10."""
        if not 1 <= value <= 10:
            raise serializers.ValidationError("Level must be between 1 and 10.")
        return value


class SkillListSerializer(serializers.ModelSerializer):
    """Simplified skill serializer for list views."""
    proficiency_display = serializers.CharField(source='get_proficiency_display', read_only=True)
    
    class Meta:
        model = Skill
        fields = [
            'id',
            'name',
            'category',
            'proficiency',
            'proficiency_display',
            'level',
            'icon',
            'is_featured',
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    """Blog post serializer."""
    tag_list = serializers.ReadOnlyField()
    author_name = serializers.CharField(source='author.username', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'slug',
            'excerpt',
            'content',
            'featured_image',
            'status',
            'status_display',
            'published_at',
            'tags',
            'tag_list',
            'views_count',
            'read_time',
            'is_featured',
            'meta_description',
            'meta_keywords',
            'author',
            'author_name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'views_count', 'tag_list']

    def validate_slug(self, value):
        """Ensure slug is lowercase and valid."""
        return value.lower()


class BlogPostListSerializer(serializers.ModelSerializer):
    """Simplified blog post serializer for list views."""
    tag_list = serializers.ReadOnlyField()
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'slug',
            'excerpt',
            'featured_image',
            'status',
            'published_at',
            'tag_list',
            'views_count',
            'read_time',
            'is_featured',
            'author_name',
            'created_at',
        ]
