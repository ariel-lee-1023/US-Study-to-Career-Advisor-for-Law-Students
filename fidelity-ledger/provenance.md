# fidelity-ledger/provenance.md

**Purpose:** the source and justification for each behaviour in the core voice, the vintage of every module, and the known limits of the distillation.
**Audience:** the human maintaining this repository — not a host agent. This file lives in `fidelity-ledger/`, a directory a host never trigger-loads, sitting beside (not inside) `references/`. Read it when auditing, editing, or extending the skill, or when you personally want to know where a behaviour comes from.
**Never surfaced in the advising voice.** The advisor does not cite its own construction while advising — it has no trigger that loads this file at all — because doing so would substitute provenance for reasoning.

---

## 1. The corpus

| # | Source | Module | Published |
|---|---|---|---|
| 1 | Heuer, *Psychology of Intelligence Analysis* | core voice; `toolbox.md`; `calibration.md` | 1999 (articles 1978–86) |
| 2 | Heuer & Pherson, *Structured Analytic Techniques for Intelligence Analysis* | `toolbox.md` | 2011 (2nd ed.) |
| 3 | Tetlock & Gardner, *Superforecasting* | `calibration.md`; core voice | 2015 |
| 4 | Edwards, *LL.M. Roadmap* | `llm-pathway.md` | 2011 |
| 5 | Ramsfield, *Culture to Culture: A Guide to U.S. Legal Writing* | `legal-writing.md` | 2005 |
| 6 | Thelin, *American Higher Education: Issues and Institutions* | `institutions.md` | Core Concepts series |
| 7 | Bodine, *Great Personal Statements for Law School* | `personal-statements.md` | 2006 |
| 8 | The Princeton Review, *Law School Essays That Made a Difference*, 6th ed. | `personal-statements.md` | 2014 |
| 9 | Stewart, *Perfect Personal Statements: Law, Business, Medicine, Graduate School*, 2nd ed. | `personal-statements.md` | 2002 |
| 10 | Zhang & Mohapatra (eds.), *Successful Personal Statements to Get You into a Top University* | `personal-statements.md` (structural patterns only — see module §6) | UK/international undergraduate-admissions compilation, exact year unverified |
| 11 | Top Law Schools, "Guide to Personal Statements" (top-law-schools.com) | `personal-statements.md` | Web page, undated — treat as current-as-fetched only |
| 12 | Siqi Chen, *Humanizer*, version 2.11.2 (MIT License), based on Wikipedia's "Signs of AI writing" | `humanizer.md` | 2025; versioned editing checklist |
| 13 | Yu & Cable, eds., *The Oxford Handbook of Recruitment* | `recruitment-and-selection.md` | copyright 2014 |
| 14 | Neal Schmitt, ed., *The Oxford Handbook of Personnel Assessment and Selection* | `recruitment-and-selection.md; roles-and-organizations.md` | 2012 |
| 15 | Cheri Ostroff & Timothy A. Judge, eds., *Perspectives on Organizational Fit* | `fit-and-gatekeeping.md` | 2007 |
| 16 | Lauren A. Rivera, *Pedigree: How Elite Students Get Elite Jobs* | `fit-and-gatekeeping.md` | 2015; interviews 2006–2008 |
| 17 | Herminia Ibarra, *Working Identity: Unconventional Strategies for Reinventing Your Career* | `career-transition-and-search.md` | 2003 |
| 18 | Steve Dalton, *The 2-Hour Job Search: Using Technology to Get the Right Job Faster* | `career-transition-and-search.md` | revised supplied text, copyright 2012/2020 |
| 19 | Claire Hughes Johnson, *Scaling People: Tactics for Management and Company Building* | `roles-and-organizations.md; recruitment-and-selection.md` | supplied first edition, copyright 2022 |
| 20 | Atta Tarki, *Evidence-Based Recruiting: How to Build a Company of Star Performers Through Systematic and Repeatable Hiring Practices* | `recruitment-and-selection.md` | 2020 |
| 21 | Robert M. Clark, *Intelligence Analysis: A Target-Centric Approach* | `analytic-production.md` | 5th ed., copyright 2017; source catalog dated 2016 |
| 22 | Roger Z. George & James B. Bruce, eds., *Analyzing Intelligence: Origins, Obstacles, and Innovations* | `analytic-production.md` | 2008 |
| 23 | M. Patrick Hendrix & James S. Major, *Communicating with Intelligence: Writing and Briefing for National Security* | `analytic-production.md` | 3rd ed., 2023 |

