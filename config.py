MAX_DECO_LVL = 3
ARMOR_PART_NAMES = ['helm', 'mail', 'braces', 'coil', 'greaves', 'charm']

UPTIMES = {
    'AGI': 0.7, 
    'MM': 0.8, 
    'CS': [0.3, 0.35, 0.45], 
    'LP': 0.5, 
    'LP_Rey_I': 150/(120+150), # activates for 150s
    'LP_Rey_II': 210/(120+210), # activates for 210s
    'Dosha': 0.8, 
    'Gore': 0.7, 
}

N_JOBS = -3
KEEP_TOP_N = 10
WEAPONS = [ # Meat: +2; Powercharm: +6; Demondrug: +7; Mega Demondrug: +10
    {
        'name': None, 
        'raw': 220 + 15, 
        'aff': 0.05, 
        'crit_bonus': 0.4, 
    }, 
]
MUST_HAVE_SKILLS = {
    'Earplugs': 2, 
}
