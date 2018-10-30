function dynamicallyLoadScript(url) {
    var script = document.createElement("script"); //Make a script DOM node
    script.src = url; //Set it's src to the provided URL
    document.head.appendChild(script); //Add it to the end of the head section of the page (could change 'head' to 'body' to add it to the end of the body section instead)
}

function resetHeight(){
	var div_particle = document.getElementById("particles-js")
	var assign_height = 0

	if (document.body.clientHeight > window.innerHeight){
		assign_height = document.body.clientHeight
	}
	else{
		assign_height = window.innerHeight
	}
	div_particle.style.height = assign_height.toString() + "px"
	
	console.log("height resetted")
}
resetHeight()
dynamicallyLoadScript("assets/js/particles.js")