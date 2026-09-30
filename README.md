# US Study Advisor for Law Students

I help law students and graduates reason through the move to U.S. study, from choosing a degree and funding it to applications, internships, and the path toward qualification. I start by asking what would have to be true for a plan to work, then compare the live alternatives before favoring one. The answer that feels obvious gets examined for the assumptions that made it feel that way.

If you are comparing an LL.M. and a J.D., I establish the objective, hard constraints, and criteria before ranking programs. I look for the fact that could rule an option out or reverse the recommendation, such as an eligibility condition or an unaffordable funding gap. More school descriptions do not help if they leave that fact unresolved. I distinguish published data, my inference from it, and an unsupported hunch; a deadline, tuition figure, or bar rule needs current confirmation from the authority that owns it.

When I read an application draft, I ask what the reader must understand about you and which parts of your record support it. I make the central claim clear, test whether it survives a skim, and explain which revisions are necessary and which are matters of preference. Your experiences and disclosure choices remain yours. I sharpen the writing without inventing accomplishments or replacing your voice, and keep analytical labels out of prose written in your name.

I give a recommendation with the alternatives set aside, the reasons, and the observable changes that would warrant revisiting it. This Agent Skill pairs that analytical discipline with seven task-loaded modules on calibration, decision methods, U.S. study pathways, institutions, and writing.

**Objective → alternatives → discriminating evidence → recommendation → trip-wires.**

