$(function(){
    $("#id_tag").keypress(function(event){
        console.log(event);
        if(event.keyCode === 13 || event.keyCode === 10){
            event.preventDefault();
            console.log("Enter was pressed!");
        }
    })
})