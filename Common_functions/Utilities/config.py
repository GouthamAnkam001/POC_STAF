import configparser
def get_data(filepath,section,key):
    config = configparser.ConfigParser()
    config.read(filepath)
    return config.get(section,key)






 # def config(path,section,key ):
