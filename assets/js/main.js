(function () {
  var doc = document.documentElement;
  doc.classList.remove('no-js');
  doc.classList.add('js');

  // Header shadow
  var header = document.querySelector('.site-header');
  function onScroll() { if (header) header.classList.toggle('is-scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('[data-nav]');
  if (burger && nav) {
    function setMenu(open) {
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', burger.getAttribute(open ? 'data-close' : 'data-open'));
      nav.classList.toggle('is-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    }
    burger.addEventListener('click', function () { setMenu(burger.getAttribute('aria-expanded') !== 'true'); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.matchMedia('(min-width: 1081px)').addEventListener('change', function (m) { if (m.matches) setMenu(false); });
  }

  // Scroll reveal
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Tabs
  document.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); });
      t.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { var n = tabs[(i + d + tabs.length) % tabs.length]; select(n); n.focus(); }
      });
    });
  });

  // Sub-nav highlight
  var sub = document.querySelectorAll('.subnav a');
  if (sub.length && 'IntersectionObserver' in window) {
    var map = {};
    sub.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          sub.forEach(function (a) { a.classList.remove('is-active'); });
          var a = map[en.target.id];
          if (a) { a.classList.add('is-active'); a.scrollIntoView({ block: 'nearest', inline: 'nearest' }); }
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) so.observe(el); });
  }

  // Enquiry form: compose a WhatsApp or email message (no server needed)
  var form = document.querySelector('[data-enquiry]');
  if (form) {
    var WA = form.getAttribute('data-wa');
    var MAIL = form.getAttribute('data-mail');
    var en = doc.lang.indexOf('en') === 0;
    function compose() {
      var f = new FormData(form);
      var L = en
        ? { hi: 'Hello JoyHome, I would like to ask about:', svc: 'Service', area: 'Area', when: 'Timing', budget: 'Budget', name: 'Name', reply: 'Contact', sep: ': ', join: ', ' }
        : { hi: '你好 JoyHome，我想查詢：', svc: '服務', area: '地區', when: '預計時間', budget: '預算', name: '名字', reply: '聯絡方法', sep: '：', join: '、' };
      var lines = [L.hi];
      var svc = f.getAll('service');
      if (svc.length) lines.push(L.svc + L.sep + svc.join(L.join));
      ['area', 'when', 'budget', 'name', 'reply'].forEach(function (k) {
        var v = (f.get(k) || '').toString().trim();
        if (v) lines.push(L[k] + L.sep + v);
      });
      var msg = (f.get('message') || '').toString().trim();
      if (msg) lines.push('', msg);
      return lines.join('\n');
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var via = e.submitter && e.submitter.value === 'email' ? 'email' : 'wa';
      var text = compose();
      if (via === 'email') {
        window.location.href = 'mailto:' + MAIL + '?subject=' + encodeURIComponent(en ? 'JoyHome website enquiry' : 'JoyHome 網站查詢') + '&body=' + encodeURIComponent(text);
      } else {
        window.open('https://wa.me/' + WA + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
      }
    });
  }

  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
