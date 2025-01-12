# Udio Forensics Tool

**Udio Forensics Tool** è un software avanzato per l'analisi forense di file audio, progettato per identificare manipolazioni, tagli o alterazioni nei registrati. Questo strumento è ideale per investigatori, esperti forensi, giornalisti e chiunque abbia bisogno di analizzare file audio per scoprire eventuali manomissioni.

---

## Funzionalità Principali

### 1. **Estrazione delle Caratteristiche Tecniche**
   - **Informazioni di Base**: Estrae dettagli come frequenza di campionamento, profondità di bit, numero di canali, durata e dimensione del file.
   - **Supporto Multi-Formato**: Compatibile con i principali formati audio, tra cui WAV, MP3, AAC, OGG, FLAC, M4A e 3GPP.

### 2. **Analisi dello Spettro Audio**
   - **Trasformata di Fourier (FFT)**: Analizza lo spettro di frequenza del segnale audio.
   - **Visualizzazione Grafica**: Genera un grafico dello spettro di magnitudine per identificare anomalie o manipolazioni.

### 3. **Rilevamento di Anomalie**
   - **Tasso di Passaggio per Zero (Zero-Crossing Rate)**: Misura la frequenza con cui il segnale audio passa per lo zero, utile per rilevare cambiamenti bruschi.
   - **Livello di Rumore di Fondo (Noise Floor)**: Calcola il livello medio di rumore per identificare sezioni con livelli di rumore inconsistenti.

### 4. **Generazione di Report**
   - **Report PDF**: Crea un report dettagliato in formato PDF che include:
     - Informazioni tecniche del file audio.
     - Risultati dell'analisi delle anomalie.
     - Grafico dello spettro di frequenza.
   - **Esportazione**: Il report può essere salvato e condiviso per ulteriori analisi o documentazione.

### 5. **Interfaccia Grafica Intuitiva**
   - **Facilità d'Uso**: Un'interfaccia grafica sviluppata con PyQt5 rende il software accessibile anche a utenti non tecnici.
   - **Visualizzazione dei Risultati**: I risultati dell'analisi vengono visualizzati direttamente nell'interfaccia, insieme al grafico dello spettro.

---

## Come Funziona

1. **Caricamento del File**: L'utente seleziona un file audio tramite l'interfaccia grafica.
2. **Estrazione delle Informazioni**: Il software estrae e visualizza le informazioni tecniche del file.
3. **Analisi Spettrale**: Viene eseguita l'analisi dello spettro di frequenza e generato il grafico corrispondente.
4. **Rilevamento delle Anomalie**: Il software analizza il segnale audio per rilevare eventuali anomalie.
5. **Generazione del Report**: Viene creato un report PDF con i risultati dell'analisi.
6. **Visualizzazione dei Risultati**: I risultati vengono visualizzati nell'interfaccia grafica, insieme al grafico dello spettro.

---

## Installazione

### Prerequisiti
- Python 3.8 o superiore.
- Pip (gestore di pacchetti Python).

### Passaggi per l'Installazione

1. Clona il repository:
   ```bash
   git clone https://github.com/tuo-repo/udio_forensics_tool.git
   cd udio_forensics_tool
   ```

2. Crea e attiva un ambiente virtuale:
   ```bash
   python -m venv env
   source env/bin/activate  # Su Windows: env\Scripts\activate
   ```

3. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

---

## Esecuzione

Esegui il software con il comando:
```bash
python main.py
```

---

## Struttura del Codice

```
udio_forensics_tool/
│
├── audio_handler.py          # Gestione dei file audio e estrazione delle informazioni tecniche
├── spectral_analysis.py      # Analisi dello spettro audio
├── anomaly_detection.py      # Rilevamento di anomalie nel segnale audio
├── report_generator.py       # Generazione del report PDF
├── gui.py                    # Interfaccia grafica utente (GUI)
├── main.py                   # Script principale per eseguire l'applicazione
├── requirements.txt          # File delle dipendenze
├── README.md                 # Documentazione del progetto
└── app.log                   # File di log per registrare errori e attività
```

---

## Licenza

Questo progetto è rilasciato sotto la licenza MIT. Per ulteriori dettagli, consulta il file [LICENSE](LICENSE).

---

## Contributi

Contributi e suggerimenti sono benvenuti! Se desideri contribuire al progetto, segui questi passaggi:

1. Fai un fork del repository.
2. Crea un nuovo branch (`git checkout -b feature/nuova-funzionalità`).
3. Fai commit delle tue modifiche (`git commit -am 'Aggiunta nuova funzionalità'`).
4. Pusha il branch (`git push origin feature/nuova-funzionalità`).
5. Apri una Pull Request.

---

## Contatti

Per domande o feedback, contattami tramite:
- **Email**: 
- **GitHub**: 

---

## Ringraziamenti

Un ringraziamento speciale a tutti i contributori e alle librerie open source che hanno reso possibile questo progetto.

---

Grazie per aver scelto **Udio Forensics Tool**! Speriamo che questo strumento sia utile per le tue analisi forensi audio. 🎧🔍
