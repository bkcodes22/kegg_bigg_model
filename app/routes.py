from flask import Blueprint, render_template, request
import pandas as pd
import requests
import re
import time
from Bio.KEGG import REST
import xml.etree.ElementTree as ET
import os

main = Blueprint('main', __name__)

# Load CSVs
data_dir = os.path.dirname(__file__)
bigg_ec_db = pd.read_csv(os.path.join(data_dir, 'bigg_ec_database.csv'))
kegg_db = pd.read_csv(os.path.join(data_dir, 'keggid_bigg_db.csv'))

@main.route('/', methods=['GET', 'POST'])
def index():
    kegg_reactions = []
    afm_reactions = []
    reaction_to_ec = {}
    map_id = ''

    if request.method == 'POST':
        map_id = request.form['map_id'].strip()

        # Get reactions for the map
        link_url = f"https://rest.kegg.jp/link/reaction/{map_id}"
        response = requests.get(link_url)
        reaction_ids = re.findall(r"rn:(R\d{5})", response.text)
        kegg_reactions = sorted(set(reaction_ids))

        # Get ECs for each reaction
        for rid in kegg_reactions:
            entry = REST.kegg_get(rid).read()
            ec_match = re.search(r"ENZYME\s+([0-9. ]+)", entry)
            ec_numbers = ec_match.group(1).strip().split() if ec_match else []
            reaction_to_ec[rid] = ec_numbers
            time.sleep(0.2)

        # Load afm-specific reactions from KGML
        kgml_url = f"https://rest.kegg.jp/get/afm{map_id[3:]}/kgml"
        response = requests.get(kgml_url)
        try:
            root = ET.fromstring(response.content)
            afm_set = set()
            for reaction in root.findall('reaction'):
                ids = re.findall(r"R\d{5}", reaction.get('name', ''))
                afm_set.update(ids)
            afm_reactions = sorted(afm_set)
        except:
            afm_reactions = []

    return render_template(
        'index.html',
        kegg_reactions=kegg_reactions,
        afm_reactions=afm_reactions,
        reaction_to_ec=reaction_to_ec,
        map_id=map_id
    )

@main.route('/ec_info/<ec_number>')
def ec_info(ec_number):
    matches = bigg_ec_db[bigg_ec_db['ec_numbers'].str.contains(rf'\b{re.escape(ec_number)}\b', regex=True, na=False)]
    if matches.empty:
        return f"<h4>No information found for EC {ec_number}</h4>"
    html = f"<h4>Entries for EC {ec_number}</h4>"
    html += matches.to_html(index=False, escape=False)
    return html

@main.route('/kegg_info/<reaction_id>')
def kegg_info(reaction_id):
    matches = kegg_db[kegg_db['kegg_reactions'].str.contains(reaction_id, na=False)]
    if matches.empty:
        return f"<h4>No information found for KEGG Reaction {reaction_id}</h4>"
    html = f"<h4>Entries for KEGG Reaction {reaction_id}</h4>"
    html += matches.to_html(index=False, escape=False)
    return html
