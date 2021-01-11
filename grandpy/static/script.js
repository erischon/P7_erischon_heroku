
$(document).ready(function(){
            
    $("#form").submit(function(e){

        e.preventDefault()

        textinlivebox = $("#livebox").val();

        $.ajax({
            method:"post",
            url:"/livesearch",
            data:{text:textinlivebox},

            beforeSend: function(){
                // Show loader & hide sections
                $("#loader").show();
                $("#responseElement").hide();
                $("#responseNone").hide();

                // Clear all the ID's
                var items = document.querySelectorAll("#result_query, #result_name, #result_address, #result_wiki_title, #result_wiki_text, #map");
                for (var i = 0; i < items.length; i++) {
                    items[i].innerHTML = "";
                }
               },
            
            success: function(res){
                // Show response

                console.log(res);
                // If there is no response
                if (res["parsing"] == false) {
                    $("#responseNone").show();
                    $("#result_none").text(
                        "Désolé je n'ai pas de réponse pour cette requête.");
                }
                // If there is a response from Google
                if (res["gresult"] == true) {            
                    $("#responseElement").show();
                    response(res)
                    initMap(res)
                    // If there is a response from Wiki
                    if (res["wresult"] == true) {
                        wikiResponse(res)
                    }
                    // If there is no response from Wiki
                    else {
                        $("#result_wiki").text("Désolé, je n'ai pas trouvé d'histoire intéressante à raconter...");
                    }          
                }
                // If there is no response from Google
                else {
                    $("#responseNone").show();
                    $("#result_none").text("Désolé je n'ai pas de réponse pour cette requête.");
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
    $("#result_query").text(res["query"]);
    $("#result_name").text(res["ginfos"]["name"]);
    $("#result_address").text(res["ginfos"]["formatted_address"]);
}

function wikiResponse(res) {
    $("#result_wiki_title").text(
        "J'ai une petite info sur " + res["wtitle"] + " :"
        );
    $("#result_wiki_text").text(
        "Peut-être ne le saviez-vous pas, mais " + res["wtext"] + " Intéressant non ?!"
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
