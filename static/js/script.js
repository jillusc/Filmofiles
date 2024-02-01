function removeAlert() {
  var alert = document.querySelector('.alert-message');
  if (alert) {
    alert.remove();
  }
}

document.addEventListener('click', function (event) {
  if (!event.target.closest('.alert')) {
    removeAlert();
  }
});

var backLink = document.getElementById('back-link');

backLink.addEventListener('click', function (event) {
    event.preventDefault();
    history.go(-1);
});