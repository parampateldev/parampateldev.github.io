(function() {
    const STORAGE_KEY = 'mportfolio-theme';
    const DEFAULT_THEME = 'dark';

    function getStoredTheme() {
        try {
            return localStorage.getItem(STORAGE_KEY) || DEFAULT_THEME;
        } catch {
            return DEFAULT_THEME;
        }
    }

    function setTheme(name) {
        const theme = ['dark', 'sunrise', 'sunset'].includes(name) ? name : DEFAULT_THEME;
        document.documentElement.setAttribute('data-theme', theme);
        try {
            localStorage.setItem(STORAGE_KEY, theme);
        } catch (_) {}
        updateSwitcherUI(theme);
    }

    function updateSwitcherUI(theme) {
        document.querySelectorAll('.theme-option').forEach(opt => {
            opt.classList.toggle('active', opt.getAttribute('data-theme') === theme);
        });
        const btn = document.querySelector('.theme-switcher-btn');
        if (btn) btn.setAttribute('aria-label', 'Theme: ' + theme);
    }

    function init() {
        setTheme(getStoredTheme());

        document.querySelector('.theme-switcher')?.addEventListener('click', function(e) {
            const opt = e.target.closest('.theme-option');
            if (opt) {
                setTheme(opt.getAttribute('data-theme'));
            }
        });

        document.querySelector('.theme-switcher-btn')?.addEventListener('click', function(e) {
            e.stopPropagation();
            this.parentElement?.classList.toggle('open');
        });

        document.addEventListener('click', function() {
            document.querySelector('.theme-switcher')?.classList.remove('open');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
