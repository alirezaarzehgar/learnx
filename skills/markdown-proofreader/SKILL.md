---
name: markdown-proofreader
description: Find and fix typos, grammar mistakes, and clarity issues in markdown files. Use this skill when proofreading README.md, documentation, guides, or any markdown content. Returns only reproducible, objective errors—same results every time you run it.
---

# Markdown Proofreader

A deterministic proofreading skill that finds and fixes the same issues every time.

## What This Skill Does

Checks markdown files for **only these objective errors**:

### 1. Typos & Spelling (HIGH PRIORITY)
- Misspelled words (detected against common English dictionary)
- Character duplicates: `teh` → `the`, `recieve` → `receive`
- Common typos: `enviroment` → `environment`, `occured` → `occurred`

### 2. Grammar Rules (HIGH PRIORITY)
Apply **only these rules** (skip anything debatable):

| Rule | Check | Example |
|------|-------|---------|
| Subject-verb agreement | Singular subject + singular verb | `The project are` → `The project is` |
| Verb tense consistency | Match surrounding text tense | Mixed past/present in paragraph |
| Article usage | `a` vs `an` before vowels | `a apple` → `an apple` |
| Capitalization | Proper nouns, sentence start | `python` (language) should be capitalized if it's a name |
| Punctuation | Missing periods, double spaces | End of sentence, double spaces |
| Common confusion | their/there/they're, its/it's | Check only these specific pairs |

### 3. Clarity (MEDIUM PRIORITY - ONLY IF AMBIGUOUS)
- Dangling modifiers that create false meaning
- Pronoun reference ambiguity (unclear "it" or "this")
- Double negatives that confuse meaning

**DO NOT FLAG:**
- Style preferences (fragment sentences, informal tone, short paragraphs)
- Word choice alternatives (unless wrong word used)
- Sentence restructuring (unless grammatically required)

---

## Gotchas & Non-Negotiables

**Preserve intent at all costs:**
- If text is grammatically loose but intentional → Note as OPTIONAL
- If technical terms are unconventional but correct → Don't change
- If tone is conversational → Don't "professionalize"
- If short sentences are for emphasis → Don't combine

**Common false positives (DO NOT FLAG):**
- Capitalization inside code blocks (preserve as-is)
- Numbers at sentence start (e.g., "10 steps to...")
- Acronyms in ALL CAPS (API, HTTP, JSON)
- URLs and file paths (don't correct)
- Intentional fragments ("No. Wrong. Try again.")

---

## Output Format

**Return ONLY this exact JSON structure** (no preamble, no markdown fences):

```json
{
  "file": "README.md",
  "total_issues": 2,
  "errors": [
    {
      "line": 5,
      "type": "typo",
      "original": "enviroment",
      "suggestion": "environment",
      "reason": "Common misspelling",
      "preserve_voice": true
    },
    {
      "line": 12,
      "type": "grammar",
      "original": "The steps are simple",
      "suggestion": "No change needed",
      "reason": "Subject-verb agreement is correct",
      "preserve_voice": true
    }
  ],
  "status": "complete",
  "summary": "Found 1 typo (must fix), 1 grammar (verified correct)"
}
```

**Issue types only:** `typo` | `grammar` | `clarity` | `punctuation`

**Always include:**
- Line number (exact)
- Original text (exact quote)
- Suggestion (fix or "No change needed")
- Reason (brief, specific)
- `preserve_voice: true` (always)

---

## Determinism Rules (CRITICAL)

**To ensure same output every run:**

1. **Check the same rules each time** — Don't add rules based on "feeling"
2. **Use a fixed dictionary** — Only flag words not in standard English dictionary
3. **Verify before suggesting** — If you're unsure, mark as OPTIONAL or skip
4. **Don't rewrite** — Only fix objective errors, never rephrase
5. **Flag ambiguities** — If a sentence could be read two ways, ask for clarification

---

## Example Workflow

**Input (Your document):**
```markdown
# Setup Guide

This guideline explain how to setup your enviroment quickly.

Steps:
1. Install dependancies
2. Run the application
```

**Your skill output:**
```json
{
  "file": "README.md",
  "total_issues": 3,
  "errors": [
    {
      "line": 3,
      "type": "grammar",
      "original": "This guideline explain",
      "suggestion": "This guide explains",
      "reason": "Subject-verb agreement: singular 'guide' needs singular 'explains'",
      "preserve_voice": true
    },
    {
      "line": 3,
      "type": "typo",
      "original": "enviroment",
      "suggestion": "environment",
      "reason": "Common misspelling",
      "preserve_voice": true
    },
    {
      "line": 6,
      "type": "typo",
      "original": "dependancies",
      "suggestion": "dependencies",
      "reason": "Misspelling",
      "preserve_voice": true
    }
  ],
  "status": "complete",
  "summary": "Found 3 errors: 1 grammar (must fix), 2 typos (must fix)"
}
```

**Second run on corrected file:**
```json
{
  "file": "README.md",
  "total_issues": 0,
  "errors": [],
  "status": "complete",
  "summary": "No errors found. Document is clean."
}
```

✅ **Same file = same result (idempotent)**

---

## How to Use This Skill

### Step 1: Provide File Content
```
Use the markdown-proofreader skill on this file:

# README.md
[paste your markdown]
```

### Step 2: Review the JSON Report
- Read each issue
- Verify the line number matches
- Check if it's a real error

### Step 3: Apply or Skip
- **Fix it**: Update your file
- **Skip it**: If you intentionally wrote it that way

### Step 4: Run Again
- Paste the updated file
- Should return `"total_issues": 0`
- If not → There was a mistake in the fix

---

## Do NOT Use This Skill For

- ✗ Code syntax checking (use ESLint, pylint, etc.)
- ✗ Style or tone changes
- ✗ Restructuring sentences unnecessarily
- ✗ Rewriting for "better English"
- ✗ Link validation or technical review

---

## Multi-File Batch

To proofread multiple files:

```
Use the markdown-proofreader skill on:
1. README.md
2. roadmap/general.md
3. docs/setup.md

[paste each file with filename header]
```

Output will be separate JSON for each file.

---

## Validation Checklist

Before considering proofreading done:

- [ ] Run skill on all files
- [ ] Review each error in context
- [ ] Apply fixes you agree with
- [ ] Run skill again on each file
- [ ] All files return `"total_issues": 0`
- [ ] Your voice and meaning are preserved

---

## Key Principle

**This skill is a detector, not a rewriter.**

It finds objective problems:
- ✅ Typos (wrong letters)
- ✅ Grammar (wrong verb form)
- ✅ Ambiguity (unclear pronouns)

It **respects your voice**:
- ✅ Fragment sentences for emphasis
- ✅ Conversational tone
- ✅ Your technical choices
- ✅ Your style

Every fix should feel like "oh, I missed that" — not "the AI rewrote me."

---

## Limitations

- Cannot catch contextual errors (a correct word used in wrong context)
- Cannot validate technical accuracy
- Cannot check if URLs are alive
- Cannot check markdown link syntax validity

For these, use:
- **Spell check tools**: Grammarly, aspell
- **Link checker**: markdown-link-check
- **Markdown linter**: markdownlint
- **Technical review**: Domain experts

---

## Support

If this skill:
- **Changes meaning** → Report it, don't apply it
- **Changes style** → Report it, don't apply it  
- **Misses obvious errors** → Note them, skill improves iteratively
- **Produces different results** → Include both runs in bug report

The skill is deterministic when used correctly. **Identical input → identical output.**
