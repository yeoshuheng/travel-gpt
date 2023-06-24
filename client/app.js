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
      document.getElementById("accoms").value = obj.accoms;
      document.getElementById("cuisine").value = obj.cuisine;
      document.getElementById("desc").value = obj.desc;
      document.getElementById("iternary").value = obj.iternary;
      document.getElementById("transportation").value = obj.transportation;
      document.getElementById("weather").value = obj.weather;
    },
    error: function (result, status) {
      console.log("POST request failed!");
      console.log(result);
    }
  });
}

