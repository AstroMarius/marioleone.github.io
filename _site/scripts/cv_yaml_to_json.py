#!/usr/bin/env python3
"""Semplice convertitore YAML->JSON Resume per il sito al-folio fork.
Legge _data/cv.yml e scrive assets/json/resume.json
"""
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
YAML_IN = ROOT / "_data" / "cv.yml"
JSON_OUT_DIR = ROOT / "assets" / "json"
JSON_OUT = JSON_OUT_DIR / "resume.json"


def convert():
    data = yaml.safe_load(YAML_IN.read_text())
    resume = {}
    # basics
    basics = data.get('basics', {})
    resume['basics'] = {
        'name': basics.get('name', 'Name'),
        'label': basics.get('label', ''),
        'email': basics.get('email', ''),
        'url': basics.get('url', ''),
        'summary': basics.get('summary', '')
    }
    # work
    resume['work'] = []
    for w in data.get('work', []):
        resume['work'].append({
            'name': w.get('company'),
            'position': w.get('position'),
            'startDate': w.get('startDate'),
            'endDate': w.get('endDate', ''),
            'summary': "\n".join(w.get('summary', [])) if w.get('summary') else ''
        })
    # education
    resume['education'] = []
    for e in data.get('education', []):
        resume['education'].append({
            'institution': e.get('institution'),
            'area': e.get('area'),
            'studyType': e.get('studyType'),
            'startDate': e.get('startDate'),
            'endDate': e.get('endDate')
        })
    # languages
    resume['languages'] = []
    for l in data.get('languages', []):
        resume['languages'].append({'language': l.get('language'), 'fluency': l.get('fluency')})
    # skills
    resume['skills'] = []
    for s in data.get('skills', []):
        resume['skills'].append({'name': s.get('name'), 'keywords': s.get('keywords', [])})

    JSON_OUT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(resume, indent=2, ensure_ascii=False))
    print(f"Wrote {JSON_OUT}")


if __name__ == '__main__':
    convert()
