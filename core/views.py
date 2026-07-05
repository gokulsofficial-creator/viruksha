from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import CompanyInfo, Statistic, Service, Material, ProductCategory, Product, Project
from .forms import EnquiryForm

def home(request):
    company_info = CompanyInfo.objects.first()
    statistics = Statistic.objects.all()
    featured_services = Service.objects.filter(is_featured=True)[:6]
    featured_materials = Material.objects.filter(is_featured=True)[:8]
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:4]
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    context = {
        'company_info': company_info,
        'statistics': statistics,
        'featured_services': featured_services,
        'featured_materials': featured_materials,
        'featured_products': featured_products,
        'featured_projects': featured_projects,
    }
    return render(request, 'core/home.html', context)

def services_view(request):
    company_info = CompanyInfo.objects.first()
    services = Service.objects.all()
    materials = Material.objects.all()
    context = {
        'company_info': company_info,
        'services': services,
        'materials': materials,
    }
    return render(request, 'core/services.html', context)

def products_view(request):
    company_info = CompanyInfo.objects.first()
    categories = ProductCategory.objects.all()
    
    # Base queryset for active products
    queryset = Product.objects.filter(is_active=True)
    
    # 1. Category Filtering
    category_slug = request.GET.get('category')
    active_category = None
    if category_slug:
        queryset = queryset.filter(category__slug=category_slug)
        active_category = categories.filter(slug=category_slug).first()
        
    # 2. Text Search
    search_query = request.GET.get('q')
    if search_query:
        queryset = queryset.filter(
            Q(name__icontains=search_query) |
            Q(sku__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(full_description__icontains=search_query)
        )
        
    # 3. Sorting
    sort_by = request.GET.get('sort', 'name_asc')
    if sort_by == 'name_asc':
        queryset = queryset.order_by('name')
    elif sort_by == 'name_desc':
        queryset = queryset.order_by('-name')
    elif sort_by == 'newest':
        queryset = queryset.order_by('-created_at')
        
    # 4. Pagination
    paginator = Paginator(queryset, 12)  # 12 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'company_info': company_info,
        'categories': categories,
        'active_category': active_category,
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_by': sort_by,
        'category_slug': category_slug,
    }
    return render(request, 'core/products.html', context)

def projects_view(request):
    company_info = CompanyInfo.objects.first()
    category_choices = Project.CATEGORY_CHOICES
    
    queryset = Project.objects.all()
    
    # Category Filtering
    category_filter = request.GET.get('category')
    if category_filter:
        queryset = queryset.filter(category=category_filter)
        
    context = {
        'company_info': company_info,
        'projects': queryset,
        'category_choices': category_choices,
        'active_category': category_filter,
    }
    return render(request, 'core/projects.html', context)

def enquiry_view(request):
    company_info = CompanyInfo.objects.first()
    success = False
    
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = EnquiryForm()  # reset form
    else:
        # Prepopulate subject from query param
        product_name = request.GET.get('product')
        subject_text = ""
        service_type = 'BOTH'
        if product_name:
            subject_text = f"Enquiry regarding Product: {product_name}"
            service_type = 'PRODUCT'
        
        custom_subject = request.GET.get('subject')
        custom_type = request.GET.get('type')
        if custom_subject:
            subject_text = custom_subject
        if custom_type == 'material':
            service_type = 'MATERIAL'
        elif custom_type == 'construction':
            service_type = 'CONSTRUCTION'
            
        form = EnquiryForm(initial={'subject': subject_text, 'service_type': service_type})
        
    context = {
        'company_info': company_info,
        'form': form,
        'success': success,
    }
    return render(request, 'core/enquiry.html', context)

def product_detail_view(request, slug):
    company_info = CompanyInfo.objects.first()
    product = get_object_or_404(Product, slug=slug, is_active=True)
    
    # Related products: same category, excluding current product, up to 4
    related_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product.id)[:4]
    
    # Parse specifications (format: Key: Value per line)
    specs = []
    if product.specifications:
        for line in product.specifications.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                specs.append({'key': key.strip(), 'value': val.strip()})
                
    context = {
        'company_info': company_info,
        'product': product,
        'related_products': related_products,
        'specs': specs,
    }
    return render(request, 'core/product_detail.html', context)

def project_detail_view(request, slug):
    company_info = CompanyInfo.objects.first()
    project = get_object_or_404(Project, slug=slug)
    
    # Related projects: same category, excluding current project, up to 3
    related_projects = Project.objects.filter(
        category=project.category
    ).exclude(id=project.id)[:3]
    
    # Parse services delivered
    services_list = []
    if project.services_delivered:
        lines = project.services_delivered.split('\n')
        for line in lines:
            parts = [p.strip() for p in line.split(',') if p.strip()]
            services_list.extend(parts)
            
    context = {
        'company_info': company_info,
        'project': project,
        'related_projects': related_projects,
        'services_list': services_list,
    }
    return render(request, 'core/project_detail.html', context)











