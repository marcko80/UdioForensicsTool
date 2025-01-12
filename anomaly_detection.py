import numpy as np
import soundfile as sf

def detect_anomalies(audio_file):
    """
    Rileva anomalie nel segnale audio per Udio Forensics Tool.
    """
    try:
        data, sample_rate = sf.read(audio_file)
        zcr = np.mean(np.abs(np.diff(np.sign(data)))) / sample_rate  # Zero-crossing rate
        noise_floor = np.mean(np.abs(data))
        return {
            'zero_crossing_rate': zcr,
            'noise_floor': noise_floor
        }
    except Exception as e:
        print(f"Errore durante il rilevamento delle anomalie: {e}")
        return None