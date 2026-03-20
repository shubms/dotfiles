from xonsh.built_ins import XSH
import keyring
import subprocess
import os

env = XSH.env
aliases = XSH.aliases
home = env["HOME"]


def _resticb(args):
    restic_env = os.environ.copy()
    restic_env["B2_ACCOUNT_ID"] = keyring.get_password("restic", "b2-id")
    restic_env["B2_ACCOUNT_KEY"] = keyring.get_password("restic", "b2-key")
    restic_env["RESTIC_FROM_PASSWORD_COMMAND"] = "keyring get restic password"
    restic_env["RESTIC_FROM_REPOSITORY"] = (
        "b2:" + keyring.get_password("restic", "b2-repo") + ":/"
    )
    restic_env["RESTIC_PASSWORD_COMMAND"] = restic_env["RESTIC_FROM_PASSWORD_COMMAND"]
    restic_env["RESTIC_REPOSITORY"] = restic_env["RESTIC_FROM_REPOSITORY"]
    subprocess.run(["restic"] + args, env=restic_env)
    return


aliases["resticb"] = _resticb


env["RESTIC_EXCLUDE_DIRS"] = [
    ".cache",
    ".local/share/containers",
    ".local/share/flatpak",
    ".local/share/zed",
    ".mozilla",
    ".var",
    "Documents",
    "Downloads",
    "Media",
    "Music",
    "Public",
]
env["RESTIC_EXCLUDE_OPTS"] = " -e " + " -e ".join(
    [env["HOME"] + "/" + i for i in env["RESTIC_EXCLUDE_DIRS"]]
)
env["NCDU_IGNORE_OPTS"] = " --exclude " + " --exclude ".join(env["RESTIC_EXCLUDE_DIRS"])
env["RESTIC_FROM_PASSWORD_COMMAND"] = "keyring get restic password"
env["RESTIC_FROM_REPOSITORY"] = home + "/Public/restic"
env["RESTIC_PASSWORD_COMMAND"] = env["RESTIC_FROM_PASSWORD_COMMAND"]
env["RESTIC_REPOSITORY"] = env["RESTIC_FROM_REPOSITORY"]

del env, home
