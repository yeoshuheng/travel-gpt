function submitForm() {
    var city = document.getElementById("cityInput").value;
    var month = document.getElementById("monthInput").value;
    var days = document.getElementById("daysInput").value;

    // Display the user inputs
    var userInput = "Location: " + city + ", Month: " + month + ", Days: " + days;
    console.log(userInput);

    // Update the userInput field
    document.getElementById("userInput").value = userInput;
}


