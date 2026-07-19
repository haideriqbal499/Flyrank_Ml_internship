# Prompt ladder — Week 2 (ML track)

**Task:** start weak, add one layer per version, compare outputs, keep notes honest.  
**Domain:** FlyRank Lane 2 — content refresh / opportunity scoring on the anonymized starter dataset.  
**Runs:** 6 total (baseline + 5). Each version names exactly one layer.

---

## Baseline (v0) — weak prompt

### Prompt
```
Explain this data.
```

### Output (representative excerpt)
> Sure! Data is information collected for analysis. In SEO and content marketing, data often includes metrics like traffic, clicks, impressions, and rankings. To explain “this data,” I’d look at trends over time, compare pages, and find insights that help you grow organic visibility. If you share a screenshot or file, I can go deeper. Here are some general tips: clean your data, check for outliers, visualize distributions, and remember correlation isn’t causation…

### Four notes
| | |
|---|---|
| **What changed in the prompt** | Nothing — this is the lazy starting point. |
| **What improved in the output** | N/A (baseline). |
| **What still failed** | It never touched my file. It taught “what is data,” invented a marketing lecture, and asked me to re-upload what I already had open. |
| **What to try next** | **Clearer goal** — ask for a decision, not a lecture. |

---

## Version 1 — layer: clearer goal

### Prompt
```
Tell me which pages need a content refresh.
```

### Output (representative excerpt)
> Pages that usually need a content refresh are ones with declining traffic, outdated publish dates, thin content, or dropping keyword rankings. Look for:
> 1. Traffic down 20%+ month over month  
> 2. Content older than 12 months  
> 3. High bounce / low time on page  
> 4. Lost featured snippets  
> Refresh by updating stats, adding FAQs, improving internal links, and republishing. Tools like Google Search Console and Analytics can help you find candidates.

### Four notes
| | |
|---|---|
| **What changed in the prompt** | Named the decision: which pages to refresh (not “explain data”). |
| **What improved in the output** | It stopped defining “data.” It aimed at a refresh triage instead of a glossary. |
| **What still failed** | Still generic textbook rules. No use of my 30k-row starter set. Invented thresholds (20%, 12 months) I never stated. |
| **What to try next** | **Defined audience** — stop teaching Search Console 101. |

---

## Version 2 — layer: defined audience

### Prompt
```
Tell me which pages need a content refresh.
Write for an SEO / content editor who already knows Search Console, CTR, impressions, and position. Do not explain those terms.
```

### Output (representative excerpt)
> Prioritize URLs where demand is still there but the page is slipping: solid impressions with softening clicks or position, aging content on competitive queries, and pages that used to win page-one but are leaking to page two. Deprioritize low-impression URLs even if the trend looks ugly — they rarely repay editor time. Build a weekly batch from the high-impression losers first, then spot-check CTR gaps on otherwise stable positions.

### Four notes
| | |
|---|---|
| **What changed in the prompt** | Locked the reader: working SEO/content editor; banned term lectures. |
| **What improved in the output** | It stopped explaining impressions/CTR. Tone got sharper and more “batch this week.” |
| **What still failed** | Still no numbers from *my* snapshot. Could be any agency blog post. |
| **What to try next** | **Real context** — paste the actual starter facts. |

---

## Version 3 — layer: real context

### Prompt
```
Tell me which pages need a content refresh.
Write for an SEO / content editor who already knows Search Console, CTR, impressions, and position. Do not explain those terms.

Context from my FlyRank internship starter dataset (anonymized):
- 30,000 content rows
- ~54% labeled declining on the snapshot proxy
- Lane 2 goal: ranked review queue (refresh / expand / protect / prune / monitor), not “predict Google”
- Editors only open the top of the list; precision@K matters more than a pretty ROC curve
- I must not claim a refresh will recover traffic from observational data alone
```

### Output (representative excerpt)
> With ~54% declining in a 30k inventory, “flag everything down” is useless — the queue has to rank. Put editor time on high-demand pages that are also declining; treat low-impression declines as monitor/prune candidates, not this week’s refresh heroes. Ship a ranked list with a suggested action and a short why. Score the list with precision@K against your review-proxy (and later against an observed next-window label). Keep claims directional: the model prioritizes review, it does not promise traffic recovery.

### Four notes
| | |
|---|---|
| **What changed in the prompt** | Added real internship facts and the honesty constraint. |
| **What improved in the output** | It used my 30k / ~54% / precision@K framing. It named the false-positive cost of flagging everything. It respected the “no causal recovery claim” line. |
| **What still failed** | Still a paragraph of advice. No concrete top-of-queue shape an editor could paste into a ticket. |
| **What to try next** | **Examples of what good looks like** — show one good queue row. |

---

## Version 4 — layer: examples of what good looks like

### Prompt
```
Tell me which pages need a content refresh.
Write for an SEO / content editor who already knows Search Console, CTR, impressions, and position. Do not explain those terms.

Context from my FlyRank internship starter dataset (anonymized):
- 30,000 content rows
- ~54% labeled declining on the snapshot proxy
- Lane 2 goal: ranked review queue (refresh / expand / protect / prune / monitor), not “predict Google”
- Editors only open the top of the list; precision@K matters more than a pretty ROC curve
- I must not claim a refresh will recover traffic from observational data alone

Example of a good queue row (illustrative only):
rank 1 | content_demo_01 | score 82 | action refresh_and_review_ctr | reasons: declining_with_demand, low_ctr_visible_page | impressions_90d 12800 | trend down
```

