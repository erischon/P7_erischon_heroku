
$(document).ready(function(){
            
    $("#form").submit(function(e){

        e.preventDefault()

        textinlivebox = $("#livebox").val();

        $.ajax({
            method:"post",
            url:"/livesearch",
            data:{text:textinlivebox},

            beforeSend: function(){
                // Show loader
                $("#loader").show();
               },
            
            success: function(res){
                // Show response

                $("#responseElement").show();

                if (res["gresult"] == true) {
                    response(res)
                    initMap(res)
                }
                else {
                    $("#result_name").append("Désolé je n'ai pas de réponse.");
                }

                if (res["wresult"] == true) {
                    wikiResponse(res)
                }
                else {
                    $("#result_wiki").append("Désolé, je n'ai pas trouvé d'histoire intéressante à raconter...");
                }                
            },

            complete:function(data){
                // Hide loader
                $("#loader").hide();
               }
        })
    });

})

function response(res) {
    $("#result_query").append(
        "Vous m'avez questionnez à propos de : " + "<strong>" + res["query"] + "</strong>"
        );
    $("#result_name").append(
        "Voici ce que j'ai trouvé dans mes petites fiches bien rangées : " + "<strong>" + res["ginfos"]["name"] + "</strong>"
        );
    $("#result_address").append(
        "Et c'est à cette adresse : " + "<strong>" + res["ginfos"]["formatted_address"] + "</strong>"
        );
}

function wikiResponse(res) {
    $("#result_wiki_title").append(
        "J'ai une petite info sur " + res["wtitle"] + " :"
        );
    $("#result_wiki_text").append(
        "Peut-être ne le saviez-vous pas, mais " + "<strong>" + res["wtext"] + "</strong>" + " Intéressant non ?!"
        );
}

function initMap(res) {
    const target = { lat: res["gcoord_lat"], lng: res["gcoord_lng"] };

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: target,
    });

    const marker = new google.maps.Marker({
    position: target,
    map: map,
    });
}
