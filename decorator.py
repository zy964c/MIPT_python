# -*- coding: utf-8 -*-
import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        res_json = json.dumps(result)
        print res_json
    return wrapper

@to_json
def get_data():
  return {
    'data': 42
  }

get_data()  # вернёт '{"data": 42}'
