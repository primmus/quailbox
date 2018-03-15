#!/bin/sh

BRIDGE=qemubr0
TAP=tap_qemu
NETWORK=192.168.3.0
NETMASK=255.255.255.0
GATEWAY=192.168.3.1
DHCPRANGE=192.168.3.2,192.168.3.254

setup_bridge_nat() {
    if ! brctl show | grep "^$1" > /dev/null 2> /dev/null; then
        brctl addbr "$1"
        brctl stp "$1" off
        brctl setfd "$1" 0
        ifconfig "$1" "$GATEWAY" netmask "$NETMASK" up
    fi
}

setup_bridge_nat "$BRIDGE"
tunctl -b -u "$USER" -t "$TAP"
ip link set "$TAP" master "$BRIDGE"
ip link set dev "$TAP" up
ip link set dev "$BRIDGE" up
