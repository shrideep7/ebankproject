import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('information', 'URL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('information', 'user_id')
        return username

    @staticmethod
    def getPassword():
        password = config.get('information', 'password')
        return password
