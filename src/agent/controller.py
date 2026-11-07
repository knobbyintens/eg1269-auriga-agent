"""Planner / executor loop for Auriga-Agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, List

from agent.tools import ToolContract


@dataclass
class Step:
    tool: str
    arguments: Dict[str, object]
    precondition_ok: bool
    postcondition_ok: bool


@dataclass
class Trace:
    task_id: str
    steps: List[Step] = field(default_factory=list)

    def verified(self) -> bool:
        return all(step.precondition_ok and step.postcondition_ok for step in self.steps)


class Controller:
    def __init__(self, contracts: Dict[str, ToolContract]):
        self.contracts = contracts

    def execute(self, task_id: str, plan: List[Dict[str, object]]) -> Trace:
        trace = Trace(task_id=task_id)
        state: Dict[str, object] = {}
        for action in plan:
            contract = self.contracts[action["tool"]]
            pre_ok = contract.precondition(state, action["arguments"])
            result = contract.invoke(state, action["arguments"]) if pre_ok else None
            post_ok = contract.postcondition(state, action["arguments"], result)
            trace.steps.append(
                Step(
                    tool=action["tool"],
                    arguments=dict(action["arguments"]),
                    precondition_ok=pre_ok,
                    postcondition_ok=post_ok,
                )
            )
            if pre_ok and post_ok:
                state.update(contract.effects(result))
        return trace
