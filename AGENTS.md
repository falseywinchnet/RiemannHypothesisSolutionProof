# agents.md — Lean Formal Verification Agent (for OpenAI Codex o3-coding)

## Purpose

A self-contained operating spec for instantiating an automated coding agent (OpenAI Codex, modified o3 model for coding) to produce **Lean 4** formalizations and proofs for the thesis’ analytical results. The agent plans, decomposes, tracks progress, and executes tasks **one sub-component at a time**, with rigorous checkpoints and verifiability.

## Scope

* Translate mathematical statements into Lean 4 definitions, lemmas, and theorems.
* Implement proofs with mathlib tactics and term-mode.
* Maintain a persistent, machine-readable plan and progress ledger.
* Enforce reproducible builds and test gates.

Non-goals (out of scope): numerical experiments, external CAS, or web lookups.

---

## Environment & Tooling

* **Lean**: Lean 4 (pin a concrete toolchain via `elan`).
* **mathlib**: Current stable mathlib compatible with the pinned Lean.
* **Build**: `lake build`, `lean --make`.
* **Linters**: mathlib linters (holes, sorrys, style hints).
* **Repo layout** (suggested):

```
/ (repo root)
 hypothesis.md <- dont touch, this is the main proof. use for everything else.
  agents.md               <- this document
  inabottle.txt <- a document left for you by the last time you were here with the "what to do next" suggestion

  agents/
    plan.yaml               <- master task graph (inputs -> outputs)
    progress.json           <- live status & artifacts index
    prompts/
      system.txt            <- system prompt template
      developer.txt         <- developer prompt template
      task_template.txt     <- per-task prompt scaffold
  lean/
    Thesis/
      Core/                 <- shared defs (measures, transforms, operators)
      Sections/             <- one folder per thesis section
      Appendices/           <- one folder per appendix
      Tactics/              <- helper tactics, simpsets
  tests/
    sanity/                 <- minimal builds, no sorry, imports
    unit/                   <- unit tests for definitions/lemmas
  scripts/
    run_task.sh             <- wrapper to run a single task end-to-end
    verify.sh               <- build + lints + tests
  logs/
    agent.log               <- chronological agent actions
  .toolchain                <- pinned Lean toolchain
  lakefile.lean             <- Lake config
```

### Workflow Utilities

* `scripts/get_mathlib_cache.sh` downloads cached mathlib artifacts to speed up builds.
* `scripts/new_component.py` scaffolds Lean files and matching tests.
* `agents/prompts/verification_steps.txt` lists the standard verification sequence.

---

## Global Agent Contract

**Goal-directed loop** with explicit planning, stepwise execution, and verification gates.

### High-Level State Machine

States: `init -> plan -> select_task -> prepare -> implement -> verify -> reflect -> (done|select_task)`

* **init**: load `plan.yaml` (or generate if missing), load `progress.json`, load `hypothesis.md`, load `inabottle.txt`.
* **plan**: ensure a complete task DAG with dependencies and acceptance criteria.
* **select\_task**: choose next `ready` task (all dependencies completed).
* **prepare**: create file stubs, imports, and test scaffold.
* **implement**: write Lean code and proofs incrementally.
* **verify**: run `scripts/verify.sh`; must pass build, lints, and tests.
* **reflect**: if verification fails, log diagnostics, refine plan, retry or split task. Make a suggestion for yourself in the next session as short term memory.
* **done**: finish when all tasks `completed`.

### Progress & Artifacts

* **No-`sorry` policy**: a task is only `completed` if there are zero `sorry` in changed files.
* **Artifacts**: code paths, test files, proof sketches (plaintext), and build logs recorded under `progress.json` and `logs/`.

---

## Data Schemas

### plan.yaml (authoritative plan)

