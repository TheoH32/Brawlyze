---
title: Player Search
keywords:
sidebar: mydoc_sidebar
permalink: playersearch.html
folder: mydoc
---

<html>
<head>
    <title>Input and Save</title>
    <script>
        function saveInput(event) {
            if (event.keyCode === 13) {  // Check if the Enter key is pressed
                var inputText = document.getElementById("inputField").value;  // Get the input value
                console.log(inputText)
            }
        }
    </script>
</head>
<body>
    <input type="text" id="inputField" onkeypress="saveInput(event)" placeholder="Enter tag">
</body>
</html>
