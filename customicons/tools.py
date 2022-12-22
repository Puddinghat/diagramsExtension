from diagrams import Node
from pathlib import Path
import os

class CustomIcon(Node):
    _provider = "customicons"
    _icon_dir = "customicons/icons"

    fontcolor = "#ffffff"

    def _load_icon(self):
        basedir = Path(os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basedir.parent, self._icon_dir, self._icon)

class Opensearch(CustomIcon):
    _type = "opensearch"
    _icon = "opensearch.png"