# -*- coding: utf-8 -*-
import json
import pytest
from src.JsonDataReader import JsonDataReader


def test_read_dict_format(tmp_path):
    data = {
        "Иванов Иван Иванович": {"математика": 91, "литература": 78},
        "Петров Петр Петрович": {"химия": 61}
    }
    p = tmp_path / "data.json"
    p.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')

    expected = {
        "Иванов Иван Иванович": [("математика", 91), ("литература", 78)],
        "Петров Петр Петрович": [("химия", 61)]
    }

    got = JsonDataReader().read(str(p))
    assert got == expected


def test_read_malformed_json(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("not a json", encoding='utf-8')
    with pytest.raises(json.JSONDecodeError):
        JsonDataReader().read(str(p))


def test_read_invalid_structure(tmp_path):
    # корень — список, или значения не являются dict
    p = tmp_path / "bad2.json"
    p.write_text(json.dumps(["wrong", "structure"]), encoding='utf-8')
    with pytest.raises(ValueError):
        JsonDataReader().read(str(p))
