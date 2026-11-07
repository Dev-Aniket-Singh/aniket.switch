# Signal to Resolution

Signal to Resolution is a small Switch workflow for moving a checkout bug from a team report to a reproduced, reviewable fix. A triager clarifies the report and hands it to a resolver. The resolver reproduces the problem, proposes a minimal change, and posts the evidence for a person to review.

## Sample issue

A customer restores a saved cart with a `SAVE10` coupon. The coupon disappears, so a $50.00 cart returns to checkout at $50.00 instead of $45.00. The sample uses integer cents and temporary files. It has no external services or customer data.

From the project root, run:

    py -3 demo/reproduce.py

Expected output before the fix:

    subtotal_cents: 5000
    coupon: SAVE10
    expected_total_cents: 4500
    actual_total_cents: 5000
    result: BUG REPRODUCED

The bug is in `load_cart`, which drops the saved coupon. The intended fix preserves it. After the fix, the reproduction should report an actual total of 4500 cents.

## Run the workflow in Switch

1. Install Switch Console and Docker, then configure a coding-agent provider using the [Switch quickstart](https://www.wemakedevs.org/hackathons/switch/resources).
2. Import `switch/triage-pair.template.yaml` in Console. Choose a team name, your configured provider, and the local Mattermost bridge for a reproducible demo.
3. Open the resolver agent's working folder and copy in `demo/checkout.py` and `demo/reproduce.py`. Switch gives agents separate working folders.
4. Open the room and paste the report from `demo/ISSUE.md`.
5. Review the resolver's diff and reproduction output in the room. A person makes the final approval decision.

The template defines the room and agent roles. The sample code is deliberately small so the workflow and handoff remain clear in the demo.

## Why Switch matters here

The report, triage decision, agent handoff, reproduction output, proposed change, and human review share one room history. The shared room carries the context as the work moves between people and agents.

## Project files

- `switch/triage-pair.template.yaml` — Switch Console template with triager and resolver agents.
- `demo/checkout.py` — checkout model containing the seeded restore bug.
- `demo/reproduce.py` — dependency-free reproduction script.
- `demo/ISSUE.md` — report to paste into the room.
- `submission/project-description.md` — short project summary.
- `submission/demo-script.md` — spoken narration and screen cues for the video.
- `submission/blog-draft.md` — project walkthrough.
- `submission/social-post.md` — short project post.

Python 3.9 or later is required. The sample uses only the Python standard library.

## References

- [Switch quickstart and resources](https://www.wemakedevs.org/hackathons/switch/resources)
- [Official triage-pair template](https://github.com/sandbox-quantum/switch/blob/main/examples/agent-templates/triage-pair.template.yaml)
- [Switch framework documentation](https://docs.switchagents.ai/switch-rooms/building/index)
