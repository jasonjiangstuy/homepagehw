window.onload = run
function run(){

const indextext1 = 'On a second note, I do not have time to build that whole walkthrough, I\'m sorry but ur on your own, Peace!!!(mic drop)' ;


var pointer = 0;
var holdstring;
var myWalk = document.querySelector('#display-screen');
var texttimer
firststory(endwalkthrough)
function firststory(){
writescript(indextext1, function() {
});
}

function secondstory(){
writescript(indextext2, function() {
});
}
// const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#Common_mistakes

// function afterme(myfunction, text, callback){
//   setTimeout( writescript(myfunction, text, callback), 3000);
// }
function writescript(text, callback){
  setTimeout(texttimer = setInterval(index, 60, text, callback), 3000);
  return 1
}

function index(text, callback) {
  // console.log(text.length);
  // console.log(pointer);
  // console.log(pointer < text.length);
  if (pointer < text.length){
    pointer += 1;
    holdstring = text.slice(0, pointer);
    myWalk.innerText = holdstring;
  }
  else {
    clearInterval(texttimer)
    endwalkthrough()
    callback()
  }
}

function endwalkthrough(){
  console.log("ending walkthrough...");
  clearInterval(texttimer)
  console.log("returning to current page...")
  const currentUrl = document.URL
  const baseUrl = currentUrl.split('/?');
  console.log(baseUrl[0]);
  window.location.href = baseUrl[0];

  //learning js using dev docs + stack over flow to find the functions i need
  //also a lot of googling to understand jargen
}
}
