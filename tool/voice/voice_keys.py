"""Klonlangan ovoz fayllari kaliti — `lib/services/cloned_voice.dart` bilan aynan bir xil."""
import re

_APOS = re.compile("[’ʻʼ'`]")
_SPACES = re.compile(r"\s+")


def normalize(text: str) -> str:
    return _SPACES.sub(" ", _APOS.sub("‘", text.strip()))


def key_for(text: str) -> str:
    h = 0xCBF29CE484222325
    for b in normalize(text).encode("utf-8"):
        h ^= b
        h = (h * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
    return f"{h:016x}"


if __name__ == "__main__":
    assert key_for("Qaysi rasm boshqalardan farq qiladi?") == "5240d0ad310e573c"
    assert key_for("Кто играет?") == "0a4defc333dc277b"
    print("ok")
