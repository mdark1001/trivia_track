/**
 * Created by miguel on 21/12/18.
 */
$(function () {
    $(".btnGetFolio").on('click', function () {

        for(var i = 0; i<10; i++) {
            srq.simpleRequest({}, '/page/folioAleatorio/', 'POST', 'json').then(function (data) {
                console.log(data);
                $("#folio").text(data['folio'][0])

            })
        }
    })
})