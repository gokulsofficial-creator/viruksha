# Viruksha Enterprises Website

A premium, modern corporate web application for **Viruksha Enterprises** to showcase their construction materials supply division and structural engineering services. It features a fully responsive product catalog, an interactive projects portfolio, and a secure customer enquiry management system.

---

## 🚀 Key Features

*   **Corporate Homepage:** Fully responsive top fold with dynamic statistics, service cards, featured materials, and portfolio highlights.
*   **Services Listing:** Separates materials supply from engineering works, incorporating smooth scroll navigation.
*   **Product Catalog:**
    *   Dynamic category filtering and search queries.
    *   Catalog list with pagination and stock badges.
    *   Detail pages showing item technical specifications.
    *   Related products carousel slider.
*   **Engineering Projects:**
    *   Masonry portfolio layout with project division filters.
    *   Details view displaying client, location, services, and photo lightbox popup.
*   **Enquiry Management:**
    *   Secure form with frontend and backend validation.
    *   Auto-populated subject lines when redirected from specific products/projects.
    *   Interactive Google Maps integration.
*   **Custom Admin Dashboard:** Branded Django Admin panel with quick actions, read-only enquiry logs, and custom styling.

---

## 🛠️ Technology Stack

*   **Backend:** Python 3.13, Django 6.0
*   **Database:** SQLite 3 (highly portable)
*   **Frontend:** HTML5, CSS3, JavaScript (ES6+), Tailwind CSS CDN, Material Symbols
*   **Assets:** Pillow (for Django image uploads)

---

## 💻 Installation & Local Development

Follow these steps to run the application locally on your machine:

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Setup Virtual Environment
Clone the repository and navigate into the root directory:
```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup & Migrations
```bash
# Run migrations to set up the database tables
python manage.py migrate
```

### 5. Seed Initial Data (Optional but Recommended)
To run the website with sample materials, products, and statistics, create a superuser and add initial records via the Django Admin:
```bash
# Create admin superuser
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.

---

## 📁 Project Structure

```text
├── core/                  # Main application app containing views, models, and forms
│   ├── migrations/        # Database migration files
│   ├── templates/core/    # HTML pages (home, services, products, projects, enquiry, detail pages)
│   ├── admin.py           # Custom branded Django Admin configurations
│   ├── models.py          # Database models (Product, Project, Enquiry, CompanyInfo, etc.)
│   └── views.py           # Page view handlers and form processing
├── static/                # Static assets
│   ├── css/               # Tailwind overrides and custom styles
│   └── js/                # Interactivity script files (mobile menu, galleries, maps)
├── templates/             # Base layouts and navigation templates
│   └── base.html          # Global wrapper template (head, nav, mobile drawer, footer)
├── viruksha_project/      # Project settings, settings.py and routing urls.py
└── requirements.txt       # Dependencies manifest
```
