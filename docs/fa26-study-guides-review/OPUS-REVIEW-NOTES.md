# OPUS REVIEW NOTES — FA26 assessment study guides (2026-09-24)

## Model confirmation

This review was produced by **Claude Opus 5.5**, running as a Cursor Cloud Agent. It is a temporary academic study-guide review only. **No munchai_v0 product code was changed.** All output is under `docs/fa26-study-guides-review/` on a dedicated branch, and nothing is merged to `main`.

## Deliverables

| Guide | Markdown | PDF |
|-------|----------|-----|
| CSC 252 Test 2 | `md/CSC252-Test2-StudyGuide.md` | `pdf/CSC252-Test2-StudyGuide.pdf` |
| CSC 252 Test 3 | `md/CSC252-Test3-StudyGuide.md` | `pdf/CSC252-Test3-StudyGuide.pdf` |
| CSC 335 Midterm | `md/CSC335-Midterm-StudyGuide.md` | `pdf/CSC335-Midterm-StudyGuide.pdf` |
| CSC 337 Midterm 1 | `md/CSC337-Midterm1-StudyGuide.md` | `pdf/CSC337-Midterm1-StudyGuide.pdf` |
| CSC 345 Exam 1 | `md/CSC345-Exam1-StudyGuide.md` | `pdf/CSC345-Exam1-StudyGuide.pdf` |
| CSC 380 Quiz 04 | `md/CSC380-Quiz04-PracticeGuide.md` | `pdf/CSC380-Quiz04-PracticeGuide.pdf` |
| CSC 380 Midterm | `md/CSC380-Midterm-StudyGuide.md` | `pdf/CSC380-Midterm-StudyGuide.pdf` |

To regenerate the PDFs, run `python3 tools/build_pdfs.py`. It needs `pip install markdown` and Google Chrome.

## Context files used (read before editing)

| Role | File |
|------|------|
| Constraints, and confirmed vs provisional facts | `CONTEXT.md` |
| Date/scope ground truth | `announced-assessments-inventory-2026-09-24.md`, `site-audit-2026-09-24.md` |
| Week-by-week topics | `csc252-topic-map.md`, `csc335-topic-map.md`, `csc337-topic-map.md`, `csc345-topic-map.md`, `csc380-topic-map.md` |
| Live Gradescope format notes | `csc252-2026-09-24.md`, `csc337-2026-09-24.md`, `csc345-2026-09-24.md`, `csc380-2026-09-24.md`, `SUMMARY-2026-09-24.md`. CSC 335 has none. |
| Current guides reviewed | All 7 `guides-pdf/*.pdf` (text extracted and page layout checked) and all 7 `guides-md/*.md` |
| Earlier format-note batch (secondary) | Used only for syllabus facts it quoted: Sim projects forbid AI; 380 quizzes are 1.5% each; 345 exams are in person. |

## Honesty banners — final state

| Guide | Date status | Scope status | Notes |
|-------|-------------|--------------|-------|
| 252 Test 2 | **Confirmed** Thu Oct 1 (25 min, in lecture; clock time NV) | **PROVISIONAL** (Decks 01–04) | Deck 05 is noted as linked that week but not claimed |
| 252 Test 3 | **Confirmed** Thu Oct 15 (25 min; clock time NV) | **PROVISIONAL / TBD**, light | Decks 05–07 preview is explicitly **not** scope and is gated on lecture |
| 335 Midterm | Scheduled Thu Oct 8 (clock time TBD) | **PROVISIONAL** (weeks 1–6) | No Gradescope; P3 remains **NV** |
| 337 Midterm 1 | **Confirmed** Tue Oct 6 (75 min) | **PROVISIONAL** (weeks 1–7) | "Closed-book" changed to **verify** |
| 345 Exam 1 | Scheduled Thu Oct 8 (clock time NV) | **PROVISIONAL** (Topics 1–3) | Topic 4 excluded |
| 380 Quiz 04 | **Due NV** — never invented | **PUBLISHED SCOPE** (Bayes, LOTP, independence; slides 43–68) | The Tuesday cadence is explicitly not treated as a due date |
| 380 Midterm | **Date NV** (tentative Oct 20, 5:00–6:15 PM) | **PROVISIONAL** (weeks 1–8), light | Re-verify during Oct 13–19 before densifying |

