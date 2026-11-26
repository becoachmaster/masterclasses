/* Motor de presentación BeCoach.
   Teclas: → / Espacio / Re Pág = siguiente · ← / Av Pág = anterior · Inicio / Fin
           F = pantalla completa · P = vista de presentador (notas, siguiente diapositiva, reloj) */
(function () {
  'use strict';
  var ICONOS = {
    Search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    Users: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    CheckCircle: '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    Key: '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
    Chat: '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    Warning: '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    Trust: '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    Anchor: '<path d="M12 22V8"/><path d="M5 12H2a10 10 0 0 0 20 0h-3"/><circle cx="12" cy="5" r="3"/>',
    Heart: '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
    Cycle: '<path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/>',
    Lightbulb: '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
    Target: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    Eye: '<path d="M2.06 12.35a1 1 0 0 1 0-.7 10.75 10.75 0 0 1 19.88 0 1 1 0 0 1 0 .7 10.75 10.75 0 0 1-19.88 0"/><circle cx="12" cy="12" r="3"/>',
    Calendar: '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
    Compass: '<circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/>',
    Mirror: '<ellipse cx="12" cy="10" rx="6" ry="8"/><path d="M12 18v4"/><path d="M8 22h8"/>'
  };

  function pintarIconos(raiz) {
    raiz.querySelectorAll('x-icon').forEach(function (el) {
      if (el.getAttribute('data-listo')) return;
      var trazo = ICONOS[el.getAttribute('name')] || ICONOS.Target;
      el.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + trazo + '</svg>';
      el.setAttribute('data-listo', '1');
    });
  }

  var deck = document.getElementById('deck');
  Array.prototype.slice.call(deck.children).forEach(function (s) { if (s.hasAttribute('hidden')) s.remove(); });
  var slides = Array.prototype.slice.call(deck.querySelectorAll(':scope > section'));
  pintarIconos(deck);

  var total = slides.length;
  var actual = 0;
  var esPresentador = new URLSearchParams(location.search).get('presentador') === '1';
  var otraVentana = null;

  function limitar(i) { return Math.max(0, Math.min(total - 1, i)); }
  function leerHash() {
    var m = location.hash.match(/^#\/?(\d+)/);
    return m ? limitar(parseInt(m[1], 10) - 1) : 0;
  }
  function destino() { return esPresentador ? window.opener : otraVentana; }
  function avisar(i) {
    var w = destino();
    if (w && !w.closed) { try { w.postMessage({ becoach: true, ir: i }, '*'); } catch (e) {} }
  }

  /* ---------- Vista de audiencia ---------- */
  function ajustarEscala() {
    var s = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
    var x = (window.innerWidth - 1920 * s) / 2, y = (window.innerHeight - 1080 * s) / 2;
    deck.style.transform = 'translate(' + x + 'px,' + y + 'px) scale(' + s + ')';
  }
  function mostrar(i) {
    slides.forEach(function (s, k) {
      s.classList.toggle('activa', k === i);
      // Un video no sigue sonando cuando se sale de su diapositiva.
      if (k !== i) s.querySelectorAll('video').forEach(function (v) { v.pause(); });
    });
  }

  /* ---------- Vista de presentador ---------- */
  var pr = {};
  function construirPresentador() {
    document.body.classList.add('presentador');
    deck.style.display = 'none';
    var raiz = document.createElement('div');
    raiz.className = 'pr';
    raiz.innerHTML =
      '<div><div class="pr-marco" id="prActual"></div></div>' +
      '<div class="pr-lado">' +
      '  <div class="pr-fila"><span id="prContador"></span><span class="pr-reloj" id="prReloj">00:00</span></div>' +
      '  <div class="pr-titulo-sig">Siguiente</div>' +
      '  <div class="pr-marco" id="prSiguiente"></div>' +
      '  <div class="pr-notas" id="prNotas"></div>' +
      '  <div class="pr-botones"><button id="prAnt">Anterior</button><button id="prSig">Siguiente</button><button id="prReloj0">Reiniciar reloj</button></div>' +
      '</div>';
    document.body.appendChild(raiz);
    pr.actual = document.getElementById('prActual');
    pr.siguiente = document.getElementById('prSiguiente');
    pr.notas = document.getElementById('prNotas');
    pr.contador = document.getElementById('prContador');
    pr.reloj = document.getElementById('prReloj');
    document.getElementById('prAnt').onclick = function () { ir(actual - 1); };
    document.getElementById('prSig').onclick = function () { ir(actual + 1); };
    var inicio = Date.now();
    document.getElementById('prReloj0').onclick = function () { inicio = Date.now(); };
    setInterval(function () {
      var t = Math.floor((Date.now() - inicio) / 1000);
      pr.reloj.textContent = String(Math.floor(t / 60)).padStart(2, '0') + ':' + String(t % 60).padStart(2, '0');
    }, 500);
    document.title = 'Presentador · ' + document.title;
  }
  function pintarEn(marco, i) {
    marco.innerHTML = '';
    if (i >= total) { marco.innerHTML = '<div class="pr-fin">Fin de la presentación</div>'; return; }
    var escena = document.createElement('div');
    escena.className = 'escena';
    var copia = slides[i].cloneNode(true);
    copia.classList.add('activa');
    copia.style.transition = 'none';
    escena.appendChild(copia);
    marco.appendChild(escena);
    escena.style.transform = 'scale(' + (marco.clientWidth / 1920) + ')';
  }
  function pintarPresentador() {
    pintarEn(pr.actual, actual);
    pintarEn(pr.siguiente, actual + 1);
    var nota = slides[actual].querySelector('aside');
    pr.notas.innerHTML = nota ? nota.innerHTML : '<em>Sin notas para esta diapositiva.</em>';
    pr.contador.textContent = 'Diapositiva ' + (actual + 1) + ' de ' + total;
  }

  /* ---------- Navegación ---------- */
  function ir(i, desdeOtra) {
    i = limitar(i);
    actual = i;
    if (esPresentador) pintarPresentador(); else mostrar(i);
    try { history.replaceState(null, '', location.pathname + location.search + '#' + (i + 1)); } catch (e) {}
    if (!desdeOtra) avisar(i);
  }

  function abrirPresentador() {
    if (otraVentana && !otraVentana.closed) { otraVentana.focus(); return; }
    var url = location.href.split('#')[0].split('?')[0] + '?presentador=1#' + (actual + 1);
    otraVentana = window.open(url, 'becoach-presentador', 'width=1280,height=820');
  }
  function pantallaCompleta() {
    if (!document.fullscreenElement) { document.documentElement.requestFullscreen && document.documentElement.requestFullscreen(); }
    else { document.exitFullscreen && document.exitFullscreen(); }
  }

  document.addEventListener('keydown', function (e) {
    if (e.target && /INPUT|TEXTAREA|BUTTON|VIDEO/.test(e.target.tagName) && e.key === ' ') return;
    var k = e.key;
    if (k === 'ArrowRight' || k === 'ArrowDown' || k === 'PageDown' || k === ' ' || k === 'Enter') { e.preventDefault(); ir(actual + 1); }
    else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 'PageUp' || k === 'Backspace') { e.preventDefault(); ir(actual - 1); }
    else if (k === 'Home') { ir(0); }
    else if (k === 'End') { ir(total - 1); }
    else if ((k === 'f' || k === 'F') && !esPresentador) { pantallaCompleta(); }
    else if ((k === 'p' || k === 'P') && !esPresentador) { abrirPresentador(); }
  });

  window.addEventListener('hashchange', function () { var i = leerHash(); if (i !== actual) ir(i); });

  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!d || !d.becoach) return;
    if (typeof d.ir === 'number' && d.ir !== actual) ir(d.ir, true);
    if (d.pedir && otraVentana) avisar(actual);
  });

  if (esPresentador) {
    construirPresentador();
    window.addEventListener('resize', pintarPresentador);
    ir(leerHash(), true);
    if (window.opener) { try { window.opener.postMessage({ becoach: true, pedir: true }, '*'); } catch (e) {} }
  } else {
    ajustarEscala();
    window.addEventListener('resize', ajustarEscala);
    ir(leerHash(), true);
    deck.addEventListener('click', function (e) { if (!e.target.closest('a, video')) ir(actual + 1); });
    var toque = null;
    deck.addEventListener('touchstart', function (e) { toque = e.touches[0].clientX; }, { passive: true });
    deck.addEventListener('touchend', function (e) {
      if (toque === null) return;
      var dx = e.changedTouches[0].clientX - toque;
      if (Math.abs(dx) > 50) ir(actual + (dx < 0 ? 1 : -1));
      toque = null;
    });
    var ayuda = document.createElement('div');
    ayuda.className = 'ayuda';
    ayuda.textContent = 'F: pantalla completa · P: vista de presentador · ← →: navegar';
    document.body.appendChild(ayuda);
    var temporizador = null;
    function mostrarAyuda() {
      ayuda.classList.add('visible');
      document.body.classList.remove('sin-cursor');
      clearTimeout(temporizador);
      temporizador = setTimeout(function () { ayuda.classList.remove('visible'); document.body.classList.add('sin-cursor'); }, 2500);
    }
    document.addEventListener('mousemove', mostrarAyuda);
    mostrarAyuda();
  }
})();
