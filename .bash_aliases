#!/usr/bin/env sh

# ~/.bash_aliases
# Alias definitions.

alias b='batcat --style full --wrap never'
alias c='batcat --style plain --paging never'
alias e='$EDITOR'
alias g=git
alias jc=journalctl
alias jcu='journalctl --user'
alias le='eza --all --color-scale all --group-directories-first --hyperlink --icons --binary --git --group --header --long --mounts --smart-group --sort extension'
alias l='eza --all --color-scale all --group-directories-first --hyperlink --icons --binary --git --group --header --long --mounts --smart-group'
alias l@='eza --all --color-scale all --group-directories-first --hyperlink --icons --binary --git --group --header --long --mounts --smart-group --extended'
alias lm='eza --all --color-scale all --group-directories-first --hyperlink --icons --binary --git --group --header --long --mounts --smart-group --sort modified'
alias lsd='eza --all --color-scale all --group-directories-first --hyperlink --icons --binary --git --group --header --long --mounts --smart-group --sort size --total-size'
alias lz='eza --all --color-scale all --group-directories-first --hyperlink --icons --binary --git --group --header --long --mounts --smart-group --context'
alias ncdu='ncdu --color dark'
alias pm=podman
alias rng=ranger
alias rstb=_restic_b2
alias rst=restic
alias sc=systemctl
alias scu='systemctl --user'
