import re
from .exceptions import EXCEPTIONS
from .utils import parse_feats

def determine_declension(lemma, gender):
    lemma = lemma.lower()
    if lemma in EXCEPTIONS:
        return "виняток (не належить до жодної відміни)"
    if (lemma.endswith("а") or lemma.endswith("я")) and gender in ("Fem", "Masc", "Com"):
        return "1 відміна"
    if gender == "Masc":
        if re.match(r".*[бвгґджзйклмнпрстфхцчшщ]$", lemma):
            return "2 відміна"
        if lemma.endswith("о"):
            return "2 відміна"
    if gender == "Neut" and (lemma.endswith("е") or lemma.endswith("о")):
        return "2 відміна"
    if lemma == "мати":
        return "3 відміна"
    if gender == "Fem" and re.match(r".*[бвгґджзйклмнпрстфхцчшщ]$", lemma):
        return "3 відміна"
    if gender == "Neut" and (lemma.endswith("а") or lemma.endswith("я")):
        return "4 відміна"
    return "невідомо (не підпадає під класичні правила)"

def analyze_text(doc):
    results = []
    for sent in doc.sentences:
        for word in sent.words:
            if word.upos == "NOUN":
                lemma = word.lemma
                feats_dict = parse_feats(word.feats)
                gender = feats_dict.get("Gender", "")
                decl = determine_declension(lemma, gender)
                results.append([word.text, lemma, gender, decl])
    return results
