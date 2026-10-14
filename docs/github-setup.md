# TV2 — GitHub labels and milestones

Owner: Trần Quốc Huy — MSSV 25125053 — `tqhuy0602`.

The issue forms, PR template, and workflow guide are stored in Git. Labels and
milestones are GitHub repository settings and must be created separately.
The commands below are instructions; their presence does not mean the settings
have been created. No deadline has been entered; obtain due dates from LMS.

Run from this repository with GitHub CLI authenticated and repository write
access:

```bash
gh label create python-hw --color 0052CC --description "Individual Python exercises" --force
gh label create w1 --color C5DEF5 --description "Week 1" --force
gh label create w2 --color BFDADC --description "Week 2" --force
gh label create w3 --color D4C5F9 --description "Week 3" --force
gh label create team-hw --color 0E8A16 --description "Shared team assignments" --force
gh api 'repos/{owner}/{repo}/milestones?state=all' --jq '.[] | {title, number, state, due_on}'
```

Create only the milestones absent from the listing:

```bash
gh api --method POST 'repos/{owner}/{repo}/milestones' -f title=PY-W1
gh api --method POST 'repos/{owner}/{repo}/milestones' -f title=PY-W2
gh api --method POST 'repos/{owner}/{repo}/milestones' -f title=PY-W3
```

After confirming the LMS deadlines, set each milestone's due date in GitHub.
Use `python-hw` and the relevant week label for individual issues/PRs; use
`team-hw` and the relevant week label for team work. Assign the corresponding
`PY-W1`, `PY-W2`, or `PY-W3` milestone manually.

Verify the remote settings after creating them:

```bash
gh label list
gh api 'repos/{owner}/{repo}/milestones?state=all' --jq '.[] | {title, state, due_on}'
```
