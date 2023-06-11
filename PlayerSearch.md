---
title: Player Search
permalink: playersearch.html
---

<body>
    <input type="text" id="inputField" onkeypress="saveInput(event)" placeholder="Enter tag without #">
    <div id="result-container">
        <div id="name">
            <h1></h1>
        </div>
        <div id="trophies">
            <h1></h1>
        </div>
        <div id="topGroup">
            <h1>TOP BRAWLERS</h1>
            <div id="topBrawlers">
                <div id="top1"></div>
                <div id="top2"></div>
                <div id="top3"></div>
            </div>
        </div>
        <div id="bottomGroup">
            <h1>BOTTOM BRAWLERS</h1>
            <div id="bottomBrawlers">
                <div id="bottom1"></div>
                <div id="bottom2"></div>
                <div id="bottom3"></div>
            </div>
        </div>
        <div id="playerStats">
        </div>
    </div>
</body>

<style>
    body {
        background-color: black;
        background-image: url("/images/background.jpg");
    }
    
    h1 {
        color: white;
    }
    #result-container {
        background-color: white;
        margin: 2em;
        text-align: center;
        border-radius: 10px;
    }

    #topGroup,
    #bottomGroup {
        border-radius: 0.6em;
        margin: 1em;
        overflow: auto;
    }

    #bottomBrawlers,
    #topBrawlers {
        display: flex;
        justify-content: center; /* Center horizontally */
        align-items: center; /* Center vertically */
    }

    #bottomBrawlers div,
    #topBrawlers div {
        display: flex;
        flex-direction: column;
        justify-content: center; /* Center content vertically */
        align-items: center; /* Center content horizontally */
        padding: 10px;
        border: 1px solid black;
        border-radius: 5px;
        background-color: lightgray;
        opacity: 0;
        transition: opacity 0.5s;
        width: 25%;
        margin: 1em;
    }

    #bottomBrawlers div.show,
    #topBrawlers div.show {
        opacity: 1; /* Show when 'show' class is added */
    }

    #name {
        color: black;
        font-size: 3.5em;
    }
    #trophies {
        margin: auto;
    }
    .post-content img {
        margin: 0px 3px 2px 0px;
        width: auto;
        height: auto;
        max-width: 100%;
        max-height: 100%;
    }  
    #playerStats {
        padding: 10px; /* Add some padding for better readability */
    }

    #playerStats table {
        width: 100%; /* Make the table width 100% of its container */
        background-color: grey;
        margin-left: auto;
        margin-right: auto;
        border: 1px solid;
    }

    #playerStats th,
    #playerStats td {
        padding: 5px; /* Add padding to table cells */
        text-align: center;
    }
</style>

