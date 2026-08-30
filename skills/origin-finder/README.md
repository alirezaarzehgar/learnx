# Origin Finder Skill

**Discover and profile the people behind tools, frameworks, and projects.**

A Claude skill for comprehensive research into who created, maintains, and significantly contributed to any technology. Perfect for technical due diligence, understanding project origins, and professional networking.

## What It Does

Origin Finder guides you through a structured research workflow to:
- ✅ Identify project creators and maintainers
- ✅ Extract GitHub contributions and activity patterns
- ✅ Build detailed profiles (background, career, education)
- ✅ Find contact information (email, social accounts)
- ✅ Assess project governance and health
- ✅ Understand the network behind a technology

Perfect for: _before learning a framework, vet the creators. Before adopting a tool, understand who maintains it._

## Installation

### Where to Place the Skill

The `origin-finder` folder should go in your Claude skills directory:

**For Claude Desktop on macOS:**
```
~/Library/Application Support/Claude/skills/
```

**For Claude Desktop on Windows:**
```
%AppData%\Claude\skills\
```

**For Claude Desktop on Linux:**
```
~/.config/Claude/skills/
```

**For Cowork (if available):**
```
Project root: /skills/
```

### Installation Steps

1. **Download or clone this directory:**
   ```bash
   # If you have the zip file
   unzip origin-finder.zip
   
   # Or if you're cloning
   git clone <skill-repo-url>
   ```

2. **Copy to your skills folder:**
   ```bash
   # macOS/Linux
   cp -r origin-finder ~/Library/Application\ Support/Claude/skills/
   # or
   cp -r origin-finder ~/.config/Claude/skills/
   
   # Windows (PowerShell)
   Copy-Item -Recurse origin-finder "$env:AppData\Claude\skills\"
   ```

3. **Restart Claude** — The skill will load automatically

4. **Verify installation** — In Claude, you should see "origin-finder" in available skills

### Directory Structure

```
origin-finder/
├── SKILL.md                          # Main skill instructions
├── README.md                          # This file
├── scripts/
│   ├── github_profiler.py             # Automated GitHub contributor extraction
│   └── profile_scraper.py             # (Coming) Multi-source profile aggregation
└── references/
    ├── finding-emails.md              # Email discovery guide
    ├── github-advanced-search.md      # GitHub query syntax
    └── social-media-signals.md        # Reading between the lines on social
```

## Quick Start

### Manual Research (No Automation)

1. **Tell Claude:** "I want to learn X. Can you help me find who created it?"
2. Claude triggers this skill and guides you through:
   - Finding the official repository
   - Identifying key maintainers
   - Building profiles on each person
   - Finding contact information

### Automated Research (with Python script)

If you use Claude Code, you can automate GitHub contributor extraction:

```bash
# Extract top 10 contributors from NATS
python3 scripts/github_profiler.py nats-io/nats-server --top 10 --format md

# Export to markdown file
python3 scripts/github_profiler.py redis/redis --top 15 --output contributors.md

# JSON format for further processing
python3 scripts/github_profiler.py owner/repo --format json --output data.json
```

**Requirements:**
- Python 3.7+
- `requests` library (`pip install requests`)
- Optional: GitHub API token for higher rate limits (set `GITHUB_TOKEN` env var)

## Usage Examples

### Example 1: Learning NATS.io

**You ask:** "Before I learn NATS, I want to understand who built it. Can you help me discover the people behind NATS.io?"

**Claude does:**
1. Goes to github.com/nats-io/nats-server
2. Extracts top contributors
3. Profiles each person (Derek Collison, Luc Perkins, etc.)
4. Finds their current roles at Synadia
5. Discovers their social media and websites
6. Maps their contributions and influence

**Output:** Detailed profiles showing creators, maintainers, their backgrounds, and how to contact them

### Example 2: Evaluating a Tool

**You ask:** "I'm considering adopting this library. Can you profile the maintainers so I can assess project health?"

**Claude does:**
1. Searches for the project
2. Identifies primary maintainers
3. Checks: Are they employed? Do they respond to issues? How long active?
4. Assesses: Is there a succession plan? Corporate backing?
5. Finds: Can I contact them directly?

