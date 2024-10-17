#!/usr/bin/env python3

import json
import os
from datetime import datetime, timedelta

with open('schedule.json', 'r') as file:
    data = json.load(file)

days = data['schedule']['conference']['days']

def render_notes(path, n, start, end, title, abstract, speaker_names, speaker_bios):
    filenname = f"{path}/speaker-notes-{n}.md"
    with open(filenname, 'w') as file:
        content = f"""\
---
documentclass: extarticle
fontsize: 20pt
---

# {speaker_names} — {title}

{start.strftime('%H:%M')} - {end.strftime('%H:%M')}

\\newpage

## Biography

{speaker_bios.replace('\r', '')}

## Abstract

{abstract.replace('\r', '')}
"""
        file.write(content)

def handle_day(path, day):
    talks = day['rooms']['Aula 4.101']
    for n, talk in enumerate(talks):
        title = talk['title']
        if title == 'Welcome' or title == 'Closing' or title.startswith('Lightning Talks'):
            continue
        start = datetime.fromisoformat(talk['date'])
        [hours, minutes] = talk['duration'].split(':')
        duration_delta = timedelta(hours=int(hours), minutes=int(minutes))
        end = start + duration_delta
        abstract = talk['abstract']
        speaker_names = 'and '.join([p['public_name'] for p in talk['persons']])
        speaker_bios = '\n\n'.join([str(p['biography']) for p in talk['persons']])
        render_notes(path, n, start, end, title, abstract, speaker_names, speaker_bios)

for n,day in enumerate(days, start=1):
    path = f"day-{n}"
    os.makedirs(path, exist_ok=True)
    handle_day(path, day)
