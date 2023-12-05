
import os
import json
import datetime
from typing import Any
from .app_errors import error_handler
from .app_errors import OpenStorageError, SaveStorageError
from services.files import settings


@error_handler
def read_all_data_from_storage() -> Any:
    try:
        with open(find_storage_path(), 'r+') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        raise OpenStorageError


@error_handler
def write_new_data_to_storage(data: dict[str, Any]) -> None:
    try:
        with open(find_storage_path(), 'w+') as json_file:
            json.dump(data, json_file, indent=4, default=datetime_serializer)
    except FileNotFoundError:
        raise SaveStorageError


def find_storage_path() -> str:
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)

    json_file_path = os.path.join(parent_dir, settings.STORAGE_FOLDER, settings.STORAGE_FILE_NAME)
    return json_file_path


def datetime_serializer(date: datetime.datetime) -> str:   
    if isinstance(date, datetime.datetime):
        return date.strftime(settings.DATA_TYPE_PRINT)
    raise TypeError
