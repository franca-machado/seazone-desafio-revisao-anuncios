# validators.py
from typing import Dict, Tuple, List

def validar_qtd_fotos(anuncio: Dict, min_photos: int = 10) -> Tuple[bool, Dict]:
    qtd = len(anuncio.get("fotos", []))
    return qtd >= min_photos, {"count": qtd, "min_required": min_photos}

def validar_resolucao(anuncio: Dict, min_w:int = 1024, min_h:int = 683) -> Tuple[bool, Dict]:
    fotos = anuncio.get("fotos", [])
    bad = []
    for f in fotos:
        w = f.get("width", 0)
        h = f.get("height", 0)
        if w < min_w or h < min_h:
            bad.append({"url": f.get("url"), "width": w, "height": h})
    return len(bad) == 0, {"bad_photos": bad, "checked": len(fotos)}

def validar_titulo(anuncio: Dict, min_chars:int = 15,
                   forbidden: List[str] = None, location_keywords: List[str] = None) -> Tuple[bool, Dict]:
    if forbidden is None:
        forbidden = ["legal", "bonito", "ótimo", "lindo"]
    if location_keywords is None:
        location_keywords = ["centro", "praia", "bairro", "vista", "perto", "próximo"]
    t = (anuncio.get("titulo") or "").lower()
    has_generic = any(w in t for w in forbidden)
    has_loc = any(w in t for w in location_keywords)
    ok = len(t) >= min_chars and (not has_generic) and has_loc
    return ok, {"length": len(t), "has_generic": has_generic, "has_location": has_loc}

def validar_descricao(anuncio: Dict, min_chars:int = 120, location_keywords: List[str] = None) -> Tuple[bool, Dict]:
    if location_keywords is None:
        location_keywords = ["centro", "seguro", "praia", "vista", "perto", "próximo"]
    desc = (anuncio.get("descricao") or "").lower()
    has_diff = any(w in desc for w in location_keywords)
    ok = len(desc) >= min_chars and has_diff
    return ok, {"length": len(desc), "has_diff": has_diff}

def validar_amenidades(anuncio: Dict, required=None) -> Tuple[bool, Dict]:
    if required is None:
        required = {"wi-fi", "cama", "banheiro", "ar-condicionado", "cozinha"}
    amenities = {a.lower() for a in anuncio.get("amenidades", [])}
    missing = list(required - amenities)
    ok = len(missing) == 0
    return ok, {"missing": missing, "checked": list(amenities)}

def validar_preco(anuncio: Dict, tolerance: float = 0.2) -> Tuple[bool, Dict]:
    price = anuncio.get("preco")
    median = anuncio.get("mediana")
    if price is None or median is None:
        return False, {"reason": "price_or_median_missing"}
    low = median * (1 - tolerance)
    high = median * (1 + tolerance)
    ok = low <= price <= high
    return ok, {"price": price, "min_accepted": low, "max_accepted": high}

def avaliar_anuncio(anuncio: Dict) -> Dict:
    """Roda todas as validações e retorna um dicionário detalhado."""
    results = {}
    fn_map = {
        "titulo": validar_titulo,
        "descricao": validar_descricao,
        "fotos_qtd": validar_qtd_fotos,
        "fotos_resolucao": validar_resolucao,
        "amenidades": validar_amenidades,
        "preco": validar_preco
    }
    for key, fn in fn_map.items():
        ok, detail = fn(anuncio)
        results[key] = {"ok": ok, "detail": detail}
    results["overall_ok"] = all(v["ok"] for v in results.values())
    return results
