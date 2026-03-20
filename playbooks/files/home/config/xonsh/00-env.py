from xonsh.built_ins import XSH

env = XSH.env
home = env["HOME"]
user_paths = [home + "/.local/bin"]

# PATH config
for path in user_paths:
    if path in env["PATH"]:
        env["PATH"].remove(path)
        env["PATH"].prepend(path)

# XDG Base Directories
env["XDG_CACHE_HOME"] = home + "/.cache"
env["XDG_CONFIG_HOME"] = home + "/.config"
env["XDG_DATA_HOME"] = home + "/.local/share"
env["XDG_STATE_HOME"] = home + "/.local/state"

# Shell
env["CARGO_HOME"] = env["XDG_STATE_HOME"] + "/cargo"
env["CONDA_BLD_PATH"] = env["XDG_STATE_HOME"] + "/conda-build"
env["EDITOR"] = "hx"
env["EZA_ALIAS_OPTS"] = [
    "--all",
    "--binary",
    "--color-scale=all",
    "--git",
    "--group",
    "--group-directories-first",
    "--header",
    "--hyperlink",
    "--long",
    "--mounts",
]
env["EZA_ICONS_AUTO"] = 1
env["EZA_ICON_SPACING"] = 1
env["MANPAGER"] = "bat -plman --strip-ansi auto"
env["VISUAL"] = env["EDITOR"]

del env, home
