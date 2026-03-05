import os
from ultimapy.sdk.art import Art
from ultimapy.sdk.gumps import Gumps


class UOClient:
    """
    Wraps ultimapy SDK access for a given UO client directory.
    Sets ULTIMA_FILES_DIR before each operation so multiple clients
    can coexist in the same process.
    """

    def __init__(self, client_path: str):
        self.client_path = os.path.abspath(client_path)
        os.environ["ULTIMA_FILES_DIR"] = self.client_path

    def _activate(self):
        """Re-apply the env var in case another UOClient was used after init."""
        os.environ["ULTIMA_FILES_DIR"] = self.client_path

    def get_static(self, item_id: int):
        self._activate()
        return Art.get_static(item_id, check_max_id=False)

    def get_land(self, tile_id: int):
        self._activate()
        return Art.get_land(tile_id)

    def get_gump(self, gump_id: int):
        self._activate()
        return Gumps.get_gump(gump_id)
