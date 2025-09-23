from detector import features, score, verdict_from_score


SYNTHETIC = [
    # Likely safe examples
    'example.com',
    'www.example.org',
    'docs.example.com/path',
    'test.example.edu/resource',

    # Suspicious patterns
    'paypal-login.example.com/verify',
    'accounts-paypa1.example.com/login',
    'xn--ppal-7ya.example.com',
    'bank-of-country-secure.example.com/signin',
    'very-long-domain-name-with-many-hyphens-and-digits-12345.example.com/path',
    '192.0.2.123/login',  # TEST-NET-1 IP range (RFC 5737)
    'login-update-security-verify-1234.xyz',
    'secure-login.mov',
    'promo-free-gift.tk/claim',
]


def test_scoring_runs_and_verdict_class_set():
    for sample in SYNTHETIC:
        f = features(sample)
        s = score(f)
        v = verdict_from_score(s)
        assert isinstance(s, int)
        assert v in ('Likely Scam', 'Suspicious', 'Likely Safe')


