from pytube import YouTube
import time
import json
import requests
import sys

print(f"Inserisci il link del video")

# Chiedi il link del video
yt = YouTube(input(">> ")) 

# Funzione per prendere le info del video
def info():
    infos = {
        "Link Video": f"https://www.youtube.com/watch?v={yt.video_id}",
        "Autore": f"{yt.author}",
        "Link Canale": f"{yt.channel_url}",
        "Iscriviti direttamente": f"{yt.channel_url}?sub_confirmation=1",
        "Titolo": f"{yt.title}",
        # La descrizione del video attraverso PyTube non è possibile scriverla
        # "Descrizione": f"{yt.description}",
        "Visualizzazioni": f"{yt.views}",
    }

    json_object =  json.dumps(infos, indent=3)

    with open(f"Video Info {yt.video_id}.json", "w") as infofile:
        infofile.write(json_object)

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
        # Se si verifica ciò salvi la thumb con il nome di "thumb + yt.video_id.jpg" es. thumb gEWUoZy69FE.jpg
        url = yt.thumbnail_url
        r = requests.get(url, allow_redirects=True)
        open(f"thumb {yt.video_id}.jpg", 'wb').write(r.content)
    elif scelta == 2:
        # Se la scelta è la seconda chiudi il programma
        sys.exit(0)
    else:
        # Altrimenti richiedi
        print(f"La tua scelta ({scelta}), non può essere presa in considerazione. Riprova tra due secondi.")
        time.sleep(2)
        thumb()


info()
thumb()