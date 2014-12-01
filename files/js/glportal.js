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

$('#particles').particleground();
