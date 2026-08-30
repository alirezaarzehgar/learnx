---
name: origin-finder
description: Discover and profile the people behind tools, frameworks, and projects before learning them. Use this skill whenever the user wants to learn about who created, maintains, or significantly contributed to a tool, library, framework, or technology — find creators, maintainers, contributors, their backgrounds, career history, social presence, and contact information. Trigger whenever you see phrases like "who built X", "creator of X", "who's behind X", "people behind this project", "before learning X let me research who made it", or when the user expresses curiosity about the origin story or people responsible for a technology. This is especially useful in Claude Code workflows when researching dependencies, evaluating tools, or understanding project origins.
---

# Origin Finder: Discover Who's Behind X

A comprehensive guide to researching and profiling the people who created, maintain, or significantly contributed to any tool, framework, project, or technology. Before diving deep into learning something, understand the humans and organizations behind it.

## When to Use This Skill

✓ **Starting a new technical learning journey** — Before investing time in a framework, find who built it and why  
✓ **Evaluating tools and libraries** — Assess maintainer credibility, community health, and backing  
✓ **Understanding project origins** — Discover the motivation, founding story, and key decision-makers  
✓ **Professional networking** — Connect with domain experts and influential contributors  
✓ **Due diligence research** — Vet the team behind open-source projects or technical products  
✓ **Finding collaborators** — Identify the right people to learn from or partner with  

## Research Workflow

The process follows a structured path, typically in this order:

### 1. Identify the Project & Organization

Start with basic reconnaissance:

- **Official repository** (GitHub, GitLab, Gitea) or project website
- **Maintaining organization** (if different from individual creator)
- **Primary language/ecosystem** (enables targeted searches)
- **Project age** (founding date, project maturity)
- **License type** (tells you about project philosophy)

Search tactics:
```
"project name" site:github.com
"project name" creator OR founder
site:github.com/[org-name]
```

### 2. Extract Maintainers & Key Contributors

From GitHub/repository:
- **Primary maintainer(s)** — Who owns the project? Check repo settings and git log
- **Core contributors** — Top 5-10 by commit count (shows sustained involvement)
- **Recent activity** — Who's actually maintaining it now? (last 6 months commits)
- **Profile links** — Each contributor's GitHub profile with bio and linked accounts
- **Issue/PR responses** — Who answers questions? Who merges changes?

From project site/documentation:
- **Founders/creators section** — Often listed in About, Team, or Credits pages
- **Founding story** — Blog posts, historical README, press releases
- **Current leadership** — Who makes architectural decisions?
- **CONTRIBUTORS file** — Many projects maintain a contributors list

### 3. Deep Dive: For Each Key Person

Build a comprehensive profile containing these sections:

#### Contact & Social
- Full email address (search GitHub commits, official site, domain patterns)
- Twitter/X handle and follower count
- LinkedIn profile URL
- Personal website or blog
- GitHub profile URL
- Mastodon, Bluesky, Threads, or other social accounts
- Mailing list subscriptions or newsletter

#### Background & Education
- Full name and common aliases/nicknames
- Educational institutions (universities, bootcamps, online courses)
- Graduation years/programs and fields of study
- Notable scholarships, awards, or academic achievements
- Geographic background (city, country)

#### Career History
- Complete employment timeline with dates
- Previous companies, roles, and responsibilities
- Notable projects outside this main one
- Any freelance or consulting work
- Founding of other startups or projects
- Corporate affiliations or board positions

#### Current Situation (Most Important)
- Current position and company
- Active projects and involvements
- Consulting or advisory roles
- Teaching, mentorship, or speaking activities
- Recent publications, blog posts, or talks
- Known collaborators and close colleagues

#### Influence & Credibility
- Follower counts across platforms
- Contribution patterns (sustained multi-year involvement vs sporadic)
- Response rate to issues/PRs (community perception)
- Community reputation and respect level
- Other major projects led or co-founded
- Speaking history (conferences, podcasts, panels)

## Research Sources & Techniques

### Primary Sources (Most Reliable) 🟢

