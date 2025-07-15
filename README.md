# 🧬 KEGG Reaction & EC Finder

An interactive Flask-based web application to explore **KEGG metabolic pathways**, **enzyme commission (EC) numbers**, and determine whether specific reactions are present in organism-specific sub-pathways (like `afm00010`).  
This lightweight app uses CSV files and the KEGG API to provide a responsive, clickable interface for bioinformatics research and metabolic modeling.

---

## 🚀 Features

- 🔍 **Pathway Search:** Enter a KEGG Map ID (e.g., `map00010`) to retrieve reactions in that pathway.
- ✅ ❌ **Organism-specific Check:** Displays whether each reaction is found in the specified organism's version of the pathway (e.g., `afm`).
- ⚡ **Interactive Details:** Click any **Reaction ID** or **EC number** to show more information from your own CSV datasets, live inside a right-side panel.
- 💻 **Clean & Responsive UI:** Modern layout with a side panel, responsive on all devices.
- 🧾 **No database needed:** Pulls info from local CSVs and KEGG REST API.

---

## 🛠 Installation Instructions

### 1. Clone the repository

```git clone https://github.com/bkcodes22/kegg_bigg_model.git```<br/>

```cd kegg_bigg_model```

### 2. Set up a virtual environment (optional but recommended)
```python -m venv venv```

```source venv/bin/activate```

```For Windows: venv\Scripts\activate```

### 3. Install dependencies

```pip install -r requirements.txt```

### 4. Run the app

```python run.py```

### 5. Then open in your browser:
```http://127.0.0.1:5000```

---

## 💡 Example KEGG Map Inputs

Here are some KEGG pathways you can try:

- `map00010` — Glycolysis / Gluconeogenesis
- `map00020` — Citrate (TCA) cycle
- `map00230` — Purine metabolism

---

## 🎯 How It Works

1. You enter a pathway ID like `map00010`.
2. The app fetches all KEGG reactions mapped to that pathway.
3. It checks if each reaction is also present in the organism version (e.g. `afm00010`) via KEGG KGML.
4. It fetches reaction-to-EC mapping using the KEGG API.
5. On click, it shows matched entries from your own CSVs in the right panel.

---

## ✏️ Customization

| To change this...             | Edit this file             |
|------------------------------|----------------------------|
| HTML layout & table columns  | `app/templates/index.html` |
| CSS styles                   | `app/static/style.css`     |
| CSV search logic             | `app/routes.py`            |
| Target organism (e.g. `afm`) | `routes.py` > KGML request |

---

## 🧪 Tips and Troubleshooting

- If reactions/EC numbers don’t appear:  
  ✅ Double-check the structure of your CSV input files.

- If the app is slow or shows KEGG errors:  
  📡 Ensure you're connected to the internet (KEGG API is called live).

- Use hard refresh (Ctrl+Shift+R) if you update HTML/CSS and don’t see changes.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🧠 Acknowledgments

- Powered by [KEGG REST API](https://www.kegg.jp/kegg/rest/)
- Built with [Flask](https://flask.palletsprojects.com/), [pandas](https://pandas.pydata.org/), and [Biopython](https://biopython.org/)
- Inspired by bioinformatics workflow challenges in pathway analysis

---

> Built with ❤️ for scientists, students, and data nerds everywhere.



