# Trigents SPSBS System

A comprehensive agent-based workflow system for Python development, data processing, and startup growth strategies. Built with specialized AI agents following Karpathy-inspired principles for reliable, minimal, and goal-driven execution.

## Overview

This repository contains:

- **Advanced Systems & Data Agents Bundle**: Three specialized agents for system architecture, deep research, and data transformation
- **Startup Growth Pipeline**: A 4-agent workflow for discovering SMB leads, enriching data, designing solutions, and creating outreach campaigns
- **Python Projects**: Sample applications including a receptionist AI system and basic scripts

## Features

### Agent Workflows
- **Advanced Systems Architect**: Designs complex systems with structured thinking
- **Deep Web Researcher**: Conducts thorough research and synthesizes insights
- **Data Enrichment & Structurer**: Cleans, enriches, and structures messy data
- **Startup Lead Discovery**: Finds SMBs with weak digital presence
- **Startup Data Enrichment**: Analyzes competitors and maps opportunities
- **Startup Growth Engineer**: Builds websites, workflows, and campaigns
- **Startup Lead System**: Orchestrates the complete lead-to-conversion pipeline

### Python Applications
- AI Receptionist: Appointment booking system with CLI and Flask API
- Basic scripts and utilities

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DerekJW36/trigents-spsbs-system.git
cd trigents-spsbs-system
```

2. Set up Python environment (for receptionist app):
```bash
cd python-projects-ai/receptionist.1
pip install -r requirements.txt
```

## Usage

### Agent Workflows
Use the `.agent.md` files in VS Code with GitHub Copilot. Reference agents in prompts like:

```
@startup-lead-system Find 5 businesses in SE Portland, OR with broken websites and weak profiles, then produce 5 message drafts to review and send.
```

### Python Apps
Run the receptionist app:
```bash
python main.py --mode cli
# or
python main.py --mode api
```

## Agent Principles

All agents follow four Karpathy-inspired principles:
- **Think Before Coding**: Clarify assumptions and surface tradeoffs
- **Simplicity First**: Minimum viable solution, no over-engineering
- **Surgical Changes**: Touch only what's necessary
- **Goal-Driven Execution**: Define success criteria and verify results

## Project Structure

```
trigents-spsbs-system/
├── .agent.md                    # General Python assistant
├── AGENTS.md                    # Agent bundle documentation
├── advanced-systems-architect.agent.md
├── data-enrichment-structurer.agent.md
├── deep-web-researcher.agent.md
├── startup-data-enrichment.agent.md
├── startup-growth-engineer.agent.md
├── startup-lead-discovery.agent.md
├── startup-lead-system.agent.md
├── hello.py                     # Basic Python script
├── python-projects-ai/
│   ├── hello.py
│   └── receptionist.1/          # AI receptionist app
│       ├── main.py
│       ├── requirements.txt
│       ├── models/
│       ├── tools/
│       └── inventory/
└── .gitignore
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes following the agent principles
4. Test thoroughly
5. Submit a pull request

## License

MIT License - See LICENSE file for details

## Contact

Repository: https://github.com/DerekJW36/trigents-spsbs-system
