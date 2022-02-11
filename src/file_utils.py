import os
import shutil


def _generate_abs_path(_root, _filename):
    return f'{_root}/{_filename}'


def _move_file(_root, _destination_path, _filename):
    os.makedirs(_destination_path, exist_ok=True)
    shutil.move(
        _generate_abs_path(_root, _filename),
        _generate_abs_path(_destination_path, _filename)
    )
