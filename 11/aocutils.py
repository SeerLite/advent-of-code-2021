from __future__ import annotations
from collections.abc import Collection
from itertools import count

DEBUG: bool = False
USE_EXAMPLE_INPUT: bool = False
EXAMPLE_OUTPUTS: Collection[int]

def printd(*args, **kwargs) -> None: # type: ignore
    if DEBUG:
        print(*args, **kwargs)

def assert_outputs(outputs: Collection[int]) -> None:
    if not USE_EXAMPLE_INPUT:
        return

    if DEBUG and len(EXAMPLE_OUTPUTS) == 0:
        printd("No example outputs provided")

    for i, output, example_output in zip(count(1), outputs, EXAMPLE_OUTPUTS):
        assert output == example_output, (
            f"output {i} doesn't match with one from official example: got {output},"
            "should be {example_output}"
        )

    assert len(outputs) >= len(EXAMPLE_OUTPUTS), (
        f"got only {len(outputs)} out of {len(EXAMPLE_OUTPUTS)} outputs"
    )
