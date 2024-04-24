# ctypes-windows-sdk

A totally incomplete and random port of the C Windows SDK for Python ctypes. No dependencies besides the Python standard library.

## Install

Requires Python 3.7+.

```
pip install ctypes-windows-sdk
```

## Example

```python

from cwinsdk.windows import GetTickCount64
tickcount = GetTickCount64()
```

## Used by
- Dobatymo/public-scripts
