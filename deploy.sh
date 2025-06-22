#!/bin/bash

# Random Data Generator API - Deployment Script for Elest.io
# This script helps prepare and deploy your API to Elest.io

set -e

echo "🚀 Random Data Generator API - Elest.io Deployment"
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if required files exist
print_status "Checking required files..."

required_files=("main.py" "requirements.txt" "Dockerfile" ".dockerignore" "elestio.yml")
missing_files=()

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -ne 0 ]; then
    print_error "Missing required files: ${missing_files[*]}"
    exit 1
fi

print_success "All required files found!"

# Check if git is initialized
if [ ! -d ".git" ]; then
    print_warning "Git repository not initialized. Initializing..."
    git init
    git add .
    git commit -m "Initial commit for Elest.io deployment"
    print_success "Git repository initialized!"
else
    print_status "Git repository found. Checking status..."
    if [ -n "$(git status --porcelain)" ]; then
        print_warning "Uncommitted changes detected. Committing..."
        git add .
        git commit -m "Update for Elest.io deployment"
        print_success "Changes committed!"
    else
        print_success "No uncommitted changes."
    fi
fi

# Test the application locally (optional)
read -p "Do you want to test the application locally before deployment? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Testing application locally..."
    
    # Check if Python is available
    if ! command -v python &> /dev/null; then
        print_error "Python is not installed or not in PATH"
        exit 1
    fi
    
    # Install dependencies
    print_status "Installing dependencies..."
    pip install -r requirements.txt
    
    # Start the application in background
    print_status "Starting application for testing..."
    python main.py &
    APP_PID=$!
    
    # Wait for application to start
    sleep 3
    
    # Test the health endpoint
    if curl -f http://localhost:8000/api/health > /dev/null 2>&1; then
        print_success "Application is running and responding!"
        print_status "You can test it at: http://localhost:8000/docs"
    else
        print_error "Application failed to start or respond"
        kill $APP_PID 2>/dev/null || true
        exit 1
    fi
    
    # Stop the application
    kill $APP_PID 2>/dev/null || true
    print_success "Local test completed!"
fi

# Deployment instructions
echo
echo "📋 Deployment Instructions for Elest.io:"
echo "========================================"
echo
echo "1. 📝 Push your code to a Git repository (GitHub, GitLab, etc.):"
echo "   git remote add origin <your-repo-url>"
echo "   git push -u origin main"
echo
echo "2. 🌐 Go to Elest.io dashboard:"
echo "   https://elest.io"
echo
echo "3. 🚀 Create a new app:"
echo "   - Click 'New App' or 'Deploy'"
echo "   - Choose 'Deploy from Git'"
echo "   - Connect your Git provider"
echo "   - Select your repository"
echo
echo "4. ⚙️  Configure your app:"
echo "   - App Name: random-data-generator-api"
echo "   - Branch: main"
echo "   - Build Command: (leave empty - uses Dockerfile)"
echo "   - Start Command: (leave empty - uses Dockerfile)"
echo
echo "5. 🔧 Environment Variables:"
echo "   - PYTHONUNBUFFERED=1"
echo "   - PORT=8000"
echo
echo "6. 💾 Resources (recommended):"
echo "   - CPU: 0.5 cores"
echo "   - Memory: 512 MB"
echo "   - Storage: 1 GB"
echo
echo "7. 🎯 Deploy:"
echo "   - Click 'Deploy'"
echo "   - Wait for build to complete (2-5 minutes)"
echo
echo "8. ✅ Test your deployment:"
echo "   - Visit: https://your-app-name.elestio.app"
echo "   - Check docs: https://your-app-name.elestio.app/docs"
echo "   - Test health: https://your-app-name.elestio.app/api/health"
echo

print_success "Deployment preparation completed!"
print_status "Follow the instructions above to deploy to Elest.io"
print_status "For detailed instructions, see: deploy.md" 