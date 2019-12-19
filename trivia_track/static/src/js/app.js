/**
 * Created by miguel on 20/12/18.
 */
var correctAnswers = 0;
var counter = 0;
const TOTAL = 50;
var questions = [];
fetch('https://opentdb.com/api.php?amount=' + TOTAL + '&difficulty=hard&type=boolean')
    .then((response) => {
        console.log(response);
        return response.json();
    }).then((data) => {
    console.log(data);
    questions = data
});
$(function () {

    var el = document.getElementById('total_questions').innerText = TOTAL
// TRUE/FALSE OPTION
    $(document).on('click', '.other_option', function () {
        $('.info').empty();
        $('.multiple_option').hide();
        var data = questions
        let category = data.results[counter].category
        let difficult = data.results[counter].difficulty
        let question = data.results[counter].question
        let allAnswers = [];

        allAnswers.push(data.results[counter].correct_answer)
        allAnswers.push(data.results[counter].incorrect_answers[0])
        allAnswers.sort();

        $('.info').append(`<h5 class="inf">${category}</h5> 
        <h5 class="inf"> Difficulty: ${difficult}</h5>
        <h3 class="question">${question}</h3><div>
        <div><button class="options btn-default btn">${allAnswers[0]}</button></div>
        <div><button class="options btn-default btn" >${allAnswers[1]}</button></div>
       `);

        $('.options').on('click', function () {
            if ($(this).text() === data.results[counter].correct_answer && counter !== TOTAL) {
                $('.info').empty();
                $('.other_option').show();
                $('.other_option').text('Next');
                correctAnswers++;
                $("#gran_total").text(correctAnswers)
            }
            if ($(this).text() !== data.results[counter].correct_answer && counter !== TOTAL) {
                $('.info').empty();
                $('.other_option').show();
                $('.other_option').text('Next');

            }
            counter++;

            if (counter === TOTAL) {

                $('.info').empty();
                $('.other_option').hide();
                $('.info').append(`<button class=" finish_trivia_track btn-default btn">ENVIAR RESPUESTAS</button>
                                        <h4>Your results</h4><h5>You got ${correctAnswers} out of ${TOTAL}</h5>`)

            }

        });

    });
    $(document).on('click', '.finish_trivia_track', function (event) {
        event.preventDefault();
        srq.simpleRequest({
            'total_correct': correctAnswers
        }, '/page/save_trivia/', 'POST', 'json').then(function (data) {
            console.log(data);
            if (data.state == 200) {
                alert("Listo ya terminamos")
                location.reload();
            }
            else {
                alert("Al parecer ocurrio un error ")
            }

        })

    })
});
