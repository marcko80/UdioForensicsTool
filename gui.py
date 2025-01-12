import sys
import os
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QProgressBar, QHBoxLayout, QMessageBox, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import audio_handler
import spectral_analysis
import anomaly_detection
import report_generator
from tampering_detection import detect_tampering

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Udio Forensics Tool')
        self.setGeometry(100, 100, 800, 600)

        # Layout principale
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Etichetta "Created by Marco Calonzi"
        self.label_credits = QLabel('Created by Marco Calonzi', self)
        self.label_credits.setAlignment(Qt.AlignCenter)
        self.label_credits.setStyleSheet("font-size: 12px; color: gray;")
        self.layout.addWidget(self.label_credits)

        # Pulsante per caricare il file audio
        self.btn_load = QPushButton('Carica File Audio', self)
        self.btn_load.clicked.connect(self.load_audio)
        self.layout.addWidget(self.btn_load)

        # Etichetta per visualizzare il file caricato
        self.label_file = QLabel('Nessun file caricato', self)
        self.label_file.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_file)

        # Pulsante per avviare l'analisi completa
        self.btn_analyze = QPushButton('Analizza e Rileva Manipolazioni', self)
        self.btn_analyze.clicked.connect(self.start_analysis)
        self.btn_analyze.setEnabled(False)  # Disabilitato fino al caricamento del file
        self.layout.addWidget(self.btn_analyze)

        # Barra di progressione
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setVisible(False)  # Nascosta inizialmente
        self.layout.addWidget(self.progress_bar)

        # Area di testo per visualizzare le informazioni
        self.text_info = QTextEdit(self)
        self.text_info.setReadOnly(True)
        self.layout.addWidget(self.text_info)

        # Etichetta per visualizzare lo spettro
        self.label_spectrum = QLabel(self)
        self.label_spectrum.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_spectrum)

        # Timer per simulare la progressione
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    def load_audio(self):
        """
        Carica un file audio.
        """
        logging.info("Avvio del caricamento del file audio.")
        options = QFileDialog.Options()
        self.audio_file, _ = QFileDialog.getOpenFileName(self, "Seleziona File Audio", "", "Audio Files (*.wav *.mp3 *.aac *.ogg *.flac *.m4a *.3gpp)", options=options)
        if self.audio_file:
            logging.info(f"File audio caricato: {self.audio_file}")
            self.label_file.setText(f'File caricato: {self.audio_file}')
            self.btn_analyze.setEnabled(True)  # Abilita il pulsante di analisi
        else:
            logging.warning("Nessun file audio selezionato.")

    def start_analysis(self):
        """
        Avvia l'analisi completa del file audio.
        """
        if not hasattr(self, 'audio_file'):
            logging.error("Nessun file audio caricato.")
            QMessageBox.warning(self, 'Errore', 'Nessun file audio caricato!')
            return

        logging.info("Avvio dell'analisi completa del file audio.")
        self.btn_load.setEnabled(False)
        self.btn_analyze.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.timer.start(100)  # Aggiorna la barra ogni 100 ms

    def update_progress(self):
        """
        Simula l'avanzamento dell'analisi e aggiorna la barra di progressione.
        """
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 10)
        else:
            self.timer.stop()
            self.perform_analysis()

    def perform_analysis(self):
        """
        Esegue l'analisi completa del file audio.
        """
        try:
            logging.info("Estrazione delle informazioni tecniche del file audio.")
            self.info = audio_handler.get_audio_info(self.audio_file)
            if not self.info:
                raise Exception("Errore durante l'estrazione delle informazioni.")

            logging.info("Rilevamento delle anomalie nel file audio.")
            self.anomalies = anomaly_detection.detect_anomalies(self.audio_file)
            if not self.anomalies:
                raise Exception("Errore durante il rilevamento delle anomalie.")

            logging.info("Generazione dello spettrogramma.")
            self.spectrum_path = os.path.join(os.path.dirname(self.audio_file), 'spectrum.png')
            spectral_analysis.plot_spectrum(self.audio_file, self.spectrum_path)

            logging.info("Rilevamento delle manipolazioni nel file audio.")
            tampering_results, discontinuita_path = detect_tampering(self.audio_file)  # Ottieni il percorso del grafico

            logging.info("Generazione del report PDF.")
            report_path = os.path.join(os.path.dirname(self.audio_file), 'audio_analysis_report.pdf')
            report_generator.generate_report(
                self.audio_file, 
                self.info, 
                self.anomalies, 
                tampering_results, 
                report_path, 
                self.spectrum_path,
                discontinuita_path  # Passa il percorso del grafico delle discontinuità
            )

            logging.info("Visualizzazione dei risultati.")
            self.text_info.setText(f'Informazioni:\n{self.info}\nAnomalie:\n{self.anomalies}\nManipolazioni rilevate:\n{tampering_results}')
            pixmap = QPixmap(self.spectrum_path)
            self.label_spectrum.setPixmap(pixmap.scaled(600, 400))

            self.btn_load.setEnabled(True)
            self.btn_analyze.setEnabled(True)
            self.progress_bar.setVisible(False)

            logging.info("Analisi completata con successo.")
            QMessageBox.information(self, 'Completato', f'Analisi completata con successo!\nReport salvato in: {report_path}')
        except Exception as e:
            logging.error(f"Errore durante l'analisi: {e}", exc_info=True)
            QMessageBox.critical(self, 'Errore', f"Si è verificato un errore durante l'analisi: {str(e)}")
            self.btn_load.setEnabled(True)
            self.btn_analyze.setEnabled(True)
            self.progress_bar.setVisible(False)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()