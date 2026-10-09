# Native Windows controller

This fork can run `ansible-playbook` directly on Windows for local Windows
automation.

Supported scope:

- Python 3.13 or newer.
- `ansible-playbook` parsing, syntax checks, and local execution.
- Built-in actions and PowerShell scripts.
- One task at a time; `--forks` is intentionally limited to one worker.

Not supported yet:

- Interactive terminal prompts or privilege escalation.
- Enforcement of legacy `SIGALRM`-based timeouts.
- Persistent connection plugins.
- Full compatibility with every POSIX-oriented plugin.

Install the fork in a virtual environment, then target `localhost` with the
`local` connection. On Windows, that connection automatically uses the
PowerShell shell plugin.

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -e .
.venv\Scripts\ansible-playbook -i "localhost," -c local playbook.yml
```
