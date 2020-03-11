window.onload = function onload(){
  var elem = document.getElementById('main-image')
  var opacity = 0;
  var currentimageid = 0
  const baseUrl = "background-image: url('/static/imgs/slideshow/teampic"
  var imgUrl = ""
  elem.setAttribute("style", "background-image: url('/static/imgs/background_nuclear_plant.png')");
  var myFade = setInterval(frame, 16);
  slideshow()
  function slideshow(){//code for starting slideshow + activate buttons to change image
    //bind buttons
    var timer = setInterval(switchmyImg, 6000);
    function switchmyImg(){
      if (currentimageid < 7){
      currentimageid = currentimageid + 1;
      imgUrl = baseUrl.concat(currentimageid, ".png')");
      elem.setAttribute("style", imgUrl);
      opacity = 0;
      var myFade = setInterval(frame, 16);
    }
    else {
      currentimageid = 0
    }
    } //build sliding thing later
    //elem.style.
  }
  function frame() {
    if (opacity >= 1) { //fade in image
      clearInterval(myFade);
    }
    else {
      opacity = opacity + 0.01;
      elem.style.opacity = opacity;
    }
  }
}
