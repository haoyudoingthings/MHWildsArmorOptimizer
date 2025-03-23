# MHWildsArmorOptimizer

MHWilds armor optimizer with effective attack power as the target function

## Usage

Run `python main.py` and wait for results

This optimizer is currently made with optimization for greatswords in mind, therefore you will see stuff like Burst only providing 5 atk. You can change the effects in `data.py`

## TODO

1. Refactor configs into another file
2. Take uptime into account properly for cases like capped out affinity
3. Add interactions between skills (e.g. Fulgur Anjanath's Will increases the uptime of Maximum Might)
4. Allow more complicated skill effects (e.g. Gore Magala's Tyranny)
5. Improve efficiency of armor search