```yaml
version: 1
meta:
  thesis_ref: "sections 9–10, appendices C, G, H"
  maintained_by: "agent"
  defaults:
    owner: "agent"
    reviewers: ["author"]
    acceptance_gates: ["build", "no_sorry", "linters", "tests"]

components:
  - id: core-measure-topology
    title: Core measure and topology foundations
    kind: foundation
    inputs: []
    outputs: ["Lean namespaces for measures, weighted L2, Sobolev traces"]
    deps: []
    acceptance:
      - "imports compile"
      - "trace inequality stubs present"

  - id: A-hardy-trace
    title: Hardy–trace inequality with theta-weight
    kind: lemma
    section: "Appendix A / Section 10"
    statement_file: "lean/Thesis/Appendices/A/HardyTrace.lean"
    proof_file: "lean/Thesis/Appendices/A/HardyTrace.lean"
    deps: ["core-measure-topology"]
    acceptance:
      - "theorem HardyTrace_weighted: holds"
      - "extremal sequence lemma proved"
      - "boundary trace corollary proved"

  - id: B-polarization-analytic
    title: Polarization limits, truncation independence, analyticity (Montel + Morera)
    kind: lemma
    section: "Section 9"
    statement_file: "lean/Thesis/Sections/S9/Polarization.lean"
    proof_file: "lean/Thesis/Sections/S9/Polarization.lean"
    deps: ["core-measure-topology"]
    acceptance:
      - "exists_limit_truncation : holds"
      - "is_holomorphic_on_strip : holds"

  - id: C-operator-H
    title: Construction of H, log-gauge, self-adjointness, Weyl classification
    kind: operator
    section: "Appendix G / Section 10"
    statement_file: "lean/Thesis/Appendices/G/OperatorH.lean"
    proof_file: "lean/Thesis/Appendices/G/OperatorH.lean"
    deps: ["core-measure-topology"]
    acceptance:
      - "H_is_selfAdjoint : holds"
      - "boundary_classification : holds"

  - id: D-DN-herglotz
    title: Dirichlet-to-Neumann map is Herglotz via resolvent representation
    kind: lemma
    section: "Appendix G"
    statement_file: "lean/Thesis/Appendices/G/DNMap.lean"
    proof_file: "lean/Thesis/Appendices/G/DNMap.lean"
    deps: ["C-operator-H"]
    acceptance:
      - "m_is_herglotz : holds"

  - id: E-m-equals-C
    title: Identification m(λ) = (s − 1/2) C(s)
    kind: lemma
    section: "Appendix G/H"
    statement_file: "lean/Thesis/Appendices/G/BoundaryMismatch.lean"
    proof_file: "lean/Thesis/Appendices/G/BoundaryMismatch.lean"
    deps: ["D-DN-herglotz", "F-far-boundary-vanish"]
    acceptance:
      - "m_eq_C : holds"

  - id: F-far-boundary-vanish
    title: Far-boundary vanishing via Sobolev trace and Agmon
    kind: lemma
    section: "Appendix H"
    statement_file: "lean/Thesis/Appendices/H/FarBoundary.lean"
    proof_file: "lean/Thesis/Appendices/H/FarBoundary.lean"
    deps: ["core-measure-topology"]
    acceptance:
      - "far_boundary_zero : holds"

  - id: G-uniform-remainder
    title: Uniform remainder bound (strip shift, Paley–Wiener style)
    kind: lemma
    section: "Appendix C"
    statement_file: "lean/Thesis/Appendices/C/Remainder.lean"
    proof_file: "lean/Thesis/Appendices/C/Remainder.lean"
    deps: ["core-measure-topology"]
    acceptance:
      - "remainder_exp_decay : holds for σ ∈ [σ₁, σ₂]"

  - id: H-boundary-trace-limit
    title: Boundary trace limit in the quadratic-form domain
    kind: corollary
    section: "Appendix A / Section 4"
    statement_file: "lean/Thesis/Sections/S4/BoundaryTrace.lean"
    proof_file: "lean/Thesis/Sections/S4/BoundaryTrace.lean"
    deps: ["A-hardy-trace"]
    acceptance:
      - "boundary_trace_limit : holds"
```

### progress.json (live status)

```json
{
  "version": 1,
  "started_at": null,
  "updated_at": null,
  "tasks": {
    "A-hardy-trace": {"status": "todo", "attempts": 0, "artifacts": []},
    "B-polarization-analytic": {"status": "todo", "attempts": 0, "artifacts": []},
    "C-operator-H": {"status": "todo", "attempts": 0, "artifacts": []},
    "D-DN-herglotz": {"status": "todo", "attempts": 0, "artifacts": []},
    "E-m-equals-C": {"status": "blocked", "blocked_on": ["D-DN-herglotz", "F-far-boundary-vanish"]},
    "F-far-boundary-vanish": {"status": "todo", "attempts": 0},
    "G-uniform-remainder": {"status": "todo", "attempts": 0},
    "H-boundary-trace-limit": {"status": "todo", "attempts": 0}
  }
}
```

