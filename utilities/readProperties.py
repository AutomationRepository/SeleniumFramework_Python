import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        url = config.get('common info', 'username')
        return url

    @staticmethod
    def getPassword():
        url = config.get('common info', 'password')
        return url
