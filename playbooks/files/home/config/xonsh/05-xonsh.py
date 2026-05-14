from xonsh.built_ins import XSH

env = XSH.env

# HISTORY
env["HISTCONTROL"] = set(("ignoredups", "ignorespace"))
env["XONSH_HISTORY_BACKEND"] = "sqlite"
env["XONSH_HISTORY_SIZE"] = (2**20, "commands")

# PROMPT
env["CASE_SENSITIVE_COMPLETIONS"] = False
env["CMD_COMPLETIONS_SHOW_DESC"] = True
env["COMMANDS_CACHE_SAVE_INTERMEDIATE"] = True
env["DYNAMIC_CWD_WIDTH"] = (20.0, "%")
env["ENABLE_ASYNC_PROMPT"] = True
env["RIGHT_PROMPT"] = "{localtime}"
env["XONSH_AUTOPAIR"] = True
env["XONSH_COLOR_STYLE"] = "native"
env["XONSH_COMPLETER_EMOJI_PREFIX"] = "::"
env["XONSH_HISTORY_MATCH_ANYWHERE"] = True

# DIRNAV
env["AUTO_CD"] = True
env["AUTO_PUSHD"] = True

del env
