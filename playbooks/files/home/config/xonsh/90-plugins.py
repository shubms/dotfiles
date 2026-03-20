import subprocess

from xonsh.built_ins import XSH
from xonsh.built_ins import DynamicAccessProxy

_env = XSH.env
_execx = DynamicAccessProxy

_env["CARAPACE_BRIDGES"] = "zsh,fish,bash,inshellisense"
_env["COMPLETIONS_CONFIRM"] = True
_starship = subprocess.run(
    ["/usr/bin/env", "starship", "init", "xonsh"], capture_output=True, text=True
)
# execx(_starship.stdout)
_zoxide = subprocess.run(
    ["/usr/bin/env", "zoxide", "init", "xonsh"], capture_output=True, text=True
)
execx(_zoxide.stdout)
_carapace = subprocess.run(
    ["/usr/bin/env", "carapace", "_carapace"], capture_output=True, text=True
)
execx(_carapace.stdout)

del _env, _execx
