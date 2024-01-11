import os
import logging
import matplotlib.pyplot as plt
import ftplib

# Verzeichnisnamen
csv_folder = '../csv_files'
log_folder = '../log_files'
export_folder = '../export_folder'

# Listen zur Datenspeicherung
data_length = []
time_difference = []

# Konfigurieren des Loggers
logger = logging.getLogger('data_generator.py')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(os.path.join(log_folder, 'sys.log'))
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def conf():
    logger.debug("conf...")
    global csv_folder, log_folder, export_folder

    with open("../data_generator.config", "r") as f:
        lines = f.readline(1)
        lines = lines.split(" , ")
        csv_folder = lines[0].strip()
        log_folder = lines[1].strip()
        export_folder = lines[2].strip()

    # Überprüfen und Erstellen der Ordner
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)
        logger.warning(f"Folder {csv_folder} created.")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
        logger.warning(f"Folder {log_folder} created.")
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
        logger.warning(f"Folder {export_folder} created.")


# Funktion zum Extrahieren von Daten aus der Log-Datei
def extract_data(file):
    logger.debug("extract_data...")
    extracted_data = []
    entries_per_day = {}
    log_levels = []

    with open(file, 'r') as f:
        lines = f.readlines()
        data_length.append(len(lines))

        for line in lines:
            parts = line.split(' - ')
            date_time = parts[0].strip()
            file_name = parts[1].strip()
            log_level = parts[2].strip()
            message = parts[3].strip()

            # Holen Sie das Datum aus dem Zeitstempel
            date = date_time.split()[0]

            # Zählen Sie die Anzahl der Einträge für dieses Datum
            if date in entries_per_day:
                entries_per_day[date] += 1
            else:
                entries_per_day[date] = 1

            log_levels.append(log_level)
            extracted_data.append((date_time, message))

            return entries_per_day, log_levels, file_name


# Funktion zum Erstellen und Speichern von Statistiken als Grafik
def create_statistic(data_1, data_2, title, y_label, x_label, legend_label, export_file):
    logger.debug("create_statistic...")
    fig, ax = plt.subplots()
    ax.grid()
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.plot(data_1, data_2, label=legend_label, color='red', marker='X', linestyle=':')
    fig.savefig(os.path.join(export_folder, export_file))
    plt.show()


# Funktion zum Erstellen eines Balkendiagramms
def create_bar_chart(data_1, data_2, title, y_label, x_label, export_file):
    logger.debug("create_bar_chart...")
    plt.bar(data_1, data_2, color='blue')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(export_folder, export_file))
    plt.show()


def export_data_ftp(files):
    logger.debug("ftp_export...")
    ftp = ftplib.FTP()
    host = "Parameros.com"
    port = 21
    ftp.connect(host, port)
    print(ftp.getwelcome())
    try:
        print("Logging in...")
        ftp.login("Server2-1", "password") # Username und Passwort
        logger.info("successful login")
        ftp.storbinary("STOR " + files, open(files, "rb"))
    except ftplib.all_errors:
        logger.error("failed login")
        print("WARNING: !!!Error was not able to connect to ftp server!!!!")


# Hauptfunktionsaufruf
def main():
    logger.info("Main...")

    entries_per_day, log_levels, files = extract_data(os.path.join(log_folder, 'sys.log'))

    # Extrahierte Daten pro Tag
    x_values = list(entries_per_day.keys())
    y_values = list(entries_per_day.values())

    create_bar_chart(x_values, y_values, 'Log-Menge pro Tag', 'Anzahl der Einträge', 'Datum', 'export_Log_Menge_pro_Tag.png')
    create_statistic(x_values, y_values, 'Log-Menge pro Tag', 'Anzahl der Einträge', 'Datum',
                     'Anzahl der Einträge pro Tag', 'export_Log_Menge_pro_Tag.png')
    logger.info("Exported data to export_Log_Menge_pro_Tag.png")

    # Anzahl der Einträge nach Log-Level
    log_level_count = [log_levels.count('DEBUG'), log_levels.count('INFO'), log_levels.count('WARNING'), log_levels.count('ERROR')]
    log_level_labels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

    create_bar_chart(log_level_labels, log_level_count, 'Anzahl der Einträge nach Log-Level', 'Anzahl der Einträge',
                     'Log-Level', 'export_Log_Level.png')
    logger.info("Exported data to export_Log_Level.png")


    log_level_labels_1 = [files.count('A_star.py'), files.count('data_generator.py'), files.count('Algorithmus.py'), files.count('Dijkstra´s_Algorithm.py')]
    log_level_count_1 = ['A_star.py', 'data_generator.py', 'main.py', 'test.py']

    create_bar_chart(log_level_count_1, log_level_labels_1, 'Anzahl der Einträge nach Datei',
                     'Anzahl der Einträge', 'Dateien', 'export_Datei.png')

    logger.info("Exported data to export_Datei.png")


# Ausführung der Hauptfunktion
if __name__ == '__main__':
    conf()
    main()
