# -*- coding: utf-8 -*-
import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        res_json = json.dumps(result)
        return res_json
    return wrapper

#@to_json
#def get_data():
#    return None

#print(get_data()) #вернёт '{"data": 42}'
