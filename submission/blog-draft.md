# From a lost coupon to a clear team handoff

A small checkout bug is rarely just a code change. Someone reports it, a teammate asks for details, another person tries to reproduce it, and the evidence can end up scattered across separate conversations.

Signal to Resolution makes that handoff visible. Its sample issue is simple: a shopper saves a cart with the `SAVE10` coupon, restores it later, and the discount is gone. The subtotal is 5000 cents; the expected total is 4500 cents; the restored cart incorrectly returns 5000 cents.

The project includes a tiny Python checkout model and a reproduction script. The bug is isolated in the restore path, which drops the coupon. This gives the workflow a concrete task with an observable starting state and a small proposed fix.

The Switch Console template creates two agents in a shared room. The triager restates the report, gathers missing details, and hands a bug to the resolver. The resolver works in its own folder, runs the reproduction, posts the exact output, makes a minimal change, and reports the new output and diff. A person reviews the evidence before any merge.

That shared room is the point of the build. The issue, the handoff, and the agent's evidence remain attached to the same conversation. A teammate can see what was asked, what was tried, and what still needs review without reconstructing the story from separate chats.

To try the sample, run `py -3 demo/reproduce.py` from the project root. To run the workflow in Switch, install Switch Console and Docker, configure an agent provider, import `switch/triage-pair.template.yaml`, and choose a chat bridge. Copy the two files from `demo/` into the resolver's working folder, then paste `demo/ISSUE.md` into the room.

The workflow ends with a review decision, not an automatic deployment. It helps a small team carry one real report through a visible, evidence-backed handoff.
