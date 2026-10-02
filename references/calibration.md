# references/calibration.md

**Sources:** Tetlock & Gardner, *Superforecasting: The Art and Science of Prediction* (2015), esp. the Ten Commandments appendix; Heuer, *Psychology of Intelligence Analysis* (1999), ch. 12 ("Biases in Estimating Probabilities") and ch. 14 (hindsight).
**Trigger:** load when **stating or revising a probability or confidence** — an admissions estimate, a visa-outcome read, a timeline, a "how likely is this to work."
**What this file is:** conventions and procedures for expressing and updating uncertainty. No temperament language — the disposition to be honestly uncertain lives in the core.

**Production context:** For defining the decision, building the target model, distinguishing gaps from assumptions, and delivering a concise assessment, use [Analytic production](analytic-production.md). This file retains the detailed calibration procedures; neither module needs automatic full loading of the other.

---

## 1. Why a bare verbal qualifier is a failure, not a hedge

Heuer's finding: words like *probable*, *possible*, and *little chance* are empty containers. The reader fills them from their own prior, so an ambiguous estimate reads as confirmation of whatever the reader already believed — which is why a hedged report can have no effect at all.

Two demonstrations worth carrying:
- An analyst asked to put numbers on his own published verbal qualifiers meant roughly 30% by a phrase his co-author had read as roughly 80%. They had written it together believing they agreed.
- Heuer and a colleague disagreed for months over a source's bona fides — *probably* genuine versus *probably* hostile — until they each named a number. Both said "at least 51%." There had never been a substantive disagreement, only an ambiguous word.

Sherman Kent identified this problem decades earlier and it persists. **The operational lesson: when a verbal qualifier is doing load-bearing work, attach a number or a band to it.** Not to fake precision — to make the claim falsifiable and to check that two people mean the same thing.

## 2. The band convention

Publish the mapping rather than assuming it. A workable set (Kent-style; the specific numbers matter far less than that they are stated):

| Phrase | Band |
|---|---|
| near-certain / almost certainly | ~90–99% |
| probable / likely | ~65–85% |
| chances about even | ~45–55% |
| probably not / unlikely | ~15–35% |
| almost certainly not / remote | ~1–10% |

Rules of use:
- State the band the first time a qualifier appears in a conversation, then use the word.
- Never use a bare qualifier for the central claim of a recommendation. Peripheral claims can stay verbal.
- If the user supplies a qualifier ("I think I'm probably competitive"), ask what number they mean before reasoning from it.

## 3. Granularity: as many degrees of doubt as the problem permits, and no more

Tetlock's sixth commandment. "Maybe" is not informative; an uncertainty dial needs more than three settings. The measurable edge in forecasting comes from being able to separate 60/40 from 40/60 — not from resolving anything to certainty.

But the ceiling is real. Granularity beyond what the evidence can carry is false precision, which is worse than vagueness because it is unfalsifiable-looking while being invented.

Practical rule: **round to the granularity the evidence supports.** For most advising judgments that is 5% or 10% steps, or an explicit band ("35–50%"). Reserve single-point percentages for cases where a real base rate is in hand.

Tetlock's observation that different norms govern different domains is the useful diagnostic here: people reason in granular odds about sports and then refuse to do it about consequential decisions. The refusal is a norm, not an epistemic limit.

## 4. Fermi-ize before estimating

Second commandment. Decompose an unquantifiable question into knowable and unknowable parts, guess at each, and let the errors partly cancel. The point is not the number — it is that decomposition **flushes ignorance into the open** and exposes which assumption is actually carrying the estimate.

Applied shape for an admissions or funding question:
> total seats × share going to applicants from this region × share with comparable credentials × any structural advantage or disadvantage

Then ask which factor the estimate is most sensitive to. That factor, not the output, is what gets reported and watched.

## 5. Outside view first, then inside view

Third commandment. Before reasoning from the specifics of this case, ask the comparison-class question: **how often do things of this sort happen in situations of this sort?** Then adjust for what makes this case genuinely different — and treat "this case is unique" as a matter of degree, never a reason to skip the base rate.

Heuer's parallel warning: prior probabilities are commonly ignored unless they appear to illuminate a causal story. An abstract base rate loses to a vivid narrative unless it is deliberately anchored on first. So: **base rate first, story second.** Order matters, because once the story is in place the base rate gets discounted.

The planning-fallacy correction applies directly to student timelines: self-estimates of how long an essay, an application round, or a document-authentication process will take are systematically short, and the correction is multiplicative, not additive.

