# %%
import pandas as pd
import numpy as np
import random

# %%
NUM_YESNO = 60
NUM_SUBJECTIVE = 40

DEPRESSION = 'depression'
AGRESSION = 'agression'
RELATIONSHIP = 'relationship'
ANXIETY = 'anxiety'

ACTION, CATEGORY, ANSWER = 'action', 'category', 'answer'

# %%
def generate_action_types():
    action_types = []
    for _ in range(NUM_YESNO):
        action_types.append('yesno')
    for _ in range(NUM_SUBJECTIVE):
        action_types.append('subjective')
    return action_types

def generate_yesno_answers_int():
    yesno_answers = list(np.random.randint(0, 2, 60))
    return yesno_answers

def generate_yesno_answers_yn():
    return ['y' if ans == 1 else 'n' for ans in generate_yesno_answers_int()]

def generate_subjective_categories():
    categories = []
    for _ in range(NUM_SUBJECTIVE // 4):
        categories += [DEPRESSION, AGRESSION, RELATIONSHIP, ANXIETY]
    random.shuffle(categories)
    return categories

def generate_subjective_categories_with_number():
    categories = [
        '1-'+DEPRESSION,
        '2-'+AGRESSION,
        '3-'+RELATIONSHIP,
        '4-'+ANXIETY,
    ]
    categories *= 10
    random.shuffle(categories)
    return categories

def generate_subjective_answers():
    subjective_answers = list(np.random.randint(1, 8, 40))
    return subjective_answers

def generate_subjective_answers_with_prefix():
    return ['s'+str(ans) for ans in generate_subjective_answers()]

# %%
def generate_yesno_display_types():
    display_types = ['ly', 'ry']
    return [random.choice(display_types) for _ in range(NUM_YESNO)]

def generate_keyboard_leftrights():
    lr = ['l', 'r']
    return [random.choice(lr) for _ in range(NUM_YESNO)]

# %%

for id in range(20):
    df_yn = pd.DataFrame({
        ACTION: ['yesno'] * NUM_YESNO,
        CATEGORY: generate_yesno_display_types(),
        ANSWER: generate_keyboard_leftrights(),
    })

    df_subjective = pd.DataFrame({
        ACTION: ['subjective'] * NUM_SUBJECTIVE,
        CATEGORY: generate_subjective_categories(),
        ANSWER: generate_subjective_answers()
    })

    pd.concat([df_yn, df_subjective], ignore_index=True)\
        .to_csv('behavior_{}'.format(str(id).zfill(2)), index=None)

# %%
