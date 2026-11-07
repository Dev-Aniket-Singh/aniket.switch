# Signal to Resolution

**Track:** Best Business Workflow

Signal to Resolution is a Switch room template for a small support team. A triager turns a checkout report into a clear handoff; a resolver reproduces the bug, proposes a minimal fix, and posts the exact result for human review.

The included sample demonstrates a realistic failure: restoring a saved cart drops its `SAVE10` coupon. A $50.00 cart then returns to checkout at $50.00 instead of $45.00. The dependency-free Python reproduction prints the expected and actual totals. The Switch template defines the shared room and two agent roles so the report, handoff, reproduction, proposed change, and review stay together.

The person remains responsible for reviewing the diff and deciding whether to merge. The workflow does not merge or deploy automatically.
