# 🏗️ Viruksha Enterprises — Premium Corporate Web Portal

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.13-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-6.0-green.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

A premium, modern corporate web portal designed and developed for **Viruksha Enterprises**. The application showcases their two key business divisions: **Construction Materials Supply** (fasteners, fittings, safety equipment) and **Construction Services** (residential, commercial, industrial building). 

This portal acts as a high-converting digital company profile, featuring a robust product catalog, an interactive engineering projects portfolio, a secure customer enquiry system, and a custom-branded Django administration control center.

---

## 🌟 Key Highlights & Features

### 🖥️ High-Fidelity Responsive Design
- Built using **Tailwind CSS** with a custom curated color palette (steel primary, warm secondary accents).
- Typographic hierarchy using **Montserrat** (headlines) and **Inter** (body text).
- Responsive mobile drawer navigation with backdrop blurs.
- Micro-interactions (hover scales, translation effects, smooth navigation scroll).

### 📦 Dynamic Product Catalog
- **Grid Listing:** Interactive cards featuring SKU identifiers, descriptions, and dynamic stock badges (`In Stock`, `On Request`, `Coming Soon`).
- **Catalog Utilities:** Real-time text search and category filtering pills.
- **Specifications Sheets:** Clean key-value properties table dynamically parsed from single-line text inputs.
- **Detail Slides:** Dynamic product image galleries with thumbnail selection and related-items sliders.

### 🏗️ Engineering Project Portfolio
- Displayed in a visual **masonry grid** featuring responsive column structures.
- Project categorization (Residential, Commercial, Industrial, Civil) with active filter states.
- Dedicated detail pages showcasing client information, locations, completion dates, and full image lightboxes.

### ✉️ Intelligent Enquiry Routing
- Secure contact form with field-specific backend validation.
- Auto-populates subjects and divisions when accessed from specific products/projects (e.g., *Enquiry regarding heavy-duty fasteners*).
- Integrated interactive Google Maps location widget.

### 🛡️ Branded Administration Center
- Branded header title, page headers, and customized page icons.
- **Security-First Enquiries:** Customer enquiry logs are immutable (read-only) inside the panel, and manual creation is blocked.
- Advanced administrative search options, category filters, and bulk actions.

---

## 📁 System Architecture

```text
├── core/
│   ├── migrations/         # Historical database migrations
│   ├── templates/core/     # High-fidelity page templates
│   │   ├── home.html           # Homepage (Hero, Stats, Featured grids)
│   │   ├── services.html       # Services directory (Materials & Construction)
│   │   ├── products.html       # Product catalog with search and filters
│   │   ├── product_detail.html # Interactive product specs and gallery
│   │   ├── projects.html       # Masonry portfolio layout
│   │   ├── project_detail.html # Project showcase sheets
│   │   └── enquiry.html        # Smart routing contact page
│   ├── admin.py            # Custom branded admin dashboard settings
│   ├── models.py           # DB Schemas (Statistic, ProductCategory, Product, etc.)
│   └── views.py            # Request routing and form validation logic
├── static/
│   ├── css/
│   │   └── styles.css      # Core styles & Tailwind utilities
│   └── js/
│       └── main.js         # Navigation drawer and header scrolls
├── templates/
│   └── base.html           # Global wrapper (header nav, drawer, footer)
├── viruksha_project/       # Core project settings and configurations
└── requirements.txt        # Third-party dependency manifest
```

---

## 🚀 Quick Start Guide

Run the application locally on your system using these steps:

### 1. Setup Virtual Environment
Clone the repository and set up a clean Python virtual environment:
```bash
# Create environment
python -m venv .venv

# Activate environment (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate environment (Linux/macOS)
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations
```bash
python manage.py migrate
```

### 4. Create Admin Account
To access the management panel and upload logo/banner details:
```bash
python manage.py createsuperuser
```

### 5. Start Server
```bash
python manage.py runserver
```
Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.

---

## 🔒 Security & Optimization

- **Database Integrity:** Utilizes Django's ORM model structures with cascade deletion rules.
- **SEO Elements:** Formatted with unique descriptive `<title>` tags, structured keywords meta tags, Open Graph (OG) properties, and Twitter cards.
- **Form Sanitization:** Employs CSRF token validation and Django ModelForm field clean validation to prevent injection attempts.
