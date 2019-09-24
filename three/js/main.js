var rendererElement = document.getElementById("renderer");

var width = window.innerWidth / 2;
var height = window.innerHeight / 2;
var viewAngle = 75;
var lightIntensity = 1.0; //Intenzita světla ve scéně
var nearClipping = 0.1; //Blízká ořezávací rovina, cokoliv je před touto vzdáleností se nebude renderovat
var farClipping = 100; //Vzdálená ořezávací rovina, cokoliv je za touto rovinou se nebude renderovat
var renderer = new THREE.WebGLRenderer(); //Vytvoření rendereru s nastavením canvasu pro renderování
var scene = new THREE.Scene(); //Vytvoření objektu scény
var camera = new THREE.PerspectiveCamera(viewAngle, width / height, nearClipping, farClipping); //Vytvoření a nastavení kamery
var controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.mouseButtons = {
    LEFT: THREE.MOUSE.PAN,
    MIDDLE: THREE.MOUSE.DOLLY,
    RIGHT: THREE.MOUSE.ROTATE
}
renderer.setSize(width, height); //Nastavení velikosti rendereru
rendererElement.appendChild(renderer.domElement);
controls.update();

/* Vytvoření kostky pro testování umístění objektu do scény */
/*var cubeGeometry = new THREE.BoxGeometry(1, 1, 1); //Geometrie kostky
var cubeMaterial = new THREE.MeshBasicMaterial({ color: 0xff00000 }); //Barva nebo textura kostky
var cube = new THREE.Mesh(cubeGeometry, cubeMaterial); //Objekt kostky
//Upravení pzice kostky, aby nebyla v kameře
cube.position.x = -2;
cube.position.z = -5;
//Přidání kostky do scény
scene.add(cube);*/

//Vytvoření osvětlení
scene.add(camera);
var keyLight = new THREE.DirectionalLight(new THREE.Color('hsl(30, 100%, 75%)'), lightIntensity);

var backLight = new THREE.DirectionalLight(0xffffff, 0.2);
backLight.position.set(100, 0, -100).normalize();

keyLight.name = "light";
camera.add(keyLight);
scene.add(backLight);

//Zaměření kamery na objekt
function fitCameraToObject(camera, object, offset, controls) {

    offset = offset || 1.25;

    const boundingBox = new THREE.Box3();

    // Získání ohraničujícího boxu objektu
    boundingBox.setFromObject(object);

    const center = boundingBox.getCenter();

    const size = boundingBox.getSize();

    //Získání maximální velikosti ohraničujícího boxu (aby seděl na šířku a výšku)
    const maxDim = Math.max(size.x, size.y, size.z);
    const fov = camera.fov * (Math.PI / 180);
    let cameraZ = Math.abs(maxDim / 4 * Math.tan(fov));

    cameraZ *= offset; //Oddálení kamery, aby objektu nebyl přesně na kraji obrazovky

    camera.position.z = cameraZ;

    const minZ = boundingBox.min.z;
    const cameraToFarEdge = (minZ < 0) ? -minZ + cameraZ : cameraZ - minZ;

    camera.far = cameraToFarEdge * 4;
    camera.updateProjectionMatrix();

    if (controls) {

        //Nastavení zaměření kamery na střed objektu
        controls.target = center;

        //Zabránění kamery, aby nešla přes vzdálenou ořezávací rovinu, tedy aby se nestalo, že objekt zmizí
        controls.maxDistance = cameraToFarEdge / 2;

        controls.saveState();

    } else {

        camera.lookAt(center)

    }
}

//Načtení více textur (později dokončit)
/*const loadManager = new THREE.LoadingManager();
const loader = new THREE.TextureLoader(loadManager);

const materials = [
    new THREE.MeshBasicMaterial({
        map: loader.load('/models/textures/gorshok.jpg')
    }),
    new THREE.MeshBasicMaterial({
        map: loader.load('/models/textures/leaf_normal.jpg')
    }),
    new THREE.MeshBasicMaterial({
        map: loader.load('/models/textures/leaf.jpg')
    }),
    new THREE.MeshBasicMaterial({
        map: loader.load('/models/textures/moh.jpg')
    }),
    new THREE.MeshBasicMaterial({
        map: loader.load('/models/textures/sand_normal.jpg')
    }),
    new THREE.MeshBasicMaterial({
        map: loader.load('/models/textures/sand.jpg')
    }),
    new THREE.MeshBasicMaterial({
        map: loader.load('/models/textures/stem.jpg')
    }),
];

//Načtení textury
var textureLoader = new THREE.TextureLoader();
var texture = textureLoader.load("/models/textures/leaf.jpg");
var material = new THREE.MeshPhongMaterial({map: texture});*/


var mtlLoader = new THREE.MTLLoader(); //Načítání materiálů objektu
mtlLoader.setPath("models/");
mtlLoader.load("01Alocasia_obj.mtl", function (materials) {
    materials.preload();

    var objLoader = new THREE.OBJLoader(); //Načtení objektu
    objLoader.setPath("models/");
    objLoader.load("01Alocasia_obj.obj", function (model) {
        model.position.set(0, 0, -50); //Posunutí objektu, aby nebyl v kameře
        model.name = "Objekt";
        /*loadManager.onLoad = () => { //Načítání textur, dodělat později
            model.traverse(function (node) {
                if (node.isMesh) {
                    
                }
            });
        };*/

        scene.add(model); //Přidání objektu do scény
        console.log(model);
        fitCameraToObject(camera, model, 2, controls); //Nastavení kamery na zaměření objektu
    });
});

function animate() { //Vykreslovací funkce volaná v nekonečném cyklu
    controls.update();
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

animate();

/* Slider pro nastavení světla ve scéně */
var slider = document.getElementById("light");
var output = document.getElementById("out");
output.innerHTML = slider.value; // Zobrazení základní hodnoty

// Aktualizace hodnot ze slideru
slider.oninput = function () {
    var light = scene.getObjectByName("light");
    light.intensity = (this.value/10);
    output.innerHTML = this.value;
}

/* JQuery area */

$(function () {
    $("#camReset").click(function () {
        fitCameraToObject(camera, scene.getObjectByName("Objekt"), 2, controls);
    });
})