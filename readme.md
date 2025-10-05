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

### 1. Prepare Your Data

Create a CSV file with the following columns:

| Column | Description | Unit |
|--------|-------------|------|
| `Np` | Cumulative oil production | STB |
| `Rp` | Cumulative produced GOR | SCF/STB |
| `Rs` | Solution GOR | SCF/STB |
| `Wp` | Cumulative water production | STB |
| `P` | Reservoir pressure | psi |

**Example CSV format:**

```csv
Np,Rp,Rs,Wp,P
1000,550,500,100,2950
2000,560,490,250,2900
3000,575,480,400,2850
```

### 2. Run the Application

```bash
python ooip_calculator.py
```

### 3. Enter Reservoir Properties

The GUI allows you to modify the following reservoir properties:

| Property | Description | Unit |
|----------|-------------|------|
| `Boi`   | Initial oil formation volume factor | RB/STB |
| `Bo`    | Oil formation volume factor         | RB/STB |
| `Bg`    | Gas formation volume factor         | RB/SCF |
| `Bgi`   | Initial gas formation volume factor | RB/SCF |
| `Bw`    | Water formation volume factor       | RB/STB |
| `Rsi`   | Initial solution GOR               | SCF/STB |
| `Cf`    | Formation compressibility           | psi⁻¹ |
| `Cw`    | Water compressibility               | psi⁻¹ |
| `Swi`   | Initial water saturation           | fraction |
| `Pi`    | Initial reservoir pressure         | psi |
| `m`     | Gas cap to oil volume ratio        | dimensionless |
| `We`    | Cumulative water influx            | RB |

### 4. Select CSV File

Choose your production data file from the dropdown menu. The application automatically detects all CSV files in the current directory.

### 5. Calculate OOIP

Click the **"Calculate OOIP"** button to generate results.

## Output

The application generates:

- A plot showing F vs Enet with data points
- Linear regression line overlaid on the plot
- **OOIP value** displayed as the slope of the regression line (in STB)
- Regression equation details

## Mathematical Background

The application implements the material balance equation:

### Main Equation

```
F = N × Enet
```

Where **N** (OOIP) is the slope of the F vs Enet plot.

### F - Underground Withdrawal

```
F = Np × Bo + Np × (Rp - Rs) × Bg + Wp × Bw
```

### Enet - Net Expansion

```
Enet = Eo + m × Eg + (1 + m) × Er + We
```

Where:

**Oil Expansion (Eo):**
```
Eo = (Bo - Boi) + Bg × (Rsi - Rs)
```

**Gas Cap Expansion (Eg):**
```
Eg = Boi × (Bg / Bgi - 1)
```

**Rock and Water Expansion (Er):**
```
Er = Boi × (Cf + Cw × Swi / (1 - Swi)) × (Pi - P)
```

## File Structure

```
.
├── ooip_calculator.py    # Main application file
├── README.md             # This file
└── *.csv                 # Production data files
```

## Example Workflow

1. Launch the application
2. Modify default reservoir properties if needed
3. Select your production data CSV file
4. Click "Calculate OOIP"
5. View the generated plot with OOIP value
6. The slope of the regression line represents your OOIP in STB

## Author

**Siddharth Gorai**  

- GitHub: [https://github.com/SiddharthGorai](https://github.com/SiddharthGorai)  
- LinkedIn: [https://www.linkedin.com/in/siddharth-gorai-ab01a7254/](https://www.linkedin.com/in/siddharth-gorai-ab01a7254/i)  
- Email: goraisiddharth@gmail.com


![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)