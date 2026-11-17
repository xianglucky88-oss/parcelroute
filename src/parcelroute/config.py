
from types import SimpleNamespace

ROOT = __import__("pathlib").Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "parcelroute.db"

SPEC = SimpleNamespace(
    slug="parcelroute",
    fmt="json",
    engine="crawl",
    endpoint="items",
    columns=["id", "name", "value", "status", "ts", "carrier"],
    page_size=4,
    int_fields=["value"],
    ts_field="ts",
)
