$(document).ready(function(){
  $('a, i').click(function(){
    $('html, body').animate({
      scrollTop: $($(this).attr('href')).offset().top
    }, 500);
    return false;
  });

  $('.clickone').click(function(){
    $('.header').fadeOut(400);
    $('.menu').fadeIn('slow').delay(800);
  });

  $('.clicktwo').click(function(){
    $('.menu').fadeOut(400);
    $('.header').fadeIn(800);
  });
});
