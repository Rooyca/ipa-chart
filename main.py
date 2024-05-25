import os, json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variables to store dictionary and last modified time
ipa_dict = {}
last_modified = None
dictionary_file = 'files/ipadict.txt'

def load_dictionary():
    global ipa_dict, last_modified
    modified_time = os.path.getmtime(dictionary_file)
    if not ipa_dict or modified_time != last_modified:
        print("=== Loading dictionary ===")
        ipa_dict = {}
        with open(dictionary_file, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                parts = [part for part in parts if part]
                word = parts[0]
                ipa = parts[-1]  # IPA representation is the last element
                ipa_dict[word] = ipa
        last_modified = modified_time

@app.route('/ipatrans', methods=['POST'])
def translate_words():
    load_dictionary() 
    data = request.get_json()

    if 'words' not in data:
        return jsonify({'error': 'Words field is missing'}), 400

    final_trans = ""

    for word in data['words'].split():
        word = word.lower()
        word = word.strip('.,!?;:')

        try:
            ipa = ipa_dict[word]
            final_trans += ipa + " "
        except KeyError:
            final_trans += " **"+word+"** "

    return jsonify({'tran': final_trans, 'org': data['words']})

@app.route('/ipachart', methods=['POST'])
def chart_ipa():
    data = request.get_json()

    if 'ipa' not in data:
        return jsonify({'error': 'IPA field is missing'}), 400

    json_f = 'files/json/general.json'
    with open(json_f, 'r', encoding='utf-8') as file:
        ipa_dict = json.load(file)

    # search ipa in json by name
    for ipa in ipa_dict:
        if ipa['name'] == data['ipa']:
            return jsonify(ipa)

    return jsonify({'error': 'IPA not found'}), 404

@app.route('/ipachart/vowels', methods=['GET'])
def chart_vowels():
    json_f = 'files/json/vowels.json'
    with open(json_f, 'r', encoding='utf-8') as file:
        ipa_dict = json.load(file)
    return jsonify(ipa_dict)

@app.route('/ipachart/consonants', methods=['GET'])
def chart_consonants():
    json_f = 'files/json/consonants.json'
    with open(json_f, 'r', encoding='utf-8') as file:
        ipa_dict = json.load(file)
    return jsonify(ipa_dict)

@app.route('/ipachart/others', methods=['GET'])
def chart_other():
    json_f = 'files/json/other.json'
    with open(json_f, 'r', encoding='utf-8') as file:
        ipa_dict = json.load(file)
    return jsonify(ipa_dict)

if __name__ == '__main__':
    app.run(debug=True)