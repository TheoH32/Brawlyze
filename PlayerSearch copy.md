---
title: Player Search
permalink: playersearch.html
---

<html>
<head>
    <title>Input and Save</title>
    <script>
        function getUsers() {
        console.log("Get users...");
        xhr = getXmlHttpRequestObject();
        xhr.onreadystatechange = dataCallback;
        // asynchronous requests
        xhr.open("GET", "http://localhost:6969/users", true);
        // Send the request over the network
        xhr.send(null);
        }
        async function saveInput(event) {
            if (event.keyCode === 13) {  // Check if the Enter key is pressed
                var inputText = document.getElementById("inputField").value;  // Get the input value
                console.log("tag :" + inputText)
                fetch('https://bsproxy.royaleapi.dev/v1/players/%239LPU200R', {
                    method: 'GET', // *GET, POST, PUT, DELETE, etc.
                    headers: {
                        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc4ZDI5NmQzLTRhZGYtNDg3MC1iZTFlLWZhZTg4YzQ5MDA0YiIsImlhdCI6MTY4NDQ1MzM2Miwic3ViIjoiZGV2ZWxvcGVyLzM4MjRmMjMxLTg5ZGItOTdjOC01YjgzLTQ3YjRhYWZlNzgzMiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNDUuNzkuMjE4Ljc5IiwiMTcyLjU4LjIwLjI0NCIsIjcyLjE5Ny4yNDYuMTAxIiwiMTcyLjU2LjE2OS44NSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.GKUj0LJ0HnPflVRXDY5U7wWLGebQ8_FkUFOiVDY-uzUnxFg3mFrmobwOsv66iWXNByyvw3BYofo1xCr088GYww'
                    }
                })
                .then(response => response.json())
                .then(data => console.log(data))
                .catch(error => console.error(error));
            }
        }
    </script>
</head>
<body>
    <input type="text" id="inputField" onkeypress="saveInput(event)" placeholder="Enter tag">
</body>
</html>