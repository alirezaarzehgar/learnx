# Finding Email Addresses

The most direct contact method, but often hidden behind privacy settings. This guide covers systematic approaches from most to least reliable.

## GitHub Commit History (Most Reliable)

### Clone and search locally
```bash
git clone https://github.com/owner/repo.git
cd repo
git log --all --format=%aE | sort -u
```

This reveals all email addresses associated with commits. You'll see patterns like:
- firstname@company.com
- firstname.lastname@company.com
- personal@domain.com

### Search GitHub's web interface
- Go to repository
- Click "Contributors"
- Click individual contributor
- Check their GitHub profile — sometimes older profiles still show email

### GitHub API
```bash
# Requires authentication
curl -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/repos/owner/repo/commits?author=username
```

## Official Project Sources

**CONTRIBUTING.md** — Often lists maintainer contact info
**MAINTAINERS file** — Sometimes includes email addresses
**Project website** — /team, /about, /contact pages
**Package metadata** — Many projects put maintainer email in package.json, setup.py, or Cargo.toml

Example from package.json:
```json
{
  "maintainers": [
    {"name": "John Doe", "email": "john@example.com"}
  ]
}
```

## Company Email Patterns

Once you know someone works at a company, try these patterns:

**Common formats:**
- firstname@company.com
- firstname.lastname@company.com
- flastname@company.com
- first_last@company.com
- fnames@company.com (rare)
- initial.lastname@company.com

**Verification tools:**
- Hunter.io (paid, checks real addresses)
- RocketReach (subscription)
- Email permutator scripts (generate patterns to test)

**Test addresses:**
- Send a benign email (calendar invite, etc.)
- Use email verification services
- Check email format against known employees

## Social Media & Public Sources

### LinkedIn
- **Most direct:** Personal email often visible in headline or About section
- Click through to website links (personal website often lists email)
- Check recommendations section (sometimes contains email)

### Twitter/X
- Check pinned tweet or profile header
- Look for links to personal website
- Email in profile verification

### Personal websites & blogs
- Contact page
- Footer information
- Author bio sections
- Newsletter signup (reveals email)

### Conference speaker listings
- PyCon, JSConf, RustConf websites
- Speaker bios often include email
- Archive.org can retrieve historical versions

## Advanced Techniques

### Domain reputation tools
- MX Lookup for company domain
- Common email format databases
- OSINT tools (Shodan, Maltego)

### Email verification (ethical)
- Check if address is in known breach databases (Have I Been Pwned API)
- Test addresses with mail forwarding services
- Look for email in Git tags/releases

### Newsletter & subscription methods
- Subscribe to their newsletter (email visible)
- GitHub Sponsors (often shows contact method)
- Patreon or similar (email associated with account)

## Red Flags & Considerations

🚩 **Don't:**
- Use email finding to spam
- Scrape emails without purpose
- Add to mailing lists without permission
- Share email publicly without consent
- Use unethical OSINT methods

✅ **Do:**
- Respect privacy settings
- Have clear, professional reason for contact
- Keep email addresses confidential
- Test contact in non-intrusive way first
- Respect "no contact info" decisions

## Real Examples

### Example 1: Finding Derek Collison (NATS creator)
1. Go to github.com/nats-io/nats-server → Contributors
2. Click Derek's profile → bio shows Synadia, has website link
3. Visit Synadia.com → /about shows his email
4. Or: Search "Derek Collison email" → LInkedIn or personal site appears

### Example 2: Finding Python package maintainer
1. Clone repo: `git clone https://github.com/owner/package.git`
2. Run: `git log --all --format=%aE | grep "@" | head -5`
3. Emails appear: `alice@company.com`, `alice@personal.dev`
4. Cross-check on GitHub profile for consistency

## Tooling

### Automated scripts
```bash
# Extract all emails from repo
git log --all --format=%aE | sort -u > emails.txt

# Find most active email author
git log --all --format=%aE | sort | uniq -c | sort -rn | head -10

# Check specific author
git log --all --author="Substring" --format=%aE | sort -u
```

### Python for pattern testing
```python
domain = "company.com"
name_first, name_last = "john", "doe"

patterns = [
    f"{name_first}@{domain}",
    f"{name_first}.{name_last}@{domain}",
    f"{name_first[0]}{name_last}@{domain}",
    f"{name_last}.{name_first}@{domain}",
]

for email in patterns:
    print(email)
```

## When Email Finding Fails

If you can't find an email:
- Use GitHub's web interface to file issues/discussions
- Contact via their company's official channels
- Look for alternative contact methods (Twitter DM, LinkedIn message)
- Try project's issue tracker or discussions section
- Accept that person may prefer not to be contacted directly

## Privacy Considerations

Respect these principles:
- People who hide their email often have good reasons
- "No contact info visible" is a signal to not pursue
- Use contact info only for stated purpose
- Assume any email is semi-private, not for distribution
- Professional context matters (networking vs. sales pitch)
