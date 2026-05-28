import json
import time
import requests

API_URL = "http://127.0.0.1:9001/generate-app"

with open("evaluation/prompts.json", "r") as f:
    prompts = json.load(f)

results = []

success_count = 0
failure_count = 0

for item in prompts:

    prompt = item["prompt"]

    start = time.time()

    try:

        response = requests.post(
            API_URL,
            json={
                "prompt": prompt
            }
        )

        latency = round(
            time.time() - start,
            2
        )

        success = response.status_code == 200

        if success:
            success_count += 1
        else:
            failure_count += 1

        results.append({
            "prompt": prompt,
            "status_code": response.status_code,
            "latency_seconds": latency,
            "success": success
        })

    except Exception as e:

        failure_count += 1

        results.append({
            "prompt": prompt,
            "error": str(e),
            "success": False
        })

report = {
    "total_tests": len(prompts),
    "success_count": success_count,
    "failure_count": failure_count,
    "success_rate": f"{(success_count / len(prompts)) * 100:.2f}%",
    "results": results
}

with open(
    "evaluation/evaluation_report.json",
    "w"
) as f:

    json.dump(
        report,
        f,
        indent=2
    )

print(json.dumps(report, indent=2))