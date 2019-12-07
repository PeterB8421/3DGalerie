$(function(){
    $("#nonRequiredFields").hide();
    $("#continue").on("click", validateRequired);

    function validateRequired(){
        var author = document.getElementById("id_author").value;
        var name = document.getElementById("id_name").value;
        var obj = document.getElementById("id_obj_file").value;
        if(author == "" || name == "" || obj == ""){
            $("#formsMsgs").show(100);
            $("#formMsgs").html("<p class=\"error\">Nejsou vyplněna všechna vyžadovaná pole!</p>");
            setTimeout(function(){
                $("#formMsgs").hide(100);
            }, 5000);
        }
        else{
            console.log("Form filled");
        }
    }
});

