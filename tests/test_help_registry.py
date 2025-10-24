from app.calculator import _HELP_REGISTRY, Command

def test_help_registry_populated():
    # at least the core commands we added should be present
    expected = {"help", "history", "clear", "undo", "redo", "save", "load", "exit"}
    assert expected.issubset(set(_HELP_REGISTRY.keys()))

def test_command_subclasses_have_names():
    # all command subclasses should have a _cmd_name set by the decorator
    names = {getattr(c, "_cmd_name", None) for c in Command.__subclasses__()}
    assert "help" in names and "exit" in names