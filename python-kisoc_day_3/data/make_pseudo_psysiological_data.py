# %%
import numpy as np
import pandas as pd

# %%
columns = [
    'CP6', 'F7', 'CP2', 'FT8', 'P1', 'PO8', 'P9', 'P4',
    'CPz', 'P6', 'FT7', 'AF8', 'Fp2', 'P2', 'CP5', 'Pz',
    'O1', 'FC5', 'F8', 'P5', 'Oz', 'FC3', 'P3', 'PO7',
    'F5', 'FC2', 'TP8', 'CP1', 'TP7', 'POz', 'CP3', 'T8',
    'Fp1', 'FC1', 'F10', 'F1', 'C3', 'T7', 'C1', 'C2',
    'C4', 'FC4', 'C6', 'C5', 'F2', 'F6', 'AF3', 'PO4',
    'P10', 'P8', 'P7', 'PO3', 'Fz', 'AF7', 'FCz', 'CP4',
    'F4', 'AF4', 'Cz', 'FC6', 'F9', 'F3', 'O2', 'AFz',
]

# %%
print([c for c in columns if 'z' in c])

# %%
len(columns)

# %%
for id in range(20):
    df = pd.DataFrame(np.random.random((250, len(columns))),
                      columns=columns,
                      index=range(-100, 400, 2))

    df.round(3).to_csv('psysiological_{}'.format(str(id).zfill(2)),
                       index_label='time')


# %%
print(columns)
