import json, glob, os, re
items = []
for p in glob.glob("reports/*.json"):
    name = os.path.basename(p)
    if not re.match(r"^(us_market_)?\d{4}-\d{2}-\d{2}\.json$", name):
        continue
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        print("skip", name, e); continue
    sp = next((i.get("change", "") for i in d.get("indices", []) if i.get("name", "").startswith("S&P")), "")
    hi = sum(1 for k in ("earnings", "indicators", "politics", "korea") for x in d.get(k, []) if x.get("level") == "상")
    items.append({"file": name, "date": d.get("date", name[:10]), "krDate": d.get("krDate", ""),
                  "headline": d.get("headline", ""), "koreaOutlook": d.get("koreaOutlook", ""),
                  "sp500": sp, "high": hi})
items.sort(key=lambda x: x["date"], reverse=True)
json.dump({"reports": items}, open("reports/manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(items), "reports")
