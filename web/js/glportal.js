$( document ).ready(function() {
    window.sr = new scrollReveal();
});

$('#teamDev a').click(function (e) {
  e.preventDefault()
  $(this).tab('teamDev')
})

$('#teamWrit a').click(function (e) {
  e.preventDefault()
  $(this).tab('teamWrit')
})

//$('.particles').particleground({
//    dotColor: '#595959',
//    lineColor: '#595959',
//    density: 50000,
//    parallax: false,
//    maxSpeedX: 0.1,
//    maxSpeedY: 0.1
//});

//$('a.modal-btn').on('click', function(e) {
//    e.preventDefault();
//    var url = $(this).attr('href');
//    $('a.modal-btn').after('<iframe width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" src="' + url + '"></iframe>');
//});​