**Output:** Risk assessment and maintainer health report

### Example 3: Professional Networking

**You ask:** "I'm interested in Rust ecosystems. Can you find the major contributors to Tokio and their connections?"

**Claude does:**
1. Maps Tokio contributors (Tokio-RS organization)
2. Identifies most influential people
3. Shows their other projects and connections
4. Finds speaking history and blogs
5. Maps the broader Rust ecosystem network

**Output:** Networking roadmap with key people to follow

## Tips for Best Results

### 🎯 Be Specific
- ✅ "Who created NATS.io and who maintains it today?"
- ✅ "Can you profile the top 5 Kubernetes maintainers?"
- ❌ "Tell me about this tool" (too vague)

### ⏰ Set Scope
- ✅ "Find me the top 3 contributors and their contact info"
- ❌ "Profile everyone ever involved" (overkill)

### 🔗 Provide Context
- ✅ "I'm considering adopting this for production. Tell me about the maintainers."
- ✅ "I want to contribute to this project. Who should I follow?"

### 🚀 Combine Skills
- Use this with other skills for research (web search, document creation)
- Export results to markdown for sharing
- Feed findings into project evaluation documents

## Advanced Features

### Automation with Claude Code

The included Python scripts can:
- Extract contributors from any GitHub repo
- Build profiles from multiple sources
- Export as markdown or JSON
- Generate comparison reports
- Track contributor activity over time

See `scripts/github_profiler.py` for usage.

### Research Checklist

The skill includes a complete research checklist to ensure you don't miss anything. Use it when doing thorough profiling.

### Email Finding Guide

See `references/finding-emails.md` for 10+ techniques to find email addresses of project maintainers.

## Limitations & Ethical Use

### What This Skill Does
- ✅ Public GitHub data
- ✅ Official project websites
- ✅ Public social media profiles
- ✅ Professional networks (LinkedIn)
- ✅ Public interviews and talks

### What This Skill Doesn't Do
- ❌ Scrape private data
- ❌ Bypass privacy settings
- ❌ Find unlisted contact info
- ❌ Violate terms of service
- ❌ Collect data for spam/harassment

### Ethical Guidelines
- **Respect privacy:** If someone hides their email, that's intentional
- **Use appropriately:** Reach out professionally, not for sales spam
- **Follow ToS:** Don't violate GitHub, LinkedIn, or Twitter terms
- **Protect data:** Keep gathered emails confidential
- **Be transparent:** Explain why you're contacting someone

## Troubleshooting

### Skill doesn't appear
- Restart Claude (must be completely closed and reopened)
- Check folder is in correct location (see "Where to Place the Skill" above)
- Verify `SKILL.md` exists in `origin-finder/` folder

### Python script fails
```bash
# Install requirements
pip install requests

# Set GitHub token for higher limits
export GITHUB_TOKEN=your_token_here

# Run with verbose output
python3 scripts/github_profiler.py --help
```

### Can't find someone's email
- See `references/finding-emails.md` for systematic approaches
- Some people intentionally don't publish emails
- Try company domain + common patterns
- Use GitHub issues/discussions as contact method

## Customization

You can customize this skill by:
- Adding your own research templates
- Extending the Python scripts
- Creating automation workflows in Claude Code
- Adding reference documents for your use case

Just edit `SKILL.md` directly or add files to `references/` and `scripts/`.

## Contributing Improvements

This skill is designed to evolve. Suggestions:
- New email-finding techniques
- Additional script examples
- Better social media signal reading
- Automation templates for common scenarios

## Support

For issues or questions:
1. Check the README and reference guides
2. Review the research checklist in SKILL.md
3. Refer to script help: `python3 scripts/github_profiler.py --help`
4. Try manual research workflow first (always works)

## License

This skill is provided as-is for research and professional use.

---

**Ready to discover who's behind X?** Start by asking Claude:

> _"I want to learn about [tool/framework]. Can you help me find and profile the people who created it?"_
