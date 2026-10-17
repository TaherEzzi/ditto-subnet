#!/usr/bin/env python3
"""Sync GitHub Project board with issue state"""

from github import Github, ProjectColumn, Issue
import os

def main():
    gh = Github(os.environ['GH_TOKEN'])
    repo = gh.get_repo('ditto-assistant/ditto-subnet')
    project = repo.get_project(1)  # DittoBench Board ID

    # Map columns: To Do → In Progress → Done
    columns = {
        col.name: col 
        for col in project.get_columns()
    }

    for issue in repo.get_issues(labels=['bounty']):
        # Extract metadata from issue body
        metadata = parse_metadata(issue.body)
        status = metadata.get('status', 'todo')
        
        # Find current column
        current_col = next((c for c in issue.get_project_cards() if c.column_name), None)
        
        # Move if status changed
        target_col = columns.get(status.title())
        if target_col and current_col.column_id != target_col.id:
            current_col.move(target_col.id)

        # Update slot counters
        update_column_counters(columns)

def parse_metadata(body: str) -> dict:
    """Extract YAML frontmatter from issue body"""
    if not body.startswith('---'):
        return {}
    _, content, _ = body.split('---', 2)
    return yaml.safe_load(content)

def update_column_counters(columns: dict[str, ProjectColumn]):
    """Show available/claimed slots in column names"""
    for name, col in columns.items():
        cards = col.get_cards()
        available = sum(1 for card in cards if 'available' in card.note)
        claimed = len(cards) - available
        col.edit(f"{name} ({available}/{available+claimed} slots)")

if __name__ == '__main__':
    main()
