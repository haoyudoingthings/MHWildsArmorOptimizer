# MHWildsArmorOptimizer

MHWilds armor optimizer with effective attack power as the target function

## Usage

Run `python main.py` and wait for results

This optimizer is currently made with optimization for greatswords in mind, therefore you will see stuff like Burst only providing 5 atk. You can change the effects in `data.py`

## TODO

- Refactor configs into another file
- Unit test?
- Keep cache
  - Use the hash of config as signature
- Allow more complicated skill effects
  - Flayer
- Improve efficiency of armor search
