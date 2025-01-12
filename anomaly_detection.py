import numpy as np
import soundfile as sf

def detect_anomalies(audio_file):
    """
    Rileva anomalie nel segnale audio per Udio Forensics Tool.
    """
    try:
        data, sample_rate = sf.read(audio_file)
        
        # Zero-crossing rate
        zcr = np.mean(np.abs(np.diff(np.sign(data)))) / sample_rate
        
        # Noise floor
        noise_floor = np.mean(np.abs(data))
        
        # Calcola il loudness (RMS-based)
        rms = np.sqrt(np.mean(data**2))
        loudness_mean = 20 * np.log10(rms) if rms > 0 else -np.inf  # Loudness medio in dBFS
        loudness_max = 20 * np.log10(np.max(np.abs(data))) if np.max(np.abs(data)) > 0 else -np.inf  # Loudness massimo in dBFS
        
        # Identifica i segmenti silenziosi
        silence_threshold = 0.01  # Soglia per considerare un segmento silenzioso
        silent_segments = np.where(np.abs(data) < silence_threshold)[0]
        silent_segments_count = len(silent_segments)
        
        # Calcola la durata del segmento non silenzioso più lungo
        non_silent_segments = np.where(np.abs(data) >= silence_threshold)[0]
        if len(non_silent_segments) > 0:
            longest_non_silent_segment = np.max(np.diff(non_silent_segments)) / sample_rate
        else:
            longest_non_silent_segment = 0
        
        return {
            'zero_crossing_rate': zcr,
            'noise_floor': noise_floor,
            'loudness_mean': loudness_mean,
            'loudness_max': loudness_max,
            'silent_segments': silent_segments_count,
            'longest_non_silent_segment': longest_non_silent_segment
        }
    except Exception as e:
        print(f"Errore durante il rilevamento delle anomalie: {e}")
        return None