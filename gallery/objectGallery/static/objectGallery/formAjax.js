$(function(){
    $("#nonRequiredFields").hide();
    var filled = [];
    $("input[required]").on("change", function(){
        $("input[required]").each(function(element){
            console.log(element);
            if($(element).val() != ""){ //Je-li element vyplněn, zkontroluj, jestli už v poli vyplněných je, popř. ho přidej
                if(!filled.includes(element))
                    filled.push(element);
            }
            else{
                if(filled.includes(element)) //Není-li element vyplněn a v poli je, smaž jej
                    filled.splice(filled.indexOf(element), 1);
            }
        })
        if(filled.length == $("input[required]").length){ //Jsou-li všechny required elementy vyplněné, vypiš to, později se odkryjí nevyžadovaná pole a pošle ajax request
            console.log("All required filled");
        }
        else{
            console.log("All required NOT filled");
        }
    });
});
