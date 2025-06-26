# Algorand Contracts - AlgoMingle

Smart contracts for the AlgoMingle decentralized messaging platform on Algorand.

## Overview

This repository contains all smart contracts powering the AlgoMingle messaging application, including:
- User registry and authentication
- Message storage and retrieval
- Group management
- Encryption key management

## Tech Stack

- **Language**: Python 3.10+
- **Framework**: PyTeal / Beaker
- **Blockchain**: Algorand
- **Testing**: pytest

## Project Structure

```
algorand-contracts-am/
├── contracts/           # Smart contract source files
│   ├── user_registry.py
│   ├── message_store.py
│   └── group_manager.py
├── tests/              # Contract test suites
├── scripts/            # Deployment and utility scripts
├── artifacts/          # Compiled contracts and ABIs
└── requirements.txt    # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.10+
- Algorand Sandbox or node access
- PyTeal and Beaker installed

### Installation

```bash
# Clone the repository
git clone https://github.com/fbratten/algorand-contracts-am.git
cd algorand-contracts-am

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Development

```bash
# Run tests
pytest

# Compile contracts
python scripts/compile_contracts.py

# Deploy to testnet
python scripts/deploy.py --network testnet
```

## Related Repositories

This is part of the AlgoMingle multi-repository project:
- [algomingle](https://github.com/fbratten/algomingle) - Frontend application
- [ai-orchestrator-am](https://github.com/fbratten/ai-orchestrator-am) - AI services
- [devops-automation-am](https://github.com/fbratten/devops-automation-am) - CI/CD automation
- [development-playbook-am](https://github.com/fbratten/development-playbook-am) - Documentation

---

## 🚧 Project Status

This repository is part of an active development project and is **not currently accepting external contributions**.

- ✅ Feel free to **explore, fork, and learn** from the code
- 💬 **Questions?** Please use the [Discussions](../../discussions) tab
- ⭐ **Like the project?** Give it a star!
- 📧 **Private inquiries:** jack.bratten@adaptivearts.ai

For more information, see [CONTRIBUTING.md](CONTRIBUTING.md).
