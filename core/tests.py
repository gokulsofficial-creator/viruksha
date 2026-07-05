from django.test import TestCase
from django.urls import reverse
from .models import CompanyInfo, Statistic, Service, ProductCategory, Product, Project, Enquiry
from .forms import EnquiryForm

class VirukshaTests(TestCase):
    def setUp(self):
        # Create base company info
        self.company = CompanyInfo.objects.create(
            company_name="Viruksha Test",
            tagline="Engineering Excellence",
            email="test@viruksha.com",
            phone="+91 99999 88888",
            address="Test Address, Chennai",
        )
        # Create a statistic
        self.stat = Statistic.objects.create(
            label="Completed Projects",
            value="10+",
            icon_class="architecture",
        )
        # Create a service
        self.service = Service.objects.create(
            title="Fasteners Supply",
            slug="fasteners-supply",
            category="MATERIAL",
            icon_class="build",
            short_description="Heavy duty fasteners",
            is_featured=True
        )
        # Create category & product
        self.category = ProductCategory.objects.create(
            name="Fasteners",
            slug="fasteners"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Heavy Duty Bolt",
            slug="heavy-duty-bolt",
            sku="HDB-001",
            short_description="Grade 8.8 steel bolt",
            is_active=True,
            is_featured=True
        )
        # Create a project
        self.project = Project.objects.create(
            title="Skyline Tower",
            slug="skyline-tower",
            category="commercial",
            client_name="Skyline Corp",
            location="Chennai",
            description="High-rise building",
            is_featured=True
        )

    def test_homepage_view(self):
        url = reverse('core:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Viruksha Test")
        self.assertContains(response, "Completed Projects")

    def test_services_view(self):
        url = reverse('core:services')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fasteners Supply")

    def test_products_catalog_view(self):
        url = reverse('core:products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Heavy Duty Bolt")

    def test_product_detail_view(self):
        url = reverse('core:product_detail', kwargs={'slug': self.product.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "HDB-001")

    def test_projects_portfolio_view(self):
        url = reverse('core:projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Skyline Tower")

    def test_project_detail_view(self):
        url = reverse('core:project_detail', kwargs={'slug': self.project.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chennai")

    def test_enquiry_form_submission(self):
        url = reverse('core:enquiry')
        # Submit valid enquiry
        post_data = {
            'name': 'John Doe',
            'email': 'john@doe.com',
            'phone': '9999988888',
            'company_name': 'Doe Corp',
            'service_type': 'MATERIAL',
            'subject': 'Fastener Enquiry',
            'message': 'Looking for bulk fasteners quote.'
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thank You")
        # Verify saved in DB
        self.assertEqual(Enquiry.objects.count(), 1)
        enquiry = Enquiry.objects.first()
        self.assertEqual(enquiry.name, 'John Doe')
        self.assertEqual(enquiry.is_read, False)

