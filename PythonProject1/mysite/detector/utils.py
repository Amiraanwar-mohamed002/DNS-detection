# detector/utils.py
import re, math, socket
from collections import Counter
from urllib.parse import urlparse
import tldextract
import dns.resolver

def domain_from_input(s: str) -> str:
    if "://" in s:
        s = urlparse(s).netloc
    return s.lower().strip()

def char_entropy(s: str) -> float:
    counts = Counter(s)
    probs = [c/len(s) for c in counts.values()] if s else []
    return -sum(p * math.log2(p) for p in probs) if probs else 0

def lexical_features(domain: str):
    ext = tldextract.extract(domain)
    sld = ext.domain
    full = domain.replace("www.", "")
    return {
        "len": len(full),
        "digits": sum(ch.isdigit() for ch in full),
        "hyphens": full.count("-"),
        "entropy": char_entropy(sld),
    }

def heuristic_predict(domain: str):
    d = domain_from_input(domain)
    feats = lexical_features(d)
    score = 0
    if feats["len"] > 25: score += 1
    if feats["digits"] > 2: score += 1
    if feats["hyphens"] > 1: score += 1
    if feats["entropy"] > 3.5: score += 1
    return 1 if score >= 2 else 0, feats, score
