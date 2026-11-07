"""Tool contracts with explicit pre/post conditions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class ToolContract:
    name: str
    precondition: Callable
    invoke: Callable
    postcondition: Callable
    effects: Callable

    @classmethod
    def simple(cls, name, required, fn):
        def pre(state, args):
            return all(key in args for key in required)

        def post(state, args, result):
            return isinstance(result, dict) and "ok" in result

        return cls(
            name=name,
            precondition=pre,
            invoke=lambda state, args: fn(**args),
            postcondition=post,
            effects=lambda result: {"last_result": result},
        )
