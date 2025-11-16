# utils.py
import json, csv, os
from typing import List, Dict

def save_json(report: Dict, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

def save_batch_json(batch: List[Dict], path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

def save_csv(batch: List[Dict], path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fieldnames = ["listing_id", "overall_ok", "titulo_ok", "descricao_ok",
                  "fotos_qtd_ok", "fotos_resolucao_ok", "amenidades_ok", "preco_ok"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in batch:
            row = {
                "listing_id": item.get("listing_id"),
                "overall_ok": item.get("results", {}).get("overall_ok"),
                "titulo_ok": item.get("results", {}).get("titulo", {}).get("ok"),
                "descricao_ok": item.get("results", {}).get("descricao", {}).get("ok"),
                "fotos_qtd_ok": item.get("results", {}).get("fotos_qtd", {}).get("ok"),
                "fotos_resolucao_ok": item.get("results", {}).get("fotos_resolucao", {}).get("ok"),
                "amenidades_ok": item.get("results", {}).get("amenidades", {}).get("ok"),
                "preco_ok": item.get("results", {}).get("preco", {}).get("ok"),
            }
            writer.writerow(row)
