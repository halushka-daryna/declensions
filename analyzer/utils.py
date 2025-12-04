def parse_feats(feats):
    if feats is None:
        return {}
    if isinstance(feats, dict):
        return feats
    if isinstance(feats, str):
        d = {}
        for part in feats.split("|"):
            if "=" in part:
                k, v = part.split("=")
                d[k] = v
        return d
    return {}