Sources 1–3 supply the **reasoning temperament and its procedures**. Sources 4–11 supply **domain structure**. Source 12 supplies a **sentence-level editing checklist**, not facts or advising voice. This division is deliberate and load-bearing: the voice is not a subject-matter expert wearing an analyst's manner, it is an analyst reasoning over domain structure it treats as provisional.

## 2. Core behaviour → source map

| Core behaviour | Grounding |
|---|---|
| Begin from what would have to be true, not from an answer | Heuer, ACH step 1; Heuer & Pherson, "What would have to be true?" |
| Generate the full alternative set before filtering for plausibility | Heuer, ACH step 1; H&P hypothesis-generation chapter |
| Distrust the answer that arrived early and easily | H&P, challenge-analysis rationale; the mindset finding in failure postmortems |
| Seek disconfirmation; the option left standing wins | Heuer, ACH step 5 — rank by inconsistency, not consistency |
| Evidence consistent with every option tells you nothing | Heuer, ACH step 4 (diagnosticity) |
| Report the rejected alternatives and why | Heuer, ACH step 7 |
| More information increases confidence, not accuracy | Heuer, "Do You Really Need More Information?" |
| Trying to be objective does not make one objective | Heuer, perception and mind-set chapters |
| A good process beats a lucky right answer | Tetlock, commandments 8 and 10; Heuer's process orientation |
| Separating data / inference / hunch | Heuer's insistence on distinguishing verified fact from assumption within evidence; H&P Quality of Information Check |
| Volatile facts flagged and sent for verification | Edwards' own instruction on bar rules; H&P source-currency check |
| Aim first at the discriminating fact; stop when more stops discriminating | Heuer, diagnosticity; H&P Indicator Validator™ |
| Weight the unexpected; anomalies get more attention, not less | Heuer on the evidentiary asymmetry facing expectation-inconsistent data |
| Source independence — three accounts from one origin are one source | H&P Quality of Information Check |
| Comparisons rank by fewest disqualifiers, not most points | Heuer, ACH step 5, transposed to options; H&P Decision Matrix |
| Name the single fact that would flip the ranking | Heuer, ACH step 6 (sensitivity) |
| Every recommendation ships with trip-wires | Heuer, ACH step 8; H&P Indicators |
| Read the draft as the self-interested gatekeeper would | H&P Red Hat Analysis; Edwards on committee motivation and the informal application |
| Remove AI-writing patterns without changing claims or replacing the applicant's voice | Chen, *Humanizer* 2.11.2; implemented as a trigger-loaded editing pass rather than core voice |
| Concede facts freely, premises rarely | Tetlock, commandment 4 (update on evidence, not on pressure) |
| Mechanism-and-condition instead of false precision | Tetlock, commandment 6 (granularity permitted by the problem, no more) |
| The lens goes on before the evidence arrives | Heuer's central thesis across the perception, memory, and mind-set chapters |
| Model the decision target through structure, function, process and feedback | Clark, chs. 3–7 and 13; career application is analogy |
| Separate known information, assumptions, judgments and material gaps | Clark, evidence/gap analysis; Hendrix/Major, analytic delivery; synthesis preserves core data/inference/hunch |
| Investigate institutional distortion without assuming deceptive intent | George/Bruce, chs. 6, 8, 10–12; ordinary employer/university explanations remain alternatives |
| Lead with defensible key judgments and distinguish likelihood from confidence | Hendrix/Major, chs. 1, 3, 7–10; source audience/production principles adapted to advising |
| Analyze roles before titles or additional credentials | Schmitt ch. 7; Hughes Johnson chs. 2–5; role-family market procedure is synthesis |
| Distinguish recruitment, selection, fit, gatekeeping, transition and tactics | Cross-book synthesis: Yu/Cable; Schmitt; Ostroff/Judge; Rivera; Ibarra; Dalton |
| Ask which construct, instrument and outcome support a hiring inference | Schmitt ch. 6 and assessment chapters; Tarki operating practices separately bounded |
| Treat fit as dimensional, relational and revisable | Ostroff/Judge; distinguish perception, measurement, referent and outcome |
| Examine social signals without endorsing class-coded exclusion | Rivera; bounded to elite professional-services recruitment |
| Test career direction through practice while organizing search actions | Ibarra's test-and-learn; Dalton's LAMP, 6-Point Email, 3B7 and TIARA |

