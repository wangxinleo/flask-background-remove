$(function () {
    $('nav#menu').mmenu();
    $("#back-to-top").click(function(){
        //$('body,html').animate({scrollTop:0},1000);
        if ($('html').scrollTop()) {
            $('html').animate({ scrollTop: 0 }, 1000);
            $("#testList").click();
            return false;
        }
        $('body').animate({ scrollTop: 0 }, 1000);
        return false;
    });

});
jQuery(document).ready(function($) {
    $(".scroll").click(function(event){
        event.preventDefault();
        $('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
    });
});
$().UItoTop({ easingType: 'easeOutQuart' });



