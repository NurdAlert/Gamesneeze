import configparser

def get_from_cfg(section : str, key : str):

    parser = configparser.ConfigParser()
    parser.read("cfg.ini")
    return parser.get(section, key)