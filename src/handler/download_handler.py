import os
import shutil
import time

from src.file_utils import _generate_abs_path
from src.resource_handler import define_destination_path


class DownloadHandler:
    def __init__(self, download, image, document, music):
        self._download = download
        self._image = image
        self._document = document
        self._music = music

    def do_execute(self):
        print(f'[INFO] - {time.ctime()} - starting migration file process ')
        print(f'###########################################################')
        for root, directories, files in os.walk(self._download, topdown=False):
            for file in files:
                print(f'[INFO] - {time.ctime()} - file {file} was found')
                _filename, _file_extension = os.path.splitext(file)
                _destination_path = define_destination_path(_file_extension)

                if not _destination_path:
                    print(f'[WARN] - {time.ctime()} - file {file} will be delete')
                    os.remove(_generate_abs_path(root, file))
                else:
                    _destination_path = self._replace_root_by_destination(root, _destination_path)
                    print(f'[INFO] - {time.ctime()} - file {file} will be moved to {_destination_path}')
                    os.makedirs(_destination_path, exist_ok=True)
                    shutil.move(
                        _generate_abs_path(root, file),
                        _generate_abs_path(_destination_path, file)
                    )
            for d in directories:
                shutil.rmtree(os.path.join(root, d))
        print(f'###########################################################')
        print(f'[INFO] - {time.ctime()} - ending migration file process')

    def _replace_root_by_destination(self, _root, _destination_path):
        return _root.replace(self._download, _destination_path)
