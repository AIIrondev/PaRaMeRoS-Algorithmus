# Log file wird in einen Grafen umgewandelt und exportiert
# Input: Log file
# Output: Graph


## import area
import os
import logging
# import pandas as pd
import matplotlib.pyplot as plt

## var Area
csv_folder = 'csv_files'
log_folder = 'log_files'
export_folder = 'export_folder'
data = []
data_length = []
fig, ax = plt.subplots()
time_span = []
time_difference = []

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
        lines = f.readlines()
        data_length.append(len(lines))
        data.append(lines)
        extracted_data = []
        time_stamps = []
        for line in lines:
            parts = line.split(' - ')
            date_time = parts[0].strip()
            file_name = parts[1].strip()
            log_level = parts[2].strip()
            message = parts[3].strip()
            extracted_data.append((date_time, file_name, log_level, message))
            print(date_time)
            time_stamps.append(date_time)
        if time_stamps:
            cleaned_string_1 = ''.join(filter(str.isdigit, time_stamps[0]))
            numeric_value_1 = cleaned_string_1
            formatted_string = '.'.join(
                [numeric_value_1[:4], numeric_value_1[4:6], numeric_value_1[6:8], numeric_value_1[8:10], numeric_value_1[10:12],
                 numeric_value_1[12:14], numeric_value_1[14:]])
            time_span.extend([min(time_stamps), max(time_stamps)])
            time_difference.append(formatted_string)
            print(time_difference)
        return extracted_data


def create_statistic(data_1, data_2, titel, ytitel, xtitel, legend_label_1, export_file):
    fig, ax = plt.subplots()
    ax.grid()
    ax.set_title(titel)
    ax.set_ylabel(ytitel)
    ax.set_xlabel(xtitel)
    ax.plot(data_1, data_2, label=legend_label_1, color='red', marker='X', linestyle=':')
    fig.savefig(os.path.join(export_folder, export_file))
    plt.show()


def export_data(data_export):
    with open(os.path.join(export_folder, 'export.csv'), 'w') as f:
        f.write(data_export)
        return data


def main():
    logger.info("Main function")

    extract_data(os.path.join(log_folder, 'sys.log'))
    # Zeit auf x-achse und y-achse die Anzahl der einträge
    x_values = time_difference
    create_statistic(x_values, data_length, 'Zeit auf Anzahl der Einträge', 'Anzahl der Einträge', 'Zeit',
                     'Anzahl der Einträge', 'export_Zeit_auf_menge.png')
    if ValueError:
        logger.error("ValueError")
    else:
        logger.info("Exported data to export_Zeit_auf_menge.png")
    # Datentypen(Error, Debug und Warning, info) auf x-achse und y-achse Anzahl der einträge
    create_statistic(data[2], data_length, 'Datentypen auf Anzahl der Einträge', 'Anzahl der Einträge', 'Datentypen',
                     'Anzahl der Einträge', 'export_Datentypen_auf_menge.png')
    if ValueError:
        logger.error("ValueError")
    else:
        logger.info("Exported data to export_Datentypen_auf_menge.png")
    # Zeit auf x-achse und y-achse Datentypen(Error, Debug und Warning, info)
    create_statistic(time_span, data[2], 'Zeit auf Datentypen', 'Datentypen', 'Zeit', 'Datentypen',
                     'export_Zeit_auf_Datentypen.png')
    if ValueError:
        logger.error("ValueError")
    else:
        logger.info("Exported data to export_Zeit_auf_Datentypen.png")
    # Verschiedene Files auf x-achse und y-achse Anzahl der einträge
    create_statistic(data[1], data_length, 'Verschiedene Files auf Anzahl der Einträge', 'Anzahl der Einträge',
                     'Verschiedene Files', 'Anzahl der Einträge', 'export_Verschiedene_Files_auf_menge.png')
    if ValueError:
        logger.error("ValueError")
    else:
        logger.info("Exported data to export_Verschiedene_Files_auf_menge.png")


## run Area
if __name__ == '__main__':
    main()
