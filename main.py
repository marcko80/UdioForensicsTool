import sys
import logging
from PyQt5.QtWidgets import QApplication
from gui import MainWindow

# Configura il sistema di logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

def main():
    logging.info("Avvio dell'applicazione Udio Forensics Tool.")
    app = QApplication(sys.argv)

    try:
        window = MainWindow()
        window.show()
        logging.info("Finestra principale visualizzata.")
        sys.exit(app.exec_())
    except Exception as e:
        logging.error(f"Errore durante l'esecuzione dell'applicazione: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()