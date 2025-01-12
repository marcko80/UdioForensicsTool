from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
import os

def generate_report(audio_path, info, anomalies, tampering_results, output_path, spectrum_path):
    """
    Genera un report PDF con i risultati dell'analisi audio.
    
    :param audio_path: Percorso del file audio.
    :param info: Informazioni tecniche estratte dal file audio.
    :param anomalies: Risultati del rilevamento delle anomalie.
    :param tampering_results: Risultati del rilevamento delle manipolazioni.
    :param output_path: Percorso di output per il report PDF.
    :param spectrum_path: Percorso dell'immagine dello spettrogramma.
    """
    # Crea il documento PDF
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Titolo del report
    story.append(Paragraph("Udio Forensics Tool - Report di Analisi", styles['Title']))
    story.append(Spacer(1, 12))

    # Informazioni sul file audio
    story.append(Paragraph("Informazioni sul File Audio", styles['Heading2']))
    info_text = f"""
    Nome file: {os.path.basename(audio_path)}<br/>
    Sample rate: {info.get('sample_rate', 'N/A')} Hz<br/>
    Bit depth: {info.get('bit_depth', 'N/A')} bit<br/>
    Canali: {info.get('channels', 'N/A')}<br/>
    Durata: {info.get('duration', 'N/A')} secondi<br/>
    Dimensione file: {info.get('file_size', 'N/A')} byte<br/>
    """
    story.append(Paragraph(info_text, styles['BodyText']))
    story.append(Spacer(1, 12))

    # Risultati delle anomalie
    story.append(Paragraph("Risultati delle Anomalie", styles['Heading2']))
    anomalies_text = f"""
    Zero crossing rate: {anomalies.get('zero_crossing_rate', 'N/A')}<br/>
    Noise floor: {anomalies.get('noise_floor', 'N/A')}<br/>
    """
    story.append(Paragraph(anomalies_text, styles['BodyText']))
    story.append(Spacer(1, 12))

    # Risultati del rilevamento delle manipolazioni
    story.append(Paragraph("Risultati del Rilevamento delle Manipolazioni", styles['Heading2']))
    if hasattr(tampering_results, 'any') and tampering_results.any():
        tampering_text = "Anomalie rilevate ai seguenti timestamp (s):<br/>"
        for timestamp in tampering_results:
            tampering_text += f"- {timestamp:.2f} s<br/>"
    else:
        tampering_text = "Nessuna anomalia rilevata."
    story.append(Paragraph(tampering_text, styles['BodyText']))
    story.append(Spacer(1, 12))

    # Aggiungi lo spettrogramma al report
    if os.path.exists(spectrum_path):
        story.append(Paragraph("Spettrogramma", styles['Heading2']))
        story.append(Image(spectrum_path, width=400, height=300))
        story.append(Spacer(1, 12))

    # Costruisci il PDF
    doc.build(story)