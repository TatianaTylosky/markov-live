$( document ).ready(function() {
  console.log("your javascript file loaded")
  $( "#button" ).click(function() {
  	console.log("button pressed")
  	$( "#input" ).submit();
});
});