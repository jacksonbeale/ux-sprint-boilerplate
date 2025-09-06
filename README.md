# UX Sprint Boilerplate

A proven framework for executing lean UX sprints with AI agent acceleration. This boilerplate provides everything you need to rapidly set up and execute user experience sprints focused on feature integration and product enhancement.

## Quick Start

1. **Clone or download this boilerplate**
2. **Run the setup script:**
   ```bash
   python3 setup.py
   ```
3. **Follow the prompts** to configure your project
4. **Navigate to your new project** and start your sprint!

## What You Get

### 🏗️ Complete Project Structure
- **Agents:** Pre-configured AI agents for each sprint phase
- **Templates:** CLAUDE.md and documentation templates  
- **Methodology:** Proven 10-day sprint framework
- **Deliverables:** Structured outputs for stakeholders

### 🤖 AI-Powered Workflow
- **Research Agent:** Automates competitive analysis and user research
- **Journey Mapping Agent:** Converts insights into user flow documentation
- **Prototyping Agent:** Generates interactive prototypes from concepts
- **Testing Agent:** Creates test plans and synthesizes feedback
- **Summary Agent:** Compiles executive-ready reports

### ⚡ Rapid Setup
- **5-minute configuration** via interactive setup script
- **Parameterized templates** adapt to any project context
- **No manual file editing** required

## Sprint Methodology

This boilerplate implements a **10-day lean UX sprint**:

1. **Days 1-2:** Research & Discovery
2. **Days 3-4:** Journey Mapping  
3. **Days 5-7:** Prototyping
4. **Days 8-9:** Testing & Validation
5. **Day 10:** Synthesis & Planning

See [METHODOLOGY.md](METHODOLOGY.md) for detailed guidance.

## Configuration Options

The setup script will prompt you for:

- **Project Details:** Name, goals, company context
- **Capabilities:** Features being integrated or developed
- **Competition:** Key competitors and market context
- **Visual Needs:** Whether visual validation is required
- **Deliverables:** What outputs stakeholders expect

## Project Types

This boilerplate works for:

- ✅ **Feature Integration Projects** - Adding new capabilities to existing products
- ✅ **Product Enhancement Sprints** - Improving existing user experiences  
- ✅ **Competitive Response** - Rapidly developing features to match market
- ✅ **User Flow Optimization** - Streamlining existing workflows
- ✅ **Cross-Platform Integration** - Connecting multiple product experiences

## Requirements

- **Python 3.6+** (for setup script)
- **Claude Code access** (for AI agent utilization)
- **Web browser** (for prototype testing)

## Customization

### Adding New Agents
1. Create agent template in `templates/agents/`
2. Add agent reference to `templates/CLAUDE.md.template` 
3. Update setup script if new configuration needed

### Modifying Sprint Structure
1. Update phase descriptions in `METHODOLOGY.md`
2. Adjust deliverable templates in `templates/`
3. Modify agent task definitions as needed

## Contributing

Found improvements or new patterns? Please contribute back:

1. **Document your learnings** in project retrospectives
2. **Update templates** with successful patterns
3. **Share methodology improvements** with other teams
4. **Enhance agent prompts** based on output quality

## Support

- Review [METHODOLOGY.md](METHODOLOGY.md) for detailed guidance
- Check existing agent templates for examples
- Refer to original Affinity project for reference implementation

---

**Version:** 1.0  
**Last Updated:** {{ current_date }}  
**Based on:** Leonardo.ai x Affinity Integration Sprint learnings