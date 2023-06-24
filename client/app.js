function submitForm() {
    var city = document.getElementById("cityInput").value;
    var month = document.getElementById("monthInput").value;
    var days = document.getElementById("daysInput").value;
     // Check if any fields are empty
     if (city === "" || month === "" || (days === "" || days <= 0) ) {
        document.getElementById("errorMessage").textContent = "Please fill in all the fields."; // Display error message
        return;
    }
    document.getElementById("errorMessage").textContent = "";
    
    var jsonData = {c : city, m : month, d : days};
    var jsonObject = JSON.stringify(jsonData);

    // Display the user inputs
    var userInput = "Location: " + city + ", Month: " + month + ", Days: " + days;
    console.log(userInput);
    console.log(jsonObject);

    // Update the userInput field
    document.getElementById("userInput").value = userInput;

    // Clear the form inputs
    document.getElementById("cityInput").value = "";
    document.getElementById("monthInput").value = "";
    document.getElementById("daysInput").value = "";

    $.ajax({
        type: "POST",
        url: "http://localhost:5000",
        data: jsonObject,
        contentType: "application/json",
        success: function (result) {
          console.log(result);
        },
        error: function (result, status) {
          console.log(result);
        }
      });
}


