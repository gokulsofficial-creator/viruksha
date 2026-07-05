from django.db import models

class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=200, default="Viruksha Enterprises")
    tagline = models.CharField(max_length=300, blank=True)
    about_text = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    google_maps_embed = models.TextField(blank=True, help_text="Iframe HTML code for Google Maps")
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_to='company/', blank=True)
    hero_image = models.ImageField(upload_to='company/', blank=True)

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"

    def __str__(self):
        return self.company_name

class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)  # e.g., "150+"
    icon_class = models.CharField(max_length=100, help_text="Material Symbol icon name, e.g., domain")
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return f"{self.label}: {self.value}"

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('MATERIAL', 'Construction Material Supply'),
        ('CONSTRUCTION', 'Construction Services'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="Material Symbol icon name, e.g., build")
    image = models.ImageField(upload_to='services/', blank=True)
    is_featured = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.title

class Material(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100, help_text="e.g., Pipe Fittings, Fasteners")
    description = models.TextField()
    image = models.ImageField(upload_to='materials/', blank=True)
    is_featured = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name

class Product(models.Model):
    AVAILABILITY_CHOICES = [
        ('IN_STOCK', 'In Stock'),
        ('ON_REQUEST', 'On Request'),
        ('COMING_SOON', 'Coming Soon'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    sku = models.CharField(max_length=50, blank=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    specifications = models.TextField(blank=True, help_text="Enter specs as key-value pairs (e.g. Size: 50mm, Material: SS304), one per line.")
    thumbnail = models.ImageField(upload_to='products/', blank=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='IN_STOCK')
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', '-created_at']

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"Image for {self.product.name}"

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('RESIDENTIAL', 'Residential Construction'),
        ('COMMERCIAL', 'Commercial Construction'),
        ('INDUSTRIAL', 'Industrial Construction'),
        ('CIVIL', 'Civil Infrastructure'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    services_delivered = models.TextField(help_text="Services delivered, separated by comma or newlines.")
    thumbnail = models.ImageField(upload_to='projects/', blank=True)
    completion_date = models.DateField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort_order', '-completion_date', '-created_at']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length=200, blank=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"Image for {self.project.title}"

class Enquiry(models.Model):
    SERVICE_CHOICES = [
        ('MATERIAL', 'Construction Material Supply'),
        ('CONSTRUCTION', 'Construction Services'),
        ('PRODUCT', 'Product Enquiry'),
        ('BOTH', 'Both / General Enquiry'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200, blank=True)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='BOTH')
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"Enquiry from {self.name} - {self.subject}"






