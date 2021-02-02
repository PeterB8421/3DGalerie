# 3DGalerie
<p>
  Cílem tohoto projektu je vytvořit webovou aplikaci pro zobrazení 3D modelů za pomoci technologie WebGL, kterou používá three.js a webového frameworku Django s databází MongoDB.
</p>
<hr>
<b>
  Instalace
  </b>
  <p>
  Pro spuštění je třeba mít Python verze <b> 3.5 nebo vyšší </b><br>
  Pro fungování projektu je nutno mít nainstalovaný funkční databázový systém, který je podporován Djangem. Poté stačí nastavit v <i>/gallery/gallery/settings.py</i> v konstantě DATABASES vaši používanou databázi (<a href=https://docs.djangoproject.com/en/3.1/ref/databases/> Zde </a> naleznete seznam základně podporvaných databázových systémů a jejich potřebné balíky pro správnou funkci). Ze základu je databázový systém nastaven na <a href=https://www.mongodb.com/>MongoDB</a>. <br>
  Poslední krok ke spuštění je sputit v <i>/gallery/</i> skript </i>manage.py</i> následovně: <b>py manage.py runserver</b> v případě požadavku akcí s databází, spusťte požadovaný příkaz, jinak projekt nebude fungovat.
  </p>
  <hr>
  <b> Použití </b>
  <p>
  Tento projekt umožňuje použít spojený databázový systém a přiložený renderer <a href=https://threejs.org/>three.js</a> pro uložení a následné prohlížení libovolného 3D modelu. Tyto modely je nutno mít uloženy ve formátu <b>.obj</b>, případně s přiloženým souborem <b>.mtl</b>, kde jsou uloženy materiály scény. Projekt neumožňuje ukládání textur a jejich mapování na objekty.
  </p>
  
