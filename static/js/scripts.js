function openSlideMenu() {
  document.getElementById('menu').style.width = '250px';
  document.getElementById('sidenav').style.marginLeft = '250px';
}
function closeSlideMenu() {
  document.getElementById('menu').style.width = '0';
  document.getElementById('sidenav').style.marginLeft = '0';
}

// Tooltips Initialization
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})