## Cross-cutting changes (all 7 guides)

1. **Time zone.** Every "PT" label became **Arizona time (MST)**. CONTEXT says America/Phoenix, and UA is in Arizona. The inventory and topic maps label times "PT", but Arizona clock time equals Pacific *daylight* time only until **Nov 1, 2026**. After that, the December finals would be off by an hour if read as Pacific. Please confirm the meta files meant Arizona local time.
2. **PDF rendering fixes.**
   - LaTeX such as `\(2^8 - 1\)` printed literally, so it is replaced with Unicode.
   - The complement mark in `Hᶜ` printed as a missing-glyph box, so it is replaced with "not-H" plus a notation note.
   - Stray `>` lines under the banners are removed.
   - The build step now inserts the blank line Python-Markdown needs before lists; without it, lists flattened into paragraphs.
   - Answer keys still start on a new page, and every page carries a "Study aid only" footer.
3. **Self-contained answer keys.** Keys that only said "see the other guide" (252 Test 3, 380 Midterm) now have full worked answers.
4. **Practice recommendation labels are kept.** Every format inferred from past Gradescope work is labelled that way, with a note on where it came from. No future exam format is claimed.
5. **Numeric grades are described in words only.** The repository `begoneBOT/munchai_v0` is **public**, so exact scores and Gradescope submission URLs were left out of these copies. Actionable signals are kept (for example, "Test 1 short-concept question was the largest loss"). The private originals are unchanged.
6. **Every numeric answer re-derived.** All binary, hex, and probability answers were checked with a script.

## Per-guide changes

### CSC 252 Test 2

- Completed the full-adder truth table, which was missing four rows.
- Added explanations of binary subtraction (with the borrow/carry-out rule), unsigned vs signed overflow, "negative or not" (MSB rule), the approximation table, and why MIPS has no real `subi` (signed 16-bit immediate). Added a practice allowable-instruction list, labelled "check the real cover sheet".
- Practice now targets the live Test 1 and Sim 1 feedback themes: Question 1 short concepts, Binary Subtraction, C-to-MIPS, and 2's complement/SUB. New items: GS-A4–A7, GS-B4–B6, GS-C4–C5, GS-D4–D6, and a 25-minute timed paper mock. All have keys.
- Added nearby deadlines. The **Asm 2 5:00 PM (PDF) vs 7:00 PM (Gradescope)** conflict is flagged: prefer Gradescope, but finishing by 5:00 PM is safe.
- Noted that the Test 1 section scores listed in the format notes (0 + 15 + 10) do not sum to 38. One 25-point section is unnamed there, and no guess was made about it.

### CSC 252 Test 3

- **Fixed weekday errors.** The old plan said "Mon Oct 13" and "Tue Oct 14" and had a stray "Wed Oct 14? wait" row. In 2026, Oct 12 is Monday, Oct 13 Tuesday, and Oct 14 Wednesday.
- Replaced "see Test 2" keys with worked continuity problems and answers (P2–P6, L1–L3).
- Added HW3 (Tue Oct 13, 7:00 PM, labelled **rule-derived**) and Asm 3 (about Oct 14, labelled **approximate**).
- Added the optional §4c preview for the Deck 05–07 titles (ALU concept, `jal`/`jr`/register conventions, R/I/J formats). It uses standard MIPS conventions, is labelled **not scope**, is to be used only after lecture covers it, and gives **no Sim 3 hints** (Sim projects forbid AI help).

### CSC 335 Midterm (no Gradescope)

