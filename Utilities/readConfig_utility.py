import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig_class:
    @staticmethod
    def username_data():
        username=config.get("Login Data", "username")
        return username
    @staticmethod
    def password_data():
        password=config.get("Login Data", "password")
        return password
    @staticmethod
    def base_url():
        base_url = config.get("Application Url", "base_url")
        return base_url

    @staticmethod
    def login_url():
        login_url = config.get("Application Url", "login_url")
        return login_url

    @staticmethod
    def signup_url():
        signup_url = config.get("Application Url", "signup_url")
        return signup_url
