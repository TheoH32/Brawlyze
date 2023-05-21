import requests

url = "https://api.brawlstars.com/v1/players/%239LPU200R"
api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjdlODUwMWM1LTc0YTItNGU5Mi05ZjNhLTc2ZDg1NGNjOWQzMyIsImlhdCI6MTY4Mzc2MjU3Miwic3ViIjoiZGV2ZWxvcGVyLzM4MjRmMjMxLTg5ZGItOTdjOC01YjgzLTQ3YjRhYWZlNzgzMiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNTQuODYuNTAuMTM5IiwiNzIuMTk3LjI0Ni4xMDEiLCIxNzIuNTYuMTY5Ljg1Il0sInR5cGUiOiJjbGllbnQifV19.DJ7mHnVINV4-dHe84N_Ac52C-BNHLwiCQBNJ5OS9T0ovKLhZLg2g8iCzaYY812EbHEelYxhSEkpU16RnxR0GXw"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {api_token}"
}

response = requests.get(url, headers=headers)

if response.ok:
    print(response.text)
else:
    print("Failed:", response.reason, ":", response.text)