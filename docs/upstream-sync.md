# Syncing Your Fork With Course Updates

Use this flow whenever new commits are pushed to the original course repo.

## 1) Fetch latest upstream changes

```bash
git fetch upstream
```

## 2) Update your local `main`

```bash
git checkout main
git merge --ff-only upstream/main
```

## 3) Push updated `main` to your fork

```bash
git push origin main
```

## 4) Rebase your feature branch (if you are on one)

```bash
git checkout <your-branch>
git rebase main
```

If rebase conflicts happen, resolve them, then continue:

```bash
git add <resolved-files>
git rebase --continue
```
