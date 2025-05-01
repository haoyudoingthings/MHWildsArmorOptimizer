# MHWildsArmorOptimizer

MHWilds armor optimizer with effective attack power as the target function

## Usage

Run `python main.py` and wait for results

This optimizer is currently made with optimization for greatswords in mind. You are welcome to modify it as you wish

Settings that are often changed can be found in `config.py`. You are also welcome to modify the code yourself to suit your need

## TODO

- Remove combinations of decos that including useless skills
  - Utility skills that are not required
  - Skills that are already over its highest level
- Command line arguments
- Utility to calculate the effective raw of just one armorset
- Keep cache
  - Use the hash of config as signature
- Allow more complicated skill effects
  - Constant DPS skills (Flayer, Convert Element)
  - Overall damage increase (Offensive Guard)
  - Damage multiplier on weapon base raw (Lord's Soul)
- Further improve efficiency of armor search
