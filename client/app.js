function submitForm() {
  var city = document.getElementById("cityInput").value;
  var months = document.getElementById("monthsInput").value;
  var days = document.getElementById("daysInput").value;
   // Check if any fields are empty
   if (city === "" || months === "" || days === "") {
    document.getElementById("errorMessage").innerHTML = "Please fill in all the boxes.";
    return;
  }

  if (days <= 0 || days > 14) {
    document.getElementById("errorMessage").innerHTML = "Please enter a valid number of days (between 1 and 14 days).";
    return;
  }
  
  // Clear the error message
  document.getElementById("errorMessage").innerHTML = "";
  var jsonData = {location : city, month : months, day : days};
  var jsonObject = JSON.stringify(jsonData);

  // Display the "Generating..." message
  document.getElementById("generating").innerHTML = "Generating...";

  // Display the user inputs
  var userInput = "Location: " + city + ", Month: " + months + ", Days: " + days;
  $.ajax({
    type: "POST",
    url: "http://localhost:5000/post_json",
    data: jsonObject,
    contentType: "application/json",
    success: function (result) {
      console.log("POST request successful!");
      const obj = result;
      var output = "";
      output += "Description: " + "<br>" + obj.desc  + "<br><br>";
      output += "Accommodations: " + "<br>" + obj.accoms  + "<br><br>";
      output += "Cuisine: " + "<br>" + obj.cuisine  + "<br><br>";
      output += "Itinerary: " + "<br>" + obj.iternary  + "<br><br>";
      output += "Transportation: " + "<br>" + obj.transportation  + "<br><br>";
      output += "Weather: " + "<br>" + obj.weather  + "<br><br>";
      output += "Eco-friendliness: " + "<br>" + obj.ecoinfo  + "<br><br>";
      output += "Budget: " + "<br>" + obj.budget + "<br><br>";
      document.getElementById("outputText").innerHTML = output;
      document.getElementById("generating").innerHTML = "";

      // Clear the form inputs
      document.getElementById("cityInput").value = "";
      document.getElementById("monthsInput").value = "";
      document.getElementById("daysInput").value = "";
      document.getElementById("generating").innerHTML = ""
    },
    error: function (result, status) {
      console.log("POST request failed!");
      console.log(result);
    }
  });
}