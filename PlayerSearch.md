---
title: Player Search
permalink: playersearch.html
---

<html>
<head>
    <title>Input and Save</title>
    <script>
        getXmlHttpRequestObject = function () {
        if (!xhr) {
            // Create a new XMLHttpRequest object 
            xhr = new XMLHttpRequest();
        }
        return xhr;
        };
        async function saveInput(event) {
            if (event.keyCode === 13) {  // Check if the Enter key is pressed
                var inputText = document.getElementById("inputField").value;  // Get the input value
                console.log("tag :" + inputText)
                console.log("Get users...");
                xhr = getXmlHttpRequestObject();
                xhr.onreadystatechange = dataCallback;
                // asynchronous requests
                xhr.open("GET", "https://brawlyzebackend.duckdns.org/api/brawl", true);
                // Send the request over the network
                xhr.send(null);
            }
        }
    </script>
</head>
<body>
    <input type="text" id="inputField" onkeypress="saveInput(event)" placeholder="Enter tag">
</body>
</html>