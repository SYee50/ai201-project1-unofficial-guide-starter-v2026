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

The Unofficial Guide uses the campus_life corpus, which contains information about different parts of student life, including courses, housing, dining, transportation, orientation, winter gear, and campus policies. Users can ask questions about information covered in these documents, such as course workloads, housing, laundry, study rooms, academic deadlines, or getting around campus. The system finds relevant information from the corpus and uses it to generate a short answer while identifying the document the answer came from. If the corpus does not have enough information to answer a question, the system says it does not have enough information instead of guessing.

## Chunking Strategy

**Chunk size:** 600 characters maximum, with each document kept as a single chunk when it fits.

**Overlap:** 0 characters.

I chose a 600 character maximum because the campus_life documents are already short. The documents average about 317 characters, and the longest document is 549 characters, so a 600 character limit allows every document in the corpus to remain intact as a single chunk. I initially tested a smaller 300 character chunk size. This produced 133 chunks instead of 88 and sometimes split sentences in the middle. For example, one chunk ended with "seating is tight; about 40 seats f". I also noticed that some posts contain related information that depends on the context earlier in the same document, such as a location followed by details about that location. Splitting these posts could separate information from the context needed to understand it. Because the documents are short and self-contained, I decided that keeping each document as one chunk would preserve the most useful context for retrieval. I used 0 overlap because there is no need to repeat content when each document is already contained in a single chunk.

## Sample Chunks

**Chunk 1** — source: admin_add_drop_deadline.txt#0 `` — produced by: chunker.py::split_documents``

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: course_biol_160.txt#0 `` — produced by: chunker.py::split_documents``

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: course_hist_118_workload.txt#0 `` — produced by: chunker.py::split_documents``

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: dining_pellew_dining_hall_followup.txt#0  `` — produced by: chunker.py::split_documents``

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: housing_innisfree_hall.txt#0 `` — produced by: chunker.py::split_document``

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

**Question:**
When is the latest a student can add a course?

**Answer:**

```
A student can add a course through the end of the second week 
(admin_add_drop_deadline.txt).
```

**My relevance cutoff:** 0.6

I kept the relevance cutoff at 0.6 because it is above all of the observed in-corpus distances (0.3277-0.4343), giving relevant questions some leeway, while remaining well below the out of scope distances (0.8246-0.9340).

| Question | In corpus? | Best distance |
|---|---|---|
|When is the latest a student can add a course?|Yes|0.4343|
|Where is a quiet location on campus?|Yes|0.4009|
|When is the best time to do laundry?|Yes|0.4270|
|How far in advance do students need to book study rooms?|Yes|0.3277|
|What is the maximum amount of hours students can work on campus each week during term?|Yes|0.3840|
|What is the capital of Mongolia?|No|0.8246|
|How do I change the oil in a diesel engine?|No|0.9340|
|Who won the 1994 World Cup?|No|0.8859|
|What is the recommended dosage of ibuprofen for a headache?|No|0.8442|
|How do I write a for loop in Rust?|No|0.8960|
|  |  |  |



## How I Used AI

**1.** I asked ChatGPT to write the chunking function based on my idea that the documents should stay together because they were short and mostly self contained. It wrote the split_documents function to keep each document as one chunk. I then asked it to try smaller chunk sizes so I could compare the results. I tested 300 character chunks and found that they created more chunks and sometimes split sentences in the middle, so I decided to keep the document sized chunks with a 600 character maximum.

**2.** I asked ChatGPT to help me understand the retrieval distances. I gave it the results from five in-scope and five out-of-scope questions, and it helped me compare the distance ranges. I decided to keep the cutoff at 0.6 because all of the in-scope questions were below it, while the out-of-scope questions were much farther away.


---

# Unit 2

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
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Retrieved chunk is 100-600 characters| 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Response within 60 seconds| 4 of 5 | 5 of 5 | 5 of 5 | 4 of 5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Real output

### When is the latest a student can add a course? — run 1

- Response time: 4.96 seconds
- Best distance: 0.4343 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_graduation_requirements.txt, admin_pass_fail_option.txt, course_biol_160_workload.txt, course_cs_340.txt

```
A student can add a course through the end of the second week (admin_add_drop_deadline.txt).
```

### Where is a quiet location on campus? — run 1

- Response time: 12.23 seconds
- Best distance: 0.4009 (passed the gate)
- Sources retrieved: housing_aldridge_hall_noise.txt, housing_calder_annexe_noise.txt, housing_innisfree_hall_noise.txt, housing_old_brewhouse_noise.txt, housing_tamsin_court_noise.txt

```
If you need quiet to work, the library is open until 2am during term (found in `housing_tamsin_court_noise.txt`, `housing_aldridge_hall_noise.txt`, `housing_old_brewhouse_noise.txt`, `housing_calder_annexe_noise.txt`, and `housing_innisfree_hall_noise.txt`). Additionally, floors 3 and 4 of Aldridge Hall are genuinely enforced quiet floors (`housing_aldridge_hall_noise.txt`).
```

### When is the best time to do laundry? — run 1

- Response time: 14.84 seconds
- Best distance: 0.4270 (passed the gate)
- Sources retrieved: housing_aldridge_hall_laundry.txt, housing_fenwick_court_laundry.txt, housing_morrow_house_laundry.txt, housing_old_brewhouse_laundry.txt, housing_tamsin_court_laundry.txt

```
The best time to do laundry is Tuesday or Wednesday morning. 

Sources: 
- housing_tamsin_court_laundry.txt
- housing_old_brewhouse_laundry.txt
- housing_aldridge_hall_laundry.txt
- housing_morrow_house_laundry.txt
- housing_fenwick_court_laundry.txt
```

### How far in advance do students need to book study rooms? — run 1

- Response time: 13.38 seconds
- Best distance: 0.3277 (passed the gate)
- Sources retrieved: advising_registration.txt, course_cs_340.txt, dining_north_kitchen_followup.txt, money_textbooks.txt, study_group_rooms.txt

```
Students need to book study rooms two weeks in advance. 

Source: study_group_rooms.txt
```

### What is the maximum amount of hours students can work on campus each week during term? — run 1

- Response time: 17.03 seconds
- Best distance: 0.3840 (passed the gate)
- Sources retrieved: course_cs_210_workload.txt, course_cs_340.txt, course_econ_101_workload.txt, course_stat_150_workload.txt, money_jobs.txt

```
The maximum amount of hours students can work on campus during term is 20 hours a week (source: money_jobs.txt).
```

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the asnwer | MET | Each of the answers came with a source that contained the answer. In the chunker, each document is one chunk. |
| 2 | Every answer names a source | MET | Each of the answers came with at least one source file name. |
| 3 | Gate stops out-of-corpus questions | MET | The results showed that all 5 out-of-corpus questions were refused as the curoff was set to 0.6 and the distances for the out-of-corpus questions ranged from 0.825-0.934. |
| 4 | Retrieved chunk is 100-600 characters | MET | In the campus_life corpus, the shortest chunk is 178 and the longest is 549, which all fall between 100 to 600. |
| 5 | Response within 60 seconds | MET | All questions, except for one, had a response time below 60 seconds. The response time range for 14 out of 15 qustions was 4.96 seconds to 41.85 seconds. There was one question that had a response time of 571.78 seconds, but the target for this criteria was still met for that run because the other 4 response times were below 60 seconds. |

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
