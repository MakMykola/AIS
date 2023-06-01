$(document).ready(function () {
    $('.catalog').click(function (event) {
        $('.catalog,.category').toggleClass('active')
        $('body').toggleClass('lock')
    })
    $('.find').click(function (event) {
        $('.find,.findd').toggleClass('active')
        $('body').toggleClass('lock')
    })
      $('.sort').click(function (event) {
        $('.sort,.sort-t').toggleClass('active')
        $('body').toggleClass('lock')
    })
})