# Tell a Whole Story in 32 Characters

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/Ngntier/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/rank.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/Ngntier/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/reward.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

An entry for the [make.fun](https://make.fun) competition
[Tell a Whole Story in 32 Characters](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978).

## What it does

`main.py` writes one Wi-Fi network name — at most 32 characters — to
`entry.txt` in the directory named by `MAKEFUN_OUTPUT_DIR`
(default `/output`). The name is a single deadpan joke that implies a
whole story: a situation, a character, and something that happened,
in the few words a phone shows in its network list.

## Run

```sh
python3 main.py
```

With a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program is deterministic: it writes the same bytes on every run,
reads nothing outside the repository, and uses no network access.
