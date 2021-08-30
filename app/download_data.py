from functions import *
import time
import os
import pdb


os.chdir('/home/alessandro/Scrivania/work/personal/QSapp/app')

FILE_CONFIG = "configs/config.ini"
DOWNLOAD_FOLDER = '/home/alessandro/Scaricati'


def get_qs_data(url):
    # Download data, extract csv from zip
    webbrowser.open(url)
    time.sleep(5)


@do_profile()
def main():
    Config = configparser_set(FILE_CONFIG)
    print(f'Ciao bello this is {Config.get("GENERAL", "version")}')
    start_time = time.time()
    url = Config.get("GENERAL", "url_qs_final")
    get_qs_data(url)
    elapsed_time = round(time.time() - start_time, 2)
    print(f'hey bello ci ha messo {elapsed_time} secondi')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
