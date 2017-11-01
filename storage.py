import os
import tempfile
import argparse
import json

def storage():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    print storage_path
    with open(storage_path, 'r+b') as f:
        try:
            data = json.load(f)
        except ValueError:
            data = {}
        print data
        parser = argparse.ArgumentParser()
        parser.add_argument("--key")
        parser.add_argument("--value")
        args = parser.parse_args()
        if not args.value:
            val = data.get(args.key)
            print ', '.join(val)
            return
        if args.key in data:
            val = data[args.key]
            val.append(args.value)
        else:
            data[args.key] = [args.value]
        print data
        f.seek(0)
        f.truncate() 
        e = json.dump(data, f)
        return

storage()
