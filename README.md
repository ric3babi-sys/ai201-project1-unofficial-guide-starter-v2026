# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size: 550**
**Overlap: 180**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->
I choose 550 for CHUNK_SIZE to balance large vs medium sizes.
For CHUNK_OVERLAP, I estimate overlapping relavent info is about a sentence long.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->
======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
## Getting around the region with limited mobility
An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

======================================================================
Chunk 2  |  source: guide_corry_vale.md#4  |  produced by: chunker.py::split_documents
======================================================================
## Where to stay
Perhaps thirty beds in the entire valley, spread across two pubs and a handful of farmhouse rooms. In summer these are booked months ahead. Camping is permitted on two marked fields and nowhere else.

======================================================================
Chunk 3  |  source: guide_givens_mill.md#1  |  produced by: chunker.py::split_documents
======================================================================
## Getting there
No station and no bus on Sundays; four buses a day from Brightwater on weekdays, taking 30 minutes. Driving is 20minutes. The village car park holds about forty cars and is full by 11am on summer Saturdays.

## Getting around
Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directi

======================================================================
Chunk 4  |  source: guide_kestrelford.md#5  |  produced by: chunker.py::split_documents
======================================================================
## When to go
Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cutoff for a day or two most winters.

======================================================================
Chunk 5  |  source: guide_regional_transport.md#2  |  produced by: chunker.py::split_documents
======================================================================
## Buses
Three operators run in the region and they do not accept each other's tickets,
which is the single most common source of confusion for visitors. Services
concentrate on weekday daytimes. Sunday service is minimal to non-existent
outside the Brightwater town routes.

The Kestrelford service is hourly on weekdays, two-hourly on Saturdays, and
does not run on Sundays. The Halden Bay coast service runs four times daily
year-round.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?

**Chunk 1** — source: guide_accessibility.md Post #0 `` — produced by: chunker.py::split_documents``

```
```

**Chunk 2** — source: guide_corry_vale.md Post #4 `` — produced by: chunker.py::split_documents``

```
```

**Chunk 3** — source: guide_givens_mill.md Post #1 `` — produced by: chunker.py::split_documents``

```
```

**Chunk 4** — source: guide_kestrelford.md Post #5 `` — produced by: chunker.py::split_documents``

```
```

**Chunk 5** — source: guide_regional_transport.md Post #2 `` — produced by: chunker.py::split_documents``

```
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
Is public transporation available in the city?

**Answer:**
(.venv) codepath@Ubuntu-dev:~/Documents/codepath/AI201/week1-2/ai201-project1-unofficial-guide-starter-v2026$ python app.py retrieve "Is public transporation available in the city?" --top-k 8

Question: Is public transporation available in the city?

#   distance   source                           preview
----------------------------------------------------------------------------------------------------
1   0.8968     guide_thornby_wells.md           ## Where to stay Two large hotels from the spa perio...
2   0.9034     guide_accessibility.md           ## Difficult **Kestrelford** is built on a slope and...
3   0.9125     guide_marchwood.md               ## Getting there Every railway line in the region me...
4   0.9188     guide_givens_mill.md             ## Getting there No station and no bus on Sundays; f...
5   0.9250     guide_pellew_sands.md            ## When to go June and September for the beach witho...
6   0.9254     guide_givens_mill.md             ## When to go The mill runs March to November and is...
7   0.9281     guide_regional_transport.md      ## Driving Roads are good between the towns and poor...
8   0.9300     guide_marchwood.md               ## What to see The city museum is free and genuinely...

Gate: best distance 0.897 is over the 0.6 cutoff — refusing

Lower is better. 0.3 is a close match, 0.9 is unrelated.
Milestone 4: run your five questions, then the five in OUT_OF_SCOPE
that your documents clearly don't cover, and look for the gap
between the two groups. Your cutoff goes in that gap.
```
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->
My questions all failed. Not even close.


| Question                                                    | In corpus? | Best distance |
|-------------------------------------------------------------|------------|---------------|
| What is the waiting time at Commons during lunch?           | NO         | 0.9126        |
| Where is the cheapest place to buy groceries in town?       | NO         | 0.9489        |
| What season has the best weather in the city?               | NO         | 0.9289        |
| Where is the most scenic spot in the city?                  | NO         | 0.9101        |
| where is the best hiking trail in the city?                 | NO         | 0.9020        |
| What is the capital of Mongolia?                            | NO         | 0.8581        |
| How do I change the oil in a diesel engine?                 | NO         | 0.9992        |
| Who won the 1994 World Cup?                                 | NO         | 0.8604        |
| What is the recommended dosage of ibuprofen for a headache? | NO         | 0.9776        |
| How do I write a for loop in Rust?                          | NO         | 0.9055        |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked AI to implement split_documents and take into account relevant details in next post. It missed the case when current post is the last. This was found in a unit test and corrected.

**2.**
Had to tweak CHUNK_OVERLAP to get a reasonable size for a single complete sentence.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
