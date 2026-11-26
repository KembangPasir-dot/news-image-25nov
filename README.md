# news-image-25nov

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/KembangPasir-dot/news-image-25nov/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/KembangPasir-dot/news-image-25nov/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up the world's news of Wednesday 25 November 2026 — "The World in One Day", rebuilt for readability: one dominant hero story (the U.S. tariff salvo on 14 trading partners), four big key numbers, and eleven compact numbered secondary stories grouped by region — plus a market bar chart under the hero and an enlarged dotted world map with numbered pins matching the stories, and a date-check line. Clean vector graphics only, no generated scene illustrations. Entry for the make.fun bounty [news-image-20261125](https://make.fun/bounty/news-image-20261125) ($100, top 50).

This is a rebuild (resubmit) of the earlier entry in this repo (live claim AF-5THHK-47V1C-YBQ5N-2V27H, rank #1,743/11,246). The first version packed 35 stories into one page; this version cuts to the 12 most important, with a clear hierarchy so the page reads at a glance — including on a phone screen. Entries close 27 Nov 2026 08:00 WITA.

## Stories

- **Hero — Washington, USA:** U.S. proposes new tariffs on 14 trading partners (USTR, after an 8-month Section 301 probe; China up to 20%, Vietnam up to 35%; hearing Jan 25).
- **Key numbers:** 14 partners in tariff salvo · KOSPI −6.1% · 9,500 LB lead azide · 31 killed in Cairo.
- **Secondary (11, numbered to match the map pins):** Army blows up 9,500 lb of lead azide in Iowa; tankers hit mines in Hormuz (IRGC claim); Houthis claim Ras Tanura hit; Gaza strike kills Hamas chief Abuelouf; Poland plans no-fly zone; chess Gukesh–Sindarov draw (1–1); Shenzhou-24 docks at Tiangong; Asia markets slide; Bangladesh wage up 36%; RSF drones kill 19 in Sudan; Cairo fuel-truck fire kills 31.
- **Markets — 25 Nov closes:** KOSPI −6.1%, Taiex −4.9%, Nikkei −2.8%, Nasdaq −0.6%, S&P 500 −0.3%, Dow +0.3%; gold +0.5% to $3,609, Bitcoin $58,734 (UTC close).

Every story happened or was first reported on Wednesday 25 November 2026; sources are tagged on the page (AP, Reuters, Chess.com, NordFX, Finnhub, Egypt Health Ministry) with CONFIRMED / REPORTED / CLAIM status. Revision 2 re-verified every number against the original wires: the Iowa headline now uses the exact source figure (9,500 LB, not the rounded "5 TONS"); Nasdaq/S&P/Dow/gold now show the verified Wednesday closes (Tuesday's closes were printed before); the Huawei verdict (Tue 24 Nov) was removed; the Cairo toll was updated 30 → 31.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` when the variable is unset), then verifies the copy by size and SHA-256. Running it twice from different working directories produces byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=kqb6jwx1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
