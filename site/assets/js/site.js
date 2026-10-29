/* Quanten Massage München – tiny, dependency-free, cookie-free */
(function () {
  'use strict';
  var d = document;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header turns solid after scrolling */
  var hdr = d.querySelector('.site-header');
  function onScroll() { if (hdr) hdr.classList.toggle('is-solid', window.scrollY > 40); }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  /* mobile menu */
  var toggle = d.querySelector('.nav-toggle'), mnav = d.getElementById('mnav');
  if (toggle && mnav) {
    var close = mnav.querySelector('.mnav-close');
    function setMenu(open) {
      mnav.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      d.body.style.overflow = open ? 'hidden' : '';
      if (open && close) close.focus(); else toggle.focus();
    }
    toggle.addEventListener('click', function () { setMenu(true); });
    close.addEventListener('click', function () { setMenu(false); });
    mnav.addEventListener('click', function (e) { if (e.target.tagName === 'A') setMenu(false); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && mnav.classList.contains('open')) setMenu(false); });
  }

  /* hero video: loads only if the file exists, motion is allowed and data saver is off */
  var vid = d.querySelector('video[data-hero]');
  if (vid) {
    var saver = navigator.connection && navigator.connection.saveData;
    if (!reduce && !saver) {
      var wide = window.innerWidth > 760;
      var base = vid.getAttribute('data-base');
      var sources = wide ? [['webm', 'video/webm'], ['mp4', 'video/mp4']] : [['mobile.mp4', 'video/mp4']];
      sources.forEach(function (s) {
        var el = d.createElement('source');
        el.src = base + (wide ? '.' + s[0] : '-' + s[0]); el.type = s[1]; vid.appendChild(el);
      });
      vid.addEventListener('error', function () { vid.remove(); btn && btn.remove(); }, true);
      var btn = d.querySelector('.vid-toggle');
      vid.addEventListener('playing', function () {
        if (btn) { btn.style.display = 'block'; }
        var img = d.querySelector('.hero-media img'); if (img) img.style.opacity = 0;
      });
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
      if (c && !c.checked) { e.preventDefault(); c.focus(); alert('Bitte bestätige kurz die Datenschutzhinweise.'); }
    });
  }
})();
