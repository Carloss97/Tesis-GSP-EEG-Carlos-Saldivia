#!/usr/bin/env python3
"""
Sync script for dual-language paper versions (English and Spanish).

This script propagates structural changes (figures, bibliography, methods, results, 
discussion, etc.) between ieee/ and ieee_es/ folders while preserving language-specific 
sections (abstract, introduction, conclusion).

Usage:
    python sync_structure.py [--direction EN_TO_ES|ES_TO_EN|BIDIRECTIONAL] [--dry-run]

Examples:
    python sync_structure.py                    # Bidirectional sync (default)
    python sync_structure.py --direction EN_TO_ES  # Copy only EN → ES
    python sync_structure.py --dry-run          # Preview changes without applying
"""

import os
import shutil
import argparse
from pathlib import Path
from typing import List, Tuple

# Files that are language-specific (should NOT be synced)
LANGUAGE_SPECIFIC_SECTIONS = {
    'abstract_es.tex', 'introduction_es.tex', 'conclusion_es.tex',  # Spanish only
    'abstract.tex', 'introduction.tex', 'conclusion.tex',  # English only
}

# Directories/files to sync (must exist in source and will be synced to destination)
SHARED_ITEMS = [
    'sections/related_work.tex',
    'sections/methods.tex',
    'sections/experiments.tex',
    'sections/results.tex',
    'sections/discussion.tex',
    'sections/reproducibility.tex',
    'figures',
    'tables',
    'bibliography',
]

class PaperSyncer:
    def __init__(self, paper_root: str, dry_run: bool = False):
        self.paper_root = Path(paper_root)
        self.ieee_en = self.paper_root / 'ieee'
        self.ieee_es = self.paper_root / 'ieee_es'
        self.dry_run = dry_run
        self.changes_count = 0
        
        # Verify directories exist
        if not self.ieee_en.exists():
            raise FileNotFoundError(f"English paper directory not found: {self.ieee_en}")
        if not self.ieee_es.exists():
            raise FileNotFoundError(f"Spanish paper directory not found: {self.ieee_es}")
    
    def _copy_item(self, src: Path, dest: Path) -> bool:
        """Copy file or directory from src to dest. Returns True if changed."""
        if src == dest:
            return False
        
        if not src.exists():
            print(f"  ⚠ Source not found: {src}")
            return False
        
        # Check if destination needs updating (simple mtime check)
        if dest.exists():
            if dest.is_file() and src.is_file():
                if dest.stat().st_mtime >= src.stat().st_mtime:
                    return False  # Destination is up-to-date
            elif dest.is_dir() and src.is_dir():
                # For directories, compare modification times recursively
                src_files = list(src.rglob('*'))
                dest_files = list(dest.rglob('*'))
                if len(src_files) == len(dest_files):
                    # Simplified: just check if counts match
                    return False
        
        # Perform the copy
        if self.dry_run:
            print(f"  [DRY-RUN] Would copy: {src.relative_to(self.paper_root)} → {dest.relative_to(self.paper_root)}")
            return True
        else:
            if dest.exists():
                if dest.is_dir():
                    shutil.rmtree(dest)
                else:
                    dest.unlink()
            
            if src.is_dir():
                shutil.copytree(src, dest)
            else:
                shutil.copy2(src, dest)
            
            print(f"  ✓ Synced: {src.name}")
            return True
    
    def sync_en_to_es(self) -> int:
        """Sync from English to Spanish (English as source of truth)."""
        print("\n🔄 Syncing English → Spanish")
        print(f"  Source: {self.ieee_en}")
        print(f"  Dest:   {self.ieee_es}")
        
        changes = 0
        for item in SHARED_ITEMS:
            src = self.ieee_en / item
            dest = self.ieee_es / item
            if self._copy_item(src, dest):
                changes += 1
        
        return changes
    
    def sync_es_to_en(self) -> int:
        """Sync from Spanish to English (Spanish as source of truth)."""
        print("\n🔄 Syncing Spanish → English")
        print(f"  Source: {self.ieee_es}")
        print(f"  Dest:   {self.ieee_en}")
        
        changes = 0
        for item in SHARED_ITEMS:
            src = self.ieee_es / item
            dest = self.ieee_en / item
            if self._copy_item(src, dest):
                changes += 1
        
        return changes
    
    def sync_bidirectional(self) -> int:
        """Sync bidirectionally: English is source of truth for shared items."""
        return self.sync_en_to_es()
    
    def report(self, changes: int):
        """Print sync report."""
        if self.dry_run:
            print(f"\n📋 [DRY-RUN] Would make {changes} change(s)")
        else:
            if changes == 0:
                print(f"\n✓ No changes needed (versions are in sync)")
            else:
                print(f"\n✓ Synced {changes} item(s)")

def main():
    parser = argparse.ArgumentParser(
        description="Sync dual-language paper versions (English and Spanish)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python sync_structure.py                      # Bidirectional sync (EN → ES)
  python sync_structure.py --direction EN_TO_ES # English to Spanish only
  python sync_structure.py --dry-run             # Preview changes
        """
    )
    
    parser.add_argument(
        '--direction',
        choices=['EN_TO_ES', 'ES_TO_EN', 'BIDIRECTIONAL'],
        default='BIDIRECTIONAL',
        help='Sync direction (default: BIDIRECTIONAL, EN is source of truth)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without applying them'
    )
    
    parser.add_argument(
        '--paper-root',
        default='.',
        help='Root directory of paper folder (default: current directory)'
    )
    
    args = parser.parse_args()
    
    try:
        syncer = PaperSyncer(args.paper_root, dry_run=args.dry_run)
        
        if args.direction == 'EN_TO_ES':
            changes = syncer.sync_en_to_es()
        elif args.direction == 'ES_TO_EN':
            changes = syncer.sync_es_to_en()
        else:  # BIDIRECTIONAL
            changes = syncer.sync_bidirectional()
        
        syncer.report(changes)
        
        if args.dry_run:
            print("\n💡 To apply changes, run without --dry-run flag")
        
        return 0
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

if __name__ == '__main__':
    exit(main())
