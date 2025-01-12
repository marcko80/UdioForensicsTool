import numpy as np
import librosa
import matplotlib.pyplot as plt
import os

def detect_tampering(audio_path, frame_length=2048, hop_length=512, threshold=0.1):
    """
    Analizza un file audio per rilevare manipolazioni come tagli o incollaggi.
    
    :param audio_path: Percorso del file audio.
    :param frame_length: Lunghezza del frame per l'analisi.
    :param hop_length: Hop length per l'analisi.
    :param threshold: Soglia per rilevare discontinuità.
    :return: Lista di timestamp dove sono state rilevate discontinuità.
    """
    try:
        # Carica il file audio
        y, sr = librosa.load(audio_path, sr=None)

        # Calcola la Short-Time Fourier Transform (STFT)
        stft = np.abs(librosa.stft(y, n_fft=frame_length, hop_length=hop_length))

        # Calcola la differenza tra frame consecutivi
        diff = np.diff(stft, axis=1)
        diff_norm = np.linalg.norm(diff, axis=0)

        # Trova i punti dove la differenza supera la soglia
        anomalies = np.where(diff_norm > threshold)[0]

        # Converti i frame in timestamp
        timestamps = librosa.frames_to_time(anomalies, sr=sr, hop_length=hop_length)

        # Salva il grafico delle discontinuità in un file immagine
        output_dir = os.path.dirname(audio_path)
        discontinuita_path = os.path.join(output_dir, 'discontinuita.png')
        
        plt.figure(figsize=(10, 4))
        plt.plot(librosa.frames_to_time(np.arange(len(diff_norm)), sr=sr, hop_length=hop_length), diff_norm)
        plt.axhline(y=threshold, color='r', linestyle='--', label='Soglia')
        plt.title("Analisi delle Discontinuità")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Differenza Norm")
        plt.legend()
        plt.savefig(discontinuita_path)
        plt.close()

        return timestamps, discontinuita_path  # Restituisce i timestamp e il percorso del grafico

    except Exception as e:
        raise Exception(f"Errore durante il rilevamento delle manipolazioni: {str(e)}")