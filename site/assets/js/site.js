/* Quanten Massage München – tiny, dependency-free, cookie-free */
(function () {
  'use strict';
  var d = document;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header turns solid after scrolling (home only), mobile dock appears after the first screen */
  var hdr = d.querySelector('.site-header'), dock = d.querySelector('.dock');
  function onScroll() {
    var y = window.scrollY;
    if (hdr) hdr.classList.toggle('is-solid', y > 40);
    if (dock) dock.classList.toggle('is-on', y > window.innerHeight * 0.6);
  }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  /* mobile menu */
  var toggle = d.querySelector('.nav-toggle'), mnav = d.getElementById('mnav');
  if (toggle && mnav) {
    var close = mnav.querySelector('.mnav-close');
    var setMenu = function (open) {
      mnav.hidden = !open;
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      d.body.style.overflow = open ? 'hidden' : '';
      (open ? close : toggle).focus();
    };
    toggle.addEventListener('click', function () { setMenu(true); });
    close.addEventListener('click', function () { setMenu(false); });
    mnav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    d.addEventListener('keydown', function (e) {
      if (mnav.hidden) return;
      if (e.key === 'Escape') setMenu(false);
      if (e.key === 'Tab') { /* keep focus inside the open menu */
        var f = mnav.querySelectorAll('a,button'), first = f[0], last = f[f.length - 1];
        if (e.shiftKey && d.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && d.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* hero video: only when motion is allowed and data saver is off; poster stays otherwise */
  var vid = d.querySelector('video[data-hero]');
  if (vid) {
    var saver = navigator.connection && navigator.connection.saveData;
    var btn = d.querySelector('.vid-toggle');
    if (!reduce && !saver) {
      var base = vid.getAttribute('data-base');
      var sources = window.innerWidth > 760 ? [[base + '.webm', 'video/webm'], [base + '.mp4', 'video/mp4']] : [[base + '-mobile.mp4', 'video/mp4']];
      sources.forEach(function (s) { var el = d.createElement('source'); el.src = s[0]; el.type = s[1]; vid.appendChild(el); });
      vid.addEventListener('error', function () { vid.remove(); if (btn) btn.remove(); }, true);
      vid.addEventListener('playing', function () {
        if (btn) btn.style.display = 'block';
        var img = d.querySelector('.hero-media img'); if (img) img.style.opacity = 0;
      }, { once: true });
      if (btn) btn.addEventListener('click', function () {
        if (vid.paused) { vid.play(); btn.textContent = 'Video pausieren'; } else { vid.pause(); btn.textContent = 'Video abspielen'; }
      });
      vid.load();
      var p = vid.play(); if (p && p.catch) p.catch(function () {});
    } else { vid.remove(); }
  }

  /* two-click map: nothing is requested from Google before the visitor clicks */
  d.querySelectorAll('[data-map]').forEach(function (box) {
    var b = box.querySelector('button');
    if (!b) return;
    b.addEventListener('click', function () {
      var f = d.createElement('iframe');
      f.src = box.getAttribute('data-map'); f.title = 'Karte: Praxis Quanten Massage, Elsässer Str. 11, München';
      f.loading = 'lazy'; f.referrerPolicy = 'no-referrer'; f.setAttribute('allowfullscreen', '');
      box.innerHTML = ''; box.appendChild(f);
    });
  });

  /* contact form: time stamp for the spam check, simple consent guard */
  var form = d.querySelector('form[data-form]');
  if (form) {
    var t = form.querySelector('input[name="t"]'); if (t) t.value = Math.floor(Date.now() / 1000);
    form.addEventListener('submit', function (e) {
      var c = form.querySelector('input[name="consent"]');
      if (c && !c.checked) { e.preventDefault(); c.focus(); c.setCustomValidity('Bitte bestätige die Datenschutzhinweise.'); c.reportValidity(); }
    });
    var c2 = form.querySelector('input[name="consent"]');
    if (c2) c2.addEventListener('change', function () { c2.setCustomValidity(''); });
  }
})();
