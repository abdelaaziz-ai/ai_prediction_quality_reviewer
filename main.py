dataset = [
    {
        "image_id": 201,
        "ground_truth": "Coca-Cola",
        "prediction": "Coca Cola",
        "confidence": 0.95
    },
    {
        "image_id": 202,
        "ground_truth": "Pepsi",
        "prediction": "Pepsi",
        "confidence": 0.87
    },
    {
        "image_id": 203,
        "ground_truth": "Sprite",
        "prediction": "7UP",
        "confidence": 0.93
    },
    {
        "image_id": 204,
        "ground_truth": "Fanta",
        "prediction": "Fanta",
        "confidence": 0.96
    },
    {
        "image_id": 205,
        "ground_truth": "Coca-Cola Zero",
        "prediction": "coca cola zero",
        "confidence": 0.72
    },
    {
        "image_id": 206,
        "ground_truth": "Pepsi Max",
        "prediction": "Pepsi",
        "confidence": 0.91
    },
    {
        "image_id": 207,
        "ground_truth": "Sprite",
        "prediction": " Sprite ",
        "confidence": 0.66
    },
    {
        "image_id": 208,
        "ground_truth": "Fanta",
        "prediction": "Fanta",
        "confidence": 0.89
    },
    {
        "image_id": 209,
        "ground_truth": "Coca-Cola",
        "prediction": "Pepsi",
        "confidence": 0.97
    },
    {
        "image_id": 210,
        "ground_truth": "Pepsi-Max",
        "prediction": "pepsi max",
        "confidence": 0.94
    }
]

for item in dataset:
    normalized_ground_truth = item["ground_truth"].strip().casefold().replace("-", " ")
    normalized_prediction = item["prediction"].strip().casefold().replace("-", " ")


    if  normalized_ground_truth == normalized_prediction:
        qa_check = 'match'
    else:
        qa_check = 'mismatch'
    item['prediction_gt'] = qa_check



    if  item["confidence"] >= 0.90 and item["prediction_gt"] == "match":
        confidence_match = 'high'
    elif item["confidence"] < 0.90 and item["prediction_gt"] == "mismatch":
        confidence_match = 'low'
    else:
        confidence_match = "potential_error"
    item['classification'] = confidence_match



    if item["classification"] == "high":
        status = "verified"
    elif item["classification"] == "low":
        status = "review"
    else:
        status = "report_error"
    item["final_status"] = status


total_records = 0
match = 0
mismatch = 0
high = 0
low = 0 
potential_error = 0
verified = 0
review = 0
report_error = 0 

for item in dataset:
    total_records += 1
    if item["prediction_gt"] == "match":
        match += 1 
    else:
        mismatch += 1

    if item["classification"] == "high":
        high += 1
    elif item["classification"] == "low":
        low += 1
    else:
        potential_error += 1

    if item["final_status"] == "verified":
        verified += 1
    elif item["final_status"] == "review":
        review += 1
    else:
        report_error += 1


metrics = {
    "total_records": total_records,
    "match": match, 
    "mismatch": mismatch, 
    "high": high, 
    "low": low, 
    "potential_error": potential_error, 
    "verified": verified, 
    "review": review, 
    "report_error":report_error
}


if total_records == match + mismatch:
    qa_check_validation = "passed"
else:
    qa_check_validation= "failed"

if total_records == high + low + potential_error:
    classification_validation = "passed"
else:
    classification_validation= "failed"

if total_records == verified + review + report_error:
    final_status_validation = "passed"
else:
    final_status_validation= "failed"

metrics["validation"] = { "qa_check_validation": qa_check_validation,
         "classification_validation": classification_validation,
         "final_status_validation": final_status_validation
         }

print(dataset)
print(metrics)