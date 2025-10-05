# OOIP Calculator from Material Balance

A **Python Tkinter-based GUI** to calculate **Original Oil in Place (OOIP)** using the **Material Balance Method**. The software allows users to input reservoir and fluid properties, select a CSV production dataset, and visualize the **F vs Enet plot** with a regression line to determine OOIP.

---

## Features

- Enter reservoir and fluid properties via GUI:
  - `Boi`, `Bo`, `Bg`, `Bgi`, `Bw`, `Rsi`, `Cf`, `Cw`, `Swi`, `Pi`, `m`, `We`
- Select CSV production data file directly from the current working directory.
- Calculate OOIP using **Material Balance equations**.
- Plot **F vs Enet** graph with a regression line and slope (OOIP value) annotated.
- User-friendly input validation for numeric values and CSV selection.

---

## Requirements

- Python 3.6+
- Packages:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `tkinter` (usually included in standard Python installation)

Install missing packages with pip:

```bash
pip install pandas numpy matplotlib
```
## File Structure

- OOIP_Calculator/
  - `production_data.csv` – CSV with Np, Rp, Rs, Wp, P columns
  - `ooip_calculator.py` – Main Python script 
  - `README.md` – This file

## Usage

1. **Place CSV production data**  
   Ensure your CSV file containing production data (`Np`, `Rp`, `Rs`, `Wp`, `P`) is in the same directory as the script.

2. **Run the Python script**  

```bash
python ooip_calculator.py
```

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


