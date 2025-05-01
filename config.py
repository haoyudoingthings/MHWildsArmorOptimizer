MAX_DECO_LVL = 3
ARMOR_PART_NAMES = ['helm', 'mail', 'braces', 'coil', 'greaves', 'charm']

UPTIMES = {
    'AGI': 0.6, 
    'MM': 0.75, 
    'CS': [0.3, 0.35, 0.45], 
    'BR1': 0.4, 
    'BR2': 0.35, 
    'LP': 0.45, # calaulated assuming hunts last anywhere between 8 to 12 min
    'LP_Rey_I': 0.5, # activates for 150s
    'LP_Rey_II': 0.6, # activates for 210s
    'Dosha': 0.8, 
    'Gore': 0.7, 
}

N_JOBS = -3
KEEP_TOP_N = 10
WEAPONS = [ # Meal: +5; Powercharm: +6; Demondrug: +5; Mega Demondrug: +7; Demon Seed/Powder: +10
    {
        'name': None, 
        'raw': 220 + 16, 
        'aff': 0.05, 
        'crit_bonus': 0.4, 
    }, 
]
MUST_HAVE_SKILLS = {
    # 'Earplugs': 2, 
    "Zoh Shia's Pulse": 2, 
}
