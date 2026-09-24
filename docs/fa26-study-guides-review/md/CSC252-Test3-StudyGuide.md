# CSC 252 — Test 3 Study Guide (spaced / light)

**Banner — scope PROVISIONAL / LIGHT.** Test 3 scope is **not published**. The **date is confirmed**: Thu Oct 15, 2026, during lecture, 25 minutes. The syllabus lectures just before Test 3 are Deck 05 (The ALU), Deck 06 (MIPS Functions), and Deck 07 (Instruction Formats and CPU Details). The course site does **not** assign those decks to any test, so this guide does **not** claim them as scope. Until coverage is published, this guide keeps Decks 01–04 skills warm and offers an **optional, clearly labelled preview** (§4c) to use only after lecture covers those topics.

Canonical maps: `csc252-topic-map.md` · `announced-assessments-inventory-2026-09-24.md` · `site-audit-2026-09-24.md`

## 1. Header

| Field | Value | Status |
|-------|-------|--------|
| Course | CSC 252 Computer Organization (FA26), TuTh 9:30–10:45 AM | Confirmed |
| Assessment | Test 3 | Confirmed |
| Date | **Thu Oct 15, 2026** | **Confirmed** (homepage) |
| Length / when | 25 minutes during lecture; exact clock time **not published** | Length confirmed; clock time NV |
| Coverage | not published | **PROVISIONAL** |
| Guide updated | 2026-09-24 (America/Phoenix) — Opus review pass | |

All times are **Arizona time (MST)**.

### Nearby deadlines (energy planning only)

| Item | When (Arizona) | Status |
|------|----------------|--------|
| Sim 3 ("An ALU") | Wed Oct 7, 7:00 PM | Homepage + Gradescope |
| HW3 | Tue Oct 13, 7:00 PM | **Rule-derived** from "due two days before each test". Not individually posted yet. |
| Asm 3 | about Wed Oct 14, 7:00 PM | Syllabus says "on or about" — approximate |

---

## 2. Topic checklist (light / TBD-aware)

| Order | Section ID | Topic | Status |
|------:|------------|-------|--------|
| 1 | `252-T3-tbd` | Official Test 3 topics | **TBD.** Watch the homepage, `tests/` folder, and lecture announcements. |
| 2 | `252-T3-cont-binary` | Continuation: binary, 2's complement, add/subtract | Keep warm. **Not** claimed as Test 3 scope. |
| 3 | `252-T3-cont-mips` | Continuation: MIPS loops and arrays | Keep warm. **Not** claimed as scope. |
| 4 | `252-T3-cont-gates` | Continuation: gates and adders | Keep warm. **Not** claimed as scope. |
| 5 | `252-T3-preview` | Optional preview of Decks 05–07 (§4c) | **Use only after lecture covers it.** Not claimed as scope. |

When scope is published, replace row 1 and regenerate this guide.

---

## 3. Explanations (light)

**Keep this short.** Until coverage is published:

- Do a 15-minute flash on Test 2 skills each week, so they stay warm for Sim 3 and later tests.
- After each lecture from Oct 1 on, write down 2–3 topic bullets and label each **"unverified until slides/homepage confirm."**
- Use the official deck titles, not guesses about what might be tested.

**How the preview works.** The deck titles near Test 3 are public. §4c turns them into self-check prompts based on **standard MIPS conventions** (Patterson & Hennessy). Match notation to the actual slides, and skip anything not yet lectured.

**Sim 3 boundary.** Sim 3 ("An ALU") prohibits AI help. §4c covers ALU **concepts only**. It contains no Sim 3 code, structure, or hints.

---

## 4. Practice — continuity set (self-contained)

**P1 (meta).** What is confirmed about Test 3 today, and what is not?

**P2 (binary add).** Add 8-bit `0100 1011` + `0110 0110`. Give the result, whether there is unsigned overflow, and whether there is signed overflow.

