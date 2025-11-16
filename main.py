# main.py
import os
from datetime import datetime
from data_loader import load_from_json
from validators import avaliar_anuncio
from utils import save_batch_json, save_csv

def process_batch(input_path: str, output_dir: str):
    anuncios = load_from_json(input_path)
    reports = []
    for a in anuncios:
        listing_id = a.get("id", a.get("titulo", "sem_id"))
        results = avaliar_anuncio(a)
        report = {
            "listing_id": listing_id,
            "checked_at": datetime.utcnow().isoformat() + "Z",
            "results": results
        }
        reports.append(report)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    json_path = os.path.join(output_dir, f"report_{timestamp}.json")
    csv_path = os.path.join(output_dir, f"report_{timestamp}.csv")

    save_batch_json(reports, json_path)
    save_csv(reports, csv_path)

    print(f"Relatório salvo: {json_path}")
    print(f"Relatório CSV salvo: {csv_path}")
    return reports

if __name__ == "__main__":
    INPUT = "examples/anuncio_exemplo.json"
    OUTPUT_DIR = "outputs/reports"
    process_batch(INPUT, OUTPUT_DIR)
