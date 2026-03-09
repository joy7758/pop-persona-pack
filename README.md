# POP Persona Pack

Reusable agent personas powered by the Persona Object Protocol (POP).

This repository demonstrates how persona objects can be loaded and used
to construct CrewAI agents.

## At a glance

- Recommended runtime: Python 3.11 or 3.12
- Main crew entry: `python crew.py`
- CI smoke validation: install dependencies, import CrewAI, build the Crew object, and verify the expected agents and tasks

## Runtime note

This repository is currently recommended for Python 3.11 or 3.12.

Some CrewAI dependency chains may fail to install under newer Python versions
(such as Python 3.14) due to transitive build issues in older dependencies.

## Example

```bash
python demo/multi_role_demo.py
```

## Minimal CrewAI crew

This repository includes a minimal 3-agent CrewAI example powered by POP-style persona objects.

Agents included:

- Marketing Manager
- Software Engineer
- Product Designer

Run:

```bash
python crew.py
```

This demonstrates the path:

```text
persona object -> agent -> task -> crew
```

## CI validation scope

The GitHub Actions workflow validates the template structure in a Python 3.11 environment:

- install dependencies
- import CrewAI
- build the Crew object
- verify the expected agents and tasks

It does **not** execute a live `crew.kickoff()` call in CI, because full execution typically requires model/provider configuration and API credentials.

## Persona concept

Instead of embedding persona in prompts, POP defines personas as portable objects.

```text
persona object -> agent config
```
