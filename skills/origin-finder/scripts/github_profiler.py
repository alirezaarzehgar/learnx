#!/usr/bin/env python3
"""
GitHub Profiler - Extract and profile top contributors from any GitHub repository.

This script automates the first steps of origin-finder: extracting maintainers and
key contributors, their GitHub profiles, and linked accounts.

Usage:
    python3 github_profiler.py owner/repo [--top N] [--min-commits M]
    
Example:
    python3 github_profiler.py nats-io/nats-server --top 10 --min-commits 5
    python3 github_profiler.py redis/redis --top 5
"""

import json
import sys
import argparse
from typing import List, Dict, Optional
from datetime import datetime

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found.")
    print("Install with: pip install requests")
    sys.exit(1)


class GitHubProfiler:
    """Extract and analyze GitHub repository contributors."""
    
    def __init__(self, github_token: Optional[str] = None):
        """
        Initialize profiler.
        
        Args:
            github_token: Optional GitHub API token for higher rate limits.
                         Set via environment variable GITHUB_TOKEN.
        """
        self.github_token = github_token
        self.base_url = "https://api.github.com"
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        
        if self.github_token:
            self.headers["Authorization"] = f"token {self.github_token}"
    
    def get_contributors(self, owner: str, repo: str, per_page: int = 100) -> List[Dict]:
        """
        Fetch contributors for a repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
            per_page: Results per page (max 100)
            
        Returns:
            List of contributor dictionaries
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/contributors"
        
        all_contributors = []
        page = 1
        
        print(f"📥 Fetching contributors from {owner}/{repo}...")
        
        while True:
            params = {"per_page": per_page, "page": page}
            response = requests.get(url, headers=self.headers, params=params)
            
            if response.status_code != 200:
                print(f"❌ Error: {response.status_code}")
                print(response.json().get("message", "Unknown error"))
                break
            
            contributors = response.json()
            
            if not contributors:
                break
            
            all_contributors.extend(contributors)
            page += 1
            print(f"  ✓ Fetched page {page-1} ({len(all_contributors)} total so far)")
        
        return all_contributors
    
    def get_user_profile(self, username: str) -> Dict:
        """
        Fetch detailed profile for a GitHub user.
        
        Args:
            username: GitHub username
            
        Returns:
            User profile dictionary
        """
        url = f"{self.base_url}/users/{username}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def extract_contact_info(self, profile: Dict) -> Dict:
        """
        Extract contact and social information from GitHub profile.
        
        Args:
            profile: GitHub user profile
            
        Returns:
            Dictionary with contact information
        """
        contact = {
            "github": f"https://github.com/{profile.get('login')}",
            "email": profile.get("email"),
            "blog": profile.get("blog"),
            "location": profile.get("location"),
            "bio": profile.get("bio"),
        }
        
        # Try to extract social handles from bio
        bio = profile.get("bio", "")
        twitter = None
        if "@" in bio:
            # Simple extraction of @handle from bio
            parts = bio.split()
            twitter = next((p for p in parts if p.startswith("@")), None)
        
        contact["twitter"] = twitter
        
        return {k: v for k, v in contact.items() if v}
    
    def profile_contributors(self, owner: str, repo: str, top_n: int = 10, 
                            min_commits: int = 1) -> List[Dict]:
        """
        Build detailed profiles for top contributors.
        
        Args:
            owner: Repository owner
            repo: Repository name
            top_n: Number of top contributors to profile
            min_commits: Minimum commits to include
            
        Returns:
            List of detailed contributor profiles
        """
        contributors = self.get_contributors(owner, repo)
        
        # Filter and sort
        filtered = [c for c in contributors if c.get("contributions", 0) >= min_commits]
        top_contributors = filtered[:top_n]
        
        print(f"\n📊 Building profiles for top {len(top_contributors)} contributors...")
        
        profiles = []
        
        for i, contributor in enumerate(top_contributors, 1):
            username = contributor.get("login")
            commits = contributor.get("contributions")
            
            print(f"  [{i}/{len(top_contributors)}] @{username} ({commits} commits)...", end=" ")
            
            user_profile = self.get_user_profile(username)
            
            if user_profile:
                profile = {
                    "rank": i,
                    "username": username,
                    "commits": commits,
                    "name": user_profile.get("name", username),
                    "company": user_profile.get("company"),
                    "location": user_profile.get("location"),
                    "bio": user_profile.get("bio"),
                    "followers": user_profile.get("followers"),
                    "public_repos": user_profile.get("public_repos"),
                    "created_at": user_profile.get("created_at"),
                    "updated_at": user_profile.get("updated_at"),
                    "contact": self.extract_contact_info(user_profile),
                    "avatar_url": user_profile.get("avatar_url"),
                }
                profiles.append(profile)
                print("✓")
            else:
                print("✗ (failed to fetch)")
        
        return profiles
    
    def export_markdown(self, profiles: List[Dict], owner: str, repo: str) -> str:
        """
        Export profiles as Markdown.
        
        Args:
            profiles: List of contributor profiles
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Markdown string
        """
        md = f"# Origin Finder: {owner}/{repo}\n\n"
        md += f"**Generated:** {datetime.now().isoformat()}\n\n"
        md += f"**Repository:** https://github.com/{owner}/{repo}\n\n"
        md += "---\n\n"
        
        for profile in profiles:
            md += f"## #{profile['rank']} — {profile.get('name', profile['username'])}\n\n"
            
            md += f"**GitHub:** [@{profile['username']}]({profile['contact'].get('github')})\n"
            
            if profile.get('company'):
                md += f"**Company:** {profile['company']}\n"
            
            if profile.get('location'):
                md += f"**Location:** {profile['location']}\n"
            
            if profile.get('bio'):
                md += f"**Bio:** {profile['bio']}\n"
            
            md += f"\n**Contributions:** {profile['commits']} commits | "
            md += f"{profile['followers']} followers | "
            md += f"{profile['public_repos']} public repos\n\n"
            
            if profile['contact'].get('email'):
                md += f"📧 **Email:** {profile['contact']['email']}\n"
            
            if profile['contact'].get('blog'):
                md += f"🌐 **Website:** {profile['contact']['blog']}\n"
            
            if profile['contact'].get('twitter'):
                md += f"🐦 **Twitter:** {profile['contact']['twitter']}\n"
            
            md += "\n---\n\n"
        
        return md
    
    def export_json(self, profiles: List[Dict]) -> str:
        """Export profiles as JSON."""
        return json.dumps(profiles, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Extract and profile top contributors from a GitHub repository."
    )
    parser.add_argument("repo", help="Repository in format 'owner/repo' (e.g., nats-io/nats-server)")
    parser.add_argument("--top", type=int, default=10, help="Number of top contributors to profile (default: 10)")
    parser.add_argument("--min-commits", type=int, default=1, help="Minimum commits to include (default: 1)")
    parser.add_argument("--output", help="Output file (json or md). If not specified, prints to stdout")
    parser.add_argument("--format", choices=["json", "md"], default="md", help="Output format (default: md)")
    parser.add_argument("--token", help="GitHub API token (or set GITHUB_TOKEN env var)")
    
    args = parser.parse_args()
    
    # Parse repo
    if "/" not in args.repo:
        print("❌ Error: Repository must be in format 'owner/repo'")
        sys.exit(1)
    
    owner, repo = args.repo.split("/", 1)
    
    # Get token from arg or environment
    token = args.token or None
    
    # Create profiler and run
    try:
        profiler = GitHubProfiler(github_token=token)
        profiles = profiler.profile_contributors(owner, repo, top_n=args.top, min_commits=args.min_commits)
        
        # Export
        if args.format == "json":
            output = profiler.export_json(profiles)
        else:
            output = profiler.export_markdown(profiles, owner, repo)
        
        # Write or print
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"\n✅ Written to {args.output}")
        else:
            print(output)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
