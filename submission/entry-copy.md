# Signal to Resolution

**Track:** Best Business Workflow

Signal to Resolution is a Switch room template for a small support team. A triager turns a checkout report into a clear handoff; a resolver reproduces the bug, proposes a minimal fix, and posts the exact result for human review.

The sample demonstrates a saved cart losing its `SAVE10` coupon after restore. The cart is worth 5000 cents; the expected total is 4500 cents, but the restored cart returns 5000 cents. The dependency-free Python reproduction shows both totals. The Switch template defines the shared room and two agent roles so the report, handoff, reproduction, proposed change, and review stay together.

A person reviews the diff and decides whether to merge. The workflow does not merge or deploy automatically.
