# quailbox
IoT honeypotting and fuzzing framework for Cuckoo/QEMU.

### Install
```
sudo apt install qemu-system-arm
pip install quailbox
git clone https://github.com/daanfs/quailbox && cd quailbox
```

### Usage
```
Usage: quailbox [OPTIONS]

Options:
  --profile TEXT  Name of profile to run.  [required]
  --interactive   Enable interactive mode (ESC to quit).
  --help          Show this message and exit.
```

##### `quailbox --profile fritzbox --interactive`
```
[+] quailbox profile fritzbox
[+] ----------------------------- quailbox console -----------------------------
[    0.000000] Booting Linux on physical CPU 0x0
[    0.000000] Linux version 4.1.17+ (sj0rz@kookoo) (gcc version 5.3.0 (GCC) ) 
[    0.000000] CPU: ARMv7 Processor [412fc0f1] revision 1 (ARMv7), cr=10c5387d
[    0.000000] CPU: PIPT / VIPT nonaliasing data cache, PIPT instruction cache
[    0.000000] Machine model: linux,dummy-virt
[    0.000000] Memory policy: Data cache writeback
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv0.2 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] CPU: All CPU(s) started in SVC mode.
[...]

# hostname
fritz.box
# id
uid=0(root) gid=0(root)
 
```