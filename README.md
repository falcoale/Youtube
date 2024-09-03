# YouTube Video Info and Thumbnail Downloader 🎥📥

Questo progetto Python consente di ottenere informazioni dettagliate su un video di YouTube e scaricare la miniatura del video. Utilizza la libreria `pytube` per accedere ai dati del video e `requests` per scaricare la miniatura.

## Contenuto del Repository 📂

- `main.py`: Il file principale che esegue lo script per raccogliere informazioni sul video e scaricare la miniatura.
- `requirements.txt`: Elenco delle librerie Python necessarie per eseguire lo script.
- `Setup.bat`: File batch per installare automaticamente le dipendenze e avviare lo script.
- `LICENSE`: File licenza

## Requisiti 🔧

Assicurati di avere Python installato sul tuo sistema. Il file `requirements.txt` contiene le librerie necessarie:

- `pytube`
- `requests`

## Installazione ⚙️

### Utilizzare il File Batch `Setup.bat` 🖱️

1. Scarica il file `Setup.bat` dal repository.
2. Esegui il file batch facendo doppio clic su di esso. Questo installerà le librerie necessarie e avvierà lo script `main.py`.

### Installazione Manuale 🛠️

Se preferisci installare le librerie manualmente, puoi seguire questi passaggi:

1. **Installa le Dipendenze:**
   - Usa il file `requirements.txt` per installare le librerie necessarie:
     ```bash
     pip install -r requirements.txt
     ```

2. **Esegui lo Script:**
   - Dopo aver installato le dipendenze, esegui lo script Python:
     ```bash
     python main.py
     ```

## Utilizzo 🚀

1. **Preparazione:**
   - Assicurati di avere Python e `pip` configurati correttamente sul tuo sistema.

2. **Esecuzione dello Script:**
   - Esegui `Setup.bat` per installare le dipendenze e avviare lo script.
   - In alternativa, puoi eseguire direttamente `main.py` dopo aver installato le dipendenze manualmente.

3. **Funzionalità:**
   - **Ottenere Informazioni sul Video:** Lo script raccoglie informazioni come il link del video, l'autore, il numero di visualizzazioni, e la data di pubblicazione. Queste informazioni vengono salvate in un file JSON denominato `Video Info <video_id>.json`.
   - **Scaricare la Miniatura:** Dopo aver inserito l'URL del video, lo script ti chiederà se desideri scaricare la miniatura del video. Se scegli di farlo, la miniatura verrà salvata come `thumb <video_id>.jpg`.

## Esempio di Utilizzo 📋

1. Esegui `Setup.bat` o `main.py`:
   ```bash
   python main.py
   ```

2. Inserisci il link del video YouTube quando richiesto:
   ```
   Inserisci il link del video
   >> https://www.youtube.com/watch?v=gEWUoZy69FE
   ```

3. Dopo aver inserito il link, lo script salverà le informazioni del video in un file JSON e ti chiederà se desideri scaricare la miniatura:
   ```
   Vuoi scaricare la copertina del video?
    [1] Sì
    [2] No
   >> 1
   ```

4. Se hai scelto di scaricare la miniatura, verrà salvata con il nome `thumb {video_id}.jpg` nella stessa directory dello script.

## Contributi 🤝

Se desideri contribuire al progetto, puoi aprire una pull request con le tue modifiche o suggerimenti. Tutti i contributi sono benvenuti!

## Licenza 📝

Questo progetto è concesso in licenza sotto la [Licenza MIT](LICENSE).

## Contatti 📬

Per qualsiasi domanda o problema, apri un [issue](https://github.com/falcoale/Youtube/issues) nel repository.
