(function () {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  // Smooth scroll for same-page anchors
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (!href || href === '#') return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // Prefetch internal pages so the next click is usually already cached
  const prefetched = new Set();

  function sameOriginPage(href) {
    try {
      const url = new URL(href, window.location.href);
      if (url.origin !== window.location.origin) return null;
      if (url.hash && url.pathname === window.location.pathname) return null;
      const path = url.pathname;
      if (!path.endsWith('.html') && path !== '/' && !path.endsWith('/')) return null;
      return url.href.split('#')[0];
    } catch {
      return null;
    }
  }

  function prefetch(href) {
    const page = sameOriginPage(href);
    if (!page || prefetched.has(page) || page === window.location.href.split('#')[0]) return;
    prefetched.add(page);

    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = page;
    link.as = 'document';
    document.head.appendChild(link);

    // Also warm the HTTP cache with a low-priority fetch
    if (window.fetch) {
      fetch(page, { priority: 'low', credentials: 'same-origin' }).catch(() => {});
    }
  }

  function prefetchAllNav() {
    document.querySelectorAll('a.nav-link, a.page-card, a.exp-jump a, .exp-jump a').forEach((a) => {
      const href = a.getAttribute('href');
      if (href) prefetch(href);
    });
  }

  document.querySelectorAll('a[href]').forEach((a) => {
    const href = a.getAttribute('href');
    if (!sameOriginPage(href)) return;
    a.addEventListener('pointerenter', () => prefetch(href), { once: true });
    a.addEventListener('focus', () => prefetch(href), { once: true });
  });

  if ('requestIdleCallback' in window) {
    requestIdleCallback(prefetchAllNav, { timeout: 1200 });
  } else {
    setTimeout(prefetchAllNav, 400);
  }

  // Light navbar shadow after scrolling a bit
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    let ticking = false;
    window.addEventListener(
      'scroll',
      () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => {
          navbar.style.boxShadow =
            window.scrollY > 50 ? '0 2px 10px rgba(0, 0, 0, 0.1)' : '0 1px 3px rgba(0, 0, 0, 0.1)';
          ticking = false;
        });
      },
      { passive: true }
    );
  }
})();
