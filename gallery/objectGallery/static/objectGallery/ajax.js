$(function () { 
    $(".ajax").click(function(e){
        e.preventDefault();
        $.ajax({
            url: $(this).attr("href") + "ajax/",
            success: function (response) { 
                if(response.status){
                    $("#model"+response.id).html("<p class=\"del\">Smazáno</p>");
                    setTimeout(function(){
                        $("#ajaxMsg").hide(100);
                    }, 5000);
                }
                else{
                    $("#ajaxMsg").html("<p class=\"error\">"+ response.type +" se nepodařilo smazat!</p>");
                    setTimeout(function(){
                        $("#ajaxMsg").hide(100);
                    }, 5000);
                }
             },
             error: function(){
                 $("#ajaxMsg").html("<p class=\"error\">Nastala chyba při zpracování požadavku!</p>");
             }
        })
    })
 })