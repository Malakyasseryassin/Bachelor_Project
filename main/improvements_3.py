import pandas as pd
import numpy as np
import re
import random

from tqdm import tqdm
tqdm.pandas()


# ── Obfuscation handling ───────────────────────────────────────────────────────
def fix_obfuscation(text):
    text = str(text)

    # Fix spaced characters like: "f u c k" → "fuck"
    text = re.sub(r'\b(?:\w\s){2,}\w\b', lambda m: m.group(0).replace(" ", ""), text)

    # Fix common split offensive words (targeted)
    text = re.sub(r'du\s?mb', 'dumb', text)
    text = re.sub(r'f\s?u\s?c\s?k', 'fuck', text)
    text = re.sub(r'b\s?i\s?t\s?c\s?h', 'bitch', text)

    # Normalize elongated words: "fuuuck" → "fuuck"
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)

    return text


# ── Slang dictionary ───────────────────────────────────────────────────────────
slang_dict = {
    "u": "you",
    "ur": "your",
    "ya": "you",
    "yo": "you",
    "im": "i am",
    "dont": "do not",
    "cant": "cannot",
    "wont": "will not",
    "nigga": "nigger",
    "niggah": "nigger",
    "btch": "bitch",
    "fck": "fuck",
    "wtf": "what the fuck",
    "omg": "oh my god",
    "afaik": "as far as i know",
    "afk": "away from keyboard",
    "asl": "age sex location",
    "atm": "at the moment",
    "b/c": "because",
    "b/w": "between",
    "b4": "before",
    "bbiab": "be back in a bit",
    "bbl": "be back later",
    "bff": "best friends forever",
    "brb": "be right back",
    "btw": "by the way",
    "ctn": "cannot talk now",
    "cye": "check your email",
    "dl": "download",
    "eta": "estimated time of arrival",
    "fwiw": "for what it is worth",
    "fyi": "for your information",
    "gg": "good game",
    "gj": "good job",
    "gl": "good luck",
    "gr8": "great",
    "gtg": "got to go",
    "gmv": "got my vote",
    "hth": "hope this helps",
    "hw": "homework",
    "iac": "in any case",
    "ic": "i see",
    "idk": "i do not know",
    "iirc": "if i remember correctly",
    "ikr": "i know right",
    "imo": "in my opinion",
    "imho": "in my humble opinion",
    "irl": "in real life",
    "jk": "just kidding",
    "k": "ok",
    "l8": "late",
    "l8r": "later",
    "lmk": "let me know",
    "lol": "laughing out loud",
    "mmb": "message me back",
    "msg": "message",
    "myob": "mind your own business",
    "n/a": "not available",
    "nc": "no comment",
    "ne1": "anyone",
    "nm": "not much",
    "noob": "newbie",
    "np": "no problem",
    "ntn": "no thanks needed",
    "omw": "on my way",
    "ot": "off topic",
    "pc": "personal computer",
    "pls": "please",
    "pos": "parent over shoulder",
    "ppl": "people",
    "qt": "cutie",
    "re": "regarding",
    "smh": "shaking my head",
    "sry": "sorry",
    "tba": "to be announced",
    "tbc": "to be continued",
    "tc": "take care",
    "thx": "thanks",
    "tia": "thanks in advance",
    "tlc": "tender loving care",
    "tmi": "too much information",
    "ttfn": "ta ta for now",
    "ttyl": "talk to you later",
    "txt": "text",
    "ty": "thank you",
    "w/e": "whatever",
    "w/o": "without",
    "w8": "wait",
    "xoxo": "hugs and kisses",
    "y": "why",
    "ynt": "why not",
    "yolo": "you only live once",
    "yw": "you are welcome",
    "zzz": "sleeping",
}


def normalize_slang(text):
    words = text.split()
    normalized = [slang_dict.get(w, w) for w in words]
    return " ".join(normalized)


# ── Hate keyword list ──────────────────────────────────────────────────────────
hate_keywords = [
    "nigger", "coon", "bitch", "fuck", "feminazi",
    "whore", "slut", "rape", "kill", "terrorist",
    "scum", "slutty", "trollop", "prude",
    "man eater", "cougar",
    "mutton dressed as lamb",
    "faded beauty",
    "catty", "bitchy",
    "gold digger", "bimbo",
    "asking for it",
    "chick", "dame",
    "witch", "matronly", "bigot", "bigotry", "nigga", "n-word", "wop", "paddy", "dago", "polack",
]


def keyword_flag(text):
    text = text.lower()
    return int(any(kw in text for kw in hate_keywords))


# ── Keyword masking ────────────────────────────────────────────────────────────
def mask_keywords(text, prob=0.3):
    words = text.split()
    masked = []

    for w in words:
        if w in hate_keywords and random.random() < prob:
            masked.append("[MASK]")
        else:
            masked.append(w)

    return " ".join(masked)


# ── Run directly (not imported) ────────────────────────────────────────────────
if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\hp\Downloads\UNI\Spring 2026\Bachelor\Bachelor_Project\data\combined_processed_v1.csv")

    # Test obfuscation
    samples = [
        "du mb idiot",
        "f u c k you",
        "this is normal text",
        "b i t c h please",
    ]
    for s in samples:
        print("ORIG:", s)
        print("FIX :", fix_obfuscation(s))
        print("-" * 40)

    df["text_obf"] = df["clean_text"].apply(fix_obfuscation)
    print(df[["clean_text", "text_obf"]].head(10))

    # Test slang normalization
    samples = [
        "u coon cant wait",
        "im gonna kill him",
        "wtf is this",
    ]
    for s in samples:
        print("ORIG:", s)
        print("SLNG:", normalize_slang(s))
        print("-" * 40)

    df["text_slang"] = df["text_obf"].apply(normalize_slang)
    print(df[["text_obf", "text_slang"]].head(10))
    print(df.sample(10)[["text_obf", "text_slang"]])

    df["keyword_flag"] = df["text_slang"].apply(keyword_flag)
    print(df.sample(10)[["text_slang", "keyword_flag"]])

    # Test masking
    test_samples = [
        "fuck you bitch",
        "you are a stupid bitch",
        "this is a normal sentence",
        "i will kill you",
        "she is a gold digger",
        "hello how are you",
        "nigger please",
        "you are amazing",
    ]
    for text in test_samples:
        masked = mask_keywords(text, prob=1.0)  # force masking for testing
        print("ORIG :", text)
        print("MASK :", masked)
        print("-" * 50)

    df["text_masked"] = df["text_slang"].apply(mask_keywords)
    print(df.sample(10)[["text_slang", "text_masked"]])

    # Finalize and export
    df["final_text"] = df["text_masked"]
    df_final = df[["final_text", "class", "keyword_flag"]]

    df_final.to_csv("improved_dataset_final.csv", index=False)

    print(df_final.shape)
    print(df_final.head())
    print(df_final[df_final["final_text"].str.strip() == ""])
    print(df_final.sample(20))
    print(df_final["keyword_flag"].value_counts())
