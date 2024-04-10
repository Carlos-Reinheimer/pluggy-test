import pluggy

hookimpl = pluggy.HookimplMarker("texteditorapplication")
"""Marker to be imported and used in plugins (and for own implementations)"""