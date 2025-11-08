#!/usr/bin/env python3
"""
Instagram Bot Runner
Redirects to compiled toolv2.cpython-312.so
"""

import sys
import os
import platform
import subprocess

def check_64bit():
    """Check if system is 64-bit"""
    arch = platform.architecture()
    if arch[0] != '64bit':
        print("❌ SORRY - 64-bit system required")
        print(f"Your system: {arch[0]}")
        print("This compiled module only works on 64-bit devices")
        sys.exit(1)
    print("✅ 64-bit system detected")

def git_pull():
    """Pull latest updates"""
    print("🔄 Checking for updates...")
    try:
        # Check if we're in a git repository first
        check_git = subprocess.run(['git', 'status'], 
                                 capture_output=True, 
                                 text=True)
        
        if check_git.returncode != 0:
            print("⚠️  Not a git repository - skipping update")
            return
        
        # Now do git pull
        result = subprocess.run(['git', 'pull'], 
                              capture_output=True, 
                              text=True, 
                              timeout=30)
        
        if result.returncode == 0:
            if "Already up to date" in result.stdout:
                print("✅ Already up-to-date")
            else:
                print("✅ Updated successfully")
                print("Changes:", result.stdout.strip())
        else:
            print(f"⚠️  Git pull failed: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("⚠️  Update check timed out")
    except Exception as e:
        print(f"⚠️  Update error: {e}")

def load_compiled_module():
    """Load the compiled .so module"""
    module_file = "toolv2.cpython-312.so"
    
    if not os.path.exists(module_file):
        print(f"❌ Compiled module not found: {module_file}")
        print("Available .so files:")
        for file in os.listdir('.'):
            if file.endswith('.so'):
                print(f"  - {file}")
        sys.exit(1)
    
    try:
        # Import the compiled module
        import importlib.util
        spec = importlib.util.spec_from_file_location("toolv2", module_file)
        toolv2 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(toolv2)
        print("✅ Compiled module loaded successfully")
        return toolv2
    except Exception as e:
        print(f"❌ Failed to load compiled module: {e}")
        sys.exit(1)

def show_menu():
    """Show the main menu"""
    print("\n" + "="*50)
    print("        INSTAGRAM BOT CONTROL PANEL")
    print("="*50)
    print("1. Free Trial [Limited]")
    print("2. Buy Followers Real, Bot at cheap")

def main():
    print("\n" + "="*50)
    print("        INSTAGRAM BOT - COMPILED VERSION")
    print("="*50)
    
    # System check
    check_64bit()
    
    # Git update
    git_pull()
    
    # Load module
    bot_module = load_compiled_module()
    
    print("\n🚀 Instagram Bot Ready!")
    print("-" * 30)
    
    # Show menu and handle user choice
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            print("\nStarting Free Trial...")
            if hasattr(bot_module, 'multi_account_follow'):
                bot_module.multi_account_follow()
            else:
                print("❌ Free trial function not available")
                
        elif choice == "2":
            print("\nTo buy premium-quality Instagram followers or bot services,")
            print("message me on my WhatsApp number: 9766912352.")
            
        else:
            print("❌ Invalid choice! Please select 1 or 2.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()        print("✅ Compiled module loaded successfully")
        return toolv2
    except Exception as e:
        print(f"❌ Failed to load compiled module: {e}")
        sys.exit(1)

def show_menu():
    """Show the main menu"""
    print("\n" + "="*50)
    print("        INSTAGRAM BOT CONTROL PANEL")
    print("="*50)
    print("1. Free Trial [Limited]")
    print("2. Buy Followers Real, Bot at cheap")

def main():
    print("\n" + "="*50)
    print("        INSTAGRAM BOT - COMPILED VERSION")
    print("="*50)
    
    # System check
    check_64bit()
    
    # Git update
    git_pull()
    
    # Load module
    bot_module = load_compiled_module()
    
    print("\n🚀 Instagram Bot Ready!")
    print("-" * 30)
    
    # Show menu and handle user choice
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            print("\nStarting Free Trial...")
            if hasattr(bot_module, 'multi_account_follow'):
                bot_module.multi_account_follow()
            else:
                print("❌ Free trial function not available")
                
        elif choice == "2":
            print("\nTo buy premium-quality Instagram followers or bot services,")
            print("message me on my WhatsApp number: 9766912352.")
            
        else:
            print("❌ Invalid choice! Please select 1 or 2.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()        spec = importlib.util.spec_from_file_location("toolv1", module_file)
        toolv1 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(toolv1)
        print("✅ Compiled module loaded successfully")
        return toolv1
    except Exception as e:
        print(f"❌ Failed to load compiled module: {e}")
        sys.exit(1)

def show_menu():
    """Show the main menu"""
    print("\n" + "="*50)
    print("        INSTAGRAM BOT CONTROL PANEL")
    print("="*50)
    print("1. Free Trial [Limited]")
    print("2. Buy Followers Real, Bot at cheap")

def main():
    print("\n" + "="*50)
    print("        INSTAGRAM BOT - COMPILED VERSION")
    print("="*50)
    
    # System check
    check_64bit()
    
    # Git update
    git_pull()
    
    # Load module
    bot_module = load_compiled_module()
    
    print("\n🚀 Instagram Bot Ready!")
    print("-" * 30)
    
    # Show menu and handle user choice
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            print("\nStarting Free Trial...")
            if hasattr(bot_module, 'multi_account_follow'):
                bot_module.multi_account_follow()
            else:
                print("❌ Free trial function not available")
                
        elif choice == "2":
            print("\nTo buy premium-quality Instagram followers or bot services,")
            print("message me on my WhatsApp number: 9766912352.")
            
        else:
            print("❌ Invalid choice! Please select 1 or 2.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
