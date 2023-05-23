---
title: Player Search
permalink: playersearch.html
---

<html>
<head>
    <title>Input and Save</title>
    <script>
        var xhr = null;
        getXmlHttpRequestObject = function () {
        if (!xhr) {
            // Create a new XMLHttpRequest object 
            xhr = new XMLHttpRequest();
        }
        return xhr;
        };
        function dataCallback() {
        // Check response is ready or not
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log("User data received!");
            dataDiv = document.getElementById("result-container");
            // Set current data text
            dataDiv.innerHTML = xhr.responseText;
        }
        }
        async function saveInput(event) {
            if (event.keyCode === 13) {  // Check if the Enter key is pressed
                var inputText = document.getElementById("inputField").value;  // Get the input value
                console.log("tag :" + inputText)
                console.log("Get users...");
                let xhr = new XMLHttpRequest();
                //POST
                xhr.open("POST", "https://brawlyzebackend.duckdns.org/api/brawl");
                xhr.setRequestHeader("Accept", "application/json");
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    console.log(xhr.status);
                    console.log(xhr.responseText);
                }};
                let data = JSON.stringify({"tag": inputText});
                xhr.send(data);
            }
        }
    </script>
</head>
<body>
    <input type="text" id="inputField" onkeypress="saveInput(event)" placeholder="Enter tag">
    <div id="result-container"></div>
</body>
</html>