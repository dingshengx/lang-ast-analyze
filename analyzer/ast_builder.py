import json

import spacy

# 加载英文模型
nlp = spacy.load("en_core_web_sm")


def build_ast(sentence):
    doc = nlp(sentence)

    tree = {
        "sentence": sentence,
        "root": {
            "verb": "",
            "subject": "",
            "object": ""
        }
    }

    for token in doc:
        if token.pos_ == "VERB":
            tree["root"]["verb"] = token.text
            for child in token.children:
                if child.dep_ in ("nsubj", "nsubjpass"):
                    tree["root"]["subject"] = child.text
                elif child.dep_ in ("dobj", "obj"):
                    tree["root"]["object"] = child.text

    return json.dumps(tree, indent=2)
