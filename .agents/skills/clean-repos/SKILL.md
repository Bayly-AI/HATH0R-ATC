---
name: clean-repos
description: Comprehensive standard operating procedure for cleaning repositories across the suite. Activates whenever the user says "clean repo", "clean repos", "clean repository", "clean repositories", or requests repository cleanup and branch hygiene.
---

# Clean Repositories Standard Operating Procedure

This workflow enforces complete repository hygiene, quality gates, documentation sync, PR lifecycle management, and branch cleanup across all repositories in the workspace or suite.

Whenever the user requests **"clean repo"** or **"clean repos"**, execute the following 13 steps in exact sequence:

---

## 13-Step Clean Repo Lifecycle

### Step 1: Capture All Repositories in the Project
- Discover all repositories in the current suite or project root (e.g. inspecting `cfg/suite.yaml` or listing git repositories in `/Users/raybayly/Development/Ray`).
- Ensure all downstream steps are systematically executed across **every** member repository.

### Step 2: Ensure All Changes Are Committed
- Run `git status -s` in each repository.
- If uncommitted modifications or untracked source files exist:
  - Verify that changes belong to source control.
  - Stage and commit with descriptive conventional commit messages (`feat:`, `fix:`, `chore:`).

### Step 3: Cleanup Development Artifacts
- Remove temporary OS artifacts (`.DS_Store`, `Thumbs.db`, `._*`).
- Remove testing, profiling, and coverage caches (`.pytest_cache`, `.coverage`, `coverage.xml`).
- Remove Python bytecode and build caches (`__pycache__`, `*.pyc`, `build/`, `dist/`, `*.egg-info`).
- Remove unneeded scratch scripts and temporary logs.
- Verify `.gitignore` is up to date to prevent re-committing artifacts.

### Step 4: Clean Up and Remove Stale Worktrees
- Check active git worktrees using `git worktree list`.
- Prune stale worktree references:
  ```bash
  git worktree prune
  ```
- Remove any unneeded detached or stale worktree directories.

### Step 5: Review Branches, Merge Changes, Resolve Conflicts & Ensure PRs Are Merged
- Query open Pull Requests using `gh pr list` and merge ready PRs (`gh pr merge --squash --delete-branch`).
- Fetch all remote branches (`git fetch --all --prune`).
- Checkout the canonical base branch (`development`, or `main`/`master` if `development` is absent) and pull latest (`git pull --rebase origin development`).
- Review every local and remote non-canonical branch (`feature/*`, `chore/*`, `fix/*`, `bugfix/*`, `enhancement/*`, `docs/*`, `claude/*`, `release/*`).
- For any branch that has unmerged commits (`git cherry development <branch>`):
  - Merge the branch into `development` (`git merge --no-edit <branch>`).
  - If merge conflicts occur, resolve them cleanly (`git merge --no-edit -X ours <branch>` or resolving tree conflicts while preserving new feature files) and commit the resolution.

### Step 6: Share Knowledge & Compound MemoryGraph (`CR-MEMORY-COMPOUND-001`)
- Update shared knowledge bases, indexing systems, and memory stores:
  - Ray-MCP / Hath0r-MCP knowledge roots.
  - Sync indexed data to `.hath0r/knowledgebase` single source of truth when applicable.
  - Compound clean-repo episode into `.hath0r/memory/graph.json`.

### Step 7: Update Documentation & AgentGraph Synchronization
- Ensure all recent features, API modifications, database schemas, and architectural changes are documented in:
  - `README.md`
  - `AGENTS.md`
  - `docs/` (playbooks, runbooks, architecture specs)
- Synchronize and validate AgentGraph state:
  ```bash
  hath0r agentgraph sync
  hath0r agentgraph validate
  ```
  Verify that 0 cycles and 0 contradictions exist before proceeding to commit.

### Step 8: Run Task Evaluation (`CR-TASK-EVAL-001`) & Commit Documentation / State Changes
- Run the 4-tier Task Evaluation (`hath0r evals run`) and synchronize SHA-256 file hashes (`hath0r memory hash --sync`).
- Stage any updated documentation, governance files, memory graphs, or evaluation artifacts and commit them cleanly:
  ```bash
  git add -A && git commit -m "docs: update documentation, evaluations, and knowledge sync [skip ci]"
  ```

### Step 9: Ensure All Changes Are PR'd or Merged into Base Branch
- If working on an active feature branch (`feature/*`) requiring PR review:
  - Push branch to remote: `git push -u origin <branch>`
  - Create Pull Request if one does not exist (`gh pr create --base development`).

### Step 10: Monitor PRs and Merge When Pass (Or Fix So It Does)
- Run status checks: `gh pr checks`
- If CI/CD checks fail:
  - Diagnose failure, apply fixes, run local tests (`pytest`, `npm test`), and push commits until green.
- Merge the PR once checks pass:
  ```bash
  gh pr merge --squash --delete-branch
  ```

### Step 11: Remove All Stale Feature Branches (Local & Remote)
- Delete all merged and stale non-canonical feature branches both locally and on `origin`:
  ```bash
  git branch -D <feature-branch>
  git push origin --delete <feature-branch> 2>/dev/null || true
  git fetch --prune
  ```

### Step 12: Switch Back to Development and Pull/Push Origin
- Switch back to `development` (or canonical base branch), pull with rebase, and push to `origin` so local and remote are 100% synchronized:
  ```bash
  git checkout development
  git pull --rebase origin development
  git push origin development
  ```
- Verify `git status` reports working tree is clean and `up to date with 'origin/development'`.

### Step 13: Verify Pre-Announce Gates & Announce Complete
- Verify `hath0r memory verify` and `hath0r evals verify` pass (`passed_gate: true`, `R_task >= 0.80`).
- Provide a structured status report confirming the clean status of all repositories, merged branches/PRs, resolved conflicts, deleted local/remote branches, and `origin/development` sync state.
