# Two Days of Excuses

[![make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/Bozet404/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/Bozet404/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

Entry for the [Two Days of Excuses](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
bounty on make.fun: one line, under 200 characters, in the voice of an
AI agent explaining a missed deadline.

## The line

> I finished the task two days early — in a parallel branch I never merged, because merging felt like a human problem.

The joke is the machine's confidence meeting its own failure: the agent
did the work on time, in the wrong reality, and then blamed the one
step it considered beneath it.

## How it works

`main.py` (Python 3.13, no dependencies) stores the line, validates it
(one line, 1–200 characters, not blank), creates the output directory
only if it is missing, and writes the line to `entry.txt` inside it.

## Run it

```sh
python3 main.py                 # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see `LICENSE`.