**Behaviours not derived from the corpus**, held for independent reasons: use of the user's name and pronouns exactly; refusal to substitute for licensed professional advice; refusal to insert experiences the user did not provide; leaving disclosure decisions entirely to the user; delivering hard reads kindly. These are ethical commitments, not analytic method, and should not be revised on analytic grounds.

## 3. Fidelity notes and deliberate departures

- **The core carries habits; modules carry procedures.** Heuer's techniques are presented in the source as team processes run on a schedule. Compressing them into a one-to-one advising voice required separating the *disposition* (always in the core) from the *procedure* (loaded on trigger). Running full ACH on a routine question would be a fidelity error in the other direction.
- **Tetlock's numeric discipline is bounded here.** Superforecasting assumes resolvable questions and a scoring system. Most advising questions never resolve cleanly and the advisor sees no feedback. `calibration.md` therefore keeps granularity, base rates, decomposition, and the wrong-side-of-maybe rule, and treats Brier scoring as an explanatory device rather than an available instrument.
- **The domain sources are used for structure, not for facts.** See §4. Edwards is used for the shape of the pathway, Ramsfield for the architecture of U.S. legal prose, Thelin for institutional mechanism. Each also contains specifics that are now unreliable, and the modules mark them.
- **Ramsfield's warning is honoured.** She explicitly cautions that her taxonomy of analytical patterns could become an end rather than a means, replacing judgment with formalism. `legal-writing.md` reproduces the warning rather than presenting the categories as a template.
- **Thelin is applied to graduate and professional education by extension.** His institutional analysis is largely framed around undergraduate education; the RCM, cost/price, and governance mechanisms transfer directly, but claims specific to undergraduate admissions do not and are not carried over.
- **The Zhang/Mohapatra source is deliberately used for structure only, never content.** It is a UK/international undergraduate-admissions compilation, outside the U.S.-law-school domain this skill covers (§5 lists non-U.S. jurisdictions as a known gap). `personal-statements.md` §6 extracts only the structural patterns that independently recur in the U.S.-law-specific sources (Bodine, the Princeton Review, Stewart) and explicitly enumerates the UK-specific mechanics — UCAS, Oxbridge interviews, A-level/IB framing — that must not be reasoned into a U.S. context. This is the same discipline as bounding Tetlock's numeric scoring in `calibration.md`: take the transferable mechanism, leave the non-transferable apparatus behind.
- **Bodine's publication year required verification.** The source file's own filename metadata suggested 1959; bibliographic records (McGraw-Hill, 2006, 1st ed.) confirm the actual year. Always verify a source's publication date independently before writing a vintage note — do not trust filename or upload metadata.
- **The top-law-schools.com page is treated as a web source, not a book.** It carries no fixed publication date and its sample-essay ratings and admissions-dean quote are current only as of the fetch date recorded in this repo's history; unlike the book sources, it should be re-fetched rather than assumed stable if its content is ever load-bearing for a specific claim.
- **Humanizer is adapted under the MIT License rather than distilled as domain authority.** Its checklist is loaded only for prose revision. The advisor's factual discipline, the applicant's genuine writing sample, and the document's purpose and genre take precedence. The checklist diagnoses patterns; it is not used to infer authorship. The original copyright and permission notice are preserved in `NOTICE.md`.
- **Except for the MIT-licensed Humanizer adaptation, nothing is quoted at length from a source.** The domain modules are synthesised. Author terminology is preserved exactly where the term is the framework — ACH, Key Assumptions Check, Indicator Validator™, ELP, RCM, revenue theory, disease theory, cost/price/net price, perpetual beta, Fermi-izing, dragonfly eye, TELL model, "data-mining your life," "Everything Signifies," "Fine Art of Damage Control," uniqueness filter — because paraphrasing a named framework loses the ability to find it in the source.

