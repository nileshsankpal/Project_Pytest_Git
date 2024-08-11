import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig_Class:
    @staticmethod
    def getusername():
        username = config.get('Login Data', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('Login Data', 'password')
        return password
