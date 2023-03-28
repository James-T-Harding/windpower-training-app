from dataclasses import dataclass

from keys.constants import MET, ELEXON


@dataclass
class Keys:
    met_key: str
    elexon_key: str

    @classmethod
    def from_data(cls, data):
        met_key = data.get(MET, "")
        elexon_key = data.get(ELEXON, "")

        return cls(met_key, elexon_key)
