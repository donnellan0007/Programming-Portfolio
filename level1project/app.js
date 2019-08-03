//SUDO CODE
//IF the first and last name variables 
//have the same [0] value, 

var firstName = prompt("Put your first name in here:") 
var lastName = prompt("Put your last name in here:")
var age = prompt("What is your age?")
var height = prompt("How tall are you?")
var pet = prompt("What is the name of you pet?")

if (firstName == "Slimy" && lastName == "Snake" && age == 13 && height == 176 && pet == "Steve") {
    console.log("Welcome agent Slimy Snake!")
}
else {
    console.log("Sorry, nothing to see here. Woosh!")
}