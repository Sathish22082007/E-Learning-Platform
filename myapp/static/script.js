/* Please ❤ this if you like it! */


(function($) { "use strict";

	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {    
			var scroll = $(window).scrollTop();
		
			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});		
		
	//Animation
	
	$(document).ready(function() {
		$('body.hero-anime').removeClass('hero-anime');
	});

	//Menu On Hover
		
	$('body').on('mouseenter mouseleave','.nav-item',function(e){
			if ($(window).width() > 750) {
				var _d=$(e.target).closest('.nav-item');_d.addClass('show');
				setTimeout(function(){
				_d[_d.is(':hover')?'addClass':'removeClass']('show');
				},1);
			}
	});	
	
	//Switch light/dark
	
	$("#switch").on('click', function () {
		if ($("body").hasClass("dark")) {
			$("body").removeClass("dark");
			$("#switch").removeClass("switched");
		}
		else {
			$("body").addClass("dark");
			$("#switch").addClass("switched");
		}
	});  

	var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 5,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-nexts",
    prevEl: ".swiper-button-prevs",
  },
  mousewheel: true,
  keyboard: true,
  loop: true,
  breakpoints: {

    300: {
      slidesPerView: 1
    },

    501: {
      slidesPerView: 1
    },

    769: {
      slidesPerView: 3,
      spaceBetween: 10
    },
    1025: {
      slidesPerView: 3,
      spaceBetween: 10
    },
  }
});

document.querySelector("#home-hero-section")
	
  })(jQuery);