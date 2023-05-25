---
title: Player Search
permalink: playersearch.html
---
<style>
    body {
        background-image: url("/images/background.jpg");
        background-repeat: no-repeat;
        background-size: cover;
        }
    h1 {
        color: white;
    }
</style>

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
                .then(result => {
                    console.log(result);
                    // Pretty-print the data
                    const p1 = JSON.parse(result)
                    const parsedData = JSON.parse(p1)
                    console.log(parsedData);
                    console.log(parsedData.name)
                    const name = parsedData.name
                    var resultContainer = document.getElementById("result-container");
                    resultContainer.innerText = name;        
                })
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
