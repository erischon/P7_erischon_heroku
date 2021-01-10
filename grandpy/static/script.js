
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
                $("#responseElement").hide();

                // Clear all the ID's
                var items = document.querySelectorAll("#result_query, #result_name, #result_address, #result_wiki_title, #result_wiki_text, #map");
                for (var i = 0; i < items.length; i++) {
                    items[i].innerHTML = "";
                }
               },
            
            success: function(res){
                // Show response
                $("#responseElement").show();

                if (res["gresult"] == true) {
                    response(res)
                    initMap(res)

                    if (res["wresult"] == true) {
                        wikiResponse(res)
                    }
                    else {
                        document.getElementById('result_wiki').innerHTML = "Désolé, je n'ai pas trouvé d'histoire intéressante à raconter...";
                        return
                    }           
                }
                else {
                    document.getElementById('result_name').innerHTML = "Désolé je n'ai pas de réponse.";
                    return
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
    document.getElementById('result_query').innerHTML = 
        "Vous m'avez questionnez à propos de : " + "<strong>" + res["query"] + "</strong>";
    document.getElementById('result_name').innerHTML =
        "Voici ce que j'ai trouvé dans mes petites fiches bien rangées : " + "<strong>" + res["ginfos"]["name"] + "</strong>";
    document.getElementById('result_address').innerHTML =
        "Et c'est à cette adresse : " + "<strong>" + res["ginfos"]["formatted_address"] + "</strong>";
}

function wikiResponse(res) {
    document.getElementById('result_wiki_title').innerHTML =
        "J'ai une petite info sur " + res["wtitle"] + " :";
    document.getElementById('result_wiki_text').innerHTML =
        "Peut-être ne le saviez-vous pas, mais " + "<strong>" + res["wtext"] + "</strong>" + " Intéressant non ?!";
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
