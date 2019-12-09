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
      <li>Ovládání kamery - přibližování, oddalování, rotace kolem objektu, s omezením ✓</li>
      <li>Ovládání světla ve scéně ✓</li>
      <li>Načtení textur ze souboru a namapování na objekt (řešené přes MTL soubor) ✓</li>
  </ul>
  </li>
  <li><h3>Django</h3><ul>
      <li>Instalace frameworku a potřebných součástí, spojení s MongoDB ✓</li>
      <li>Vytvoření databázového modelu, migrace db ✓</li>
      <li>Vytvoření administrátorského rozhraní ✓</li>
      <li>Vytvoření Views ✓</li>
      <li>Vytvoření url pro stránky ✓</li>
      <li>Vytvoření stránek v templatovacím systému ✓</li>
      <li>Vytvoření formulářů a validace dat s ukládáním souborů do db ✓</li>
      <li>Dodělání CRUD modelu ✓</li>
      <li>Implementace three.js a předávání souborů do JS ✓</li>
      <li>Multi File Upload pro galerii ✓</li>
      <li>Validace OBJ souborů při vytváření záznamu</li>
      <li>Vytvoření uživatelů a systému s přístupem k administraci ✓</li>
      <li>Zlepšit tagy</li>
      <li>Vyhledávání v modelech</li>
      <li>Styly na stránce</li>
      <li>AJAX na stránky ✓</li>
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
<hr>
<li>16. 9. 2019 - Vyřešeno načítání textur a aplikace na objektu, zatím pouze 1 textura. <br><i>Čas: <b>1 hodina</b></i></li>
<hr>
<li>18. 9. 2019 - Práce s více texturami odložena na později, řešení ovládání ve scéně. Osvětlení vyřešeno, chybí slider pro dynamické nastavování osvětlení ve scéně. Textury se momentálně nebudou zobrazovat, pokračovat u jejich zobrazování budu někdy v budoucnu. https://stackoverflow.com/a/16463562<br><i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>24. 9. 2019 - Odstranění stávajícího slideru pro ovládání intenzity osvětlení, nefunkční. Hledání alternativy. Alternativa nalezena na W3Schools (https://www.w3schools.com/howto/howto_js_rangeslider.asp). Ovládání intenzity světla funkční.<br>Vytvoření projektu Django do složky gallery, složka three obsahuje statickou stránku s vykreslováním objektů, které implementuji do Djanga později.<br>Nainstalován Django framework a propojen s MongoDB.<br>Vytvoření databázového modelu a připojení k Django systému, provedena migrace.<br>Vytvoření administrátorského rozhraní. <br> <i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>25. 9. 2019 - Vytvoření Views a namapování URL stránek. Vytvoření odezvy na dotaz na stránku, později dodělám vrácení templatu. <br> <i>Čas: <b>1 hodina</b></i></li>
  <hr>
  <li>30. 9. 2019 - Úprava modelu s přidanou validací a úprava časového pásma v nastavení. Vytvoření hlavní stránky, nutno nadesignovat. <br> <i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>2. 10. 2019 - Vytvoření složky pro statické soubory (https://help.pythonanywhere.com/pages/DjangoStaticFiles/). Vytvoření formuláře pro vložení dat (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms, špatný tutoriál). Později dokončím. <br> <i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>3. 10. 2019 - Renderování formuláře na stránku a ověření, zda funguje validace. Změněn validátor pro přípony souborů v models.py, aby používal modul z pythonu. <br> <i>Čas: <b>1 hodina</b></i></li>
  <hr>
  <li>7. 10. 2019 - Zprovoznění uploadu souboru (https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html). Validace formuláře (https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/). Přidání flash message (https://docs.djangoproject.com/en/2.2/ref/contrib/messages/). Vytvoření složky pro statické soubory (css, js...) v modulu objectGallery.<br><i>Čas: <b>3 hodiny</b></i>
  <hr>
  <li>8. 10. 2019 - Vytvoření editačního formuláře a mazání záznamů z databáze (https://stackoverflow.com/questions/4673985/how-to-update-an-object-from-edit-form-in-django).
  <br><i>Čas: <b>2 hodiny</b></i>
  <hr>
  <li>13. 10. 2019 - Vytvoření stránky pro zovrazení detailu modelu. Nutno dořešit zobrazení obrázků.<br><i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>16. 10. 2019 - Zobrazení obrázků dořešeno, testování ajax requestů s Djangem (https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html), pro předávání souborů použito URL na stránce, přes které loader je schopný načíst požadované soubory. <br><i>Čas: <b>2 hodiny</b></i></li>
  <li>24. 10. 2019 - Uživatelský systém v Djangu (https://docs.djangoproject.com/en/2.2/topics/auth/).<br><i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>29. 10. 2019 - Dokončení uživatelského systému. <br><i>Čas: <b>1 hodina</b></i>
  <hr>
  <li>6. 11. 2019 - Testování Multiple file uploadu na separátním projektu, oprava requirements.txt.<br><i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>11. 11. 2019 - Multiple File Upload testování <br><i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>14. 11. 2019 - Galerie obrázků k modelům, CRUD model, mazání souborů, zprovoznění cizího klíče, implementace Multiple File Uploadu. <br><i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>20. 11. 2019 - Zprovoznění textur v three.js, úprava modelu v Djangu, již nevyžaduje MTL soubor, není-li k dispozici MTL soubor, renderer nastaví modelu barvu jako materiál. <br><i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>21. 11. 2019 - Přidání ajax requestů pro mazání modelů a obrázků. Oprava mazání MTL souboru z modelu.<br><i>Čas: <b>2 hodiny</b></i></li>
  <hr>
  <li>4. 12. 2019 - Předělání formuláře pro vstup na ajax. <br><i>Čas: <b>1 hodina</b></i></li>
  <hr>
  <li>7. 12. 2019 - Validace formuláře v JS. <br><i>Čas: <b>1 hodina</b></i></li>
  <hr>
  <li>9. 12. 2019 - Zprovoznění části formuláře ve form-ajax branchi. <br><i>Čas: <b>1 hodina</b></i></li>
</ul>

<h2>Problémy: </h2>
<ul>
  <li>Nelze pouze nastavit renderer na vlastní canvas, nutno vytvořit přes three.js a připojit za jiný HTML element <b>(vyřešen)</b></li>
  <li>Nefunguje zobrazení MTL a OBJ souborů ve scéně (chybějící světla) <b>(vyřešen)</b></li>
  <li>Nedaří se exportovat textury z 3ds Maxu, při opětovném importu se nezobrazí <b>(vyřešen)</b> </li>
  <li>Načítání více textur a správné aplikování na objekt (https://stackoverflow.com/questions/16491238/three-js-assign-material-color-to-object) <b>(vyřešen)</b></li>
  <li>Slider si automaticky nastavuje výšku na 0px a nechce se nechat přemluvit přes CSS. https://getbootstrap.com/docs/4.1/components/forms/#range <b>(vyřešen)</b></li>
  <li>Při odeslání formuláře se data neodešlou a nezpracují, pole pro soubory OBJ a MTL píší "This field is required", ikdyž tam je soubor <b>(vyřešen)</b></li>
  <li>URL na obrázek nahraný uživatelem vrací 404, na stránce se nenačte. (<b>vyřešeno</b>, špatné URL)</li>
  <li>Multiple file upload problémy
    <li>Cizí klíče v Djangu https://stackoverflow.com/questions/30017334/django-foreign-key-must-be-an-instance(<b>Vyřešeno</b>)
    </li>
  </li>
  <li>Volba správného typu materiálu v THREE.js</li>
</ul>
