# Installation Guide — Origin Finder Skill

**3-step installation. Takes 1 minute.**

## Step 1: Locate Your Skills Folder

Choose your platform:

### macOS
```bash
~/Library/Application Support/Claude/skills/
```

**Quick link:**
```bash
open ~/Library/Application\ Support/Claude/
```

### Windows
```
%AppData%\Claude\skills\
```

**In PowerShell:**
```powershell
explorer "$env:AppData\Claude\"
```

### Linux
```bash
~/.config/Claude/skills/
```

**Create if it doesn't exist:**
```bash
mkdir -p ~/.config/Claude/skills/
```

---

## Step 2: Place the Skill

Copy the entire `origin-finder/` folder into your skills directory.

**From terminal:**
```bash
# macOS/Linux
cp -r origin-finder ~/Library/Application\ Support/Claude/skills/
# or
cp -r origin-finder ~/.config/Claude/skills/

# Windows PowerShell
Copy-Item -Recurse origin-finder "$env:AppData\Claude\skills\"
```

**Expected structure after installation:**
```
skills/
└── origin-finder/
    ├── SKILL.md
    ├── README.md
    ├── INSTALL.md
    ├── scripts/
    │   └── github_profiler.py
    └── references/
        ├── finding-emails.md
        ├── github-advanced-search.md
        └── social-media-signals.md
```

---

## Step 3: Restart Claude

**Close and reopen Claude completely.**

- If using Claude Desktop app: ⌘Q (Mac) or close window (Windows/Linux)
- Then reopen the app

Wait 2-3 seconds for it to fully load.

---

## Verification ✓

**In Claude chat, try:**
```
I want to learn about Redis. Can you help me find who created it?
```

If Claude responds with the origin-finder workflow, installation is successful! ✅

---

## What You'll See

When the skill triggers, Claude will guide you through:
1. Finding the official repository
2. Identifying key maintainers
3. Building detailed profiles
4. Finding contact information
5. Assessing project health

## Troubleshooting

### Skill doesn't appear

**Check:**
- [ ] Folder is in correct location (see Step 1)
- [ ] Folder is named exactly `origin-finder`
- [ ] `SKILL.md` file exists inside the folder
- [ ] Claude is completely restarted (not just refreshed)

**Try:**
```bash
# Verify file structure
ls -la ~/Library/Application\ Support/Claude/skills/origin-finder/SKILL.md
```

### Python scripts don't work

The skill works without Python scripts. If you want automation:

```bash
# Install requirements
pip3 install requests

# Test script
python3 origin-finder/scripts/github_profiler.py --help
```

### Still stuck?

1. Delete and reinstall the folder
2. Check folder permissions (`chmod 755 origin-finder/`)
3. Restart your computer if issues persist

---

## Next Steps

**Once installed:**

1. **Read the full guide** — `README.md` in the skill folder
2. **Try an example** — Ask Claude about a project you want to research
3. **Automate (optional)** — Use `scripts/github_profiler.py` for batch research

**Quick start prompt:**
> Before I learn NATS, I want to understand who built it. Can you help me find and profile the people behind NATS.io?

---

## Uninstalling

To remove the skill:
```bash
# macOS/Linux
rm -rf ~/Library/Application\ Support/Claude/skills/origin-finder/

# Windows PowerShell
Remove-Item -Recurse "$env:AppData\Claude\skills\origin-finder"
```

Restart Claude. The skill will disappear.

---

**That's it! Enjoy discovering who's behind your favorite technologies.** 🚀

For full documentation, see `README.md` after installation.