### Output (representative excerpt)
> Here is your top refresh queue:  
> 1. content_demo_01 — score 82 — refresh_and_review_ctr — declining_with_demand, low_ctr_visible_page — 12,800 impressions — down  
> 2. content_demo_02 — score 81 — refresh_and_review_ctr — declining_with_demand, low_ctr_visible_page — 9,400 impressions — down  
> 3. content_demo_03 — score 80 — refresh — declining_with_demand — 7,100 impressions — down  
> …  
> These demo-style IDs mirror the pattern in your example. Refresh the CTR laggards first, then expand thin winners. Expected lift: stronger engagement within two sprint cycles.

### Four notes
| | |
|---|---|
| **What changed in the prompt** | Added one illustrative “good row” example. |
| **What improved in the output** | Structure looked more like a queue (rank / action / reasons). |
| **What still failed** | **This made it worse.** It cloned `content_demo_*` IDs, invented a full leaderboard, and slipped a causal “expected lift” claim I had banned. The example became a costume for hallucination instead of a format hint. |
| **What to try next** | **Specified output format** — demand a template without fake IDs; forbid inventing content_ids. |

---

## Version 5 — layer: specified output format

### Prompt
```
Tell me which pages need a content refresh.
Write for an SEO / content editor who already knows Search Console, CTR, impressions, and position. Do not explain those terms.

Context from my FlyRank internship starter dataset (anonymized):
- 30,000 content rows
- ~54% labeled declining on the snapshot proxy
- Lane 2 goal: ranked review queue (refresh / expand / protect / prune / monitor), not “predict Google”
- Editors only open the top of the list; precision@K matters more than a pretty ROC curve
- I must not claim a refresh will recover traffic from observational data alone

Output format (strict):
1) Five bullets: how to build the top-of-queue rule from the signals above (no invented page IDs).
2) A markdown table with columns: Priority band | Suggested action | Why it earns editor time | What would falsify this.
3) One short “limits” line: what this does not prove.
4) If you lack row-level data, say so and give the query/filter logic instead of fake IDs.
```

### Output (representative excerpt)
> **How to build the top of the queue**  
> - Keep rows with meaningful demand (e.g. impressions_90d ≥ 500); park the long tail.  
> - Rank declining high-demand pages above declining low-demand pages.  
> - Prefer visible / page-one soft slides when impressions are still large.  
> - Attach an action from {refresh, expand, protect, prune, monitor} plus short reason codes.  
> - Judge the list with precision@K on a held-out slice — not vibe.  
>
> | Priority band | Suggested action | Why it earns editor time | What would falsify this |
> |---|---|---|---|
> | High | refresh_and_review_ctr | High demand + down trend + weak CTR vs peers | CTR already fine after manual check; decline is seasonality |
> | High | refresh | High demand + down trend, content aged | Newer competing URL already covers the intent |
> | Medium | monitor | Decline but low absolute demand | Suddenly spikes impressions next window |
> | Low | prune / merge | Chronic low demand + thin engagement | Page is required for non-search reasons |
>
> **Limits:** This prioritizes *review*. It does not prove a refresh will recover traffic, and without the row file attached I cannot name real `content_id`s.

### Four notes
| | |
|---|---|
| **What changed in the prompt** | Locked the shape of the answer; banned fake IDs; required a falsification column and a limits line. |
| **What improved in the output** | Stopped inventing `content_demo_*` rows. Gave actionable filter logic + a table an editor can argue with. Kept the honesty line without burying the decision. |
| **What still failed** | Still not a live scored queue from `refresh_queue.csv` — that needs the file or a notebook cell, not chat alone. |
| **What to try next** | (Optional later) **Verification requirements** — “cite only columns that exist in the data dictionary.” |

---

## Side-by-side (what each layer bought)

| Version | Layer added | Output verdict |
|---|---|---|
| v0 | — | Embarrassing glossary |
| v1 | Clearer goal | Aimed at refresh, still generic rules |
| v2 | Defined audience | Dropped SEO 101 padding |
| v3 | Real context | Used my numbers and Lane 2 honesty |
| v4 | Examples of good | **Worse** — hallucinated demo IDs + causal lift |
| v5 | Specified output format | Recovered: logic + table, no fake pages |

---

## Final reusable prompt (stranger-ready)

Copy-paste for anyone on the ML / Search Intelligence track working a content-refresh ranking lane:

```
You are helping an SEO/content editor prioritize which pages to review for refresh.

Audience: they already know Search Console metrics (impressions, clicks, CTR, average position). Do not define those terms.

Goal: produce decision support for a ranked review queue with suggested actions from {refresh, expand, protect, prune, monitor}. This is not “predict Google’s algorithm,” and you must not claim a refresh will recover traffic from observational data alone.

Context I will paste next:
- dataset size and any declining / demand rates I measured
- unit of analysis (usually one page / content_id)
- success metric (usually precision@K for the top of the queue)
- any columns I am allowed to use (never treat snapshot trend labels as model features if I say they are labels)

If I do not paste row-level data, do not invent content_ids or scores. Give filter/ranking logic instead.

Output (strict):
1) Five bullets: how to build the top-of-queue from the signals I provided.
2) A markdown table: Priority band | Suggested action | Why it earns editor time | What would falsify this.
3) One “limits” line: what this does not prove.
4) Three questions you still need answered before you could score a real queue.
```

**How to use:** paste the block, then paste your measured context (row counts, rates, metric, column list). Swap the action set if your lane differs.

---

## Self-check

- [x] Six runs (v0–v5)
- [x] Each version = exactly one named layer
- [x] Notes talk about **output** changes, not only prompt edits
- [x] Honest failure: v4 examples made hallucination worse
- [x] Final prompt usable by a stranger on the track
