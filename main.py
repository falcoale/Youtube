from pytube import YouTube
import time
import os
import requests
import sys

print(f"Inserisci il link del video")

# Chiedi il link del video
yt = YouTube(input(f">> ")) 

# Stampi il titolo del video
print(f"Il titolo del video è: {yt.title}")

# Dai la possibilità di scaricare la thumb
def thumb():
    print(f"Vuoi scaricare la copertina del video?\n [1] Sì\n [2] No")
    scelta = input(">> ")
    
    # Converti la stringa ad intero
    if scelta.isdigit():
        scelta = int(scelta)
    else:
        print(f"La tua scelta ({scelta}), non può essere presa in considerazione. Riprova tra due secondi.")
        time.sleep(2)
        thumb()
    
    # If che gestisce la scelta
    if scelta == 1:
        url = yt.thumbnail_url
        r = requests.get(url, allow_redirects=True)
        open('thumb.jpg', 'wb').write(r.content)
    elif scelta == 2:
        sys.exit(0)
    else:
        print(f"La tua scelta ({scelta}), non può essere presa in considerazione. Riprova tra due secondi.")
        time.sleep(2)
        thumb()


thumb()