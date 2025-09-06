#!/usr/bin/env python3
"""
UX Sprint Boilerplate Setup Script
Initializes a new UX sprint project from templates
"""

import json
import os
import shutil
import re
from pathlib import Path

class BoilerplateSetup:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.templates_dir = self.base_dir / "templates"
        self.config = {}
        
    def load_config(self):
        """Load configuration from project-config.json"""
        config_file = self.base_dir / "project-config.json"
        with open(config_file, 'r') as f:
            self.config = json.load(f)
    
    def get_user_input(self):
        """Collect custom values from user"""
        print("UX Sprint Boilerplate Setup")
        print("=" * 40)
        
        # Required fields
        self.config['project_name'] = input(f"Project name [{self.config['project_name']}]: ") or self.config['project_name']
        self.config['company_name'] = input(f"Company name [{self.config['company_name']}]: ") or self.config['company_name']
        self.config['product_name'] = input(f"Product name [{self.config['product_name']}]: ") or self.config['product_name']
        self.config['project_goal'] = input(f"Project goal [{self.config['project_goal']}]: ") or self.config['project_goal']
        
        # Capabilities (comma-separated)
        capabilities_str = input(f"Key capabilities (comma-separated) [{', '.join(self.config['capabilities'])}]: ")
        if capabilities_str:
            self.config['capabilities'] = [cap.strip() for cap in capabilities_str.split(',')]
        
        # Competitors (comma-separated) 
        competitors_str = input(f"Main competitors (comma-separated) [{', '.join(self.config['competitors'])}]: ")
        if competitors_str:
            self.config['competitors'] = [comp.strip() for comp in competitors_str.split(',')]
        
        # Visual validation
        has_visual = input(f"Include visual validation? (y/n) [{'y' if self.config['has_visual_validation'] else 'n'}]: ")
        self.config['has_visual_validation'] = has_visual.lower() == 'y' if has_visual else self.config['has_visual_validation']
        
    def replace_placeholders(self, content):
        """Replace template placeholders with actual values"""
        # Handle arrays specially
        if '{{capabilities_list}}' in content:
            capabilities_bullets = '\n'.join([f"- **{cap}**" for cap in self.config['capabilities']])
            content = content.replace('{{capabilities_list}}', capabilities_bullets)
        
        if '{{competitors_list}}' in content:
            competitors_str = ', '.join(self.config['competitors'])
            content = content.replace('{{competitors_list}}', competitors_str)
            
        if '{{deliverables_list}}' in content:
            deliverables_bullets = '\n'.join([f"* {deliv}" for deliv in self.config['deliverables']])
            content = content.replace('{{deliverables_list}}', deliverables_bullets)
        
        # Replace all other placeholders
        for key, value in self.config.items():
            placeholder = f"{{{{{key}}}}}"
            if isinstance(value, (list, dict)):
                continue  # Skip complex types (handled above)
            content = content.replace(placeholder, str(value))
        
        return content
    
    def copy_and_process_file(self, src_path, dest_path):
        """Copy template file and replace placeholders"""
        if src_path.suffix == '.template':
            # Process template file
            with open(src_path, 'r') as f:
                content = f.read()
            
            processed_content = self.replace_placeholders(content)
            
            # Remove .template extension
            final_dest = dest_path.parent / dest_path.name.replace('.template', '')
            with open(final_dest, 'w') as f:
                f.write(processed_content)
        else:
            # Copy non-template files as-is
            shutil.copy2(src_path, dest_path)
    
    def create_project_structure(self, target_dir):
        """Create the project structure from templates"""
        target_path = Path(target_dir)
        target_path.mkdir(exist_ok=True)
        
        # Copy template structure
        for item in self.templates_dir.rglob('*'):
            if item.is_file():
                # Calculate relative path from templates dir
                rel_path = item.relative_to(self.templates_dir)
                dest_path = target_path / rel_path
                
                # Create parent directories if needed
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Process the file
                self.copy_and_process_file(item, dest_path)
        
        # Copy non-template files
        for file in ['METHODOLOGY.md', 'README.md']:
            if (self.base_dir / file).exists():
                shutil.copy2(self.base_dir / file, target_path / file)
    
    def run(self):
        """Main setup process"""
        self.load_config()
        self.get_user_input()
        
        project_name_slug = re.sub(r'[^a-zA-Z0-9-_]', '-', self.config['project_name'].lower())
        target_dir = f"../{project_name_slug}"
        
        print(f"\nCreating project in: {target_dir}")
        self.create_project_structure(target_dir)
        
        print(f"\n✅ Project '{self.config['project_name']}' created successfully!")
        print(f"📁 Location: {os.path.abspath(target_dir)}")
        print("\nNext steps:")
        print("1. cd into the project directory")
        print("2. Initialize git: git init")
        print("3. Review and customize the generated files")
        print("4. Start your UX sprint!")

if __name__ == "__main__":
    setup = BoilerplateSetup()
    setup.run()