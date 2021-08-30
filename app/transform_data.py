from functions import *
import time
import pandas as pd


FILE_CONFIG = "./app/configs/config.ini"
DOWNLOAD_FOLDER = '/home/alessandro/Scaricati'
OUTPUT_FOLDER = './app/data'


COLOR = "black"
BACKGROUND_COLOR = "#fff"


def read_qs_data(DOWNLOAD_FOLDER):
    files = glob.glob(os.path.join(DOWNLOAD_FOLDER, '*.zip'))
    last_download = max(files, key=os.path.getctime)
    data = pd.read_csv(last_download)
    return data



def clean_data(data):
    # Set datetime index
    today = date.today()
    day = []
    for i in range(0, len(data)):
        day.append(data['Informazioni cronologiche'][i][0:10])
    data['day'] = day
    data['day'] = pd.to_datetime(data['day'])
    data.set_index('day', inplace=True)
    data.sort_index(ascending=True)
    data = data.loc[:today]
    return data



def main():
    Config = configparser_set(FILE_CONFIG)
    print(f'Ciao bello this is {Config.get("GENERAL", "version")}')
    start_time = time.time()
    data = read_qs_data(DOWNLOAD_FOLDER)
    data = clean_data(data)
    elapsed_time = round(time.time() - start_time, 2)
    print(f'hey bello ci ha messo {elapsed_time}')
    # write_configparser_set(FILE_CONFIG, elapsed_time)
    data.to_csv(os.path.join(OUTPUT_FOLDER, 'data.csv'))



if __name__ == '__main__':
    main()
    print('transformation finito!!')
