import pytest

# Akademiya Darshan Privilege Matrix
ROLE_LEVELS = {
    "Student": 1,
    "Researcher": 3,
    "Grand Sage": 5
}

@pytest.mark.parametrize("role,required_level,expected_result", [
    ("Student", 1, True),
    ("Student", 5, False),
    ("Researcher", 3, True),
    ("Researcher", 5, False),
    ("Grand Sage", 5, True)
])
def test_akademiya_rbac_security(role, required_level, expected_result):
    user_level = ROLE_LEVELS.get(role, 0)
    has_permission = user_level >= required_level
    assert has_permission == expected_result, f"Privilege escalation vulnerability detected for role: {role}!"