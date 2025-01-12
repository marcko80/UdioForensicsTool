import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def plot_spectrum(audio_file, output_path):
    """
    Analizza lo spettro audio e genera un grafico per Udio Forensics Tool.
    """
    try:
        data, sample_rate = sf.read(audio_file)
        fft = np.fft.fft(data)
        magnitude = np.abs(fft)
        frequency = np.fft.fftfreq(len(data), d=1/sample_rate)
        plt.figure(figsize=(12, 6))
        plt.plot(frequency[:len(frequency)//2], magnitude[:len(magnitude)//2])
        plt.title('Udio Forensics Tool - Magnitude Spectrum')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.savefig(output_path)
        plt.close()
    except Exception as e:
        print(f"Errore durante l'analisi spettrale: {e}")