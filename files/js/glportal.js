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

$('.particles').particleground({
    dotColor: '#595959',
    lineColor: '#595959',
    density: 60000,
    parallax: false,
    maxSpeedX: 0.1,
    maxSpeedY: 0.1
});
