from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class TimeStampedModel(models.Model):
    """Abstract base model with created_at and updated_at fields."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(TimeStampedModel):
    """User profile with personal information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    # Social media links
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    
    # Professional info
    job_title = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Project(TimeStampedModel):
    """Portfolio project model."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    tags = models.CharField(max_length=500, help_text="Comma-separated tags")
    technologies = models.CharField(max_length=500, help_text="Comma-separated technologies")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    
    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-is_featured', 'order', '-start_date']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_published', '-created_at']),
        ]

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        """Return tags as a list."""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    @property
    def technology_list(self):
        """Return technologies as a list."""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class Experience(TimeStampedModel):
    """Professional experience model."""
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if current")
    is_current = models.BooleanField(default=False)
    company_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=500, blank=True, help_text="Comma-separated technologies")
    order = models.IntegerField(default=0)
    
    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['-is_current', '-start_date']
        indexes = [
            models.Index(fields=['-start_date']),
        ]

    def __str__(self):
        return f"{self.position} at {self.company}"

    @property
    def technology_list(self):
        """Return technologies as a list."""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class Education(TimeStampedModel):
    """Academic education model."""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=50, blank=True)
    institution_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"


class Skill(TimeStampedModel):
    """Skills and competencies model."""
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('framework', 'Framework'),
        ('database', 'Database'),
        ('tool', 'Tool'),
        ('language', 'Language'),
        ('soft_skill', 'Soft Skill'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate')
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=5,
        help_text="Skill level from 1 to 10"
    )
    description = models.TextField(blank=True)
    years_of_experience = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="Years of experience with this skill"
    )
    icon = models.CharField(max_length=100, blank=True, help_text="Icon class or URL")
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['-is_featured', 'category', 'order', 'name']
        unique_together = ['user', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"


class BlogPost(TimeStampedModel):
    """Blog post model."""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    excerpt = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateTimeField(null=True, blank=True)
    tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tags")
    views_count = models.IntegerField(default=0)
    read_time = models.IntegerField(default=5, help_text="Estimated read time in minutes")
    is_featured = models.BooleanField(default=False)
    
    # SEO fields
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    
    # Relationships
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status', '-published_at']),
        ]

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        """Return tags as a list."""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
