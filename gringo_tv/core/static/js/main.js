$(function(){
  url = window.location.pathname;
  $('.sidebar .sidebar-menu [href="'+url+'"]').parent().addClass('active');
});
