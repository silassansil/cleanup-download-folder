import yaml

with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    _folder = config['folder']
    _extensions = config['extensions']
    _delete_unknown_file = config['delete']['unknown']


def retrieve_config_data():
    return _folder, _extensions, _delete_unknown_file
