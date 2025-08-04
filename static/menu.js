document.addEventListener('DOMContentLoaded', () => {
    const userMenu = document.getElementById('userMenu');
    const userMenuContent = document.getElementById('userMenuContent');
    const topNavBurger = document.getElementById('topNavBurger');
    const topNavMenu = document.getElementById('topNavMenu');
    const productNavBurger = document.getElementById('productNavBurger');
    const productNavMenu = document.getElementById('productNavMenu');

    if (userMenu && userMenuContent) {
        userMenu.querySelector('i').addEventListener('click', (e) => {
            e.stopPropagation();
            userMenuContent.classList.toggle('show');
        });

        document.addEventListener('click', () => {
            userMenuContent.classList.remove('show');
        });

        userMenuContent.addEventListener('click', (e) => {
            e.stopPropagation();
        });
    }

    if (topNavBurger && topNavMenu) {
        topNavBurger.addEventListener('click', () => {
            topNavMenu.classList.toggle('active');
        });
    }
    if (productNavBurger && productNavMenu) {
        productNavBurger.addEventListener('click', () => {
            productNavMenu.classList.toggle('active');
        });
    }
});
