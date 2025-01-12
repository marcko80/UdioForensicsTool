from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(audio_file, info, anomalies, report_path, spectrum_path):
    """
    Genera un report PDF per Udio Forensics Tool.
    """
    try:
        c = canvas.Canvas(report_path, pagesize=letter)
        c.drawString(100, 750, 'Udio Forensics Tool - Audio Analysis Report')
        c.drawString(100, 730, '============================================')
        c.drawString(100, 700, f'File: {info["filename"]}')
        c.drawString(100, 680, f'Sample Rate: {info["sample_rate"]} Hz')
        c.drawString(100, 660, f'Bit Depth: {info["bit_depth"]} bits')
        c.drawString(100, 640, f'Channels: {info["channels"]}')
        c.drawString(100, 620, f'Duration: {info["duration"]} seconds')
        c.drawString(100, 600, f'File Size: {info["file_size"]} bytes')
        c.drawString(100, 580, 'Anomalies:')
        c.drawString(120, 560, f'Zero Crossing Rate: {anomalies["zero_crossing_rate"]}')
        c.drawString(120, 540, f'Noise Floor: {anomalies["noise_floor"]}')
        c.drawImage(spectrum_path, 100, 100, width=500, height=400)
        c.save()
    except Exception as e:
        print(f"Errore durante la generazione del report: {e}")