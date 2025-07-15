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

