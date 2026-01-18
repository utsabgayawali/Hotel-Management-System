function toggleMenu() {
    const navLinks = document.getElementById('navLinks');
    const menuBtn = document.querySelector('.menu-btn');
    
    navLinks.classList.toggle('active');
    // For hamburger animation
    menuBtn.classList.toggle('change');
}

window.addEventListener('scroll', () => {
    const nav = document.getElementById('mainNav');
    if (window.scrollY > 80) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Auto-fill dates
document.querySelectorAll('input[type="date"]').forEach(input => {
    if (!input.value) input.valueAsDate = new Date();
});