from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from faker import Faker
import random
import json
import os
from datetime import datetime, timedelta

# Initialize Faker with multiple locales
fake = Faker(['en_US', 'en_GB', 'de_DE', 'fr_FR', 'es_ES'])

app = FastAPI(
    title="Random Data Generator API",
    description="A comprehensive API for generating various types of random data",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class PersonData(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    city: str
    state: str
    zipcode: str
    country: str
    date_of_birth: str
    ssn: str
    username: str

class CompanyData(BaseModel):
    name: str
    industry: str
    website: str
    email: str
    phone: str
    address: str
    city: str
    state: str
    zipcode: str
    country: str
    founded_year: int
    employee_count: int

class CreditCardData(BaseModel):
    number: str
    expiry: str
    cvv: str
    card_type: str
    holder_name: str

class ProductData(BaseModel):
    name: str
    category: str
    price: float
    description: str
    sku: str
    brand: str

class TechnicalData(BaseModel):
    ip_address: str
    user_agent: str
    mac_address: str
    uuid: str
    hash: str

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Random Data Generator API",
        "version": "1.0.0",
        "endpoints": {
            "person": "/api/person",
            "company": "/api/company", 
            "credit_card": "/api/credit-card",
            "product": "/api/product",
            "technical": "/api/technical",
            "custom": "/api/custom"
        },
        "docs": "/docs"
    }

@app.get("/api/person", response_model=PersonData)
async def generate_person(
    locale: Optional[str] = Query("en_US", description="Locale for data generation")
):
    """Generate random person data"""
    try:
        fake_locale = Faker(locale)
        return PersonData(
            first_name=fake_locale.first_name(),
            last_name=fake_locale.last_name(),
            email=fake_locale.email(),
            phone=fake_locale.phone_number(),
            address=fake_locale.street_address(),
            city=fake_locale.city(),
            state=fake_locale.state(),
            zipcode=fake_locale.zipcode(),
            country=fake_locale.country(),
            date_of_birth=fake_locale.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
            ssn=fake_locale.ssn(),
            username=fake_locale.user_name()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating person data: {str(e)}")

@app.get("/api/person/bulk", response_model=List[PersonData])
async def generate_persons(
    count: int = Query(10, ge=1, le=100, description="Number of persons to generate"),
    locale: Optional[str] = Query("en_US", description="Locale for data generation")
):
    """Generate multiple random person records"""
    try:
        fake_locale = Faker(locale)
        persons = []
        for _ in range(count):
            persons.append(PersonData(
                first_name=fake_locale.first_name(),
                last_name=fake_locale.last_name(),
                email=fake_locale.email(),
                phone=fake_locale.phone_number(),
                address=fake_locale.street_address(),
                city=fake_locale.city(),
                state=fake_locale.state(),
                zipcode=fake_locale.zipcode(),
                country=fake_locale.country(),
                date_of_birth=fake_locale.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
                ssn=fake_locale.ssn(),
                username=fake_locale.user_name()
            ))
        return persons
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating person data: {str(e)}")

@app.get("/api/company", response_model=CompanyData)
async def generate_company(
    locale: Optional[str] = Query("en_US", description="Locale for data generation")
):
    """Generate random company data"""
    try:
        fake_locale = Faker(locale)
        industries = ["Technology", "Healthcare", "Finance", "Retail", "Manufacturing", "Education", "Real Estate"]
        return CompanyData(
            name=fake_locale.company(),
            industry=random.choice(industries),
            website=fake_locale.url(),
            email=fake_locale.company_email(),
            phone=fake_locale.phone_number(),
            address=fake_locale.street_address(),
            city=fake_locale.city(),
            state=fake_locale.state(),
            zipcode=fake_locale.zipcode(),
            country=fake_locale.country(),
            founded_year=random.randint(1950, 2023),
            employee_count=random.randint(10, 10000)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating company data: {str(e)}")

@app.get("/api/company/bulk", response_model=List[CompanyData])
async def generate_companies(
    count: int = Query(10, ge=1, le=100, description="Number of companies to generate"),
    locale: Optional[str] = Query("en_US", description="Locale for data generation")
):
    """Generate multiple random company records"""
    try:
        fake_locale = Faker(locale)
        industries = ["Technology", "Healthcare", "Finance", "Retail", "Manufacturing", "Education", "Real Estate"]
        companies = []
        for _ in range(count):
            companies.append(CompanyData(
                name=fake_locale.company(),
                industry=random.choice(industries),
                website=fake_locale.url(),
                email=fake_locale.company_email(),
                phone=fake_locale.phone_number(),
                address=fake_locale.street_address(),
                city=fake_locale.city(),
                state=fake_locale.state(),
                zipcode=fake_locale.zipcode(),
                country=fake_locale.country(),
                founded_year=random.randint(1950, 2023),
                employee_count=random.randint(10, 10000)
            ))
        return companies
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating company data: {str(e)}")

@app.get("/api/credit-card", response_model=CreditCardData)
async def generate_credit_card():
    """Generate random credit card data"""
    try:
        card_types = ["Visa", "Mastercard", "American Express", "Discover"]
        card_type = random.choice(card_types)
        
        # Generate appropriate card number based on type
        if card_type == "Visa":
            number = fake.credit_card_number(card_type='visa')
        elif card_type == "Mastercard":
            number = fake.credit_card_number(card_type='mastercard')
        elif card_type == "American Express":
            number = fake.credit_card_number(card_type='amex')
        else:
            number = fake.credit_card_number(card_type='discover')
        
        return CreditCardData(
            number=number,
            expiry=fake.credit_card_expire(),
            cvv=fake.credit_card_security_code(),
            card_type=card_type,
            holder_name=fake.name()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating credit card data: {str(e)}")

@app.get("/api/product", response_model=ProductData)
async def generate_product():
    """Generate random product data"""
    try:
        categories = ["Electronics", "Clothing", "Books", "Home & Garden", "Sports", "Beauty", "Toys"]
        brands = ["Apple", "Samsung", "Nike", "Adidas", "Sony", "LG", "Dell", "HP", "Canon", "Nikon"]
        
        category = random.choice(categories)
        
        # Generate appropriate product name based on category
        if category == "Electronics":
            products = ["Smartphone", "Laptop", "Tablet", "Headphones", "Camera", "Speaker", "Monitor"]
        elif category == "Clothing":
            products = ["T-Shirt", "Jeans", "Shoes", "Jacket", "Dress", "Sweater", "Hat"]
        elif category == "Books":
            products = ["Novel", "Textbook", "Biography", "Cookbook", "Travel Guide", "Self-Help"]
        else:
            products = ["Product", "Item", "Goods", "Merchandise"]
        
        product_name = random.choice(products)
        
        return ProductData(
            name=f"{random.choice(brands)} {product_name}",
            category=category,
            price=round(random.uniform(10.0, 1000.0), 2),
            description=fake.text(max_nb_chars=200),
            sku=fake.ean13(),
            brand=random.choice(brands)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating product data: {str(e)}")

@app.get("/api/technical", response_model=TechnicalData)
async def generate_technical_data():
    """Generate random technical data"""
    try:
        return TechnicalData(
            ip_address=fake.ipv4(),
            user_agent=fake.user_agent(),
            mac_address=fake.mac_address(),
            uuid=fake.uuid4(),
            hash=fake.sha256()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating technical data: {str(e)}")

@app.get("/api/custom")
async def generate_custom_data(
    data_type: str = Query(..., description="Type of data to generate"),
    count: int = Query(1, ge=1, le=100, description="Number of records to generate"),
    locale: Optional[str] = Query("en_US", description="Locale for data generation")
):
    """Generate custom random data based on specified type"""
    try:
        fake_locale = Faker(locale)
        result = []
        
        for _ in range(count):
            if data_type.lower() == "name":
                result.append(fake_locale.name())
            elif data_type.lower() == "email":
                result.append(fake_locale.email())
            elif data_type.lower() == "phone":
                result.append(fake_locale.phone_number())
            elif data_type.lower() == "address":
                result.append(fake_locale.address())
            elif data_type.lower() == "text":
                result.append(fake_locale.text())
            elif data_type.lower() == "sentence":
                result.append(fake_locale.sentence())
            elif data_type.lower() == "word":
                result.append(fake_locale.word())
            elif data_type.lower() == "url":
                result.append(fake_locale.url())
            elif data_type.lower() == "date":
                result.append(fake_locale.date())
            elif data_type.lower() == "time":
                result.append(fake_locale.time())
            elif data_type.lower() == "datetime":
                result.append(fake_locale.date_time().isoformat())
            elif data_type.lower() == "color":
                result.append(fake_locale.color_name())
            elif data_type.lower() == "job":
                result.append(fake_locale.job())
            elif data_type.lower() == "company":
                result.append(fake_locale.company())
            elif data_type.lower() == "city":
                result.append(fake_locale.city())
            elif data_type.lower() == "country":
                result.append(fake_locale.country())
            elif data_type.lower() == "currency":
                result.append(fake_locale.currency())
            elif data_type.lower() == "file_path":
                result.append(fake_locale.file_path())
            elif data_type.lower() == "file_name":
                result.append(fake_locale.file_name())
            elif data_type.lower() == "file_extension":
                result.append(fake_locale.file_extension())
            else:
                raise HTTPException(status_code=400, detail=f"Unsupported data type: {data_type}")
        
        return {
            "data_type": data_type,
            "count": count,
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error generating custom data: {str(e)}")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 