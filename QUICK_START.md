# Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the API
```bash
python start.py --reload
```

### 3. Test the API
Open your browser and go to: **http://localhost:8000/docs**

## 🎯 Quick Examples

### Generate a Random Person
```bash
curl http://localhost:8000/api/person
```

### Generate 5 Random People
```bash
curl "http://localhost:8000/api/person/bulk?count=5"
```

### Generate Company Data
```bash
curl http://localhost:8000/api/company
```

### Generate Credit Card Data
```bash
curl http://localhost:8000/api/credit-card
```

### Generate Custom Data (10 emails)
```bash
curl "http://localhost:8000/api/custom?data_type=email&count=10"
```

## 📚 Available Endpoints

| Endpoint | Description | Example |
|----------|-------------|---------|
| `/api/person` | Single person data | `GET /api/person` |
| `/api/person/bulk` | Multiple people | `GET /api/person/bulk?count=10` |
| `/api/company` | Company data | `GET /api/company` |
| `/api/company/bulk` | Multiple companies | `GET /api/company/bulk?count=5` |
| `/api/credit-card` | Credit card info | `GET /api/credit-card` |
| `/api/product` | Product data | `GET /api/product` |
| `/api/technical` | Technical data | `GET /api/technical` |
| `/api/custom` | Custom data types | `GET /api/custom?data_type=name&count=3` |

## 🌍 Supported Locales

Add `?locale=XX_XX` to any endpoint:
- `en_US` - English (US)
- `en_GB` - English (UK)  
- `de_DE` - German
- `fr_FR` - French
- `es_ES` - Spanish

Example: `GET /api/person?locale=de_DE`

## 🔧 Custom Data Types

Use `/api/custom?data_type=TYPE&count=N` where TYPE can be:
- `name`, `email`, `phone`, `address`
- `text`, `sentence`, `word`, `url`
- `date`, `time`, `datetime`, `color`
- `job`, `company`, `city`, `country`
- `currency`, `file_path`, `file_name`, `file_extension`

## 📖 Full Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/api/health

## 🧪 Test the API

Run the test script to verify everything works:
```bash
python test_api.py
```

## 🛠️ Development

### Start with auto-reload (development)
```bash
python start.py --reload
```

### Start on different port
```bash
python start.py --port 8080
```

### Start with multiple workers (production)
```bash
python start.py --workers 4
```

## 📁 Project Structure

```
Random Data Gen/
├── main.py              # Main FastAPI application
├── start.py             # Startup script
├── test_api.py          # Test script
├── requirements.txt     # Dependencies
├── README.md           # Full documentation
├── QUICK_START.md      # This file
└── .gitignore          # Git ignore rules
```

## 🎉 You're Ready!

Your Random Data Generator API is now running and ready to use! 

Visit http://localhost:8000/docs to explore the interactive API documentation. 