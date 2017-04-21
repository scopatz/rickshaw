"""Main entry point for rickshaw"""
try:
    from pprintpp import pprint
except ImportError:
    from pprint import pprint
import os
import json
from argparse import ArgumentParser

from rickshaw import generate


def main(args=None):
    p = ArgumentParser('rickshaw')
    p.add_argument('-n', dest='n', type=int, help='number of files to generate',
                   default=None)
    p.add_argument('-i', dest='i', type=str, help='name of input file', default=None)
    ns = p.parse_args(args=args)
    
    if ns.i is not None:
        try:
            print(ns.i)
            ext = os.path.splitext(ns.i)[1]
            if ext == '.json':
                with open(ns.i) as jf:
                    simspec = json.load(jf)
                    print(simspec) 
            elif ext == '.py':
                with open(ns.i) as pf:
                    simspec = json.load(pf)
                    print(simspec) 
        except:
            pass 
    
    if ns.n is not None:
        i = 0
        while i < ns.n:
            try:
                input_file = generate.generate()
            except Exception:
                continue
            jsonfile = str(i) + '.json'
            with open(jsonfile, 'w') as jf:
                json.dump(input_file, jf, indent=4)
            i += 1
    else:
        input_file = generate.generate()
        pprint(input_file)


if __name__ == '__main__':
    main()
