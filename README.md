# ctypes-windows-sdk

A totally incomplete and random port of the C Windows SDK for Python ctypes. No dependencies besides the Python standard library.

## Windows SDK coverage

The shared, user-mode, and kernel-mode bindings are verified against the Windows SDK and Windows Driver Kit (WDK) `10.0.26100.0` headers, corresponding to Windows 11, version 24H2 (build 26100). The `shared` and `um` headers come from the SDK; the `km` headers come from the WDK. See Microsoft’s [Windows versions and SDK overview](https://learn.microsoft.com/en-us/windows/apps/get-started/versioning-overview) for the official version mapping.

Microsoft’s [WDK download guidance](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk) states that SDK and WDK build numbers should match for driver builds. The [supported WDK versions](https://learn.microsoft.com/en-us/windows-hardware/drivers/other-wdk-downloads) page lists the `26100` WDK family; the [WDK `10.0.26100.6584` installer](https://download.microsoft.com/download/41fb59c2-1723-45f9-a270-96b73ad58233/KIT_BUNDLE_WDK_MEDIACREATION/wdksetup.exe) is the official QFE installer for that build family.

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
