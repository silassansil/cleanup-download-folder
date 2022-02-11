import yaml

with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    _folder = config['folder']
    _extensions = config['extensions']


def retrieve_config_data():
    return _folder, _extensions
