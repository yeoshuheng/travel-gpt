function submitForm() {
    var city = document.getElementById("cityInput").value;
    var month = document.getElementById("monthInput").value;
    var days = document.getElementById("daysInput").value;
    var jsonData = {c : city, m : month, d : days};
    var jsonObject = JSON.stringify(jsonData);
    
    // Display the user inputs
    var userInput = "Location: " + city + ", Month: " + month + ", Days: " + days;
    console.log(userInput);
    console.log(jsonObject);

    // Update the userInput field
    document.getElementById("userInput").value = userInput;

   
}


