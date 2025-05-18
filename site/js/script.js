document.addEventListener('DOMContentLoaded', () => {
    // Инициализация анимации появления при скролле
    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                obs.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Инициализация аккордеонов
    document.querySelectorAll('.accordion-header').forEach(header => {
        header.addEventListener('click', () => {
            const isOpen = header.classList.contains('active');
            document.querySelectorAll('.accordion-header.active').forEach(h => {
                h.classList.remove('active');
                h.nextElementSibling.style.maxHeight = null;
            });
            if (!isOpen) {
                header.classList.add('active');
                const body = header.nextElementSibling;
                body.style.maxHeight = body.scrollHeight + 'px';
            }
        });
    });

    // Инициализация кнопок "Читать далее"
    document.querySelectorAll('.read-more').forEach(btn => {
        btn.addEventListener('click', function() {
            const myP = this.closest('.card-body').querySelector('p');
            document.querySelectorAll('.card-body p.expanded').forEach(p => {
                if (p !== myP) {
                    p.classList.remove('expanded');
                    p.style.maxHeight = '';
                    const otherBtn = p.closest('.card-body').querySelector('.read-more');
                    if (otherBtn) otherBtn.textContent = 'Читать далее';
                }
            });

            if (myP.classList.contains('expanded')) {
                myP.classList.remove('expanded');
                myP.style.maxHeight = '';
                this.textContent = 'Читать далее';
            } else {
                myP.classList.add('expanded');
                myP.style.maxHeight = myP.scrollHeight + 'px';
                this.textContent = 'Свернуть';
            }
        });
    });

    // Инициализация кнопки прокрутки вверх
    const scrollBtn = document.getElementById('scrollTopBtn');
    if (scrollBtn) {
        window.addEventListener('scroll', () => {
            scrollBtn.classList.toggle('show', window.scrollY > 300);
        });
        scrollBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Загрузка карточек с анимацией
    setTimeout(() => {
        document.querySelectorAll('.card-grid').forEach(grid => {
            grid.classList.add('loaded');
        });
    }, 300);

    // Эффекты при наведении на карточки
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-8px)';
            card.style.boxShadow = '0 15px 35px rgba(0, 0, 0, 0.1)';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
            card.style.boxShadow = '';
        });
    });

    // Фиксированная шапка при скролле
    window.addEventListener('scroll', () => {
        const header = document.querySelector('header');
        if (header) {
            if (window.scrollY > 10) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }
    });
}); 