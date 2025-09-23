import re
import math
from urllib.parse import urlparse


def entropy(value: str) -> float:
    if not value:
        return 0.0
    frequency_by_char = {}
    for ch in value:
        frequency_by_char[ch] = frequency_by_char.get(ch, 0) + 1
    ent = 0.0
    length = len(value)
    for count in frequency_by_char.values():
        probability = count / length
        ent -= probability * math.log2(probability)
    return ent


PUNYCODE_PREFIX = "xn--"
SUSPICIOUS_TLDS = {
    # Commonly abused or cheap TLDs; heuristic only
    "zip", "mov", "ru", "tk", "top", "work", "gq", "cf", "ml", "xyz", "click",
    "country", "link", "casino", "loan", "live", "kim", "win", "men", "cricket",
}


def _extract_domain_and_path(raw: str) -> tuple[str, str]:
    parsed = urlparse(raw if "://" in raw else "http://" + raw)
    domain = (parsed.hostname or "").lower()
    path = parsed.path or ""
    return domain, path


def _is_ipv4_address(host: str) -> bool:
    return bool(re.match(r"^\d+\.\d+\.\d+\.\d+$", host))


def _has_non_ascii(text: str) -> bool:
    try:
        text.encode("ascii")
        return False
    except UnicodeEncodeError:
        return True


def features(url: str) -> dict:
    domain, path = _extract_domain_and_path(url)
    domain_parts = domain.split(".") if domain else []
    tld = domain_parts[-1] if len(domain_parts) >= 1 else ""

    feature_map = {
        "domain": domain,
        "len": len(domain),
        "digits": sum(character.isdigit() for character in domain),
        "hyphens": domain.count("-"),
        "subdomain_parts": len(domain_parts) if domain else 0,
        "has_ip": _is_ipv4_address(domain),
        "path_len": len(path),
        "entropy": round(entropy(domain), 3),
        "punycode": domain.startswith(PUNYCODE_PREFIX),
        "non_ascii": _has_non_ascii(domain),
        "suspicious_tld": tld in SUSPICIOUS_TLDS,
    }
    return feature_map


def score(feature_map: dict) -> int:
    suspiciousness = 0
    suspiciousness += 2 if feature_map["len"] > 25 else 0
    suspiciousness += 2 if feature_map["digits"] > 3 else 0
    suspiciousness += 1 if feature_map["hyphens"] >= 2 else 0
    suspiciousness += 2 if feature_map["has_ip"] else 0
    suspiciousness += 1 if feature_map["path_len"] > 30 else 0
    suspiciousness += 1 if feature_map["punycode"] else 0
    suspiciousness += 1 if feature_map["non_ascii"] else 0
    suspiciousness += 2 if feature_map["suspicious_tld"] else 0
    suspiciousness += 1 if feature_map["entropy"] > 3.5 else 0
    return suspiciousness


def verdict_from_score(total_score: int) -> str:
    if total_score >= 6:
        return "Likely Scam"
    if total_score >= 3:
        return "Suspicious"
    return "Likely Safe"


