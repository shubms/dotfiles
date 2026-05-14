from xonsh.built_ins import XSH
import os

env = XSH.env
home = env["HOME"]
user_paths = [os.path.join(home, ".local", "bin")]

# PATH config
for path in user_paths:
    if path in env["PATH"]:
        env["PATH"].remove(path)
        env["PATH"].prepend(path)
    else:
        env["PATH"].prepend(path)

# XDG Base Directories
env["XDG_CACHE_HOME"] = os.path.join(home, ".cache")
env["XDG_CONFIG_HOME"] = os.path.join(home, ".config")
env["XDG_DATA_HOME"] = os.path.join(home, ".local", "share")
env["XDG_STATE_HOME"] = os.path.join(home, ".local", "state")

# Shell
env["CARGO_HOME"] = os.path.join(env["XDG_CACHE_HOME"], "cargo")
env["CONDA_BLD_PATH"] = os.path.join(env["XDG_CACHE_HOME"], "conda-build")
env["CONDA_REPO_PATH"] = os.path.join(env["XDG_CACHE_HOME"], "conda-repo")
env["EDITOR"] = "micro"
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
env["MANPAGER"] = " ".join(
    ["bat", "--style=plain", "--language=man", "--strip-ansi", "auto"]
)
env["SSH_AUTH_SOCK"] = os.path.join(
    env["HOME"],
    ".var",
    "app",
    "com.bitwarden.desktop",
    "data",
    ".bitwarden-ssh-agent.sock",
)
env["RUFF_CACHE_DIR"] = os.path.join(env["XDG_CACHE_HOME"], "ruff")
env["VISUAL"] = env["EDITOR"]
env["BASH_COMPLETIONS"].add(os.path.join(env["PIXI_HOME"], "completions","bash"), replace=True, front=True)

del env, home
