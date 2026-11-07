"""Tiny checkout model for the Signal to Resolution demo."""

import json
from pathlib import Path
from typing import Any


def save_cart(cart: dict[str, Any], path: Path) -> None:
    path.write_text(json.dumps(cart), encoding="utf-8")


def load_cart(path: Path) -> dict[str, Any]:
    saved = json.loads(path.read_text(encoding="utf-8"))
    return {
        "subtotal_cents": int(saved["subtotal_cents"]),
        "coupon": None,
    }


def checkout_total_cents(cart: dict[str, Any]) -> int:
    subtotal = int(cart["subtotal_cents"])
    if cart.get("coupon") == "SAVE10":
        return subtotal - subtotal // 10
    return subtotal