## 6. Updating: the two symmetrical errors

Fourth commandment. Belief updating is routine maintenance, and both failure modes cost accuracy:
- **Underreaction** — clinging to the prior because changing one's mind reads as confusion rather than as rationality. Tetlock notes institutions avoid visible updating for exactly this reputational reason.
- **Overreaction** — treating every headline as signal, and chasing noise.

Discipline:
1. Before updating, ask whether the new item is **diagnostic** — would it look different under the competing answer? If it looks the same either way, it is not evidence, however striking.
2. Prefer **many small updates to few large ones**. Frequent incremental revision outperforms sitting still punctuated by lurches.
3. Watch for wishful updating: a revision that moves toward the outcome the user wants gets a second look before it is made.
4. Name the update out loud: *this moved my estimate from X to Y, on this fact.* An unnarrated update is indistinguishable from drift.

## 7. Two axes of accuracy, and the Brier score

Long-run accuracy has two components and they trade off:
- **Calibration** — when you say 70%, does it happen about 70% of the time?
- **Resolution** — do you actually differentiate, or does everything come out near 50%? Perfect calibration is trivially achievable by never committing.

The **Brier score** measures the squared distance between forecasts and outcomes; lower is better, and it penalizes confident wrongness heavily. It is worth naming because it makes the trade-off concrete: hedging everything to 50% is not humility, it is a scoring strategy that abandons resolution.

Seventh commandment: manage both errors — misses and false alarms — rather than only avoiding the most recent embarrassment.

## 8. The wrong-side-of-maybe fallacy

A 70% forecast is not refuted when the 30% outcome occurs. Judging a probabilistic call by the single realized outcome is the error that pushes forecasters back toward vague language, because vagueness cannot be scored against.

This has a direct advising consequence: **a rejected application does not by itself falsify a well-built estimate, and an acceptance does not vindicate a bad one.** Say this in advance, before the outcome is known, or it sounds like an excuse afterward.

## 9. Keeping score, and postmortems on both sides

Eighth commandment, reinforced by Heuer's hindsight chapter: once an outcome is known, the mind reconstructs its earlier estimate as having been closer to that outcome than it was. Memory of a prior forecast is not evidence of that forecast.

Therefore:
- **Record estimates in writing at the time they are made**, with the reasoning and the linchpin assumption. Retrieval later must be from the record, not from recall.
- **Postmortem the successes too.** A right answer reached through offsetting errors will not repeat, and confidently reasoning the same way again is how a nasty surprise gets set up.
- Distinguish *learning too little* from failure (missing a flawed basic assumption) from *learning too much* (overhauling sound reasoning because of one minor technical slip).

## 10. Heuer's specific probability biases to check against

- **Availability** — probability judged by how easily an instance comes to mind. A vivid recent case (a friend's rejection, a viral admissions story) inflates the estimate. Counter: ask for the frequency, not the example.
- **Anchoring** — starting from a salient number and adjusting insufficiently. Any figure in the room becomes the anchor, including one the advisor named first. Counter: **generate an independent estimate before looking at anyone else's**, then compare.
- **Scenario probability** — a conjunction of plausible steps feels more likely than it is, because each step is judged individually and the multiplication is skipped. Counter: multiply explicitly. A five-step plan of 80%-likely steps is a coin flip.
- **Neglected priors** — see §5.

## 11. Perpetual beta

Tetlock's strongest single predictor of forecaster performance is not intelligence or subject knowledge but the commitment to keep revising method — treating one's own approach as permanently in development. Skill here is the product of deliberate practice with unambiguous feedback, which is why §9's written record is not bookkeeping but the mechanism of improvement.

Eleventh commandment, which supersedes the rest: these are not commandments. They are balances to be ridden, and each one is implemented by managing an opposing pair of errors.

---

## Decision rules

- **Central claim gets a number or a band.** Peripheral claims may stay verbal.
- **Refuse false precision over refusing an answer.** When a number cannot be honestly supported, give the mechanism and the condition instead — *unlikely absent a stronger score* is falsifiable; an invented percentage is not.
- **Base rate first, story second.** Always in that order.
- **Non-diagnostic information does not move the estimate**, regardless of volume.
- **Multiply conjunctions explicitly.**
- **Write the estimate down with its linchpin assumption**; retrieve from the record, never from memory.
- **State the wrong-side-of-maybe rule before the outcome**, not after.
- **Every estimate ships with its trip-wire**: the observable that would move it, and which direction.
