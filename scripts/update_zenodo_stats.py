from pathlib import Path
import re
import time
import requests
import yaml

BIB_FILE = Path("_bibliography/papers.bib")
OUTPUT_FILE = Path("_data/zenodo_stats.yml")

ZENODO_API = "https://zenodo.org/api/records/{}"


def extract_zenodo_records_from_bib(bib_text):
    entries = re.findall(r"@(\w+)\s*\{\s*([^,]+),(.*?)(?=\n@\w+\s*\{|\Z)", bib_text, flags=re.S)
    records = []

    for entry_type, key, body in entries:
        zenodo_match = re.search(r"zenodo\s*=\s*\{([^}]+)\}", body, flags=re.I)
        doi_match = re.search(r"doi\s*=\s*\{([^}]+)\}", body, flags=re.I)
        title_match = re.search(r"title\s*=\s*\{([^}]+)\}", body, flags=re.I | re.S)

        zenodo_id = None

        if zenodo_match:
            zenodo_id = zenodo_match.group(1).strip()

        elif doi_match:
            doi = doi_match.group(1).strip()
            doi_record_match = re.search(r"10\.5281/zenodo\.(\d+)", doi)
            if doi_record_match:
                zenodo_id = doi_record_match.group(1)

        if zenodo_id:
            title = title_match.group(1).replace("\n", " ").strip() if title_match else key

            records.append({
                "key": key.strip(),
                "entry_type": entry_type.lower(),
                "zenodo_id": zenodo_id,
                "title": title,
            })

    return records


def get_stat(stats, possible_keys):
    for key in possible_keys:
        if key in stats and stats[key] is not None:
            return stats[key]
    return 0


def fetch_zenodo_stats(record):
    response = requests.get(ZENODO_API.format(record["zenodo_id"]), timeout=30)
    response.raise_for_status()

    data = response.json()
    stats = data.get("stats", {})

    views = get_stat(stats, [
        "views",
        "all_versions_views",
        "version_views",
    ])

    downloads = get_stat(stats, [
        "downloads",
        "all_versions_downloads",
        "version_downloads",
    ])

    unique_views = get_stat(stats, [
        "unique_views",
        "all_versions_unique_views",
        "version_unique_views",
    ])

    unique_downloads = get_stat(stats, [
        "unique_downloads",
        "all_versions_unique_downloads",
        "version_unique_downloads",
    ])

    return {
        "key": record["key"],
        "title": record["title"],
        "zenodo_id": record["zenodo_id"],
        "url": f"https://zenodo.org/records/{record['zenodo_id']}",
        "views": int(views or 0),
        "downloads": int(downloads or 0),
        "unique_views": int(unique_views or 0),
        "unique_downloads": int(unique_downloads or 0),
    }


def main():
    if not BIB_FILE.exists():
        raise FileNotFoundError(f"Could not find {BIB_FILE}")

    bib_text = BIB_FILE.read_text(encoding="utf-8")
    records = extract_zenodo_records_from_bib(bib_text)

    output_records = []

    for record in records:
        try:
            print(f"Fetching Zenodo stats for {record['key']} / {record['zenodo_id']}")
            output_records.append(fetch_zenodo_stats(record))
            time.sleep(0.3)
        except Exception as exc:
            print(f"Warning: failed to fetch {record['key']} ({record['zenodo_id']}): {exc}")
            output_records.append({
                "key": record["key"],
                "title": record["title"],
                "zenodo_id": record["zenodo_id"],
                "url": f"https://zenodo.org/records/{record['zenodo_id']}",
                "views": 0,
                "downloads": 0,
                "unique_views": 0,
                "unique_downloads": 0,
            })

    totals = {
        "records": len(output_records),
        "views": sum(item["views"] for item in output_records),
        "downloads": sum(item["downloads"] for item in output_records),
        "unique_views": sum(item["unique_views"] for item in output_records),
        "unique_downloads": sum(item["unique_downloads"] for item in output_records),
    }

    data = {
        "totals": totals,
        "records": output_records,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)

    print(f"Written {OUTPUT_FILE}")
    print(totals)


if __name__ == "__main__":
    main()