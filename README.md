# 🧬 StructViz Pro

**A real-time 3D protein visualization tool.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://struct-viz-pro.streamlit.app/)

## 📌 Overview
**StructViz Pro** is an interactive bioinformatics tool that allows researchers and students to visualize 3D protein structures directly in the browser. It integrates with the **RCSB PDB** database to fetch structures instantly or accepts local `.pdb` file uploads for custom analysis.

## 🚀 Key Features
* **Dual Input System:** Fetch real-time data from RCSB PDB using 4-character IDs (e.g., `1AON`, `6LU7`) or upload local files.
* **3D Rendering Engine:** Built on `py3Dmol` and `stmol` for high-performance WebGL visualization.
* **Multi-Style View:** Switch between **Cartoon** (secondary structure), **Stick** (bond connectivity), and **Sphere** (Van der Waals radii) modes.
* **Customization:** Interactive color pickers and spin animation controls.

## 🛠️ Tech Stack
* **Python 3.9+**
* **Streamlit** (Frontend)
* **py3Dmol** (Molecular visualization)
* **stmol** (Streamlit component wrapper)

## 💻 How to Run Locally
If you want to run this tool on your own machine:

1. **Clone the repository**
    ```bash
   git clone https://github.com/my-user-name/protein-visualizer.git
   ```
   
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the app**
    ```bash
    streamlit run app.py
    ```

## 👨‍🔬 Author
**Monika Yadav**
* MSc Bioinformatics Candidate
* BSc (Hons.)/MSc Biotechnology

[LinkedIn](will add soon) | [GitHub](https://github.com/rao-monika-yadav)

---

*Disclaimer: This tool is intended for research and educational purposes only.*
