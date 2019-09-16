# 3DGalerie
<p>
  Cílem tohoto projektu je vytvořit webovou aplikaci pro zobrazení 3D modelů za pomoci technologie WebGL, kterou používá three.js a webového frameworku Django s databází MongoDB.   
</p>
<hr>
<h2>Harmonogram práce:</h2>
<ol>
  <li><h3>Three.js</h3>
  <ul>
    	<li>Vytvoření stránky s linkem na veškeré Javascript knihovny ✓</li>
      <li>Vytvoření scény s kamerou ✓</li>
      <li>Načtení objektu ze souboru a umístění do scény ✓</li>
      <li>Načtení textur ze souboru a namapování na objekt</li>
      <li>Ovládání kamery - přibližování, oddalování, rotace kolem objektu</li>
      <li>Ovládání světla ve scéně</li>
  </ul>
  </li>
  <li><h3>Django</h3><ul>
      <li>Instalace frameworku a potřebných součástí, spojení s MongoDB</li>
      <li>Vytvoření databázového modelu, migrace db</li>
      <li>Vytvoření administrátorského rozhraní</li>
      <li>Vytvoření url pro stránky</li>
      <li>Vytvoření Views</li>
      <li>Vytvoření stránek v templatovacím systému</li>
      <li>Vytvoření formulářů a validace dat s ukládáním souborů do db</li>
      <li>Dodělání CRUD modelu</li>
      <li>Implementace three.js a předávání souborů do JS</li>
    </ul>
  </li>
</ol>
<hr>
<h2>Práce na projektu</h2>
<ul>
<li>4.9.2019 – Tutoriál: https://docs.djangoproject.com/en/2.2/intro/tutorial01/ 
Začátek s frameworkem Django, vytváření webové aplikace dle tutoriálu. Instalace Django, instalace Djongo (MongoDB ovladače pro Django). Routování, vytváření View, nastavení spojení s databází MongoDB. Tutoriál pro templatovací systém Django.<br> <i>Čas: <b>2 hodiny</b></i></li>
<hr>
<li>5.9.2019 – Testy v Django
  Tutoriál: https://docs.djangoproject.com/en/2.2/intro/tutorial06/<br> <i>Čas: <b>2 hodiny</b></i></li>
<hr>
<li>6.9.2019 – Úvod do three.js
Začátek s knihovnou three.js, importování souborů OBJ a MTL, pochopení základní logiky knihovny, seznámení se s hlavními funkcemi. <br><i>Čas: <b>2 hodiny</b></i></li>
<hr>
<li>14.9.2019 – Three.js začátek vývoje
Vytvoření statické stránky pro vykreslování 3 D objektů, kterou poté bude nutno převést do dynamické verze s použitím načtení objektů z databáze. 
Požívané zdroje: https://www.creativebloq.com/how-to/get-started-with-webgl-using-threejs <br><i>Čas: <b>2 hodiny</b></i></li>
<li>16. 9. 2019 - Vyřešeno načítání textur a aplikace na objektu, zatím pouze 1 textura. <br><i>Čas: <b>1 hodina</b></i></li>
  <hr>
</ul>

<h2>Problémy: </h2>
<ul>
  <li>Nelze pouze nastavit renderer na vlastní canvas, nutno vytvořit přes three.js a připojit za jiný HTML element <b>(vyřešen)</b></li>
  <li>Nefunguje zobrazení MTL a OBJ souborů ve scéně (chybějící světla) <b>(vyřešen)</b></li>
  <li>Nedaří se exportovat textury z 3ds Maxu, při opětovném importu se nezobrazí, vyřešeno </li>
</ul>