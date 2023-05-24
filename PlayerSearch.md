---
title: Player Search
permalink: playersearch.html
---

<html>
<head>
    <title>Input and Save</title>
    <script>
        async function saveInput(event) {
            if (event.keyCode === 13) {  // Check if the Enter key is pressed
                var inputText = document.getElementById("inputField").value;  // Get the input value
                console.log("tag :" + inputText)
                console.log("Get users...");
                var myHeaders = new Headers();
                myHeaders.append("Content-Type", "application/json");
                myHeaders.append("Accept", "application/json");
                var raw = JSON.stringify({
                "tag": inputText
                });
                var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                body: raw,
                redirect: 'follow'
                };
                fetch("https://brawlyzebackend.duckdns.org/api/brawl", requestOptions)
                .then(response => response.text())
                .then(result => document.getElementById("result-container").innerText = result)
                .catch(error => console.log('error', error)); 
            }
        }
    </script>
</head>
<body>
    <input type="text" id="inputField" onkeypress="saveInput(event)" placeholder="Enter tag">
    <div id="result-container"></div>
</body>
</html>