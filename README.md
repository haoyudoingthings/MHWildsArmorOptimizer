# MHWildsArmorOptimizer

MHWilds armor optimizer with effective attack power as the target function

## Usage

Run `python main.py` and wait for results

This optimizer is currently made with optimization for greatswords in mind; therefore you will see stuff like Burst only providing 5 atk

Settings that are often changed can be found in `config.py`. You are also welcome to modify the code yourself to suit your need

## TODO

- Unit test?
- Keep cache
  - Use the hash of config as signature
- Allow more complicated skill effects
  - Constant DPS skills (Flayer, Convert Element)
  - Overall damage increase (Offensive Guard)
- Further improve efficiency of armor search
