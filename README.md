# AutoLoadDATPlus Plugin for QGIS
# AutoLoadDATPlus

![QGIS](https://img.shields.io/badge/QGIS-3.14+-green?logo=qgis)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![License](https://img.shields.io/github/license/Hubber86/AutoLoadDATPlus)
![Last Commit](https://img.shields.io/github/last-commit/Hubber86/AutoLoadDATPlus)
![Issues](https://img.shields.io/github/issues/Hubber86/AutoLoadDATPlus)


AutoLoadDATPlus is a QGIS plugin that allows users to automatically load `.dat` files (space-separated numeric datasets) as point layers in QGIS. It intelligently pre-processes `.dat` files to clean and convert them into a format compatible with QGIS, mapping fields automatically to X, Y, and Z coordinates.

## 📦 Features

- One-click loading of multiple `.dat` files
- Automatic cleaning and conversion to tab-delimited format
- X/Y/Z field mapping (e.g., X = field_3, Y = field_2, Z = field_4)
- Auto zoom to layer extent
- Debug info printed to console
- Compatible with QGIS 3.x (tested with 3.14+)

## 📂 File Format Assumption

The plugin expects `.dat` files with whitespace-separated numeric values like:
```
457144.118 31.7392607788 35.2061274441 809.387 2 183.9222271698 0.063 0.079 8.5190840091 0.0252549736
```

## 🛠 Installation

1. Clone or download this repository.
2. Copy the plugin folder into your QGIS plugin directory:
   - Windows: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
3. Restart QGIS and enable "AutoLoadDATPlus" in Plugin Manager.

## 🚀 Usage

1. In QGIS, go to `Plugins > 4.0 AutoLoadDATPlus > Load .DAT File`.
2. Select one or more `.dat` files.
3. The plugin will preprocess and add each file as a point layer.

## 📸 Example

After loading:
- The data will appear as point geometry
- The layer extent is automatically set
- Console logs show URI, validity, feature count, and sample rows

## 🔧 Debug Console Output

Example:
```
=== DEBUG ===
URI: file:///.../tmp123abc.csv?type=csv&delimiter=\t&xField=field_3&yField=field_2&zField=field_4&header=no&...
Valid: True
Fields: ['field_1', 'field_2', 'field_3', 'field_4', ...]
Feature Count: 43438
Sample Feature: [457144.237, 31.739251728, 35.2061274014, ...]
==========================
```
🛠️ Developer Notes
Built for datasets where latitude, longitude, and elevation are embedded as space-separated values.

Auto-detects structure without needing headers or consistent tabs.

## 🧑‍💻 Author

Developed by [Prajwal Kalashetty](https://github.com/Hubber86)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

© 2025 Prajwal Kalashetty
