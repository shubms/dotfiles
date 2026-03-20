from xonsh.built_ins import XSH

env = XSH.env
aliases = XSH.aliases
_admin_auth = "run0"
_admin_edit = "vim"

aliases["b"] = ["bat"]
aliases["bw"] = ["flatpak", "run", "--command=bw", "com.bitwarden.desktop"]
aliases["c"] = ["bat", "--style=plain", "--paging=never"]
aliases["e"] = env["EDITOR"]
aliases["jcs"] = ["journalctl"]
aliases["jcu"] = ["journalctl", "--user"]
aliases["l"] = ["eza"] + env["EZA_ALIAS_OPTS"]
aliases["s"] = [_admin_auth]
aliases["sc"] = [_admin_auth, "bat"]
aliases["se"] = [_admin_auth, _admin_edit]
aliases["sys"] = ["systemctl"]
aliases["syu"] = ["systemctl", "--user"]
aliases["vnstat"] = ["podman", "exec", "-it", "vnstat", "vnstat"]
aliases["x"] = ["xdg-open"]

del aliases, env
