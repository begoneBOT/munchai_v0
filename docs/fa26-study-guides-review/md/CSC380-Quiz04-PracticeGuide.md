# CSC 380 — Quiz 04 Practice Guide

**Banner — PUBLISHED SCOPE; due date NEEDS VERIFICATION.**
- **Scope is published** (D2L announcement, Sep 18, 2026): Bayes' rule, the law of total probability (LOTP), and independence, covering **slides pp. 43–68**.
- **The due date is not verified.** Quiz 04 was not on Gradescope as of the 2026-09-24 audit (~14:03 Arizona time). The syllabus cadence ("quizzes every Tuesday unless noted") is **not** a verified due date. **Never invent a due date.** This is an open practice guide, not a countdown plan.

Canonical maps: `csc380-topic-map.md` · `announced-assessments-inventory-2026-09-24.md`

## 1. Header

| Field | Value | Status |
|-------|-------|--------|
| Course | CSC 380 Principles of Data Science (FA26), TuTh 5:00–6:15 PM, M Pacheco ILC 130 | Confirmed |
| Assessment | Quiz 04 (practice guide) | Item announced |
| Due date/time | **Needs verification** — do not invent | **NV** |
| Coverage | Bayes' rule; LOTP; independence; slides 43–68 | **PUBLISHED SCOPE** |
| Quiz policy (syllabus) | 12 quizzes, each 1.5% of the grade; the two lowest are dropped; no make-ups | Confirmed (syllabus) |
| Past quiz format | Quiz 01 was **one** graded rubric question on a **one-page** submission, worth 1.5 points | Practice recommendation (Gradescope notes) |
| Guide updated | 2026-09-24 (America/Phoenix) — Opus review pass | |

All times are **Arizona time (MST)**.

**Related but separate:** HW3 (Probability 2) is due **Tue Sep 29, 11:59 PM**. It has **two** Gradescope items, HW03 (written) and HW03 Code, and both must be submitted. It overlaps these topics, but HW3 is **not** this guide's target, and nothing here solves it.

**Notation.** In this guide, **not-A** means the complement of A (often written Aᶜ or Ā on slides). P(A | B) is read "probability of A given B."

---

## 2. Topic checklist (learning order)

| Order | Section ID | Topic | Blind ✓ | Check ✓ | Retake ✓ |
|------:|------------|-------|:-------:|:-------:|:--------:|
| 1 | `380-Q04-refresh` | Conditional probability refresher | | | |
| 2 | `380-Q04-lotp` | Law of total probability | | | |
| 3 | `380-Q04-bayes` | Bayes' rule | | | |
| 4 | `380-Q04-indep` | Independence (vs. mutually exclusive) | | | |
| 5 | `380-Q04-slides` | Work the examples on slides 43–68 | | | |

Alias: `380-L-prob3` ≈ `380-Q04-bayes`, for calendar continuity.

---

## 3. Plain explanations + worked examples

### Conditional probability refresher (`380-Q04-refresh`)

P(A | B) = P(A and B) / P(B), when P(B) > 0.

Rearranged, this gives the **multiplication rule**: P(A and B) = P(A | B)·P(B).

The Gradescope scores show the week-2 quiz (conditional probability) was the weakest of the three, so this refresher comes first.

### Law of total probability (`380-Q04-lotp`)

