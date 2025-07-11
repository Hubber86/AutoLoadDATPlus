# AutoLoadDATPlus Plugin for QGIS

![QGIS](https://img.shields.io/badge/QGIS-3.14+-green?logo=qgis)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![License](https://img.shields.io/github/license/Hubber86/AutoLoadDATPlus)
![Last Commit](https://img.shields.io/github/last-commit/Hubber86/AutoLoadDATPlus)
![Issues](https://img.shields.io/github/issues/Hubber86/AutoLoadDATPlus)

**AutoLoadDATPlus** is a QGIS plugin that enables users to automatically load `.dat` files (containing space-separated numeric data) as point layers in QGIS. It intelligently pre-processes the files, cleans and converts them into a tab-delimited format, and automatically maps the relevant fields to X, Y, and Z coordinates.

---

## 📦 Features

- ✅ One-click loading of multiple `.dat` files
- 🧹 Automatic cleaning and conversion to tab-delimited `.csv`
- 🧭 Field mapping:
  - X = `field_3`
  - Y = `field_2`
  - Z = `field_4`
- 🔍 Auto zoom to layer extent
- 🐞 Console debug information
- 💻 Compatible with QGIS 3.14 and above

---

## 📂 File Format Assumption

The plugin assumes that `.dat` files are formatted with space-separated numeric values, such as:

```
457144.118 31.7392607788 35.2061274441 809.387 2 183.9222271698 0.063 0.079 8.5190840091 0.0252549736
```


There is no header row, and all values are numeric.

---

## 🛠 Installation

1. Clone or download this repository.
2. Copy the plugin folder into your QGIS plugin directory:

   - **Windows**:  
     `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins`
   - **Linux/macOS**:  
     `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`

3. Restart QGIS and enable **AutoLoadDATPlus** in the Plugin Manager.

---
## 📂 File Structure
```
AutoLoadDATPlus/
├── AutoLoadDATPlus.py # Main plugin code
├── init.py # Initializes the plugin for QGIS
├── metadata.txt # QGIS plugin metadata (required)
├── icon.png # Plugin icon (optional, 16x16 or 32x32)
├── README.md # Project documentation (this file)
└── LICENSE # License file (e.g., MIT)
```
---
## ✅ Requirements

- QGIS 3.14 Pi or newer
- Python 3 (comes with QGIS)
- No external dependencies

---
## 🚀 Usage

1. Open QGIS and go to:  
   `Plugins > AutoLoadDATPlus > Load .DAT File`
2. Select one or more `.dat` files.
3. The plugin will preprocess and load each as a point layer.

---
## 🔧 How It Works

1. Prompts the user to select one or more `.dat` files.
2. Preprocesses each file:
   - Cleans extra whitespace
   - Converts to tab-delimited temporary file
3. Loads the processed file using QGIS's Delimited Text provider.
4. Automatically sets:
   - `field_3` as X coordinate
   - `field_2` as Y coordinate
   - `field_4` as Z value
5. Adds the layer to the map and zooms to its extent.

---
## 📸 Example Output

After loading:

- Points will be visualized as a new layer
- QGIS zooms automatically to the new layer's extent
- Console logs show detailed debug info

### 🔧 Sample Debug Console Output

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
---

## 🛠 Developer Notes

- Designed for datasets where latitude, longitude, and elevation are embedded as space-separated values.
- Automatically detects structure—no need for headers or consistent delimiters.

---
## ✅ Tested Environment

- **QGIS**: Version 3.14 (Pi) and above  
- **Operating System**: Windows (should also work on macOS/Linux if file paths are correctly set)  
- **Python**: Version 3.x
---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Make sure to follow the project's coding standards and commit message guidelines, if any.

Thank you for helping improve this project!
---

## 🧑‍💻 Author

Developed by [Prajwal Kalashetty](https://github.com/Hubber86)

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

© 2025 Prajwal Kalashetty
