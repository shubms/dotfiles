with open(p"~/.config/restic/exclude") as _exclude_file:
    _restic_exclude = _exclude_file.read().split()

_dua_exclude = " -i ".join(_restic_exclude).split()
