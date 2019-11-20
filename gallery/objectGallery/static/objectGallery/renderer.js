var obj_file;
var mtl_file;

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

console.log("MTL File val: "+document.getElementById("mtl_file").value);
console.log("MTL File type: "+ typeof(document.getElementById("mtl_file").value));
if (document.getElementById("mtl_file").value != "") { 
    var mtlLoader = new THREE.MTLLoader(); //Načítání materiálů objektu
    mtlLoader.load("/uploads/" + document.getElementById("mtl_file").value, function (materials) {
        materials.preload();

        var objLoader = new THREE.OBJLoader(); //Načtení objektu
        objLoader.setMaterials(materials); //Nastavení materiálů
        objLoader.load("/uploads/" + document.getElementById("obj_file").value, function (model) {
            model.position.set(0, 0, -50); //Posunutí objektu, aby nebyl v kameře
            model.name = "Objekt";

            scene.add(model); //Přidání objektu do scény
            console.log(model);
            fitCameraToObject(camera, model, 2, controls); //Nastavení kamery na zaměření objektu
        });
    });
} else {
    var mat = new THREE.MeshLambertMaterial({color: 0xFF0000});
    var objLoader = new THREE.OBJLoader(); //Načtení objektu
    objLoader.load("/uploads/" + document.getElementById("obj_file").value, function (model) {
        model.position.set(0, 0, -50); //Posunutí objektu, aby nebyl v kameře
        model.name = "Objekt";
        model.traverse(function(child){
            if(child instanceof THREE.Mesh)
                child.material = mat;
        })

        scene.add(model); //Přidání objektu do scény
        console.log(model);
        fitCameraToObject(camera, model, 2, controls); //Nastavení kamery na zaměření objektu
    });
}



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
    light.intensity = (this.value / 10);
    output.innerHTML = this.value;
}

/* jQuery area */
$(function () {
    $("#camReset").click(function () {
        fitCameraToObject(camera, scene.getObjectByName("Objekt"), 2, controls);
    });
});