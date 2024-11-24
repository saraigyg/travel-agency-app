let slideIndex = 0;
showSlides(slideIndex);

function changeSlide(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    const slides = document.querySelectorAll('.slide');
    if (n >= slides.length) {
        slideIndex = 0; // Reset to first slide
    }
    if (n < 0) {
        slideIndex = slides.length - 1; // Go to last slide
    }

    slides.forEach((slide, index) => {
        slide.style.display = (index === slideIndex) ? 'block' : 'none'; // Show or hide slides
    });
}

// Optional: Auto slide every 5 seconds
setInterval(() => {
    changeSlide(1);
}, 5000);

document.addEventListener('DOMContentLoaded', () => {
    const packagesNav = document.querySelector('.packages');
    const destinationsNav = document.querySelector('.destinations');

    if (packagesNav) {
        packagesNav.addEventListener('mouseenter', () => {
            document.querySelector('.packages-list').style.display = 'block';
        });

        packagesNav.addEventListener('mouseleave', () => {
            document.querySelector('.packages-list').style.display = 'none';
        });
    }

    if (destinationsNav) {
        destinationsNav.addEventListener('mouseenter', () => {
            document.querySelector('.destinations-list').style.display = 'block';
        });

        destinationsNav.addEventListener('mouseleave', () => {
            document.querySelector('.destinations-list').style.display = 'none';
        });
    }
});

// Toggle between login and registration forms
function toggleForms() {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    if (loginForm && registerForm) {
        if (loginForm.style.display === 'none') {
            loginForm.style.display = 'block';
            registerForm.style.display = 'none';
        } else {
            loginForm.style.display = 'none';
            registerForm.style.display = 'block';
        }
    }
}

// Simple mock login functionality
function loginUser(event) {
    event.preventDefault();
    const email = document.getElementById('login-email')?.value;
    const password = document.getElementById('login-password')?.value;

    // Mock validation
    if (email === "test@example.com" && password === "password123") {
        alert("Login successful!");
    } else {
        document.getElementById('login-error').style.display = 'block';
    }
}

// Simple mock registration functionality
function registerUser(event) {
    event.preventDefault();
    const firstName = document.getElementById('first-name')?.value;
    const lastName = document.getElementById('last-name')?.value;
    const email = document.getElementById('register-email')?.value;
    const password = document.getElementById('register-password')?.value;
    const confirmPassword = document.getElementById('confirm-password')?.value;
    const phone = document.getElementById('phone')?.value;

    // Validate registration fields
    if (password !== confirmPassword) {
        const errorElement = document.getElementById('register-error');
        errorElement.textContent = "Passwords do not match!";
        errorElement.style.display = 'block';
        return false;
    }

    // Mock registration logic
    if (firstName && lastName && email && password && phone) {
        alert("Registration successful!");
        toggleForms(); // Switch to login form
    } else {
        document.getElementById('register-error').style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('input[type="date"]').forEach(input => {
        input.addEventListener('focus', function () {
            if (!this.value) this.placeholder = 'DD/MM/YY';
        });

        input.addEventListener('blur', function () {
            this.placeholder = 'DD/MM/YY';
        });

        input.addEventListener('input', function () {
            if (this.value) {
                const [year, month, day] = this.value.split('-');
                if (day && month && year) {
                    this.placeholder = `${day}/${month}/${year.slice(2)}`;
                }
            }
        });
    });
});
