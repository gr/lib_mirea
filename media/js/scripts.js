$(document).ready(function() {

/* Placeholder for Search field */
  var searchLabel = 'В каталоге и на сайте';
  if ($('#search_field').val() == '' || $('#search_field').val() == searchLabel) {
  	$('#search_field').addClass('placeholder').val(searchLabel);
  }
  $('#search_field').focus(function() {
    if (this.value == searchLabel) {
      $(this).removeClass('placeholder').val('');
    };
  }).blur(function() {
    if (this.value == '') {
      $(this).addClass('placeholder').val(searchLabel);
    };
  });
  $('form#search_form').submit(function() {
    if ($('#search_field').val() == searchLabel) {
      $('#search_field').val('');
    }
  });
  
  $.smoothAnchors("fast", "swing", false);

/* CSS для неподдерживаемых ИЕ селекторов */
  if ($.browser.msie) {
		$("div#content.simple h2 + p").css({ marginTop:"0" });
		$("div#content.simple p + blockquote").css({ marginTop: "1.375em" });
		$("div#content.simple ul li").prepend("&mdash;&nbsp;");
		$("div#content p + p").css({ marginTop: "0" });
		$("div#content p + p").css({ textIndent: "2.75em" });
		$("div#events p + p").css({ marginTop: "0" });
		$("div#events p + p").css({ textIndent: "2.75em" });
  }

/* Special Pages Scripts */
/* Сборник трудов 55 */
	$("dl.ntk-list dd").hide();
	$("dl.ntk-list dt.part-3 a").click(function () {
      if ($("dl.ntk-list dd.part-3").is(":hidden")) {
        $("dl.ntk-list dd.part-3").slideDown("slow");
      } else {
        $("dl.ntk-list dd.part-3").slideUp("slow");
      }
    });
  $("dl.ntk-list dt.part-4 a").click(function () {
      if ($("dl.ntk-list dd.part-4").is(":hidden")) {
        $("dl.ntk-list dd.part-4").slideDown("slow");
      } else {
        $("dl.ntk-list dd.part-4").slideUp("slow");
      }
    });
});