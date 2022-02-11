from src.handler.config_handler import retrieve_config_data


def define_destination_path(_extension):
    _folders, _extensions = retrieve_config_data()
    _type_file = next(
        (k for k, v in _extensions.items() if _extension in v), None
    )
    return _folders.get(
        _type_file, None
    )


if __name__ == '__main__':
    define_destination_path('.pdf')
