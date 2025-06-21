# Hmong-Thai Machine Translation System

A neural machine translation system that translates between Hmong (Hmong) and Thai languages. This project includes both the trained models and a web-based translation interface.

## 🌟 Features

- **Bidirectional Translation**: Translate from Hmong to Thai and Thai to Hmong
- **Web Interface**: User-friendly web application with modern UI
- **Real-time Translation**: Instant translation with API endpoints
- **Clipboard Integration**: Copy/paste functionality for easy text handling
- **Responsive Design**: Works on desktop and mobile devices
- **High-Quality Models**: Fine-tuned transformer models with BLEU scores up to -

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU (recommended for inference)
- 8GB+ RAM

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YangNobody12/MachineTranslation-th-hmn.git
   cd Translation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web application**
   ```bash
   python server.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Translation/
├── server.py                 # Flask web server
├── templates/
│   └── index.html           # Web interface template
├── static/
│   ├── style.css            # CSS styling
│   └── script.js            # Frontend JavaScript
├── model-th-hmn-3/          # Hmong→Thai model
├── model-th-hmn-4/          # Thai→Hmong model
├── data_small.json          # Training dataset small
├── data_meduim.json         # Training dataset medium
├── machine_translation.ipynb # Training notebook
└── README.md
```

## 🎯 Usage

### Web Interface

1. **Select Languages**: Choose source and target languages from the dropdown menus
2. **Input Text**: Type or paste text in the input box
3. **Translate**: Click the "Translate" button
4. **Copy Result**: Use the copy button to copy translated text

### API Usage

```python
import requests

# Translate Hmong to Thai
response = requests.post('http://localhost:5000/api/translator', 
    json={
        'text': 'Kuv nyob hauv Thailand',
        'source': 'hmn',
        'target': 'th'
    })
result = response.json()
print(result['translated_text'])  # "ฉันอาศัยอยู่ในประเทศไทย"
```

## 🤖 Model Information

### Model Architecture
- **Base Model**: Helsinki-NLP/opus-mt-th-en (MarianMT)
- **Architecture**: Transformer (Encoder-Decoder)
- **Training**: Fine-tuned on custom Hmong-Thai dataset

### Model Performance

| Model | Direction | BLEU Score | Training Steps |
|-------|-----------|------------|----------------|
| model-th-hmn-3 | Hmong→Thai | - | 34,100 |
| model-th-hmn-4 | Thai→Hmong | - | 63,900 |

### Training Details
- **Dataset Size**: 12,781 sentence pairs
- **Training Split**: 80% train, 20% test
- **Learning Rate**: 2e-5
- **Batch Size**: 16
- **Epochs**: 100
- **Optimizer**: AdamW
- **Mixed Precision**: FP16

## 📊 Dataset

The training dataset contains parallel Hmong-Thai sentence pairs covering various domains:
- Daily conversations
- Educational content
- Medical terminology
- Technology terms
- Cultural expressions

### Sample Data
```json
{
    "id": 1,
    "translation": {
        "hmn": "Nplooj ntoo tig hauv dav hlau thaum lub caij ntuj.",
        "th": "ใบไม้ร่วงในป่าเมื่อฤดูหนาวมา"
    }
}
```

## 🔧 Technical Details

### Dependencies
- **Transformers**: Hugging Face transformers library
- **Flask**: Web framework for the API
- **Datasets**: Hugging Face datasets library
- **Evaluate**: For BLEU score calculation
- **WandB**: Training monitoring

### Training Configuration
```python
training_args = Seq2SeqTrainingArguments(
    output_dir="model-th-hmn-4",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=100,
    predict_with_generate=True,
    fp16=True,
    push_to_hub=True,
)
```

## 🌐 Web Interface Features

### User Experience
- **Language Swapping**: Quick swap between source and target languages
- **Auto-resize**: Text areas automatically adjust to content
- **Clipboard Operations**: One-click copy/paste functionality
- **Clear Function**: Reset input and output fields
- **Error Handling**: User-friendly error messages

### Design
- **Responsive Layout**: Works on all screen sizes
- **Modern UI**: Clean, intuitive interface
- **Thai Font Support**: Noto Sans Thai for proper Thai text rendering
- **Accessibility**: ARIA labels and keyboard navigation

## 📈 Performance Optimization

### Inference Optimization
- **Model Quantization**: Reduced model size for faster inference
- **Batch Processing**: Efficient handling of multiple requests
- **Caching**: Model loading optimization

### Web Performance
- **Minimal Dependencies**: Lightweight frontend
- **Efficient API**: RESTful endpoints with JSON responses
- **Error Recovery**: Graceful handling of network issues

## 🔍 Evaluation Metrics

The models are evaluated using:
- **BLEU Score**: Primary metric for translation quality
- **Generation Length**: Average length of generated translations
- **Training Loss**: Convergence monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Helsinki-NLP**: Base MarianMT model
- **Hugging Face**: Transformers library and ecosystem
- **Weights & Biases**: Training monitoring and experiment tracking
- **Hmong Community**: Language expertise and cultural insights

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Contact the development team
- Check the documentation

---

**Note**: This system is designed for educational and research purposes. For production use, additional validation and testing is recommended.
