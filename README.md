# 🎤 Udio Forensics Tool 🕵️‍♂️

**Udio Forensics Tool** è un'applicazione desktop progettata per l'analisi forense di file audio. Questo strumento consente di rilevare manipolazioni, anomalie e caratteristiche tecniche di registrazioni audio, fornendo un report dettagliato in formato PDF. Ideale per investigatori, esperti forensi e chiunque abbia bisogno di analizzare file audio in modo professionale. 🔍🎧

---

## 🚀 Funzionalità principali

- **🎚️ Analisi delle caratteristiche tecniche:**
  - Estrazione di informazioni come frequenza di campionamento, profondità di bit, durata, formato e dimensioni del file.

- **📊 Analisi spettrale:**
  - Generazione di uno spettrogramma per visualizzare le componenti frequenziali del segnale audio.

- **🔍 Rilevamento di anomalie:**
  - Calcolo del tasso di zero-crossing, loudness medio e massimo, segmenti silenziosi e durata del segmento non silenzioso più lungo.

- **⚠️ Rilevamento di manipolazioni:**
  - Identificazione di tagli, incollaggi o altre discontinuità nel segnale audio.

- **📄 Generazione di report PDF:**
  - Creazione di un report dettagliato in formato PDF con i risultati dell'analisi, inclusi grafici e dati tecnici.

---

## 🛠️ Tecnologie utilizzate

- **🐍 Python**: Linguaggio di programmazione principale.
- **📦 Librerie Python**:
  - `PyQt5`: Per l'interfaccia grafica.
  - `soundfile` e `librosa`: Per l'elaborazione e l'analisi del segnale audio.
  - `matplotlib`: Per la generazione di grafici.
  - `reportlab`: Per la creazione di report PDF.
- **🖼️ Interfaccia grafica**: Semplice e intuitiva, progettata per un uso immediato.

---

## 📦 Installazione

1. **Clona il repository:**
   ```bash
   git clone https://github.com/tuo-repository/UdioForensicsTool.git
   cd UdioForensicsTool
   ```

2. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Avvia l'applicazione:**
   ```bash
   python main.py
   ```

---

## 🖥️ Come usare l'applicazione

1. **Carica un file audio**:
   - Clicca su "Carica File Audio" e seleziona un file audio supportato (es. `.wav`, `.mp3`, `.flac`).

2. **Avvia l'analisi**:
   - Clicca su "Analizza e Rileva Manipolazioni" per avviare l'analisi completa.

3. **Visualizza i risultati**:
   - I risultati dell'analisi verranno visualizzati nell'interfaccia grafica e salvati in un report PDF.

4. **Esporta il report**:
   - Il report PDF verrà salvato nella stessa cartella del file audio analizzato.

---

## 📂 Struttura del progetto

```
UdioForensicsTool/
├── audio_handler.py          # Gestione delle informazioni tecniche del file audio
├── anomaly_detection.py      # Rilevamento di anomalie nel segnale audio
├── spectral_analysis.py      # Generazione dello spettrogramma
├── tampering_detection.py    # Rilevamento di manipolazioni nel file audio
├── report_generator.py       # Generazione del report PDF
├── gui.py                    # Interfaccia grafica dell'applicazione
├── main.py                   # Punto di ingresso dell'applicazione
├── requirements.txt          # Dipendenze del progetto
└── README.md                 # Documentazione del progetto
```

---

## 📄 Esempio di report PDF

Il report generato include:
- **Introduzione**: Informazioni generali sul file audio.
- **Caratteristiche tecniche**: Dettagli come durata, formato, canali, frequenza di campionamento e risoluzione.
- **Analisi del contenuto audio**: Loudness medio e massimo, segmenti silenziosi e durata del segmento non silenzioso più lungo.
- **Spettrogramma**: Visualizzazione delle componenti frequenziali del segnale audio.
- **Analisi delle discontinuità**: Grafico delle discontinuità rilevate nel file audio.

---

## 🤝 Contributi

Se desideri contribuire al progetto, segui questi passaggi:
1. Fai un fork del repository.
2. Crea un nuovo branch per la tua feature (`git checkout -b feature/nuova-feature`).
3. Fai commit delle tue modifiche (`git commit -m 'Aggiunta nuova feature'`).
4. Pusha il branch (`git push origin feature/nuova-feature`).
5. Apri una Pull Request.

---

## 📜 Licenza

Questo progetto è rilasciato sotto la licenza **MIT**. Per ulteriori dettagli, consulta il file [LICENSE](LICENSE).

---

## 👨‍💻 Autore

**M. C.**  
📧 Email: marcko80 @ gmail.com
🌐 LinkedIn: 
🐙 GitHub: 

---

Grazie per aver scelto **Udio Forensics Tool**! 🎉  
Se hai domande o suggerimenti, non esitare a contattarmi. 😊
