/**
 * Created by miguel on 21/12/18.
 */
$(function () {
    var miInit = {
        method: 'POST',
    };
    $(".btnGetFolio").on('click', function () {
        $("#folio_tbody").html('')
        for (var i = 0; i < 3; i++) {

            fetch('/page/folioAleatorio/', miInit)
                .then((response) => {
                    console.log(response);
                    return response.json();
                }).then((data) => {
                console.log(data);
                for (var index in data.folio) {
                    let f = data.folio[index]
                    $("#folio_tbody").append(`<tr><td>${f.folio}</td><td>${f.user}</td></tr>`)
                }

            });
            // srq.simpleRequest({}, '/page/folioAleatorio/', 'POST', 'json').then(function (data) {
            //     console.log(data);
            // })
        }

    })
})