**P3 (2's complement).** Negate `0001 1100` in 8-bit 2's complement. Then sign-extend the result to 16 bits, in hex.

**P4 (subtraction).** Compute `0x50 − 0x68` in 8 bits using "invert, add 1, add". Give the signed result and say whether a borrow happened.

**P5 (MIPS loop).** Write a loop that sums the word array at `$s0` with length `$s1` into `$s2`, using only allowable-style instructions.

**P6 (gates).** Write Cout of a full adder as a sum of products, and say how many full adders a 32-bit ripple-carry adder needs.

**P7 (planning).** After Oct 1, list three lecture topics that might feed Test 3. Label each **unverified**.

## 4b. Light Gradescope-format continuity — **Practice recommendation**

This is inferred from the Test 1 result structure only: a scanned, hand-written paper of about 6 pages, with short-concept, binary-arithmetic, and C-to-MIPS questions. It is **not** a published Test 3 format.

**GS-T3-L1.** Round-trip unsigned 8-bit `0xD4` to binary, then to decimal, then back to hex. Show work as on a test page.

**GS-T3-L2.** In one line each: is `0xD4` negative as 8-bit 2's complement? What is its signed value?

**GS-T3-L3.** Write 3–5 MIPS lines that clear `$t0`, load word 2 of the array at `$s0` into `$t1`, and add it to `$t0`.

## 4c. OPTIONAL preview — Decks 05–07 (**not** claimed scope)

**Only use these after the matching lecture has happened.** Answers use standard MIPS and Patterson & Hennessy conventions. If the slides use different notation, follow the slides.

**PV1 (Deck 05, ALU concept).** A 1-bit ALU slice computes AND, OR, and add, then picks one result. Which circuit element selects the result, and what drives its select lines?

**PV2 (Deck 05, ALU concept).** How can an adder-based ALU compute A − B without a separate subtractor circuit?

**PV3 (Deck 06, functions).** Which instruction calls a function, and where does it save the return address? Which instruction returns?

**PV4 (Deck 06, functions).** Which registers must a function preserve if it modifies them (callee-saved), and which may it overwrite freely (caller-saved)? Why does a function that calls another function need to save `$ra`?

**PV5 (Deck 07, formats).** Give the field layout and bit widths of the R-format, I-format, and J-format instructions.

<!-- PAGEBREAK -->

## 5. ANSWER KEY

**A1.** Confirmed: Thu Oct 15, 2026, a 25-minute test during lecture. Not confirmed: scope and the exact clock time.

**A2.** `0100 1011` (75) + `0110 0110` (102) = `1011 0001` (177).
- No carry out, so **no unsigned overflow**.
- Both inputs are positive but the result's MSB is 1, so there **is signed overflow**. The true sum, 177, exceeds 127.

**A3.** `0001 1100` = 28. Inverted: `1110 0011`. Plus 1: `1110 0100` = −28 (0xE4). Sign-extended to 16 bits: `0xFFE4`.

**A4.** −`0x68`: `0110 1000` inverted is `1001 0111`, plus 1 is `1001 1000` (0x98). Then `0x50 + 0x98 = 0xE8` = `1110 1000`. As a signed value that is 232 − 256 = **−24** (check: 80 − 104 = −24). The carry-out is 0, so **a borrow happened**.

**A5.**

```
      add  $s2, $zero, $zero
      add  $t0, $zero, $zero
LOOP: beq  $t0, $s1, DONE
      sll  $t1, $t0, 2
      add  $t1, $s0, $t1
      lw   $t2, 0($t1)
      add  $s2, $s2, $t2
      addi $t0, $t0, 1
      j    LOOP
DONE:
```

**A6.** Cout = A·B + A·Cin + B·Cin. A 32-bit ripple-carry adder needs 32 full adders. Bit 0 can be a half adder if there is no carry-in, but using a full adder there enables subtraction by setting Cin = 1.

**A7.** Your own list, with every item labelled unverified.

**GS-T3-L1.** `0xD4` = `1101 0100` = 128 + 64 + 16 + 4 = 212, which is back to `0xD4`.

**GS-T3-L2.** Yes, it is negative (MSB 1). 212 − 256 = **−44**.

**GS-T3-L3.**

```
add  $t0, $zero, $zero     # t0 = 0
lw   $t1, 8($s0)           # word index 2 -> byte offset 8
add  $t0, $t0, $t1
```

### Preview keys (confirm against slides)

**PV1.** A multiplexer (MUX) selects the result. The operation / control bits drive its select lines.

**PV2.** Invert B (XOR each bit with 1, or use a "B-invert" MUX) and set the carry-in to 1. That computes A + (~B) + 1 = A − B, which is 2's complement again.

**PV3.** `jal label` jumps to the function and saves the return address (PC + 4) in `$ra`. `jr $ra` returns.

**PV4.** Callee-saved: `$s0–$s7` (plus `$sp`, and `$ra` in practice). Caller-saved: `$t0–$t9`, `$a0–$a3`, `$v0–$v1`. A function that makes a call runs `jal`, which overwrites `$ra`, so it must push `$ra` on the stack first and restore it before `jr $ra`.

**PV5.** Each format totals 32 bits.

| Format | Fields (bit widths) |
|--------|---------------------|
| R-format | op (6), rs (5), rt (5), rd (5), shamt (5), funct (6) |
| I-format | op (6), rs (5), rt (5), immediate (16) |
| J-format | op (6), address (26) |

---

## 6. Common mistakes + readiness

- Treating Test 2 topics, or the §4c preview, as confirmed Test 3 scope.
- Studying Deck 05–07 material before it has been lectured, or instead of Sim 3.
- Mixing up unsigned overflow (carry-out) with signed overflow (sign flip).
- Skipping sleep the night before Oct 15.

**Readiness (spaced):** 2–3 short sessions per week after Oct 8. Expand once scope is published or decks have been lectured.

---

## 7. Day-by-day (spaced; no day-before cram)

Weekdays checked against the 2026 calendar.

| Day | Plan |
|-----|------|
| Fri Oct 2 – Wed Oct 7 | Almost nothing for Test 3. Finish Sim 3 (due Wed Oct 7, 7:00 PM). Optional 15-minute continuity flash. |
| Thu Oct 8 – Sat Oct 10 | Light: add lecture notes to `252-T3-tbd`; one short MIPS or binary flash. |
| Sun Oct 11 | Short mixed continuity set, plus §4c for any lectured decks. |
| Mon Oct 12 | Structured review of **known, lectured** material only. Deep-ish day. |
| Tue Oct 13 | **LIGHT** only — class day; HW3 due 7:00 PM (rule-derived). |
| Wed Oct 14 | Calm recall — **no cram**. Asm 3 due about 7:00 PM (approximate). |
| Thu Oct 15 morning | Buffer, then Test 3 in lecture. |

---

## 8. Changes in this review (2026-09-24)

- Fixed the day plan's weekday errors. The old plan said "Mon Oct 13" and "Tue Oct 14" and had a stray "Wed Oct 14? wait" row; in 2026, Oct 12 is Monday, Oct 13 Tuesday, and Oct 14 Wednesday.
- Made the answer keys self-contained. The old keys said "see the Test 2 guide"; A2–A4 and L1–L3 now have full worked answers.
- Added the 25-minute length, clock-time-NV status, and nearby deadlines. HW3 is labelled **rule-derived**, and Asm 3 is labelled **approximate**.
- Added the optional §4c preview for Decks 05–07. It uses standard MIPS conventions, is explicitly **not** claimed as scope, is gated on lecture coverage, and gives no Sim 3 hints.
- Changed times to Arizona time.

## 9. Disclaimer

Study aid only — not for submitted work. Follow CSC 252 and UA academic-integrity and AI policies. Coverage is **provisional/TBD** until the instructor publishes it.
