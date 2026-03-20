from xonsh.built_ins import XSH
from xonsh.tools import register_custom_style

env = XSH.env
catppuccin = {
    "Literal.String.Single": "#ff88aa",
    "Literal.String.Double": "#ff4488",
    "RED": "#008800",
}

# register_custom_style("catppuccin", catppuccin, base="nord")

# env["XONSH_COLOR_STYLE"] = "catppuccin"

del env
