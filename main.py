from src.handler.config_handler import retrieve_config_data
from src.handler.download_handler import DownloadHandler

if __name__ == '__main__':
    _folders, _, _ = retrieve_config_data()
    _handler = DownloadHandler(
        download=_folders['download'],
        music=_folders['music'],
        image=_folders['image'],
        document=_folders['document'],
    ).do_execute()
