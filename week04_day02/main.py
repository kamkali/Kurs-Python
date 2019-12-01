import sklearn.neighbors
import pandas as pd
import logger


@logger.log_exec_time
def transform_data():
    log = logger.get_logger('exec_time.log')

    log.info("-----Reading data.csv-----")
    malware_data = pd.read_csv('data.csv')
    malware_data.drop_duplicates().dropna()
    # malware_data.drop('Name', axis='columns')
    print(malware_data.head(1))
    # print(malware_data[90000::])


if __name__ == '__main__':
    transform_data()
