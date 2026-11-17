/* Galeria na stronie głównej: 2 najnowsze albumy + 2 losowe, a jako "twarz"
   każdego albumu losowe zdjęcie z niego. Losowanie przy każdym wejściu na stronę.
   Bez JavaScriptu zostaje wersja wylosowana podczas budowania strony. */
(function () {
  var data = document.getElementById("gal-data");
  var strip = document.querySelector(".strip[data-gal]");
  if (!data || !strip) return;

  var d;
  try { d = JSON.parse(data.textContent); } catch (e) { return; }
  if (!d.newest || !d.newest.length) return;

  function pick(list) { return list[Math.floor(Math.random() * list.length)]; }

  var pool = d.pool.slice();
  for (var i = pool.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var t = pool[i]; pool[i] = pool[j]; pool[j] = t;
  }
  var albums = d.newest.concat(pool.slice(0, 2));

  strip.textContent = "";
  albums.forEach(function (a) {
    if (!a.p || !a.p.length) return;
    var el = document.createElement("a");
    el.className = "si";
    el.href = a.u;
    el.title = a.t;
    el.style.backgroundImage = "url(" + pick(a.p) + ")";
    var yr = document.createElement("span");
    yr.className = "yr";
    yr.textContent = a.r;
    var nm = document.createElement("span");
    nm.className = "nm";
    nm.textContent = a.n;
    el.appendChild(yr);
    el.appendChild(nm);
    strip.appendChild(el);
  });
})();
