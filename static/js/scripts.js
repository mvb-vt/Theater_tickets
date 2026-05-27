(function () {
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-bar-collapse');

    if (toggle && menu) {
        toggle.addEventListener('click', function () {
            const isOpen = menu.classList.toggle('is-open');
            toggle.setAttribute('aria-expanded', String(isOpen));
        });
    }
})();

(function () {
    const items = document.querySelectorAll('.performance-item');
    if (!items.length) {
        return;
    }

    let activeIndex = 0;

    setInterval(function () {
        items[activeIndex].classList.remove('is-active');
        activeIndex = (activeIndex + 1) % items.length;
        items[activeIndex].classList.add('is-active');
    }, 4000);
})();
