from os import path
import json



def _load_icon_list():
    icon_list_path = path.join(path.dirname(__file__), "src", "icons.json")
    with open(icon_list_path, "r") as f:
        icon_list = json.load(f)
    return icon_list


def lavenderIcon(ext):
    icon_list = _load_icon_list()
    ext = ext.upper()
    if ext in icon_list:
        return icon_list[ext]
    else:
        return icon_list["DEFAULT"]

__all__ = ["lavenderIcon"]
