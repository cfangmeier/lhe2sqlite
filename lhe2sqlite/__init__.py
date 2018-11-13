
from os.path import isfile
from os import remove
import xml.etree.ElementTree as ET
import gzip
import sqlite3

__all__ = [
    'convert'
]

__version__ = '0.1.0'

CONN = None


def init_tables():
    CONN.executescript('''
CREATE TABLE event (
    event_number INTEGER PRIMARY KEY,
    procId INTEGER,
    weight FLOAT,
    scale FLOAT,
    aqed FLOAT,
    aqcd FLOAT
);
CREATE TABLE particle (
    event_number INTEGER REFERENCES event(event_number),
    pdgId INTEGER,
    status INTEGER,
    mother1 INTEGER,
    mother2 INTEGER,
    color1 INTEGER,
    color2 INTEGER,
    px FLOAT,
    py FLOAT,
    pz FLOAT,
    e FLOAT,
    m FLOAT,
    lifetime FLOAT,
    spin FLOAT
);
''')


def convert(filename_in, filename_out):
    global CONN
    if not isfile(filename_in):
        raise FileNotFoundError('file ' + filename_in + 'does not exist')

    uncompressed = filename_in.endswith('.lhe')
    compressed = filename_in.endswith('.lhe.gz')
    if not uncompressed and not compressed:
        raise ValueError("Invalid input: " + filename_in)


    if filename_out is None:
        if filename_in.endswith('.lhe'):
            filename_out = filename_in[:-3] + 'sqlite3'
        else:  # '.lhe.gz'
            filename_out = filename_in[:-6] + 'sqlite3'
    if isfile(filename_out):
        remove(filename_out)

    CONN = sqlite3.connect(filename_out)
    init_tables()

    if compressed:
        lhe_open = gzip.open
    else:
        lhe_open = open

    with lhe_open(filename_in, 'r') as f:
        event_idx = 0
        for _, element in ET.iterparse(f, events=['end']):
            if element.tag != "event":
                continue
            data = element.text.split('\n')[1:-1]
            evnt_line, part_lines = data[0], data[1:]

            evnt_toks = evnt_line.split()
            items = [event_idx] + evnt_toks[1:]
            CONN.execute('''\
            INSERT INTO event VALUES (?,?,?,?,?,?) 
            ''', items)

            for part_line in part_lines:
                part_toks = part_line.split()
                items = [event_idx] + part_toks
                CONN.execute('''\
                INSERT INTO particle VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) 
                ''', items)

            # TODO: Look through children to fill in reweight info.
            # for child in element:
            #     print(child.tag)
            event_idx += 1
    CONN.commit()