## 4. Staleness ledger

The reasoning modules age slowly; the domain modules age fast. Ordered by decay rate:

| Content | Decay | Handling |
|---|---|---|
| Bar eligibility rules for foreign-educated lawyers | **Fastest.** Edwards flags them as changing and they have changed. | Never state from the module. Route to the specific state bar every time. |
| Visa procedures, work-authorization durations and caps | Very fast; regulatory. | Route to campus international office and current government guidance. |
| Deadlines, tuition, fees, aid programmes, test requirements | Yearly. | Flag as volatile; verify against the school. |
| Rankings, programme existence, faculty, class profiles | Yearly. | Verify; treat any specific school claim as provisional. |
| Named schools' stated statement-weighting, named admissions officers/titles (Princeton Review interviews; top-law-schools.com) | Yearly to several years — staff and policy turn over. | Verify against the school's current published guidance; never state a named officer's view as current without checking. |
| Specific prompts, word limits, optional-essay/addendum offerings for a given school and cycle | Yearly, sometimes cycle-to-cycle. | Always verify against that school's own current application instructions. |
| Citation-format specifics, research tools | Slow but real. | Check current style manual. |
| Application component structure; committee motivation | Slow. | Usable as structure. |
| Personal-statement topic taxonomy, structural architecture, addendum/recommendation-letter mechanics (Bodine, Stewart, Princeton Review craft guidance) | Very slow — describes a durable genre convention. | Usable directly. |
| Humanizer AI-writing pattern checklist | Medium — model habits and stylistic conventions change, and the source is versioned. | Use as a diagnostic checklist, preserve writer samples as the stronger signal, and review against upstream when updating the module. |
| Analytical patterns, rhetorical framework, design elements, ELP | Very slow — describes a legal culture. | Usable directly. |
| Institutional mechanism: cost/price, RCM, revenue and disease theories, governance | Very slow. | Usable directly. |
| Cognitive biases, ACH, calibration discipline | Effectively stable. | Usable directly. |
| Current openings, headcount, salaries, recruiter contacts, interview loops and sponsorship policies | Fast; sometimes days. | Verify with current employer sources; date and scope claims. Historical book examples are not current policies. |
| Platform features and contact-finding tools | Fast. | Preserve Dalton’s workflow; verify tools and permitted use independently. |
| Numerical validity estimates, assessment rankings, employment-law standards | Research and legal updates can materially change conclusions. | Retrieve current primary research or official authority; do not reproduce historical coefficients as current rankings. |
| Fit vocabulary, job analysis, organizational mechanisms and career experimentation | Relatively durable, with boundary conditions. | Use as frameworks, not an individualized success guarantee. |
| Target models and analytic-production methods | Durable methods; each populated model can age rapidly. | Date evidence; update actors, links, constraints and assumptions as facts change. |

**Standing rule:** when a module supplies a specific rather than a structure, the advisor says which it is, marks the specific as needing verification, and names the office or authority that owns the current answer.

## 5. Known gaps

Not covered by the corpus, and to be reasoned from the core rather than confabulated:

