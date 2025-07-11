from qgis.PyQt.QtWidgets import QAction, QFileDialog, QMessageBox
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsVectorLayer, QgsProject
import csv
import os
import tempfile
import re

class AutoLoadDATPlusPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def initGui(self):
        self.action = QAction(QIcon(), "4.0 Load .DAT File (AutoLoadDATPlus)", self.iface.mainWindow())
        self.action.triggered.connect(self.load_dat_files)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("4.0 AutoLoadDATPlus", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("4.0 AutoLoadDATPlus", self.action)

    def load_dat_files(self):
        file_paths, _ = QFileDialog.getOpenFileNames(None, "Select .dat Files", "", "DAT Files (*.dat)")
        for file_path in file_paths:
            self.preprocess_and_load(file_path)

    def preprocess_and_load(self, file_path):
        layer_name = os.path.splitext(os.path.basename(file_path))[0]

        # Read and split using regex
        with open(file_path, 'r') as f:
            lines = f.readlines()

        cleaned_rows = []
        for line in lines:
            parts = re.split(r"\s+", line.strip())
            if len(parts) >= 4:
                cleaned_rows.append(parts)

        if not cleaned_rows:
            QMessageBox.warning(None, "AutoLoadDATPlus", f"No valid data found in file: {file_path}")
            return

        print("Sample cleaned row:", cleaned_rows[0])  # debug

        # Save as UTF-8 tab-delimited CSV
        tmp_path = tempfile.mktemp(suffix=".csv")
        with open(tmp_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
            writer.writerows(cleaned_rows)

        # Use actual '\t' instead of %09
        uri = (
            f"file:///{tmp_path}?type=csv&"
            "delimiter=\\t&"
            "xField=field_3&"
            "yField=field_2&"
            "zField=field_4&"
            "header=no&"
            "crs=EPSG:4326&"
            "detectTypes=yes&"
            "geomType=point"
        )

        layer = QgsVectorLayer(uri, layer_name, "delimitedtext")

        # Debug info
        print("=== DEBUG ===")
        print("URI:", uri)
        print("Valid:", layer.isValid())
        print("Fields:", [f.name() for f in layer.fields()])
        print("Feature Count:", layer.featureCount())
        for feat in layer.getFeatures():
            print("Sample Feature:", feat.attributes())
            break
        print("==========================")

        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
            self.iface.mapCanvas().setExtent(layer.extent())
            self.iface.mapCanvas().refresh()
        else:
            QMessageBox.warning(None, "AutoLoadDATPlus", f"Failed to load: {layer_name}\nCheck file format.")
