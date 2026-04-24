# pymcu-avr-toolchain

Pre-built AVR-GCC toolchain for PyMCU, packaged as a Python wheel for easy installation.

Includes: `avr-gcc`, `avr-g++`, `avr-as`, `avr-ld`, `avr-ar`, `avr-objcopy`, `avr-objdump`, `avr-size`, `avr-nm`, `avr-strip`, `avr-ranlib`, `avr-gdb`, and the AVR-LibC headers/libraries.

## Installation

```bash
pip install pymcu-avr-toolchain
```

## Usage

```python
import pymcu_avr_toolchain

bin_dir = pymcu_avr_toolchain.get_bin_dir()
print(bin_dir)  # Path to the bin/ directory containing avr-gcc, avr-as, etc.
```

Or use the CLI helper:

```bash
pymcu-avr-toolchain-info
```

## Toolchain versions

| Component | Version |
|-----------|---------|
| AVR-GCC   | 15.2.0  |
| Binutils  | 2.45    |
| GDB       | 16.3    |
| AVR-LibC  | 2.2.1   |

## Source

Built from [ZakKemble/avr-gcc-build](https://github.com/ZakKemble/avr-gcc-build) and packaged by [PyMCU](https://github.com/PyMCU/avr-gcc-build).

## License

GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-2-Clause
