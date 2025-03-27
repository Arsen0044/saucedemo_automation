import os
import configparser


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def set_env_config():
    abs_path = f'{ROOT_DIR}/configuration.ini'
    config = configparser.RawConfigParser()
    config.read(abs_path)
    return config


class ReadAppInfoConfig:

    def __init__(self):
        self.config = set_env_config()

    def get_base_url(self):
        return self.config.get('app_info', 'base_url')


class ReadUserDataConfig:

    def __init__(self):
        self.config = set_env_config()

    def get_standard_user_name(self):
        return self.config.get('user_data', 'standard_user_name')

    def get_standard_user_password(self):
        return self.config.get('user_data', 'standard_user_password')


class Constants:

    """Read configuration constants"""
    app_info_configs = ReadAppInfoConfig()
    user_data_config = ReadUserDataConfig()

    """Links"""
    base_url = app_info_configs.get_base_url()

    """User Data"""
    standard_user_name = user_data_config.get_standard_user_name()
    standard_user_password = user_data_config.get_standard_user_password()