1. **GitHub profile**
   - Official profile page shows: bio, location, company, website
   - Contribution graph reveals activity patterns
   - Pinned repositories show priorities
   - Follow list shows their interests
   - Check "Contributions" tab for all activity (not just commits)

2. **Official project documentation**
   - README files (often mention creators)
   - CONTRIBUTING.md (has team/maintainer info)
   - HISTORY.md or CHANGELOG (founding context)
   - About pages on official websites
   - Team/Authors pages

3. **Project website and blog**
   - /team or /about sections
   - Historical blog posts about founding
   - Announcement posts (often signed by founders)
   - Press releases
   - Founding story narratives

4. **LinkedIn**
   - Complete career history with dates
   - Education section
   - Endorsements and skills
   - Recommendations from colleagues
   - Current company and position
   - Groups and associations

5. **Personal website or portfolio**
   - Direct information from the person
   - Projects they highlight
   - Interests and expertise areas
   - Contact information
   - Speaking engagements

6. **Author pages on dev platforms**
   - Medium, Dev.to, Hashnode bios
   - Substack subscriber pages
   - YouTube channel About sections
   - Newsletter headers with author info

### Secondary Sources (Contextual) 🟡

7. **Twitter/X and social media**
   - Follow patterns reveal interests
   - Pinned posts often have important info
   - Recent activity shows current focus
   - Mentioned connections (collaborators)
   - Retweets reveal their network
   - Search "[name] works at" tweets

8. **Company websites**
   - Employee bios and team pages
   - Press releases about new hires
   - Company blog posts (employee spotlights)
   - Organizational charts or team structures
   - LinkedIn company page employee lists

9. **Conference speaker listings**
   - PyCon, JSConf, RustConf, etc.
   - Speaker bios usually public with contact info
   - Talk descriptions reveal expertise
   - Event websites archive past speakers
   - Conference proceedings often have author info

10. **Interview archives**
    - Tech podcasts (e.g., Software Engineering Daily, Syntax)
    - Interview recordings with timestamps
    - Blog interviews and Q&As
    - YouTube interviews and talks
    - Conference talk recordings

11. **Academic profiles** (if applicable)
    - Google Scholar profiles
    - ResearchGate accounts
    - University faculty pages
    - Published research papers
    - Academic citations

12. **Open source contribution graphs**
    - Reveals coding patterns and commitment
    - Shows active periods vs quiet periods
    - Demonstrates breadth of interests
    - Tools like GitHub Archive show historical data

### Specialized Search Techniques 🔍

**GitHub advanced search:**
```
author:username project_name
repo:owner/repo author:username
"name" path:profile type:user
commits-by:username repo:owner/repo
```

**Google dorking:**
```
site:github.com/[person] [project name]
site:linkedin.com "[person name]"
"[name]" "[project]" interview OR talk OR podcast
"[name]" email [company domain]
```

**Social media cross-reference:**
```
"[name]" "[project]" site:twitter.com
"[name]" "[company]" site:linkedin.com
"[name]" about.me OR linktree
```

**Email finding patterns:**
- Check GitHub commit emails: `git log --all --format=%aE | sort -u`
- Try common company patterns: firstname@company.com, fname@domain.com, f.lastname@domain.com
- Search "[name] email contact" in quotes
- Check project CONTRIBUTING.md for maintainer emails
- Look at issue/PR signatures for email traces

**Company research:**
```
"[company name]" employees OR team
site:[company domain] [person name]
"[company name]" "[person name]" announcement OR hired
```

## Output Format

For each person discovered, organize findings using this standardized template:

