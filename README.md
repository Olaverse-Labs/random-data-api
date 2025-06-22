# Random Data Generator API

A comprehensive FastAPI-based REST API for generating various types of random data. Perfect for testing, development, and data seeding purposes.

## Features

- **Person Data**: Names, emails, addresses, phone numbers, SSNs
- **Company Data**: Company names, industries, contact information
- **Credit Card Data**: Card numbers, expiry dates, CVVs
- **Product Data**: Product names, categories, prices, descriptions
- **Technical Data**: IP addresses, user agents, MAC addresses, UUIDs
- **Custom Data**: Flexible endpoint for generating any supported data type
- **Bulk Generation**: Generate multiple records at once
- **Multi-locale Support**: Generate data in different locales

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd random-data-generator-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Deployment

### Deploy to Elest.io

This API is ready for deployment to Elest.io! Follow these steps:

1. **Run the deployment script** (optional):
```bash
chmod +x deploy.sh
./deploy.sh
```

2. **Push to Git repository**:
```bash
git add .
git commit -m "Ready for Elest.io deployment"
git push origin main
```

3. **Deploy on Elest.io**:
   - Go to [elest.io](https://elest.io)
   - Create new app → Deploy from Git
   - Connect your repository
   - Configure with the provided `elestio.yml`
   - Deploy!

For detailed deployment instructions, see [deploy.md](deploy.md).

### Other Deployment Options

- **Docker**: Use the provided `Dockerfile`
- **Railway**: Connect your Git repository
- **Render**: Use the Dockerfile for deployment
- **Heroku**: Add a `Procfile` with: `web: uvicorn main:app --host 0.0.0.0 --port $PORT`

## API Endpoints

### Base URL
```
http://localhost:8000
```

### Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Available Endpoints

#### 1. Root Endpoint
- **GET** `/` - API information and available endpoints

#### 2. Person Data
- **GET** `/api/person` - Generate single person data
- **GET** `/api/person/bulk?count=10` - Generate multiple person records

#### 3. Company Data
- **GET** `/api/company` - Generate single company data
- **GET** `/api/company/bulk?count=10` - Generate multiple company records

#### 4. Credit Card Data
- **GET** `/api/credit-card` - Generate credit card information

#### 5. Product Data
- **GET** `/api/product` - Generate product information

#### 6. Technical Data
- **GET** `/api/technical` - Generate technical data (IP, user agent, etc.)

#### 7. Custom Data
- **GET** `/api/custom?data_type=email&count=5` - Generate custom data types

#### 8. Health Check
- **GET** `/api/health` - API health status

## Usage Examples

### Generate a Single Person
```bash
curl http://localhost:8000/api/person
```

### Generate Multiple People
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

### Generate Custom Data
```bash
# Generate 10 email addresses
curl "http://localhost:8000/api/custom?data_type=email&count=10"

# Generate 5 random names
curl "http://localhost:8000/api/custom?data_type=name&count=5"

# Generate 3 random addresses
curl "http://localhost:8000/api/custom?data_type=address&count=3"
```

### Using Different Locales
```bash
# Generate person data with German locale
curl "http://localhost:8000/api/person?locale=de_DE"

# Generate company data with French locale
curl "http://localhost:8000/api/company?locale=fr_FR"
```

## Supported Data Types for Custom Endpoint

- `name` - Full names
- `email` - Email addresses
- `phone` - Phone numbers
- `address` - Full addresses
- `text` - Random text paragraphs
- `sentence` - Random sentences
- `word` - Random words
- `url` - URLs
- `date` - Dates
- `time` - Times
- `datetime` - Date and time
- `color` - Color names
- `job` - Job titles
- `company` - Company names
- `city` - City names
- `country` - Country names
- `currency` - Currency codes
- `file_path` - File paths
- `file_name` - File names
- `file_extension` - File extensions

## Supported Locales

- `en_US` - English (United States)
- `en_GB` - English (United Kingdom)
- `de_DE` - German
- `fr_FR` - French
- `es_ES` - Spanish

## Response Examples

### Person Data Response
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "(555) 123-4567",
  "address": "123 Main St",
  "city": "New York",
  "state": "NY",
  "zipcode": "10001",
  "country": "United States",
  "date_of_birth": "1985-03-15",
  "ssn": "123-45-6789",
  "username": "johndoe123"
}
```

### Company Data Response
```json
{
  "name": "TechCorp Solutions",
  "industry": "Technology",
  "website": "https://techcorp-solutions.com",
  "email": "info@techcorp-solutions.com",
  "phone": "(555) 987-6543",
  "address": "456 Business Ave",
  "city": "San Francisco",
  "state": "CA",
  "zipcode": "94102",
  "country": "United States",
  "founded_year": 2010,
  "employee_count": 250
}
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- `200` - Success
- `400` - Bad Request (invalid parameters)
- `500` - Internal Server Error

## Development

### Project Structure
```
random-data-generator-api/
├── main.py              # Main FastAPI application
├── start.py             # Startup script
├── test_api.py          # Test script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── .dockerignore        # Docker ignore rules
├── elestio.yml          # Elest.io configuration
├── deploy.sh            # Deployment script
├── deploy.md            # Deployment guide
├── README.md           # This file
├── QUICK_START.md      # Quick start guide
└── .gitignore          # Git ignore rules
```

### Adding New Data Types

To add new data types to the custom endpoint, modify the `generate_custom_data` function in `main.py` and add new conditions for your data type.

### Testing

You can test the API using:
- The built-in Swagger UI at `/docs`
- curl commands
- Any HTTP client like Postman or Insomnia
- Run `python test_api.py` for automated testing

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 