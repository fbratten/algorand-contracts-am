"""Setup script for AlgoMingle smart contracts development environment"""

import subprocess
import sys
import os


def setup_environment():
    """Set up the Python environment for smart contract development"""
    print("🚀 Setting up AlgoMingle Smart Contracts environment...")
    
    # Create virtual environment
    print("\n📦 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", ".venv"])
    
    # Determine pip path based on OS
    pip_path = ".venv\\Scripts\\pip" if os.name == "nt" else ".venv/bin/pip"
    
    # Upgrade pip
    print("\n📦 Upgrading pip...")
    subprocess.run([pip_path, "install", "--upgrade", "pip"])
    
    # Install requirements
    print("\n📦 Installing dependencies...")
    subprocess.run([pip_path, "install", "-r", "requirements.txt"])
    
    print("\n✅ Setup complete!")
    print("\nTo activate the environment:")
    if os.name == "nt":
        print("  .venv\\Scripts\\activate")
    else:
        print("  source .venv/bin/activate")
    
    print("\nNext steps:")
    print("  1. Set up your Algorand node or use AlgoKit LocalNet")
    print("  2. Configure .env with your Algorand credentials")
    print("  3. Run tests: pytest")


if __name__ == "__main__":
    setup_environment()
