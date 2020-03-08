var myWalk = document.querySelector('#display-screen')


var texttimer = setInterval(index, 13)
var pointer = 0
const indextest1 = ''' Welcome to my walkthrough, sit back, relax and enjoy the experience '''
const indextext2 = ''' In this walkthrough I will be walking though a summary of my life '''
const indextext3 = ''' And who I
function index(text) {
  myWalk.innerHTML =
}

function endwalkthrough(){
  console.log("ending walkthrough...");
  clearInterval(index)
  console.log("returning to current page...")
  const currentUrl = document.URL
  const baseUrl = currentUrl.split('/?');
  console.log(baseUrl[0]);
  Response.redirect(baseUrl[0], 302);

  //learning js using dev docs + stack over flow to find the functions i need
  //also a lot of googling to understand jargen
}