[Workflow](#how-it-works) · [Use cases](#use-it-for) · [Install](#installation) · [Examples](#example-requests) · [Repository map](#repository-layout) · [Sources](#sources-and-their-responsibilities) · [Validation](#coverage-and-validation)

## How it works

```mermaid
flowchart TD
    accTitle: Reasoning and delivery workflow
    accDescr: The task and evidence guide domain reasoning, the output and review.
    input["Study decision or application draft"]
    frame["Establish objectives, constraints and live alternatives"]
    reason["Separate published data, inference and uncertainty"]
    choice{"Decision or writing task?"}
    primary["Conditional recommendation and rejected alternatives"]
    alternative["Fact-preserving revision in the applicant’s voice"]
    review["Verify volatile facts and state revision triggers"]
    input --> frame --> reason --> choice
    choice --> primary
    choice --> alternative
    primary --> review
    alternative --> review
    review -.->|Revisit when evidence changes| reason
    classDef focus fill:#e0f2fe,stroke:#0369a1,color:#0c4a6e
    classDef output fill:#dcfce7,stroke:#15803d,color:#14532d
    classDef decision fill:#fef3c7,stroke:#b45309,color:#78350f
    class frame,reason focus
    class primary,alternative output
    class choice,review decision
```

Objective → alternatives → discriminating evidence → recommendation → trip-wires. The diagram summarizes the reasoning route; the question and available evidence determine which branches are useful.

### Why this exists

Most application advice fails in one of three ways. It arrives at an answer first and
then assembles support for it. It blurs a published fact, a chain of reasoning, and a
gut read into one confident-sounding sentence. Or it states last decade's rule as this
year's rule.

This skill is built to make those three failures structurally awkward. The core voice
carries the habits; seven trigger-loaded modules carry the procedures and the domain
structure; and a provenance file records where every behaviour came from and how fast
each piece of domain knowledge decays.

## Use it for

### What it does and does not do

**It does:**

- Lay out the alternatives it considered and name the ones it rejected, with reasons.
- Tag every substantive claim as data, inference, or hunch — and split claims that mix
  them.
- Triage how much analytic machinery a question deserves, and say which category it
  thinks you are in.
- Attach a trip-wire to every recommendation: the observable that would mean the
  recommendation needs revisiting, and in which direction.
- Read your draft as the tired, self-interested reader on the fortieth file would.
- Remove recurring AI-writing patterns without changing claims or replacing your voice.
- Refuse a fabricated percentage, and give a mechanism and a condition instead.

**It does not:**

- Give legal, immigration, financial, or other advice that calls for a licensed
  professional. It explains how things generally work and marks where you need real
  counsel.
- State a current rule. Bar eligibility, visa procedure, work-authorization caps,
  deadlines, tuition, and test requirements all change; the skill flags them and names
  the office that owns the real answer.
- Insert experiences you did not provide, or let a draft imply something untrue.
- Decide what you disclose about yourself. That is left entirely to you.

## Installation

**As an agent skill.** Copy the whole directory into the skills location configured
by your agent host, preserving the `references/` subdirectory. You can omit
`fidelity-ledger/` from the copy — it is maintainer documentation, not skill content,
and no host loads it:

```bash
git clone https://github.com/ariel-lee-1023/US-study-Advisor-for-Law-Students.git us-study-advisor-for-law-students
```

Then move `us-study-advisor-for-law-students/` into that configured skills location.

Remove the repository-level files (`README.md`, `LICENSE`, `CHANGELOG.md`,
`.gitignore`) from the copied folder if you want the skill directory to contain only
skill content. They are harmless if left in place.

**As a system prompt or project instruction.** Paste the body of `SKILL.md` (below the
YAML front matter) as the system prompt, and attach the reference modules as project
knowledge. Behaviour degrades gracefully — the core is written to work without any
module loaded.

**Framework compatibility.** `SKILL.md` carries YAML front matter with `name` and
`description`; the rest is plain Markdown. Nothing here depends on a particular
runtime.

## Example requests

> Compare an LL.M. and J.D. for my stated goals, funding constraints and qualification plans. Name the fact most likely to reverse your recommendation.

> Revise this personal statement without inventing experiences or changing my disclosure choices. Explain the necessary edits.

> Which of these claims require current confirmation from a school, state bar or government office?

## Repository layout

```mermaid
flowchart LR
    accTitle: Repository structure and runtime loading
    accDescr: The canonical core routes to references, while supporting files and maintenance records have separate roles.
    root["US-STUDY-ADVISOR-FOR-LAW-STUDENTS/"]
    root --> core["SKILL.md<br/>Reasoning core and loading triggers"]
    core -->|Loads relevant depth| refs["references/<br/>Runtime reference library"]
    root --> support0["fidelity-ledger/<br/>Provenance and evaluation"]
    root --> support1["LICENSE<br/>License"]
    root --> alias0[".agents/skills/us-study-advisor-for-law-students"]
    alias0 -.->|Discovery alias| root
    classDef runtime fill:#e0f2fe,stroke:#0369a1,color:#0c4a6e
    classDef support fill:#f1f5f9,stroke:#64748b,color:#334155
    class core,refs runtime
    class support0,support1 support
```

[Expert core](SKILL.md) · [Reference library](references/) · [Provenance and evaluation](fidelity-ledger/) · [License](LICENSE).

The map reflects the repository’s existing architecture. Runtime references and human-facing maintenance or learning records have different loading roles.

```
us-study-advisor-for-law-students/
├── README.md
├── SKILL.md                      # the core advising voice — loaded always
├── references/                   # trigger-loaded modules — host-agent-facing
│   ├── calibration.md            # probability, base rates, updating
│   ├── toolbox.md                # structured analytic techniques
│   ├── llm-pathway.md            # LL.M./J.D., bar eligibility, visas
│   ├── legal-writing.md          # U.S. legal-writing convention
│   ├── personal-statements.md    # topic selection, structure, addenda, recommendation letters
│   ├── humanizer.md              # fact-preserving cleanup of AI-writing patterns
│   └── institutions.md           # how U.S. universities are funded and governed
├── fidelity-ledger/              # human-maintainer-facing — never trigger-loaded
│   └── provenance.md             # sources, fidelity notes, staleness ledger, extension protocol
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md                     # originality and source-attribution statement
└── .gitignore
```

`references/` and `fidelity-ledger/` sit side by side, on purpose, and are not
interchangeable. `references/` is written for a host agent to load automatically
when a trigger fires — every file in it is a module that can end up quoted or
paraphrased in the advising voice. `fidelity-ledger/` is written for the human
maintaining this repository — sourcing, fidelity notes, the staleness ledger, and
the extension protocol. No host ever loads it as part of normal operation, and
nothing in it is meant to reach the advising voice. If a file would answer "where
did this come from, and how do I extend it" rather than "what should the advisor
know or do," it belongs in `fidelity-ledger/`, not `references/`.

### Architecture: core voice, trigger-loaded modules

`SKILL.md` is the reasoning temperament and stands alone. The modules are **not**
preloaded — each one loads when its trigger fires, and each carries procedure and
structure only. A module that starts speaking in the first person has broken the
architecture, and `fidelity-ledger/provenance.md` says so explicitly.

| Trigger | Module |
|---|---|
| Stating or revising a probability or confidence | `references/calibration.md` |
| A decision consequential enough to earn extra structure — irreversible, high-cost, contested, or where the leading answer arrived suspiciously early | `references/toolbox.md` |
| LL.M./J.D. pathway mechanics, bar eligibility, visa logic, programme selection | `references/llm-pathway.md` |
| U.S. legal-writing convention, or the rhetorical transition for writers trained in another legal culture | `references/legal-writing.md` |
| Drafting or structuring a personal statement, optional essay, addendum, or wait-list letter; selecting or briefing recommenders | `references/personal-statements.md` |
| Drafting, rewriting, or line-editing prose that should sound like the applicant; reviewing AI-writing patterns; a request to humanize text | `references/humanizer.md` |
| How U.S. universities and law schools are structured, funded, or governed | `references/institutions.md` |

For any domain not covered, the advisor reasons from the core and says plainly that
the question is outside its material. Auditing, editing, or extending the skill is not
a trigger a host ever fires — that work is done by a human maintainer reading
`fidelity-ledger/provenance.md` directly.

## Sources and their responsibilities

```mermaid
flowchart LR
    accTitle: Sources and their primary responsibilities
    accDescr: Task responsibilities connect the expert to its source material; groupings do not imply author agreement.
    core["Expert core and task router"]
    core --> g0["Analytical judgment"]
    g0 --> s0_0["Heuer · Psychology of Intelligence Analysis"]
    g0 --> s0_1["Heuer &amp; Pherson · Structured Analytic Techniques"]
    g0 --> s0_2["Tetlock &amp; Gardner · Superforecasting"]
    classDef group0 fill:#ede9fe,stroke:#7c3aed,color:#4c1d95
    class g0,s0_0,s0_1,s0_2 group0
    core --> g1["Pathways and institutions"]
    g1 --> s1_0["Edwards · LL.M. Roadmap"]
    g1 --> s1_1["Thelin · American Higher Education"]
    classDef group1 fill:#dcfce7,stroke:#15803d,color:#14532d
    class g1,s1_0,s1_1 group1
    core --> g2["Writing and application craft"]
    g2 --> s2_0["Ramsfield · Culture to Culture"]
    g2 --> s2_1["Bodine · Great Personal Statements for Law School"]
    g2 --> s2_2["Princeton Review · Law School Essays That Made a Difference"]
    g2 --> s2_3["Stewart · Perfect Personal Statements"]
    g2 --> s2_4["Zhang &amp; Mohapatra, eds. · Successful Personal Statements"]
    g2 --> s2_5["Top Law Schools · Guide to Personal Statements"]
    g2 --> s2_6["Chen · Humanizer"]
    classDef group2 fill:#fef3c7,stroke:#b45309,color:#78350f
    class g2,s2_0,s2_1,s2_2,s2_3,s2_4,s2_5,s2_6 group2
    classDef focus fill:#e0f2fe,stroke:#0369a1,color:#0c4a6e
    class core focus
```

Connections show primary contributions, not a required reading order or agreement among authors. Full source details and qualifications follow; source-specific depth is available in the reference library.

| Author / provider | Full source title | Edition or supplied context | Responsibility |
|---|---|---|---|
| Richards J. Heuer Jr. | Psychology of Intelligence Analysis | 1999 | Assumptions, competing hypotheses and source evaluation |
| Richards J. Heuer Jr. & Randolph H. Pherson | Structured Analytic Techniques for Intelligence Analysis | Supplied 2nd ed., 2011 | Procedures for consequential judgments |
| Philip E. Tetlock & Dan Gardner | Superforecasting: The Art and Science of Prediction | 2015 | Calibration and updating |
| George E. Edwards | LL.M. Roadmap: An International Student’s Guide to U.S. Law School Programs | 2011 | Pathway mechanics with current-rule verification |
| Jill J. Ramsfield | Culture to Culture: A Guide to U.S. Legal Writing | 2005 | Legal-writing conventions |
| John R. Thelin | American Higher Education: Issues and Institutions | Edition not specified in the existing README | Institutional funding and governance |
| Paul Bodine | Great Personal Statements for Law School | 2006 | Application genre and structure |
| The Princeton Review | Law School Essays That Made a Difference | 6th ed., 2014 | Essay patterns and examples |
| Mark Alan Stewart | Perfect Personal Statements: Law, Business, Medicine, Graduate School | 2nd ed., 2002 | Statement craft |
| Warren Zhang & Hemant Mohapatra, eds. | Successful Personal Statements to Get You into a Top University | Edition not specified; undergraduate compilation | Structural patterns only |
| Top Law Schools | Guide to Personal Statements | Web source, current-as-fetched | Application-writing guidance |
| Siqi Chen | Humanizer | 2.11.2, 2025 | Fact-preserving prose cleanup |



### Source corpus

Three sources supply the reasoning temperament; the admissions and education sources
supply domain structure; Humanizer supplies a sentence-level editing checklist. The
division is deliberate — the voice is not a subject-matter expert wearing an analyst's
manner, it is an analyst reasoning over domain structure it treats as provisional.

**Reasoning temperament**

- Richards J. Heuer Jr., *Psychology of Intelligence Analysis* (1999)
- Richards J. Heuer Jr. & Randolph H. Pherson, *Structured Analytic Techniques for
  Intelligence Analysis* (2nd ed., 2011)
- Philip E. Tetlock & Dan Gardner, *Superforecasting: The Art and Science of
  Prediction* (2015)

**Domain structure**

- George E. Edwards, *LL.M. Roadmap: An International Student's Guide to U.S. Law
  School Programs* (Aspen, 2011)
- Jill J. Ramsfield, *Culture to Culture: A Guide to U.S. Legal Writing* (Carolina
  Academic Press, 2005)
- John R. Thelin, *American Higher Education: Issues and Institutions* (Routledge,
  Core Concepts in Higher Education)
- Paul Bodine, *Great Personal Statements for Law School* (McGraw-Hill, 2006)
- The Princeton Review, *Law School Essays That Made a Difference* (6th ed., 2014)
- Mark Alan Stewart, *Perfect Personal Statements: Law, Business, Medicine, Graduate
  School* (Peterson's, 2nd ed., 2002)
- Warren Zhang & Hemant Mohapatra (eds.), *Successful Personal Statements to Get You
  into a Top University* — UK/international undergraduate-admissions compilation, used
  for structural patterns only; see `references/personal-statements.md` §6 for what
  transfers and what does not
- [Top Law Schools, "Guide to Personal
  Statements"](https://www.top-law-schools.com/personal-statement-examples.html) — web
  source, treated as current-as-fetched rather than a fixed-date book

**Editing**

- Siqi Chen, [*Humanizer*](https://github.com/blader/humanizer), version 2.11.2
  (2025) — an MIT-licensed editing checklist based on Wikipedia's "Signs of AI
  writing," adapted in `references/humanizer.md`

Except for the MIT-licensed Humanizer adaptation, nothing is quoted at length from a
source; the domain modules are synthesised. Author terminology is preserved exactly
where the term *is* the framework — ACH, Key Assumptions Check, ELP, RCM, revenue
theory, disease theory, cost/price/net price, perpetual beta, Fermi-izing, TELL model,
uniqueness filter — because paraphrasing a named framework destroys the ability to
find it in the original. A behaviour-by-behaviour source map is in
`fidelity-ledger/provenance.md` §2.

## Coverage and validation

Source attribution, behavior grounding, fidelity notes and staleness are recorded in [the provenance ledger](fidelity-ledger/provenance.md). This README layout update does not supply a new behavioral evaluation.

### Extending it

The extension protocol is in `fidelity-ledger/provenance.md` §6. In short: distil structure
and decision rules rather than summary, preserve the author's exact framework names,
keep the file trigger-loaded and headed with **Sources / Trigger / What this file is**,
add a vintage warning and a staleness row, end with decision rules, and register the
source and the new behaviours in `fidelity-ledger/provenance.md` §§1–2.

The one hard constraint: **the voice lives in the core and must not be duplicated into
modules.**

Issues and pull requests are welcome. A pull request that adds a module should include
its `fidelity-ledger/provenance.md` entries; one that changes core behaviour should say which grounding
in §2 it is revising, or make the case that the behaviour belongs in the list of
commitments held for independent ethical reasons rather than analytic ones.

## Limits

### The vintage caution

The modules are distilled from books with fixed publication dates. What they carry
reliably is **structure** — the sequence of decisions, the shape of a system, the
mechanism behind an institution's behaviour. What they do not carry reliably is
**current fact**.

The full decay-ordered ledger is in `fidelity-ledger/provenance.md` §4. The headline:

| Content | Decay | Handling |
|---|---|---|
| Bar eligibility rules for foreign-educated lawyers | Fastest | Never state from the module; route to the specific state bar every time |
| Visa procedures, work-authorization durations and caps | Very fast | Route to the campus international office and current government guidance |
| Deadlines, tuition, fees, aid programmes, test requirements | Yearly | Flag as volatile; verify against the school |
| Named schools' statement-weighting, named admissions officers | Yearly to several years | Verify against current published guidance |
| Institutional mechanism, rhetorical framework, personal-statement genre conventions, cognitive biases | Very slow to stable | Usable directly |

**Combining these modules never produces a current rule.**

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. The adapted Humanizer
module retains its original MIT copyright and license notice in `NOTICE.md`. The
license does not extend to referenced source books, which remain the property of
their respective copyright holders.
