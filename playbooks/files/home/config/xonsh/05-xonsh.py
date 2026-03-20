from xonsh.built_ins import XSH

env = XSH.env

# History
env["HISTCONTROL"] = "erasedups"
env["XONSH_HISTORY_BACKEND"] = "sqlite"
env["XONSH_HISTORY_SIZE"] = (2**20, "commands")

# Xonsh
env["AUTO_CD"] = True
env["AUTO_PUSHD"] = True
env["CASE_SENSITIVE_COMPLETIONS"] = False
env["COMMANDS_CACHE_SAVE_INTERMEDIATE"] = True
env["DYNAMIC_CWD_WIDTH"] = (20.0, "%")
env["ENABLE_ASYNC_PROMPT"] = True
env["RIGHT_PROMPT"] = "{localtime}"
env["XONSH_AUTOPAIR"] = True
env["XONSH_AUTOPAIR"] = True
env["XONSH_COLOR_STYLE"] = "native"
env["XONSH_HISTORY_MATCH_ANYWHERE"] = True

del env
