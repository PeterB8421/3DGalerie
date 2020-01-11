$(function(){
    $("#id_tag").attr("placeholder", "Pro přidání tagu napište název a stiskněte ENTER");
    $("#id_tag").keypress(function(event){
        if(event.keyCode === 13 || event.keyCode === 10){
            event.preventDefault();
            console.log("Enter was pressed!");
            $.ajax({
                url: "/tagCreate/"+$("#model_id").val()+"/"+$("#id_tag").val()+"/",
                success: function(response, status){
                    console.log(response);
                    debugger;
                    var tags;
                    tags = $("#modelTags").html();
                    for(var i = 0; i < response.model_tags.length; i++){                        
                        $("#modelTags").html(tags + "<span class=\"glyphicon glyphicon-remove tag-remove\"></span><span class=\"tag\" data-id=\""+response.model_tags[i].id+"\">"+response.model_tags[i].tag+"</span>");
                    }
                    $("#id_tag").val("");
                },
                error: function(response, status){
                    $("#ajaxMsgs").show();
                    $("#ajaxMsgs").html("<p class=\"error\">Nastala chyba při přidávání tagu. Error: " + status + "</p>");
                    setTimeout(function(){
                        $("#ajaxMsgs").hide(100);
                    }, 5000);
                }
            })
        }
    });
    $(".tag-remove").click(function(){
        var tag_id = $(this).parent().attr("data-id");
        var model_id = $("#model_id").val();
        $.ajax({
            url: "/tagDelete/"+model_id+"/"+tag_id+"/",
            success: function(response, status){
                setTimeout(function(){
                    $("#ajaxMsgs").hide(100);
                }, 5000);
                $("span.tag[data-id="+tag_id+"]").hide(100);
            },
            error: function(response, status){
                $("#ajaxMsgs").show();
                    $("#ajaxMsgs").html("<p class=\"error\">Nastala chyba při mazání tagu. Error: " + status + "</p>");
                    setTimeout(function(){
                        $("#ajaxMsgs").hide(100);
                    }, 5000);
            }
        })
    })
})