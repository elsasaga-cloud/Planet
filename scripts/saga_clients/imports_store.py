"""Tiny helper: append/replace per-household ImportYeti findings.
Usage (python):  from imports_store import put;  put('SA-021', name=..., found=True, ...)
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
P = os.path.join(ROOT, 'data', 'saga_clients', 'imports', 'importyeti_us_2026-10-27.json')

def load():
    return json.load(open(P, encoding='utf-8'))

def save(D):
    json.dump(D, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def put(code, **kw):
    D = load()
    kw.setdefault('fetched', '2026-10-27')
    D['rows'][code] = kw
    save(D)
    return len(D['rows'])
