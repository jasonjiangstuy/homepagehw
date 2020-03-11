window.onload = run
function run(){
const indextext1 = 'Welcome to my walkthrough, sit back, relax and enjoy the experience. If you wish to be on your own, click anywhere on the screen to be free!! In this walkthrough I will be walking though the experiences and people who made me the person that I am today!!' ;


var pointer = 0;
var holdstring;
var myWalk = document.querySelector('#display-screen');
var texttimer
firststory()

function firststory(){
writescript(indextext1, function() {
  // writescript(indextext2, function() {
  //   writescript(indextext3, function() {
  //     writescript(indextext4, function() {
          //     });
  //   });
  // });
});
 // afterme(index, indextext1, afterme(index, indextext2, afterme(index, indextext3, writescript(index, indextext4))));
 // wait(2*1000).then(() => texttimer = setInterval(index, 30, indextext1), 0).catch(console.log("1 index failed"););
 // wait(2*1000).then(() => texttimer = setInterval(index, 30, indextext2), 0).catch(console.log("2 index failed"););
 //
 // texttimer = resolveAfterxSeconds(
 // texttimer = resolveAfterxSeconds(setInterval(index, 30, indextext2), 5000)
 // texttimer = resolveAfterxSeconds(setInterval(index, 30, indextext3), 10000)
 // texttimer = resolveAfterxSeconds(setInterval(index, 30, indextext4), 15000)

}

// const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#Common_mistakes

// function afterme(myfunction, text, callback){
//   setTimeout( writescript(myfunction, text, callback), 3000);
// }
function writescript(text, callback){
  setTimeout(texttimer = setInterval(index, 60, text, callback), 3000);
  callback();
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
    console.log("end");
    console.log(holdstring);
    clearInterval(texttimer)
    console.log("act one done");
    const currentUrl = document.URL
    const baseUrl = currentUrl.split('&');
    console.log(baseUrl[0]);
    window.location.href = baseUrl[0] + "&" + "sequence=2#";

    callback()
  }
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
