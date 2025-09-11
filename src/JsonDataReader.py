# -*- coding: utf-8 -*-
import json
from Types import DataType
from DataReader import DataReader


class JsonDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as f:
            obj = json.load(f)

        if not isinstance(obj, dict):
            raise ValueError("JSON root must be an object mapping names"
                             "to subject dicts")

        students: DataType = {}
        for name, subjects in obj.items():
            if not isinstance(subjects, dict):
                raise ValueError("Each student value must be an object"
                                 "mapping subject to score")
            students[name] = []
            for subj, score in subjects.items():
                students[name].append((str(subj), int(score)))
        return students
