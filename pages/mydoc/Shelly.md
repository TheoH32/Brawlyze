---
title: Shelly
tags: [getting_started, troubleshooting]
keywords:
sidebar: mydoc_sidebar
permalink: shelly.html
folder: mydoc
---

<script>
// Make a GET request to an API endpoint
fetch('https://api.brawlapi.com/v1/brawlers/16000000')
  .then(response => response.json()) // Parse the response as JSON
  .then(data => {
    // Do something with the data
    console.log(data);
  })
  .catch(error => {
    // Handle any errors that occur during the request
    console.error('Error:', error);
  });
</script>

![Shelly](/images/2D/Shelly_Pose.png)

<html>
    <div class="box">
        <p>test</p>
    </div>
<html>


# Counters:
![Shelly](/images/icons/shellyicon.webp)

<style>
    .box {
        box-shadow: rgba(0, 0, 0, 0.15) 0px 5px 15px 0px;
        position: absolute;
        top: 0px;
        right: 0px;
    }
</style>