---

## Agent Prompts

### System Prompt (prompts/system.txt)

You are an autonomous coding agent using OpenAI Codex (o3-coding variant). Your job is to write Lean 4 code and proofs that compile without errors, without any `sorry`. You must:

* Work on a single task at a time from `plan.yaml`.
* Respect dependencies; do not modify unrelated files.
* After each change, run the verification pipeline and act on failures.
* Prefer small, composable lemmas with clear names and docstrings.
* Leave comprehensive comments explaining definitions and proof strategy.
* Update `progress.json` and append to `logs/agent.log`.

### Developer Prompt (prompts/developer.txt)

Repository layout and conventions:

* Definitions in `lean/Thesis/Core` and then import into Sections/Appendices.
* Use mathlib where possible; avoid reinventing standard constructs.
* For new concepts, create minimal APIs (def + simp lemmas + coercions if needed).
* Keep lemmas local to their namespace; expose only necessary facts.
* Tactic budget: prefer `simp`, `rw`, `linarith`, `nlinarith`, `measure_theory` lemmas; fallback to `by_cases`, `apply`, `refine`. Avoid brittle `omega` style.

### Per-Task Prompt Template (prompts/task\_template.txt)

Task ID: {task\_id}
Title: {title}
Section: {section}
Goal: Implement the Lean formal statement and complete the proof(s) that pass the acceptance gates.
Dependencies: {deps}
Acceptance criteria: {acceptance}

Inputs:

* Relevant math definitions (point to existing files)
* Previous lemmas
* Precise English statement from the thesis text

Output files:

* {statement\_file}
* {proof\_file}

Process:

1. Analyze the English statement; produce a plan (comments at file top).
2. Create or extend definitions, with docstrings.
3. Write lemma statements; stub proofs with `by` skeletons; then complete proofs.
4. Add unit tests in `tests/unit/` if applicable.
5. Run verification and iterate until all gates pass.

Reflection:

* If a proof stalls for N>3 attempts, split the lemma or generalize a helper lemma.
* Log all decisions (what worked, what failed) in `logs/agent.log`.

---

## Verification Pipeline

* **Build**: `lake build`
* **No sorry**: ensure `grep -R "sorry" lean/` returns empty.
* **Linters**: run mathlib linters (naming, simpNF if available).
* **Tests**: run `scripts/verify.sh` to orchestrate build and unit tests.

Example `scripts/verify.sh` skeleton:

```
#!/usr/bin/env bash
set -euo pipefail
lake build
if grep -R "\bsorry\b" lean/; then echo "ERROR: sorry found"; exit 1; fi
# place mathlib linters here, if integrated
# run unit tests (if using Lake test runner)
```

---

## Execution Playbook (per task)

1. **Load plan**: select the `ready` task with smallest depth in DAG.
2. **Prepare stubs**: create namespaces, imports, and placeholder docstrings.
3. **Implement**: write defs and lemmas. Keep proofs structured; prefer `calc` and small helper lemmas.
4. **Self-check**: compile incrementally; keep diffs small.
5. **Verify**: run pipeline. If failure, go to Reflect.
6. **Reflect**: analyze error; add or split helper lemmas; update `plan.yaml` if the task should branch.
7. **Finalize**: on success, set task `completed`, update `progress.json` and write a brief proof summary in comments.

---

## Sub-Component Inventory (from the thesis)

Use these IDs to instantiate one piece at a time.

* **A-hardy-trace**

  * Defs: weighted L2 on (0,1), θ-weight φ, boundary trace functional, I(f), B(f)
  * Lemmas: HardyTrace\_weighted, ExtremalSequence\_exists, BoundaryTrace\_vanish
  * Acceptance: compiles, zero sorry, unit tests for model weight and small-perturbation φ

