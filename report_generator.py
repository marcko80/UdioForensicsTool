from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import os

def generate_report(audio_path, info, anomalies, tampering_results, output_path, spectrum_path, discontinuita_path):
    """
    Genera un report PDF con i risultati dell'analisi audio.
    
    :param audio_path: Percorso del file audio.
    :param info: Informazioni tecniche estratte dal file audio.
    :param anomalies: Risultati del rilevamento delle anomalie.
    :param tampering_results: Risultati del rilevamento delle manipolazioni.
    :param output_path: Percorso di output per il report PDF.
    :param spectrum_path: Percorso dell'immagine dello spettrogramma.
    :param discontinuita_path: Percorso dell'immagine del grafico delle discontinuità.
    """
    # Crea il documento PDF
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Titolo del report
    story.append(Paragraph(f'Relazione Tecnica Forense sul File Audio "{os.path.basename(audio_path)}"', styles['Title']))
    story.append(Spacer(1, 12))

    # 1. Introduzione
    story.append(Paragraph("1. Introduzione", styles['Heading2']))
    intro_text = f"""
    Il file audio oggetto di analisi, denominato "{os.path.basename(audio_path)}", è stato ricevuto in formato "{info.get('format', 'N/A')}" ed è stato sottoposto ad analisi forense completa.
    """
    story.append(Paragraph(intro_text, styles['BodyText']))
    story.append(Spacer(1, 12))

    # 2. Caratteristiche Tecniche
    story.append(Paragraph("2. Caratteristiche Tecniche", styles['Heading2']))
    tech_info_text = f"""
    Il file presenta le seguenti proprietà complessive:

    Durata complessiva: {info.get('duration', 'N/A')} secondi<br/>
    Formato: {info.get('format', 'N/A')}<br/>
    Canali audio: {info.get('channels', 'N/A')}<br/>
    Frequenza di campionamento: {info.get('sample_rate', 'N/A')} Hz<br/>
    Risoluzione campione: {info.get('bit_depth', 'N/A')} bit<br/>
    """
    story.append(Paragraph(tech_info_text, styles['BodyText']))
    story.append(Spacer(1, 12))

    # 3. Analisi del Contenuto Audio
    story.append(Paragraph("3. Analisi del Contenuto Audio", styles['Heading2']))
    analysis_text = f"""
    Durata: {info.get('duration', 'N/A')} secondi<br/>
    Loudness medio: {anomalies.get('loudness_mean', 'N/A')} dBFS<br/>
    Loudness massimo: {anomalies.get('loudness_max', 'N/A')} dBFS<br/>
    Segmenti silenziosi identificati: {anomalies.get('silent_segments', 'N/A')}<br/>
    Durata del segmento non silenzioso più lungo: {anomalies.get('longest_non_silent_segment', 'N/A')} secondi<br/>
    """
    story.append(Paragraph(analysis_text, styles['BodyText']))
    story.append(Spacer(1, 12))

    # Aggiungi lo spettrogramma al report
    if os.path.exists(spectrum_path):
        story.append(Paragraph("Spettrogramma", styles['Heading2']))
        story.append(Image(spectrum_path, width=400, height=300))
        story.append(Spacer(1, 12))

    # Aggiungi il grafico delle discontinuità al report
    if os.path.exists(discontinuita_path):
        story.append(Paragraph("Analisi delle Discontinuità", styles['Heading2']))
        story.append(Image(discontinuita_path, width=400, height=300))
        story.append(Spacer(1, 12))

    # Costruisci il PDF
    doc.build(story)