```markdown
## [Full Name]

**Role in Project:** Creator / Co-founder / Lead Maintainer / Core Contributor  
**Involvement Duration:** [Start Year] – Present / [Start Year] – [End Year]  
**GitHub Contribution:** [X commits] (top X% of project)

### Current Position
- **Title:** [Job Title]
- **Company:** [Company Name]  
- **Location:** [City/Region]

### Contact Information
- **Email:** [primary@email.com]
- **GitHub:** [@github_handle](https://github.com/username)
- **Twitter:** [@twitter_handle](https://twitter.com/handle)
- **LinkedIn:** [linkedin.com/in/profile](https://linkedin.com/in/profile)
- **Website:** [personal-site.com](https://personal-site.com)
- **Other:** [Mastodon, Bluesky, or other platforms]

### Background & Education
- **Full Name Variations:** [Aliases, nicknames]
- **Education:** 
  - [University Name], [Degree], [Year]
  - [Other educational background]
- **Known As:** [How recognized in community — "The X expert", "Creator of Y"]

### Career Timeline
- **[Year-Year]:** [Company/Role] — [Key achievements]
- **[Year-Year]:** [Company/Role] — [Key achievements]
- **[Year-Present]:** [Current role] — [Current focus]

### Contributions to [Project Name]
- **Activity Status:** Active / Maintained / Historical contributor
- **Commit Count:** [X commits] out of [Total] ([X%])
- **Key Contributions:** [Major features, areas, or systems they own]
- **Issue Response:** [Pattern — e.g., "Responds within 48 hours", "Triages weekly"]
- **Community Role:** [E.g., "Breaks ties on design decisions", "Onboards new contributors"]

### Influence & Network
- **Platform Followers:**
  - Twitter: [X followers]
  - GitHub: [X followers]
  - LinkedIn: [X connections]
- **Known Close Collaborators:** [Other notable people in project/team]
- **Mentors/Mentees:** [If known]

### Additional Context
- **Notable Talks:** 
  - [Title] @ [Conference/Event], [Year]
  - [Link to video if available]
- **Blog/Publications:**
  - [Recent post title] ([Link], [Date])
  - [Book or major publication]
- **Other Major Projects:** [Worth knowing about]
- **Reputation:** [How they're viewed in community — reliable, visionary, etc.]
- **Last Seen:** [Most recent activity date and type]
```

## Pro Tips for Effective Research

### 🎯 Start Narrow, Expand Carefully
- Begin with GitHub's auto-populated "Contributors" tab
- Filter by sustained involvement: multiple years OR 100+ commits
- Don't profile every casual contributor unless specifically needed
- Focus on decision-makers first (project owners, lead maintainers)

### 🔗 Connect the Dots
- Cross-reference names across platforms (people use consistent handles)
- Follow LinkedIn connection chains to find teams
- Check company org pages for related team members
- Look for mentions in project issues/discussions ("thanks to X for...")
- Use GitHub's "Follows" relationships to map influence networks

### ⏰ Assess Recency (Critical)
- Last commit date matters — active vs abandoned/legacy?
- Recent tweets/activity shows current interests
- Job changes indicate shifting focus or availability
- Company layoffs might explain reduced maintenance
- Check: Are they still employed? Still interested in this project?

### 🚩 Red Flags & Green Flags

**Green Flags** ✅
- Consistent activity over multiple years
- Responsive to community (answers issues promptly)
- Clear communication style
- Multiple successful projects
- Known speaker/educator
- Community respect

**Red Flags** ⚠️
- Single-person project with no succession plan
- No response to critical issues for months
- Abandoned projects
- No public contact information
- Inconsistent or hostile communication
- No clear maintenance roadmap

**Questions to Answer:**
- Is there a funding model? (Solo hobby, VC-backed, sponsored, corporate)
- Are there co-maintainers? (Bus factor — what if they leave?)
- Is there a clear contributor onboarding? (Project health indicator)

### 📧 Finding Email Addresses (Detailed)

**GitHub commit history** (most reliable):
```bash
git clone [repo]
cd [repo]
git log --all --format=%aE | grep "name" | sort -u
```

**Common domain patterns:**
- firstname@company.com
- f.lastname@company.com
- flastname@company.com
- firstnamelastname@company.com
- For startups: firstname@startup.io or similar