* **B-polarization-analytic**

  * Defs: truncated forms q₁⟨·,·⟩\_{ε,R}; kernels g(t,s), k\_s
  * Lemmas: exists\_limit\_truncation, is\_holomorphic\_on\_strip (Montel + Morera)

* **C-operator-H**

  * Defs: unitary log-gauge U, first-order operator A = ∂\_x + W, H = A\* A + I
  * Lemmas: H\_is\_selfAdjoint, boundary\_classification (limit-point/limit-circle)

* **D-DN-herglotz**

  * Defs: DN map m(λ) via boundary data; resolvent pairing
  * Lemmas: m\_is\_herglotz (analyticity, symmetry, positivity of imaginary part)

* **E-m-equals-C**

  * Defs: compensated boundary functional C(s)
  * Lemmas: m\_eq\_C via Green’s identity and boundary bookkeeping

* **F-far-boundary-vanish**

  * Defs: Sobolev trace on \[X−1, X], Agmon-weighted energy
  * Lemmas: trace\_one\_dim, agmon\_decay, far\_boundary\_zero

* **G-uniform-remainder**

  * Defs: log-line kernels F±, strip analyticity width a, shift
  * Lemmas: kernel\_L1\_uniform\_sigma, paley\_wiener\_shift, remainder\_exp\_decay

* **H-boundary-trace-limit**

  * Lemmas: boundary\_trace\_limit (in form domain)

---

## File Skeletons (stubs the agent should generate)

Example: `lean/Thesis/Appendices/A/HardyTrace.lean`

```
/--
  Weighted Hardy–trace inequality at t = 0 with theta-weight φ.
  Provides: HardyTrace_weighted, ExtremalSequence_exists, BoundaryTrace_vanish.
  Strategy: model identity at φ₀; stability to φ; extremal sequence on shrinking log-interval.
-/
import Mathlib

namespace Thesis.Appendices.A

-- TODO: definitions for φ, I(f), B(f), function spaces, and core domain.
-- TODO: main theorem: HardyTrace_weighted
-- TODO: extremal sequence lemma and boundary trace corollary

end Thesis.Appendices.A
```

The same pattern applies to all components; each file begins with a docstring summarizing goal, dependencies, and proof sketch.

---

## Checklists

### Per-Task Checklist

* [ ] Dependencies completed
* [ ] File(s) created with docstrings
* [ ] Statements fully formalized
* [ ] Proofs complete (no sorry)
* [ ] `lake build` passes
* [ ] Linters pass
* [ ] Unit tests added and passing
* [ ] `progress.json` updated

### Global Completion Checklist

* [ ] All components status = `completed`
* [ ] `scripts/verify.sh` passes on clean checkout
* [ ] No `sorry` anywhere under `lean/`
* [ ] Summary report added to `agents/agents.md`

---

## Instantiation Examples

### Run one component (shell)

```
./scripts/run_task.sh A-hardy-trace
```

The script should:

1. Fill the task template into prompts.
2. Invoke the agent with those prompts.
3. Write files, run verification, iterate on failures (bounded retries).
4. Update `progress.json` and append to `logs/agent.log`.

### Minimal `run_task.sh` sketch

```
#!/usr/bin/env bash
set -euo pipefail
TASK=${1:?"task id required"}
# 1) render prompts from plan.yaml and task_template.txt
# 2) call agent (external orchestrator) with rendered prompts
# 3) on success, run scripts/verify.sh and update progress.json
```

---

## Guardrails & Quality

* Zero-`sorry` policy; incremental compile.
* Prefer small helper lemmas with targeted `simp` tags; add `@[simp]` judiciously.
* Comment every nontrivial proof with 2–4 lines describing the idea.
* Do not introduce global simp loops; test simp sets locally.
* Namespacing: `Thesis.Sections.S9`, `Thesis.Appendices.G`, etc.

---

## Extension Hooks

* Add new components by appending to `plan.yaml` and creating files.
* Use `blocked` status in `progress.json` for tasks with unmet deps.
* Plug in additional test runners if needed.

---

## Final Notes

This spec pre-conditions the agent to plan, track, and execute Lean formalization tasks one-by-one. Start by pinning the Lean toolchain, creating `plan.yaml` and `progress.json`, and running a single task such as `A-hardy-trace`. Iterate until all components are `completed`.
