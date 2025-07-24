# main.py
from flask import Flask, request, jsonify
from app.ocr import extract_text_from_document
from app.classifier import classify_document
from app.extractor import extract_information
from app.complexity import assess_complexity
from app.router import route_claim

app = Flask(__name__)

@app.route("/process-claim", methods=["POST"])
def process_claim():
    file = request.files["document"]
    filepath = f"data/{file.filename}"
    file.save(filepath)

    text = extract_text_from_document(filepath)
    doc_type = classify_document(text)
    info = extract_information(text, doc_type)
    complexity_score = assess_complexity(info)
    routing_decision = route_claim(info, complexity_score)

    return jsonify({
        "document_type": doc_type,
        "extracted_info": info,
        "complexity_score": complexity_score,
        "routing_decision": routing_decision
    })

if __name__ == "__main__":
    app.run(debug=True)
