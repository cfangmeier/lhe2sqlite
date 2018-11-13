# lhe2sqlite
Simple utility to convert LesHouchesEvents files to a sqlite database

## Setup

To run, simply install the package

```sh
pip install lhe2sqlite [--user]
```

Then run with:

```sh
convertlhe2sqlite input.lhe output.sqlite3
```

Then you can examine the content with either stright SQL or your analysis tool of choice (eg pandas).

## Example Usage

Once the sqlite db has been created, one can plot simple kinematic distributions
using basic pandas. For example, to plot the pt distribution of top quarks in a sample.

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_sql_query(('select px, py, pz from particle '
                        'where abs(pdgid)==6 and abs(status)==1'),
                       'sqlite:///result.sqlite3')
df['pt'] = np.sqrt(df['px']**2 + df['py']**2)
df['pt'].hist()
plt.show()
```

## Schema

The resulting database has just 2 tables, `event`, and `particle` with a one-to-many relationship between them.

```sql
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
```

