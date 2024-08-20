#!/usr/bin/env sh

# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

# XDG
export XDG_CACHE_HOME="${HOME}/.cache"
export XDG_CONFIG_HOME="${HOME}/.config"
export XDG_DATA_HOME="${HOME}/.local/share"
export XDG_STATE_HOME="${HOME}/.local/state"

# EDITOR
export EDITOR="hx"
export VISUAL="hx"

# SHELL
MANPAGER="sh -c 'col -bx | batcat -l man -p'"

# APP_HOMES
export CARGO_HOME="${XDG_CACHE_HOME}/cargo"
export GNUPGHOME="${XDG_CONFIG_HOME}/gnupg"
export RUSTUP_HOME="${XDG_CACHE_HOME}/rustup"

# RESTIC
export RESTIC_REPOSITORY="/media/restic"
export RESTIC_PASSWORD_FILE="${XDG_CONFIG_HOME}/restic/pass"
export RESTIC_FROM_REPOSITORY="/media/restic"
export RESTIC_FROM_PASSWORD_FILE="${XDG_CONFIG_HOME}/restic/pass"
