---
title: Player Search
permalink: playersearch.html
---

<html>
<head>
    <title>Input and Save</title>
    <script>
        function saveInput(event) {
            if (event.keyCode === 13) {  // Check if the Enter key is pressed
                var inputText = document.getElementById("inputField").value;  // Get the input value
                console.log(inputText)
                const headers = {
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjdlODUwMWM1LTc0YTItNGU5Mi05ZjNhLTc2ZDg1NGNjOWQzMyIsImlhdCI6MTY4Mzc2MjU3Miwic3ViIjoiZGV2ZWxvcGVyLzM4MjRmMjMxLTg5ZGItOTdjOC01YjgzLTQ3YjRhYWZlNzgzMiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNTQuODYuNTAuMTM5IiwiNzIuMTk3LjI0Ni4xMDEiLCIxNzIuNTYuMTY5Ljg1Il0sInR5cGUiOiJjbGllbnQifV19.DJ7mHnVINV4-dHe84N_Ac52C-BNHLwiCQBNJ5OS9T0ovKLhZLg2g8iCzaYY812EbHEelYxhSEkpU16RnxR0GXw'
                };
                fetch('https://api.brawlstars.com/v1/players/%239LPU200R', {
                    method: 'GET',
                    headers: headers
                })
                    .then(response => response.json())
                    .then(data => {
                        // Process the data returned from the API
                        console.log(data);
                    })
                    .catch(error => {
                        // Handle any errors that occurred during the fetch request
                        console.error('Error:', error);
                    });
            }
        }
    </script>
</head>
<body>
    <input type="text" id="inputField" onkeypress="saveInput(event)" placeholder="Enter tag">
</body>
</html>