<script>
    let isCooldownActive = false; // Track if cooldown is active
    const cooldownDuration = 2000; // Cooldown period in milliseconds
    async function saveInput(event) {
        if (event.keyCode !== 13 || isCooldownActive) return; // Exit if Enter key is not pressed or cooldown is active
        isCooldownActive = true; // Set cooldown active
        const playerStatsDiv = document.getElementById("playerStats");
        while (playerStatsDiv.firstChild) {
            playerStatsDiv.removeChild(playerStatsDiv.firstChild);
        }
        try {
            const inputText = document.getElementById("inputField").value;
            const response = await fetch("https://brawlyzebackend.duckdns.org/api/brawl", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({ "tag": inputText })
            });
            console.log("data received");
            const result = await response.json();
            // PARSING DATA + DEFINING VARIABLES
            const parsedData = JSON.parse(result);
            console.log(parsedData);
            const { name, trophies, soloVictories, duoVictories, '3vs3Victories': threeVsThreeVictories, brawlers } = parsedData;
            const nameDiv = document.getElementById("name");
            // NAME
            nameDiv.innerText = name;
            // TROPHIES
            const trophiesDiv = document.getElementById("trophies");
            trophiesDiv.innerHTML = `<img src="/images/trophy2.png" style="width: 20px">${trophies}`;
            // WINS TABLE
            if (!playerStatsDiv.querySelector("table")) {
                const table = document.createElement("table");
                const soloWinPic = `<img src="images/soloshowdown.png" style="width: 30px">`;
                const duoWinPic = `<img src="images/duoshowdown.png" style="width: 30px">`;
                const threeWinPic = `<img src="images/gemgrab.png" style="width: 30px">`;
                const headers = [soloWinPic + "<br>" + "Solo Wins", duoWinPic + "<br>" + "Duo Wins", threeWinPic + "<br>" +"3v3 Wins"];
                table.innerHTML = `
                    <tr>${headers.map(headerText => `<th>${headerText}</th>`).join("")}</tr>
                    <tr>${[soloVictories, duoVictories, threeVsThreeVictories].map(winCount => `<td>${winCount}</td>`).join("")}</tr>
                `;
                playerStatsDiv.appendChild(table);
            }
            // TOP AND BOTTOM TABLE
            const sortedBrawlers = brawlers.slice().sort((a, b) => b.trophies - a.trophies);
            const top3Brawlers = sortedBrawlers.slice(0, 3);
            const bottom3Brawlers = sortedBrawlers.slice(-3).reverse();
            const trophieimg = "images/trophy2.png";
            const trophypic = `<img src="${trophieimg}" style="width: 20px">`;
            const topGroupDiv = document.getElementById("topGroup")
            const bottomGroupDiv = document.getElementById("bottomGroup")
            topGroupDiv.style.backgroundColor="grey";
            bottomGroupDiv.style.backgroundColor="grey";

            const top1Div = document.getElementById("top1");
            const top2Div = document.getElementById("top2");
            const top3Div = document.getElementById("top3");
            const top1pic = `<img src="images/icons/${top3Brawlers[0].name}.webp" style="width: 40px">`;
            const top2pic = `<img src="images/icons/${top3Brawlers[1].name}.webp" style="width: 40px">`;
            const top3pic = `<img src="images/icons/${top3Brawlers[2].name}.webp" style="width: 40px">`;

            top1Div.innerHTML = top1pic + "<br>" + top3Brawlers[0].name + "<br>" + trophypic + top3Brawlers[0].trophies;
            top2Div.innerHTML = top2pic + "<br>" + top3Brawlers[1].name + "<br>" + trophypic + top3Brawlers[1].trophies;
            top3Div.innerHTML = top3pic + "<br>" + top3Brawlers[2].name + "<br>" + trophypic + top3Brawlers[2].trophies;
            top1Div.classList.add("show");
            top2Div.classList.add("show");
            top3Div.classList.add("show");

            const bottom1Div = document.getElementById("bottom1");
            const bottom2Div = document.getElementById("bottom2");
            const bottom3Div = document.getElementById("bottom3");
            const bottom1pic = `<img src="images/icons/${bottom3Brawlers[0].name}.webp" style="width: 40px">`;
            const bottom2pic = `<img src="images/icons/${bottom3Brawlers[1].name}.webp" style="width: 40px">`;
            const bottom3pic = `<img src="images/icons/${bottom3Brawlers[2].name}.webp" style="width: 40px">`;
            bottom1Div.innerHTML = bottom1pic + "<br>" + bottom3Brawlers[0].name + "<br>" + trophypic + bottom3Brawlers[0].trophies;
            bottom2Div.innerHTML = bottom2pic + "<br>" + bottom3Brawlers[1].name + "<br>" + trophypic + bottom3Brawlers[1].trophies;
            bottom3Div.innerHTML = bottom3pic + "<br>" + bottom3Brawlers[2].name + "<br>" + trophypic + bottom3Brawlers[2].trophies;
            bottom1Div.classList.add("show");
            bottom2Div.classList.add("show");
            bottom3Div.classList.add("show");

            // BRAWLERS TABLE
            const table = document.createElement("table");
            const headers = ["Name", "Power", "Rank", "Trophies"];
            const headerRow = document.createElement("tr");
            headers.forEach(headerText => {
                const th = document.createElement("th");
                th.textContent = headerText;
                headerRow.appendChild(th);
            });
            table.appendChild(headerRow);
            brawlers.forEach(brawler => {
                const row = document.createElement("tr");
                const { name, power, rank, trophies } = brawler;
                const rowData = [name, power, rank, trophies];
                rowData.forEach(cellData => {
                    const td = document.createElement("td");
                    td.textContent = cellData;
                    row.appendChild(td);
                });
                table.appendChild(row);
            });
            playerStatsDiv.appendChild(table);
        } catch (error) {
            console.error("Error occurred:", error);
        } finally {
            setTimeout(() => {
                isCooldownActive = false; // Reset cooldown after the specified duration
            }, cooldownDuration);
        }
    }
</script>