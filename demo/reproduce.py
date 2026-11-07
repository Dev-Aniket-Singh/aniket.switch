"""Print a deterministic reproduction for the intentionally broken cart restore."""

from pathlib import Path
from tempfile import TemporaryDirectory

from checkout import checkout_total_cents, load_cart, save_cart


def main() -> None:
    original_cart = {"subtotal_cents": 5000, "coupon": "SAVE10"}
    expected_total = 4500

    with TemporaryDirectory() as temp_dir:
        saved_path = Path(temp_dir) / "cart.json"
        save_cart(original_cart, saved_path)
        restored_cart = load_cart(saved_path)
        actual_total = checkout_total_cents(restored_cart)

    print(f"subtotal_cents: {original_cart['subtotal_cents']}")
    print(f"coupon: {original_cart['coupon']}")
    print(f"expected_total_cents: {expected_total}")
    print(f"actual_total_cents: {actual_total}")
    print("result: BUG REPRODUCED" if actual_total != expected_total else "result: BUG NOT REPRODUCED")


if __name__ == "__main__":
    main()
