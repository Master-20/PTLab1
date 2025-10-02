# -*- coding: utf-8 -*-
import pytest
from src.ThirdQ import ThirdQ
from src.Types import DataType


def sample_data() -> DataType:
    return {
        "A Student": [("mat", 100)],
        "B Student": [("mat", 80)],
        "C Student": [("mat", 60)],
        "D Student": [("mat", 40)]
    }


def test_threshold_and_top():
    data = sample_data()
    tq = ThirdQ(data)
    thr = tq.threshold()
    # значения рейтингов:
    # [100,80,60,40] -> 75-й процентиль = 85.0 (интерполяция)
    #                   50-й процентиль = 70.0 (интерполяция)
    assert pytest.approx(thr[0], rel=1e-6) == 70.0
    assert pytest.approx(thr[1], rel=1e-6) == 85.0

    top = tq.thirdq_students()
    assert list(top.keys()) == ["B Student"]
    assert top["B Student"] == 80


def test_print_top(capsys):
    tq = ThirdQ(sample_data())
    tq.print_3q()
    captured = capsys.readouterr()
    assert "Third quartile students" in captured.out
    assert "B Student: 80.0000" in captured.out


def test_empty_data():
    tq = ThirdQ({})
    with pytest.raises(ValueError):
        tq.threshold()
