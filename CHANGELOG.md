# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Because this is a skill rather than a library, the version numbers are read as:

- **MAJOR** — the core voice changes, or the module architecture changes in a way
  that would alter the advice a host agent gives.
- **MINOR** — a new reference module is added, or an existing module gains new
  structure or decision rules.
- **PATCH** — wording, formatting, typo, or vintage-note corrections that do not
  change behaviour.

---

## [2026-10-02] — Study-to-career and analytic production upgrade

### Added

- Four integrated employment modules covering actual work and market hypotheses, recruitment/selection, fit/gatekeeping, and transition/search, grounded in eight supplied books.
- One analytic-production module integrating Clark's target models, George/Bruce's institutional failure analysis, and Hendrix/Major's decision-focused communication.
- Source/reading/coverage records, development and final scenario groups, and module-aware structural validation. Behavioral comparison remains unrun.

### Changed

- Renamed the project, skill slug and discovery alias to US Study-to-Career Advisor for Law Students. Local checkout and GitHub repository names follow `US-Study-to-Career-Advisor-for-Law-Students`.
- Extended the core from study and admissions through general U.S. employment questions, with particular attention to law students and internationally educated candidates. Preserved existing study, drafting, identity/disclosure and source-currency commitments.
- Added production links to toolbox and calibration, retained one canonical runtime, and refreshed the README introduction and source map.
- Explicitly distinguished research conclusions, practitioner recommendations, bounded elite-hiring findings and advisor synthesis. Current facts remain live-verification items.

## [Unreleased]

### Added

- New reference module `references/humanizer.md`: fact-preserving prose revision,
  voice matching, and a diagnostic checklist of recurring AI-writing patterns.
  Adapted from Siqi Chen's MIT-licensed Humanizer 2.11.2. `SKILL.md` now routes
  drafting and humanization requests to it after facts, purpose, structure, and
  stance are settled, and keeps data/inference/hunch labels out of applicant-facing
  prose. `README.md`, `NOTICE.md`, and `fidelity-ledger/provenance.md` record the new
  module and its license.
- New reference module `references/personal-statements.md`: personal-statement,
  optional-essay, addendum/diversity-statement, wait-list-letter, and
  recommendation-letter craft. Distilled from Paul Bodine's *Great Personal
  Statements for Law School* (2006), The Princeton Review's *Law School Essays That
  Made a Difference* (6th ed., 2014), Mark Alan Stewart's *Perfect Personal
  Statements* (2nd ed., 2002), and the [Top Law Schools personal-statement
  guide](https://www.top-law-schools.com/personal-statement-examples.html), with
  structural patterns only (never content or mechanics) drawn from Warren Zhang &
  Hemant Mohapatra's UK/international undergraduate-admissions compilation. Fills the
  gap `legal-writing.md` and `llm-pathway.md` left around statement topic selection,
  architecture, and recommender strategy. `SKILL.md`'s trigger table and front-matter
  description, `README.md`'s layout tree, trigger table, source corpus, and vintage
  table, and `fidelity-ledger/provenance.md` §§1, 3, 4, 5 are updated accordingly.

### Changed

- **Moved `provenance.md` out of `references/` into a new top-level `fidelity-ledger/`
  directory**, so it now lives at `fidelity-ledger/provenance.md`. `references/` is
  reserved for modules a host agent trigger-loads into the advising voice;
  `provenance.md` is maintainer-facing documentation — sourcing, fidelity notes, the
  staleness ledger, and the extension protocol — that is never loaded by a host and
  never meant to surface in the advising voice, so it should never have shared a
  directory with the modules that are. `SKILL.md`'s trigger table no longer lists
  `provenance.md` as a trigger (it was never actually one); `README.md`'s layout tree,
  installation section, and all in-body citations now point at the new path. If you
  installed a previous version by copying `references/`, re-copy `fidelity-ledger/`
  separately (or skip it — it is documentation, not skill content, and nothing in
  `references/` or `SKILL.md` depends on it being present at runtime).
- Renamed the skill to **US Study Advisor for Law Students** (`us-study-advisor-for-law-students`).
  The front-matter `name`, the README title and layout block, the installation commands,
  and the changelog comparison links all follow the new name.
- Narrowed the stated scope to match the new name and what the modules actually cover:
  law students and law graduates going to the United States. The front-matter description
  and the README opening now say so, replacing the "not limited to any one field or
  application type" framing.

### Fixed

- The `git clone` command in the README's installation section used a `USERNAME`
  placeholder, so copying it verbatim failed. Now points at the actual repository, as do
  the changelog comparison links.
- Added the `.gitignore` that the layout block and the 1.0.0 scaffolding note both
  already listed.
- The layout block omitted `README.md` and `NOTICE.md`.

## [1.0.0] — 2026-07-24

First public release.

### Added

- `SKILL.md` — the core advising voice: alternative generation before plausibility
  filtering, disconfirmation over confirmation, triage of how much analytic
  machinery a question earns, the data / inference / hunch separation, volatile-fact
  flagging, source-independence and deception-aware review, ranking by fewest
  disqualifiers, weight-before-score discipline, gatekeeper reading of drafts,
  and trip-wires attached to every recommendation.
- `references/calibration.md` — verbal-probability bands, granularity limits,
  Fermi decomposition, outside-view-first ordering, update discipline, the
  wrong-side-of-maybe rule, and Heuer's probability biases.
- `references/toolbox.md` — technique selection guide, the full eight-step ACH
  procedure, Key Assumptions Check, Quality of Information Check (with the
  deception-aware extension), Indicators, Decision Matrix,
  Pros-Cons-Faults-and-Fixes, High Impact/Low Probability, What If?, and the
  challenge techniques.
- `references/llm-pathway.md` — LL.M./J.D. pathway sequence, program taxonomy,
  selection criteria, admission components, visa category logic, work
  authorization structure, funding, and bar eligibility.
- `references/legal-writing.md` — the four rhetorical considerations, the four
  families of analytical pattern, the six design elements, English for Legal
  Purposes, and the cross-cultural transition points.
- `references/institutions.md` — cost / price / net price, the revenue and disease
  theories of rising cost, RCM budgeting, governance and organized anarchy,
  stratification, and internationalisation as a revenue strategy.
- `references/provenance.md` — the corpus, the behaviour-to-source map, fidelity
  notes and deliberate departures, the staleness ledger, known gaps, and the
  extension protocol.
- `README.md`, `LICENSE`, `.gitignore`, and this changelog.

[Unreleased]: https://github.com/ariel-lee-1023/US-Study-to-Career-Advisor-for-Law-Students/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ariel-lee-1023/US-Study-to-Career-Advisor-for-Law-Students/releases/tag/v1.0.0