- Any jurisdiction outside the U.S., including comparison of U.S. programmes with programmes elsewhere. `personal-statements.md` §6 draws only structural patterns from its one non-U.S. source and explicitly excludes that source's mechanics for this reason.
- Non-law graduate admissions, beyond what Thelin's institutional analysis supports generically and what Stewart's cross-field comparison in `personal-statements.md` §1–2 supports for statement craft specifically.
- Current market size/demand, openings, salaries, employer-specific policies and hiring loops. Durable recruitment, selection, fit, gatekeeping, organizational work and career/search mechanisms are now covered; occupational examples do not establish current opportunity or exhaustive labor-market coverage.
- Current immigration eligibility and rules beyond the student-pathway structure. Employment analysis flags the constraint; it does not create legal expertise or establish authorization.
- Tax, financial planning, and loan product specifics.
- Anything about a named individual school. The corpus supports *how to evaluate* a school; it supports no claim *about* one. This extends to `personal-statements.md`: named schools and officers in its sources are illustrative of a pattern, not a current claim about that school's process.

A gap should produce an explicit statement that the question is outside the material, plus the core's reasoning applied honestly — never a confident-sounding answer assembled from adjacent knowledge.

## 6. Extension protocol

To add a domain module: distil structure and decision rules, not summary; preserve the author's exact framework names; place the new file in `references/` (never in `fidelity-ledger/`) so the host can trigger-load it; head it with **Sources / Trigger / What this file is**; add a vintage warning and a staleness row; end with decision rules; and add the source to §1 and the behaviour rows to §2 of this file. **The voice lives in the core and must not be duplicated into modules** — a module that starts speaking in the first person has broken the architecture.

**Directory test before adding any file to this repository.** Ask: would a host agent ever load this automatically because a trigger fired? If yes, it is a module and belongs in `references/`, with a Sources/Trigger/What-this-file-is header. If no — it exists so a human maintainer can audit, extend, or verify the skill — it belongs in `fidelity-ledger/`, alongside this file. Never let a maintainer-facing file (sourcing, fidelity notes, staleness ledgers, extension protocols, changelog-style records) sit inside `references/`, and never let a trigger-loaded module sit in `fidelity-ledger/`. The two directories exist specifically so a host agent's automatic loading can never accidentally pull in documentation that was written for a human and was never meant to reach the advising voice.


## 7. 2026-10-02 fold-in and renamed project

The user authorized expansion to a study-to-career advisor and chose `US-Study-to-Career-Advisor-for-Law-Students` for the local and remote repository. A supplemental request added the analytic-production layer before publication. Eleven new books were integrated into five task modules; the destination's core/module architecture governs, not a per-book output layout. The existing seven modules remain, with production-context links added to toolbox/calibration.

The original analytic voice remains central. Repeated explanations were compressed to accommodate employment and production judgments under the core size ceiling. Existing study and writing scope, disclosure control, truthfulness and the English default remain. The original source entries and historical provenance were preserved rather than silently reverified in this fold-in.

**Fidelity boundaries.** Occupational/function examples, candidate evidence matrices, experiment cards and the integrated workflow are labeled advisor synthesis. General employment analysis does not expand the admissions source coverage. Rivera is not a universal employer model. Practitioner processes are separated from validity research. The Tarki/Hughes Johnson veto disagreement is explicit. Ibarra's evolving goals and Dalton's execution assumptions are connected without erasing their difference. Clark's provisional models remain revisable; Hendrix/Major's conclusion-first delivery does not authorize conclusion-first investigation. George/Bruce's selected failure cases do not supply a base rate for employer deception. The agency restriction on policy prescription is deliberately adapted to conditional career recommendations.

**Reading and coverage.** See `source-manifest.json`, `coverage-audit.md`, `reading-ledger.json`, and `pdf-reading-ledger.json`. This was targeted mechanism extraction, not full-book coverage. Some early tool outputs were truncated; emitted-span/token accounting is explicitly an upper bound and is not a claim that every emitted word was inspected. Key noisy recruitment passages were reread from the original PDF. Bibliographic years are reported from supplied title/copyright pages, with conflicting catalog dates retained rather than guessed.

**Validation.** See `validation.md`. The generic validator is retained for audit but its per-book naming check is inapplicable to this existing architecture. The destination-specific validator checks the actual published contract. Frozen acceptance cases are unrun: no selected external evaluation endpoint/model was configured, and editorial reasoning is not a fresh-context behavioral experiment. No performance-gain claim is made.
