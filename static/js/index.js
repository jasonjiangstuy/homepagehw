window.onload = function onload(){
  var elem = document.getElementById('main-image') 
  var opacity = 0;
  var id = setInterval(frame, 16);
  function frame() {
    if (opacity >= 1) {
      clearInterval(id);
    } else {
      opacity = opacity + 0.01;
      elem.style.opacity = opacity;
    }
  }
}
