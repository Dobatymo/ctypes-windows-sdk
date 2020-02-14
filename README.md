# ctypes-windows-sdk

A totally incomplete and random port of the C Windows SDK for Python ctypes. No dependencies besides the Python standard library.

## Install

```
pip install ctypes-windows-sdk
```

## Example

```python

from cwinsdk.windows import GetTickCount64
tickcount = GetTickCount64()
```
