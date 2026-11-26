# news-image-25nov

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/KembangPasir-dot/news-image-25nov/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/KembangPasir-dot/news-image-25nov/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up the world's news of Wednesday 25 November 2026 — "The World in One Day", rebuilt for readability: one dominant hero story (the US Army's controlled detonation of 5 tons of lead azide in Iowa), four big key numbers, and twelve compact secondary stories grouped by region — plus a dotted world map, a simple market bar chart, and a date-check line. Clean vector graphics only, no generated scene illustrations. Entry for the make.fun bounty [news-image-20261125](https://make.fun/bounty/news-image-20261125) ($100, top 50).

This is a rebuild (resubmit) of the earlier entry in this repo (live claim AF-5THHK-47V1C-YBQ5N-2V27H, rank #1,743/11,246). The first version packed 35 stories into one page; this version cuts to the 13 most important, with a clear hierarchy so the page reads at a glance — including on a phone screen. Entries close 27 Nov 2026 08:00 WITA.

## Stories

- **Hero — Iowa, USA:** Army blows up 5 tons of lead azide (68 drums, Iowa Army Ammunition Plant, 9:00 AM CST); EPA monitors found no lead in the air.
- **Key numbers:** 5 TONS lead azide · KOSPI −6.1% · Bitcoin $59,258 · 30 killed in Cairo.
- **Secondary (12):** US tariffs on 14 partners; Huawei convicted; tankers hit mines in Hormuz; Houthis strike Saudi refinery; Gaza strike kills Hamas chief; Poland plans no-fly zone; chess Gukesh–Sindarov draw (1–1); Shenzhou-24 docks at Tiangong; Asia markets slide; Bangladesh wage up 36%; RSF drones kill 19 in Sudan; Cairo fuel-truck fire kills 30.
- **Markets — 25 Nov:** KOSPI −6.1%, Taiex −4.9%, Nikkei −2.8%, Nasdaq −1.5%, S&P 500 −0.5%; Dow +0.9%, gold −2.2% to $3,556.

Every story was first reported on Wednesday 25 November 2026; sources are tagged on the page (AP, Reuters, BBC, Chess.com, NordFX) with CONFIRMED / REPORTED / CLAIM status.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` when the variable is unset), then verifies the copy by size and SHA-256. Running it twice from different working directories produces byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=kqb6jwx1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
