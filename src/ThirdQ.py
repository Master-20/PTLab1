# -*- coding: utf-8 -*-
from Types import DataType
from CalcRating import CalcRating
from typing import Dict, List

RatingType = dict[str, float]


class ThirdQ:

    def __init__(self, data: DataType) -> None:
        self.data = data

    def ratings(self) -> RatingType:
        return CalcRating(self.data).calc()

    def _percentile(self, values: List[float], p: float) -> float:
        if not values:
            raise ValueError("Empty values")
        values_sorted = sorted(values)
        n = len(values_sorted)
        # линейная интерполяция: индекс = (n-1) * p
        idx = (n - 1) * p
        low = int(idx // 1)
        high = min(low + 1, n - 1)
        frac = idx - low
        return values_sorted[low] + frac * (values_sorted[high]
                                            - values_sorted[low])

    def threshold(self) -> List[float]:
        vals = list(self.ratings().values())
        return self._percentile(vals, 0.5), self._percentile(vals, 0.75)

    def thirdq_students(self) -> Dict[str, float]:
        r = self.ratings()
        thr = self.threshold()
        return {k: v for k, v in r.items() if (v >= thr[0] and v < thr[1])}

    def print_3q(self) -> None:
        ts = self.thirdq_students()
        if not ts:
            print("No students in the third quartile")
            return
        print("Third quartile students:")
        for name, score in sorted(ts.items(), key=lambda x: x[1],
                                  reverse=True):
            print(f"{name}: {score:.4f}")
