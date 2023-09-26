# Log file wird in einen Grafen umgewandelt und exportiert
# Input: Log file
# Output: Graph


## import area
import os
import logging
import pandas as pd
import matplotlib.pyplot as plt


## var Area
csv_folder = 'csv_files'
log_folder = 'log_files'
export_folder = 'export_files'
data = {}

# Konfigurieren des Loggers für die Protokollierung von Informationen
logger = logging.getLogger('A_star.py')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(os.path.join(log_folder, 'sys.log'))
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Überprüfen und Erstellen der Ordner für CSV-Dateien und Log-Dateien
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)
    logger.warning(f"Folder {csv_folder} created.")
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    logger.warning(f"Folder {log_folder} created.")
if not os.path.exists(export_folder):
    os.makedirs(export_folder)
    logger.warning(f"Folder {export_folder} created.")


## def Area
def extract_data(file):
    with open(file, 'r') as f:
        f.read()
        data.append(f)
        return data

def export_data(data):
    with open(os.path.join(export_folder, 'export.csv'), 'w') as f:
        f.write(data)
        return data

def main():
    print("Main function")
    # zeit auf x-achse und y-achse die Anzahl der einträge

    # Datentypen(Error, Debug und Warning , info) auf x-achse und y-achse Anzahl der einträge

    # Zeit auf x-achse und y-achse Datentypen(Error, Debug und Warning , info)

    
## run Area
if __name__ == '__main__':
    main()