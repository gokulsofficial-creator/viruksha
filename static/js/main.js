// main.js - Core layout interactivity for Viruksha Enterprises

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile navigation menu drawer controls
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileNavDrawer = document.getElementById('mobile-nav-drawer');
    const mobileMenuClose = document.getElementById('mobile-menu-close');
    const mobileNavBackdrop = document.getElementById('mobile-nav-backdrop');

    function openMobileMenu() {
        mobileNavDrawer.classList.remove('translate-x-full');
        document.body.classList.add('overflow-hidden'); // Prevent background scroll
    }

    function closeMobileMenu() {
        mobileNavDrawer.classList.add('translate-x-full');
        document.body.classList.remove('overflow-hidden');
    }

    if (mobileMenuBtn && mobileNavDrawer) {
        mobileMenuBtn.addEventListener('click', openMobileMenu);
    }

    if (mobileMenuClose) {
        mobileMenuClose.addEventListener('click', closeMobileMenu);
    }

    if (mobileNavBackdrop) {
        mobileNavBackdrop.addEventListener('click', closeMobileMenu);
    }

    // Close mobile menu on clicking any link inside it
    const drawerLinks = mobileNavDrawer ? mobileNavDrawer.querySelectorAll('a') : [];
    drawerLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });

    // 2. Navbar shrink/shadow on scroll
    const navbar = document.querySelector('nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow-md', 'h-16');
            navbar.classList.remove('shadow-sm', 'h-20');
            navbar.querySelector('div').classList.add('h-16');
            navbar.querySelector('div').classList.remove('h-20');
        } else {
            navbar.classList.add('shadow-sm', 'h-20');
            navbar.classList.remove('shadow-md', 'h-16');
            navbar.querySelector('div').classList.add('h-20');
            navbar.querySelector('div').classList.remove('h-16');
        }
    });
});