- **Filled the scope gap.** The banner said "syllabus weeks 1–6", but the guide covered only the week 1–3 decks. Added lambdas/anonymous classes, generics/frameworks, the Collections Framework with Iterator and Template Method, and JavaFX with Observer and Composite. Each is tagged **[Syllabus-only]**, since no deck was observed, and uses standard Java and Gang-of-Four definitions.
- Added a JUnit 4 vs JUnit 5 table. The deck uses `@Before`, so both styles are shown in the keys.
- Added generic written-exam practice (T1–T4 traces, W1–W3 code, S1–S4 short answer), explicitly labelled **not Gradescope-derived**. **No Gradescope format was invented.**
- Changed "closed-book" to **verify**. Flagged that the 335 midterm and the 345 exam may be **back-to-back in The Commons 305** (12:30 PM and 2:00 PM) if both are held in class; clock times are unverified.

### CSC 337 Midterm 1

- **Added "Get & Post"** (syllabus week 4), which was missing from the checklist.
- **Removed Assignment 4–specific solution material:** the working email validator for A4's exact rule, A4's validation list, and A4's filenames. A4 is open (due Sep 29, 3:30 PM) and individual-only. Drills are re-specified: ZIP validator, letter counts, a DOM "double" button, and guess-count reasoning.
- Added a timing caveat: DOM (week 6) is not yet lectured, and client/server (week 7) falls in the midterm week itself.
- Changed "closed-book" to **verify**. Rebuilt specificity as tuples. Added JavaScript traps and DOM safety material, a 45-minute mock, and keys.
- Fixed "all eight IDs" (there were ten; there are now eleven).

### CSC 345 Exam 1

- **Filled Topic 1–3 gaps** from the site audit and topic map: orthogonal lists and array storage (row-/column-major formulas), recursion, step-counting vs profiling, Ω/Θ, Dijkstra, and MCST/topological sort (marked "only as far as lectured").
- Added proof practice matching the Homework 1 rubric habit: a four-part O-proof, a "not O(n)" proof, an induction proof, and the handshake lemma. Added traces for the Master Theorem ×3, step count, BFS/DFS with distances, Dijkstra, stack/queue, and Kruskal/topological sort. Hand traces only; **no PP2 code**.
- Restored "best 5 quizzes count, no make-ups", citing the **syllabus** rather than Gradescope.
- Fixed the ambiguous "Fri Sep 25 / Oct 2" plan row.

### CSC 380 Quiz 04

- Kept the **PUBLISHED SCOPE** and **due-NV** banners. No due date was added.
- Added four one-page, 1.5-point mock quizzes (three parts at 0.5 points each) matching the Quiz 01 structure (one rubric question, one page), plus a filled Bayes table and a stretch sequential-update item. All have keys.
- Added syllabus quiz policy and the HW3 **two-item** (written + Code) reminder.

### CSC 380 Midterm

- Kept the **date NV** and **LIGHT** banners.
- Made the key self-contained. Added the week-3 **Combinations** topic, which had been merged into independence with no practice. Added ten short items on random variables, the binomial distribution, covariance/correlation, visualization, and pandas.
- Noted that the weeks 6–8 lectures have not happened yet.

## Not done / limits

- No Gradescope or D2L pages were opened. No attempts were started and nothing was submitted.
- On-box slide decks (`/workspace/csc252_slides/...` and similar) are **not** in this environment. Explanations rely on the topic maps, the site audit, the current guides, and standard textbook conventions, and each is labelled where the notation should be confirmed against the slides.
- No study material is based on other students' information.

## Open questions for Arshia

1. Were the "PT" times in the inventory and topic maps really Arizona local time? (See cross-cutting change 1.)
2. For CSC 337 and CSC 335, is the midterm closed-book, and how is it delivered (paper or Gradescope)?
3. Once instructors publish the Test 2/3, Midterm, and Exam 1 scopes or the Quiz 04 due date, the banners should be updated and the provisional sections trimmed.
