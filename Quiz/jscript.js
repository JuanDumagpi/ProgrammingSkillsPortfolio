function result(){
var score = 0;
if (document.getElementById('right1').checked){score++}
if (document.getElementById('right2').checked){score++}
if (document.getElementById('right3').checked){score++}

if (score==3){document.write ("Your score is: " + score + "/3 Excellent")}
if (score==2){document.write ("Your score is: " + score + "/3 Good")}
if (score==1){document.write ("Your score is: " + score + "/3 Try better next time!")}
if (score==0){document.write ("Your score is: " + score + "/3 Needs to review!")}

}
    