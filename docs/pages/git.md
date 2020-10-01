---
layout: default
---

# Git Issues

## Multiple Users Local Terminal
Need to remove git username and email from config, and delete credentials on computer:
- https://www.quora.com/Why-does-git-config-list-show-2-emails
- https://stackoverflow.com/questions/22844806/how-to-change-my-git-username-in-terminal

Edit the config file to reflect new email and name (use your username for name)
```
git config --global --edit 
```

Windows Search -> Credentials Manager -> Windows Credentials -> Generic Credentials -> `git.https://github.com` -> Remove

This will prompt git to make you login on your next push/pull.

---
