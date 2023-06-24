function submitForm() {
  var city = document.getElementById("cityInput").value;
  var months = document.getElementById("monthsInput").value;
  var days = document.getElementById("daysInput").value;
   // Check if any fields are empty
   if (city === "" || months === "" || (days === ""|| days <= 0) ) {
      return;
  }
  
  var jsonData = {location : city, month : months, day : days};
  var jsonObject = JSON.stringify(jsonData);

  // Display the user inputs
  var userInput = "Location: " + city + ", Month: " + months + ", Days: " + days;

  // Clear the form inputs
  document.getElementById("cityInput").value = "";
  document.getElementById("monthsInput").value = "";
  document.getElementById("daysInput").value = "";
  
  $.ajax({
    type: "POST",
    url: "http://localhost:5000/post_json",
    data: jsonObject,
    contentType: "application/json",
    success: function (result) {
      console.log("POST request successful!");
      const obj = result;
      var output = "";
      output += "Accommodations: " + obj.accoms + ", ";
      output += "Cuisine: " + obj.cuisine + ", ";
      output += "Description: " + obj.desc + ", ";
      output += "Itinerary: " + obj.iternary + ", ";
      output += "Transportation: " + obj.transportation + ", ";
      output += "Weather: " + obj.weather + ", ";
      output += "Eco-friendliness: " + obj.ecoinfo + ", ";
      output += "Budget: " + obj.budget;
      document.getElementById("outputText").value = output;
    },
    error: function (result, status) {
      console.log("POST request failed!");
      console.log(result);
    }
  });
}

