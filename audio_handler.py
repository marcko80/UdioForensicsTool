import soundfile as sf
import os

def get_audio_info(audio_file):
    """
    Estrae le informazioni tecniche del file audio per Udio Forensics Tool.
    """
    try:
        data, sample_rate = sf.read(audio_file)
        info = sf.info(audio_file)
        # Calcola la profondità di bit in base al tipo di dato
        bit_depth = data.dtype.itemsize * 8 if hasattr(data, 'dtype') else 'N/A'
        return {
            'filename': os.path.basename(audio_file),
            'sample_rate': info.samplerate,
            'bit_depth': bit_depth,
            'channels': info.channels,
            'duration': info.duration,
            'file_size': os.path.getsize(audio_file)
        }
    except Exception as e:
        print(f"Errore durante l'estrazione delle informazioni: {e}")
        return None