from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)
app.config["DEBUG"] = True

# โหลดโมเดล (คุณสามารถเปลี่ยน model ตามภาษาที่รับ/ส่ง)
translate_pipeline_hmn_to_th = pipeline("translation_hmn_to_th", model="./model-th-hmn-3")
translate_pipeline_th_to_hmn = pipeline("translation_th_to_hmn", model="./model-th-hmn-4")

def translator(text, source, target):
    # คุณสามารถเช็ค pair ภาษาได้ที่นี่ ถ้ามีหลายโมเดล เช่น hm -> th, en -> th ฯลฯ
    if source == "hmn" and target == "th":
        translate_pipeline = translate_pipeline_hmn_to_th
    elif source == "th" and target == "hmn":
        translate_pipeline = translate_pipeline_th_to_hmn
    result = translate_pipeline(text)
    return result[0]["translation_text"]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/translator', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    source = data.get('source', '')
    target = data.get('target', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        translated = translator(text, source, target)
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
