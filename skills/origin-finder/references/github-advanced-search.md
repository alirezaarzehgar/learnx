# GitHub Advanced Search Guide

Master GitHub's search syntax to find people, repositories, and patterns faster.

## User Search

### Find by username/name
```
user:@username
username:@octocat
is:user
```

### Find by location
```
location:"San Francisco"
location:Berlin
```

### Find by company
```
company:github
company:"GitHub Copilot"
```

### Find by followers
```
followers:>1000
followers:100..1000
followers:<10
```

### Find by repository count
```
repos:>50
public_repos:>100
```

### Find by account creation date
```
created:2015-01-01
created:>2015-01-01
created:<2015-01-01
created:2015-01-01..2016-01-01
```

### Find by last activity
```
updated:>2024-01-01
pushed:2024
```

### Combine user searches
```
user:@username location:Berlin followers:>500 repos:>20
```

## Repository Search

### Basic repo search
```
repo:owner/name
is:public
is:private (only shows your private repos)
```

### Search by language
```
language:python
language:javascript
language:go
```

### Search by stars
```
stars:>1000
stars:100..1000
stars:<10
```

### Search by forks
```
forks:>100
forks:<5
```

### Search by size
```
size:>1000
size:<50
```

### Search by topics
```
topic:nats
topic:message-broker
```

### Search by license
```
license:MIT
license:Apache-2.0
license:"GPL-3.0"
```

### Search by archived status
```
archived:true
archived:false
```

### Combine repo searches
```
topic:message-broker language:go stars:>500 archived:false
```

## Commit & Code Search

### Find commits by author
```
author:@username
author-email:user@domain.com
```

### Find commits by date
```
committer-date:>2024-01-01
author-date:2024-01-15..2024-02-15
```

### Find commits by message
```
commit-message:"fix bug"
```

### Search code in specific repo
```
repo:owner/repo "search term"
```

### Search by file extension
```
filename:*.json
path:src/
extension:py
```

### Find code patterns
```
class:MyClass
function:processData
```

### Find commented code (often reveals history)
```
//TODO
//FIXME
//deprecated
```

## Issue & Pull Request Search

### Find issues by state
```
is:issue is:open
is:issue is:closed
is:pr is:open
```

### Find by assignee
```
assignee:@username
no:assignee
```

### Find by creator
```
author:@username
```

### Find by labels
```
label:bug
label:enhancement
label:documentation
```

### Find by mentions
```
mentions:@username
```

### Find by milestone
```
milestone:v1.0
```

### Find by comment count
```
comments:>10
comments:<3
```

## Real-World Examples

### Find top contributors to a project
```
# In repository: owner/repo
# Go to Contributors tab, but search can find them:
repo:owner/repo is:issue is:closed author:@username
```

### Find someone's most starred repos
```
user:@username is:public is:repo stars:>500
```

### Find projects in a specific language by someone
```
user:@username language:python archived:false
```

### Find recent contributions
```
author:@username pushed:>2024-01-01
```

### Find projects seeking contributors
```
label:"good first issue" language:python stars:>100
```

### Find someone's forks and modifications
```
user:@username fork:true is:repo
```

### Find code they wrote (not just repos they own)
```
author:@username repo:*
# Or specific org:
org:python language:python author:@username
```

### Find old projects (good for history)
```
org:python created:<2010
```

### Find all projects someone is an owner/admin of
```
# Search GitHub org pages for:
org:ORGNAME members
# Then look for admin badge
```

## Workflow: Finding Someone's Technical Depth

**Goal:** Understand what technology someone is expert in

1. Find their profile:
   ```
   user:@username
   ```

2. Find their repos:
   ```
   user:@username is:repo is:public stars:>10
   ```

3. Find their commits:
   ```
   author:@username language:python
   author:@username language:go
   ```

4. Find their contributions to major projects:
   ```
   author:@username repo:golang/go
   author:@username repo:torvalds/linux
   ```

5. Find their active periods:
   ```
   author:@username pushed:>2023-01-01
   author:@username pushed:2022-01-01..2022-12-31
   ```

## Workflow: Profiling a Project's Health

**Goal:** Assess who's actually maintaining a project

1. List contributors:
   ```
   repo:owner/project
   ```
   (Use GitHub UI Contributors tab, but you can verify with search)

2. Find recent activity:
   ```
   repo:owner/project pushed:>2024-01-01
   ```

3. Find who responds to issues:
   ```
   repo:owner/project is:issue is:closed sort:updated-desc
   ```

4. Find key decision makers:
   ```
   repo:owner/project is:pr merged author:@username
   ```

5. Identify bottlenecks:
   ```
   repo:owner/project is:issue is:open label:waiting-for-maintainer
   ```

## Advanced Tricks

### Find forks of a project to see variants
```
fork:true repo:owner/original-project
```

### Find if someone is active RIGHT NOW
```
author:@username pushed:2024-01-15
```

### Find emerging contributors
```
repo:owner/project is:pr merged committer-date:2024
# (Finding people with recent first merges)
```

### Find abandoned projects by an author
```
user:@username archived:true
```

### Find different email addresses used by same person
```
author-email:john@personal.com
author-email:john@company.com
```

### Find code that violates patterns (can reveal history)
```
repo:owner/project "console.log" language:javascript
# (To see when debugging code was added)
```

## Combining Search with Git CLI

Once you've identified someone/repo via GitHub search, use git locally:

```bash
# Clone and analyze locally
git clone https://github.com/owner/repo.git
cd repo

# Find all commits by person
git log --author="@username" --oneline

# Find their typical work hours (commit timestamps)
git log --author="@username" --format="%aI" | cut -d'T' -f2 | sort

# Find what they worked on
git log --author="@username" --name-status | grep "^[A-Z]" | sort | uniq -c

# Find their email addresses
git log --all --format=%aE | grep "@" | sort -u

# Find commits referencing their name
git log --grep="@username" --oneline

# See their contribution percentage
git shortlog -sn
```

## Search Tips & Tricks

### ⚡ Performance
- Searches with wildcards are slow
- Use specific criteria to narrow results
- `site:github.com` for Google search works too

### 🔗 Combining Multiple Criteria
- Use `AND` (implied, just space-separated)
- Use `NOT` for negation
- Parentheses for grouping not supported, so order matters

### 📊 Common Patterns
```
# Highly active developers
followers:>500 repos:>50 public_repos:>20

# Open source project quality
stars:>1000 language:python archived:false

# Emerging developers
followers:50..500 repos:5..20 created:>2020

# Research/academic
followers:<100 repos:>100 public_repos:>50
```

## Rate Limits

- Unauthenticated: 10 requests/minute
- Authenticated: 30 requests/minute
- GitHub API (for scripts): 5,000 requests/hour with token

## See Also

- [GitHub Search Documentation](https://docs.github.com/en/search-github)
- [Advanced Search UI](https://github.com/search/advanced)
- [Git CLI documentation](https://git-scm.com/docs)