**Where to look:**
- Project files: CONTRIBUTING.md, MAINTAINERS.md, AUTHORS
- GitHub contributor list pages (sometimes emails visible)
- Comments on their own issues/PRs
- Older GitHub profiles (sometimes listed email before privacy settings)
- Company employee directories
- Conference speaker pages

**Social engineering (ethical):**
- Search "[name] email" on Google
- Search "[name] [company]" on LinkedIn
- Check if they have a newsletter (email visible in signup)
- Look for "contact" pages on personal websites

## Integration with Claude Code

When using this skill in **Claude Code**, automate the research process:

**Python script example** — See `scripts/github_profiler.py` for automated contributor extraction from any GitHub project.

**What you can automate:**
- GitHub API queries to extract all contributors
- Email finding from commit history
- Social account discovery
- Timeline generation from career data
- Influence metrics calculation
- Markdown report generation

**Typical workflow:**
1. User provides project URL
2. Script fetches top 10 contributors
3. Cross-reference each on GitHub, LinkedIn, Twitter
4. Generate structured profiles
5. Export as markdown or interactive dashboard

## Research Checklist

Use this checklist to ensure thorough research:

- [ ] Found main project repository/website
- [ ] Identified primary creator/founder(s)
- [ ] Listed top 5-10 contributors with commit counts
- [ ] Verified current maintainer(s)
- [ ] Checked GitHub profiles for linked accounts
- [ ] Researched background (education, previous roles)
- [ ] Found current position, title, and company
- [ ] Located email address (or reasonable alternative contact)
- [ ] Found social media handles (Twitter, LinkedIn, personal site)
- [ ] Reviewed recent activity (commits, posts, talks, interviews)
- [ ] Documented project governance model
- [ ] Assessed maintenance plan and succession strategy
- [ ] Identified other projects by key people
- [ ] Evaluated project health and funding model
- [ ] Created profiles for 3-5 key people minimum

## Example: NATS.io Deep Research

**Target:** Understand who built NATS and who maintains it today.

**Step 1: Identify**
- Project: NATS.io (message broker/pub-sub system)
- Repository: github.com/nats-io/nats-server
- Organization: Synadia (backing company, synadia.com)
- Language: Go, with clients in many languages

**Step 2: Extract on GitHub**
- Go to github.com/nats-io → Contributors
- Sort by commits — top 5 people immediately visible
- Click each person's avatar → their GitHub profile
- Read their bios — look for linked accounts

**Step 3: For each top contributor:**
- What's their GitHub bio say? (Company, location, interests)
- Where do they work? (Click company link or search LinkedIn)
- What's their recent activity? (Last 6 months commits?)
- What other projects are they in? (Pinned repos)
- Any linked website or social? (Click the website link)

**Step 4: Go deeper on founders**
- Search "NATS Derek Collison" (common search pattern)
- Look for: early GitHub commits, blog posts about founding
- Read Synadia.com/about or /team page
- Search "Derek Collison LinkedIn" → full career history
- Search "Derek Collison" + "interview" → podcasts, talks
- Check Synadia.com for press releases (often mention key people)

**Step 5: Map the network**
- Who works together at Synadia?
- Who else contributes significantly?
- What's the geographic distribution?
- How many maintainers are there really?

**Output:** 3-5 detailed profiles + governance diagram

---

## Quick Start

**Next action:** 
1. Take the tool/framework/library you want to learn about
2. Go to GitHub (search for its official repository)
3. Click the "Contributors" tab
4. Start with the top 3 people by commit count
5. Follow the research workflow above

**Time estimate:** 
- Quick version (names + emails): 15-30 min
- Thorough version (full profiles): 45-90 min
- Deep dive (includes network analysis): 2-3 hours

---

## Additional Resources

For help with specific research areas, see the `references/` folder:
- `finding-emails.md` — Detailed email discovery techniques
- `github-advanced-search.md` — Advanced GitHub query syntax
- `social-media-signals.md` — Reading LinkedIn and Twitter for signals

For automation scripts, see `scripts/`:
- `github_profiler.py` — Extract contributor data from any GitHub repo
- `profile_scraper.py` — Build profiles from common data sources
