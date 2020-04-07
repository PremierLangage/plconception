
# Un timer pour un exercice

l'idée est que l'on a une balise timer qui donne en miliseconde le temps que l'on a pour faire l'exercice.






Voici le code d'un timer qui permet de limiter le temps de réalisation d'un exercice.



<pre>
<p id="bob" />
<form>
  <input id="chronotime" value="0:00:00:0" style="width:40px"/>
  </form>

<script>
var initialtime = 61000 // 60000*minutes + 1000 * secondes
var diff = initialtime
var timerID = 0
var timerlength = 100
window.onload = starteverything;


function starteverything(){
document.getElementById("bob").innerHTML = " C'est parti "
chrono()
}

function chrono(){

	if (diff <60000) {
    	 document.getElementById("bob").innerHTML = "Attention plus que 1 Minute"
         document.getElementById("bob").style= "background: #ff9900;"
	}
	if (diff <5000) {
    	 document.getElementById("bob").innerHTML = "Attention plus que 5 secondes"
         document.getElementById("bob").style= "background: #ff0000;"
	}
	if (diff <1) {
    	  document.getElementById("bob").innerHTML = "PERDU !!"
          document.getElementById("bob").style= "background: #000099;color: white;"
          // appeler l'ajax de fin d'exercice (abandon)
         return
	}
	diff = diff - timerlength
    diff=new Date(diff)
	var msec = diff.getMilliseconds()
	var sec = diff.getSeconds()
	var min = diff.getMinutes()

    
	if (min < 10){
		min = "0" + min
	}
	if (sec < 10){
		sec = "0" + sec
	}
	msec = msec/100
	document.getElementById("chronotime").value =  min + ":" + sec + ":" + msec
	timerID = setTimeout("chrono()", timerlength)
}


</script>

</pre>
