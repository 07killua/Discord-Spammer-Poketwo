from webserver import keep_alive
import requests

channelID = 1017792645562630304
headers = {
    "authorization": OTU0NDExOTg1NjQ1MjExNjQ5.GoSaLf.OB_R5q39UCwMCA8__w1_C-QYILpDdbXl_Qs6qE
    "YOUR TOKEN HERE"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
