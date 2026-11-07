# Signal to Resolution: video narration

## Opening

“Hi, this is Signal to Resolution. It shows how a small support team can take a checkout bug from the first report to a reviewed fix using Switch.

“The example is simple. A customer saves a cart with a SAVE10 coupon. After the cart is restored, the coupon disappears. The cart is worth 50 dollars, so the expected total is 45 dollars, but the current total is 50.”

**On screen:** Show the project title, then the Switch room with the triager, resolver, and human participant visible.

## Intake and handoff

“I’m posting the issue in the room. The triager restates the problem, checks the expected and actual results, and hands the bug to the resolver. The report and handoff are visible in the same conversation.”

**On screen:** Paste `demo/ISSUE.md`. Show the triager's classification and its message to the resolver.

## Reproduce the bug

“The resolver is working in its own folder. It runs the reproduction and posts the exact output. We can see the saved coupon, the expected total of 4500 cents, and the actual total of 5000 cents.”

**On screen:** Show the resolver run and the output in the room.

## Show the fix

“The cause is in the cart restore step. It saves the subtotal but drops the coupon. The resolver makes a small change to preserve that value, then runs the same reproduction again. The total is now 4500 cents.”

**On screen:** Show the changed code, the diff, and the new reproduction output.

## Human review

“I’m reviewing the diff and the output before approving anything. The agent proposes the change, but a person decides whether it is ready to merge. Nothing is deployed automatically.”

**On screen:** Review the diff in the room and state your actual decision. Do not show an approval if you have not approved the change.

## Close

“Signal to Resolution keeps the report, agent handoff, reproduction, proposed fix, and human review together in a Switch room. That gives the team one visible path from a customer problem to a decision.”

**On screen:** End on the room history with the report, handoff, reproduction, diff, and review visible.
