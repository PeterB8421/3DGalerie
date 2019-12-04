for (var i = 0; i < document.getElementsByTagName("input").length; i++) {
    if (document.getElementsByTagName("input")[i].getAttribute("type") !== "submit")
        document.getElementsByTagName("input")[i].setAttribute("class", "form-control");
}
$(function () {
    $("textarea").attr({
        "class": "form-control"
    });
});