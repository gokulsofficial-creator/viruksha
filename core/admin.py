from django.contrib import admin
from .models import CompanyInfo, Statistic, ServiceCategory, Service, Material, ProductCategory, Product, ProductImage, Project, ProjectImage, Enquiry

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'icon_class', 'sort_order')
    list_editable = ('value', 'icon_class', 'sort_order')

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_order')
    list_editable = ('sort_order',)
    exclude = ('slug',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'sort_order', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'short_description')
    list_editable = ('is_featured', 'sort_order')
    exclude = ('slug',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'linked_product', 'is_featured', 'sort_order', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('name', 'category', 'description')
    list_editable = ('linked_product', 'is_featured', 'sort_order')
    exclude = ('slug',)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_order')
    list_editable = ('sort_order',)
    exclude = ('slug',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sku', 'availability', 'is_featured', 'is_active', 'sort_order')
    list_filter = ('category', 'availability', 'is_featured', 'is_active')
    search_fields = ('name', 'sku', 'short_description')
    list_editable = ('availability', 'is_featured', 'is_active', 'sort_order')
    inlines = [ProductImageInline]
    exclude = ('slug',)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'completion_date', 'is_featured', 'sort_order')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'location', 'client_name')
    list_editable = ('is_featured', 'sort_order')
    inlines = [ProjectImageInline]
    exclude = ('slug',)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service_type', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'service_type', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'company_name', 'service_type', 'subject', 'message', 'created_at')
    actions = ['mark_as_read']

    def has_add_permission(self, request):
        return False

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Selected enquiries have been marked as read.")
    mark_as_read.short_description = "Mark selected enquiries as read"

admin.site.site_header = "Viruksha Enterprises Admin"
admin.site.site_title = "Viruksha Admin Portal"
admin.site.index_title = "Welcome to Viruksha Management Control Panel"





