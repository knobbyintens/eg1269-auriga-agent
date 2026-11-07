# Auriga-Agent

Tool-using agent with mechanically verifiable execution traces.

## Layout

- `src/agent/controller.py` - planner / executor loop
- `src/agent/tools.py` - tool contracts with preconditions and postconditions
- `data/execution_tasks.jsonl` - task suite used in the paper
- `experiments/ablation.md` - ablation of trace verification

## Running

```
python -m agent.controller --tasks data/execution_tasks.jsonl
```

Released under the MIT license.
