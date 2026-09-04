import json
import pytest
from pathlib import Path

# Load dataset from data directory
DATA_FILE = Path(__file__).parent.parent / "data" / "mock_manuscripts.json"

def load_manuscripts():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.mark.parametrize("manuscript", load_manuscripts())
def test_manuscript_integrity_audit(manuscript):
    # Ensure corrupted or forbidden knowledge data is properly flagged
    if manuscript["is_corrupted"]:
        assert manuscript["access_level"] == "Grand Sage", f"Security breach: {manuscript['title']} has improper access level!"
    else:
        assert manuscript["is_corrupted"] is False, f"Valid manuscript {manuscript['title']} incorrectly flagged as corrupted!"