If B₁, …, Bₖ **partition** the sample space (they don't overlap and together cover everything):

P(A) = Σᵢ P(A | Bᵢ)·P(Bᵢ)

With two parts: P(A) = P(A | B)·P(B) + P(A | not-B)·P(not-B).

The intuition: split the world into cases, find A's probability in each case, and weight each case by how likely it is.

### Bayes' rule (`380-Q04-bayes`)

P(Bⱼ | A) = P(A | Bⱼ)·P(Bⱼ) / P(A), where P(A) comes from LOTP.

**Table method** (it makes normalizing automatic):

| Hypothesis | Prior | Likelihood P(data given H) | Prior × likelihood | Posterior |
|------------|-------|----------------------------|--------------------|-----------|
| … | … | … | … | (row value) ÷ (column sum) |

**Worked example (disease test).** P(D) = 0.01, P(+ | D) = 0.9, and P(+ | not-D) = 0.05.
- P(+) = 0.9·0.01 + 0.05·0.99 = 0.009 + 0.0495 = 0.0585.
- P(D | +) = 0.009 / 0.0585 ≈ **0.154**.

The disease is rare (a low **base rate**), so most positive results are false positives, even though the test is fairly accurate.

### Independence (`380-Q04-indep`)

A and B are independent when **P(A and B) = P(A)·P(B)**. Equivalently, P(A | B) = P(A) (when P(B) > 0), or P(B | A) = P(B).

- **Coin example.** For two fair flips, P(H₁ and H₂) = 1/4 = (1/2)(1/2), so the flips are independent.
- **Mutually exclusive is not independent.** If P(A) > 0 and P(B) > 0 but they cannot both happen, then P(A and B) = 0 ≠ P(A)·P(B). Knowing A happened tells you B did not, which is maximal dependence.
- To **check** independence, compute both sides of the product rule. Don't rely on intuition.

---

## 4. Practice questions (core)

**Recall**
- R1. Write Bayes' rule for hypotheses H and not-H, given data D.
- R2. State independence in three equivalent ways.

**Solve**
- S1. Three urns are equally likely: U1 has 2 red and 1 blue, U2 has 1 red and 1 blue, U3 has 0 red and 2 blue. You pick an urn at random and draw one ball, which is red. What is P(U1 | red)?
- S2. P(A) = 0.3, P(B) = 0.4, P(A and B) = 0.12. Are A and B independent?
- S3. P(A | B) = 0.5, P(B) = 0.2, P(A | not-B) = 0.1. Find P(A) and P(B | A).

**Trace**
- T1. For S1, fill in the Bayes table: prior, likelihood, prior × likelihood, posterior.

**Explain**
- E1. Why does LOTP appear in the denominator of Bayes' rule?
- E2. What is the difference between independent and mutually exclusive?

**Code (optional study aid)**
- C1. Simulate about 10,000 draws of the S1 setup in Python. Compare the fraction of red draws that came from U1 with the exact answer.

---

## 4b. One-page mock quizzes (1.5 points each) — **Practice recommendation**

**Where this format comes from.** Quiz 01's Gradescope result was one rubric question on a one-page submission, worth 1.5 points. Each mock below is **one multi-part problem that fits on one page**, with three parts worth 0.5 points each. The Quiz 04 interface and due date are **not known**. Give each mock **10 minutes**, closed-notes.

### Mock Quiz A — LOTP + Bayes (factory)

Machine M1 makes 60% of the items, and 2% of its items are defective. Machine M2 makes the other 40%, and 5% of its items are defective.
- (a) [0.5] Find P(defective).
- (b) [0.5] An item is defective. Find P(M2 | defective).
- (c) [0.5] In one sentence, explain why (b) is larger than 0.4.

### Mock Quiz B — Independence (dice)

Roll two fair six-sided dice. Let A = "the first die shows 6", B = "the sum is 7", and C = "the sum is 12".
- (a) [0.5] Are A and B independent? Show the product check.
- (b) [0.5] Are A and C independent? Show the product check.
- (c) [0.5] P(E) = 0.2, P(F) = 0.5, and E and F are mutually exclusive. Are they independent?

### Mock Quiz C — Table → conditional → independence

Of 200 students, 80 drink coffee. 50 of the coffee drinkers are night owls, and 40 of the non-coffee drinkers are night owls.
- (a) [0.5] Find P(night owl).
- (b) [0.5] Find P(coffee | night owl).
- (c) [0.5] Are "coffee" and "night owl" independent? Justify with numbers.

### Mock Quiz D — Bayes (spam filter)

P(spam) = 0.3. The word "free" appears in 40% of spam emails and in 5% of non-spam emails.
- (a) [0.5] Find P("free").
- (b) [0.5] Find P(spam | "free").
- (c) [0.5] Explain in one sentence the mistake in saying "P(spam | free) = 0.4".

### Quick checks

- **Qμ1.** P(A) = 0.5, P(B) = 0.4, P(A and B) = 0.1. Independent? Give a one-line reason.
- **Qμ2.** Write LOTP for an event D with the partition {B, not-B}.
- **Qμ3.** P(H) = 0.2, P(E | H) = 0.9, P(E | not-H) = 0.3. Find P(H | E), showing the LOTP denominator.
- **Qμ4.** True or false: mutually exclusive events with positive probabilities are independent.
- **Qμ5 (stretch).** Using the disease test from §3, a second, independent test is also positive. Assume the two results are independent given disease status. Find P(D | both positive).

<!-- PAGEBREAK -->

## 5. ANSWER KEY (separate — check after a blind attempt)

### Core keys

**R1.** P(H | D) = P(D | H)·P(H) / [P(D | H)·P(H) + P(D | not-H)·P(not-H)]

**R2.** P(A and B) = P(A)·P(B); P(A | B) = P(A); P(B | A) = P(B). The last two require the conditioning event to have positive probability.

**S1.** P(red) = (2/3)(1/3) + (1/2)(1/3) + 0 = 2/9 + 1/6 = 7/18. So P(U1 | red) = (2/9) / (7/18) = **4/7**.

**S2.** 0.3 × 0.4 = 0.12, which equals P(A and B). **Yes, independent.**

**S3.** P(A) = 0.5·0.2 + 0.1·0.8 = **0.18**. P(B | A) = 0.10 / 0.18 = **5/9**.

**T1.**

| Urn | Prior | Likelihood | Prior × likelihood | Posterior |
|-----|-------|------------|--------------------|-----------|
| U1 | 1/3 | 2/3 | 2/9 = 4/18 | 4/7 |
| U2 | 1/3 | 1/2 | 1/6 = 3/18 | 3/7 |
| U3 | 1/3 | 0 | 0 | 0 |
| Sum | 1 | | 7/18 | 1 |

**E1.** The denominator is P(data), the total probability of the data across all hypotheses. LOTP computes exactly that, and dividing by it makes the posteriors sum to 1.

**E2.** Mutually exclusive means P(A and B) = 0. Independent means P(A and B) = P(A)·P(B), which is usually greater than 0. With positive probabilities, the two properties cannot both hold.

**C1.** The empirical fraction should land near 4/7 ≈ 0.571, within about ±0.02 for 10,000 draws.

### Mock quiz keys

**Quiz A.**
- (a) 0.6·0.02 + 0.4·0.05 = 0.012 + 0.020 = **0.032**.
- (b) 0.020 / 0.032 = **0.625**.
- (c) M2 has the higher defect rate, so seeing a defect shifts belief toward M2, from the prior of 0.4 up to 0.625.

**Quiz B.**
- (a) P(A) = 1/6. P(B) = 6/36 = 1/6. P(A and B) = P(first die 6, second die 1) = 1/36, and (1/6)(1/6) = 1/36. **Independent.**
- (b) P(C) = 1/36. P(A and C) = 1/36, but P(A)·P(C) = 1/216. **Not independent.**
- (c) P(E and F) = 0, but P(E)·P(F) = 0.1. **Not independent.**

**Quiz C.**
- (a) (50 + 40) / 200 = **0.45**.
- (b) 50 / 90 = **5/9 ≈ 0.556**.
- (c) P(owl | coffee) = 50/80 = 0.625, which is not P(owl) = 0.45. Equivalently, P(coffee and owl) = 0.25, but P(coffee)·P(owl) = 0.4·0.45 = 0.18. **Not independent.**

**Quiz D.**
- (a) 0.4·0.3 + 0.05·0.7 = 0.12 + 0.035 = **0.155**.
- (b) 0.12 / 0.155 ≈ **0.774**.
- (c) 0.4 is P(free | spam), the likelihood. Treating it as P(spam | free), the posterior, ignores the prior and the base rate.

**Quick-check keys**
- **Qμ1.** No. 0.5·0.4 = 0.2 ≠ 0.1.
- **Qμ2.** P(D) = P(D | B)·P(B) + P(D | not-B)·P(not-B).
- **Qμ3.** P(E) = 0.9·0.2 + 0.3·0.8 = 0.42. P(H | E) = 0.18 / 0.42 = **3/7 ≈ 0.429**.
- **Qμ4.** False. Their intersection has probability 0, but the product of their probabilities is greater than 0.
- **Qμ5.** 0.81·0.01 / (0.81·0.01 + 0.0025·0.99) = 0.0081 / 0.010575 ≈ **0.766**. Equivalently, use 0.154 as the new prior and update once more.

---

## 6. Common mistakes + readiness checklist

- Confusing P(A | B) with P(B | A) (base-rate neglect).
- Forgetting to normalize, i.e. skipping the LOTP denominator.
- Treating mutually exclusive events as independent.
- Using a "partition" whose parts overlap or leave gaps.
- **Inventing a Quiz 04 due date** from the Tuesday cadence.

**Ready if:**
- [ ] Mock Quizzes A–D are each done in 10 minutes or less with at least 1.0 of 1.5 points
- [ ] Three independence checks are done by computing both sides
- [ ] The examples on slides 43–68 are worked
- [ ] **No countdown cram** until the due date is verified

---

## 7. Open practice checklist (no due-date cram plan)

| Mode | Action |
|------|--------|
| Anytime | Rotate short sets for `380-Q04-refresh`, `lotp`, `bayes`, and `indep` |
| Alongside HW3 (due Sep 29, 11:59 PM) | Work these topics as separate practice. Upload **both** HW03 and HW03 Code. |
| When the due date is posted on Gradescope or D2L | Add a light review 24–48 hours before. **Do not invent the date now.** |
| Tuesdays and Thursdays | Keep light around classes. Do deep drills Mon/Wed/Fri and weekends. |

---

## 8. Changes in this review (2026-09-24)

- Kept the **PUBLISHED SCOPE** and **due-date NV** banners unchanged in meaning.
- Replaced the complement symbol "ᶜ" with "not-A", because it rendered as a missing-glyph box in the old PDF. Added a notation note.
- Added quiz policy facts from the syllabus (12 quizzes, drop the 2 lowest, no make-ups) and the HW3 two-item submission reminder.
- Added Mock Quizzes A–D (one page, three parts at 0.5 points each), a filled Bayes table (T1), and a stretch sequential-update item. All have keys.
- Stated the weak-early-quiz signal in words only, with no scores, because the repository is public.
- Changed times to Arizona time.

## 9. Study-aid / AI-policy disclaimer

Study aid only — not for submitted work (Quiz 04, HW, exams). Follow CSC 380 and UA academic-integrity and AI policies.
