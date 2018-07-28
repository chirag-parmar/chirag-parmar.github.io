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