# Sample issue: coupon disappears after cart restore

**Type:** Bug  
**Impact:** A shopper who saves and restores a cart loses the discount at checkout.  
**Scope:** Preserve the saved coupon when the cart is restored. Do not change other checkout behavior.

## Reproduction

1. From the project root, run `python demo/reproduce.py`.
2. The demo saves a 5000-cent cart with coupon `SAVE10`, restores it, and calculates the total.

## Expected

The coupon remains attached to the restored cart and the total is 4500 cents.

## Actual

The restored cart loses the coupon and the total remains 5000 cents.

## Requested outcome

Please reproduce this in the resolver's workspace, post the exact output in the Switch room, make the smallest fix, run the reproduction again, and post the diff and exact output for a person to review. Do not merge or deploy.
