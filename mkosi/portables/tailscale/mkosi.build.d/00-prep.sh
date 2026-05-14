#!/bin/sh
set -ex

mkdir -p "${DESTDIR}/etc" \
         "${DESTDIR}/var/cache/tailscale" \
         "${DESTDIR}/var/lib/tailscale"
cp /usr/lib/os-release "${DESTDIR}"/etc/os-release
cat >> "${DESTDIR}/etc/os-release" <<EOF
PORTABLE_PRETTY_NAME="Tailscale Portable Service"
EOF

touch "${DESTDIR}/etc/resolv.conf"
