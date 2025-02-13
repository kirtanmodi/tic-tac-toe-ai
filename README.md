# Your Project Name

A full-stack application built with React and FastAPI.

## Overview

Brief description of your project and its main features.

## Tech Stack

### Frontend
- React
- TypeScript
- Create React App

### Backend
- Python
- FastAPI
- Uvicorn
- Pandas (for data processing)
- SQLAlchemy (if you're using a database)

### Infrastructure
- Docker
- Docker Compose
- Nginx (reverse proxy)

## Getting Started

### Prerequisites
- Node.js (v14 or higher)
- Python 3.8 or higher
- pip
- Docker & Docker Compose

### Installation

#### Local Development

1. Clone the repository:
```bash
git clone <your-repo-url>
```

2. Frontend setup:
```bash
cd frontend
npm install
npm start
```

3. Backend setup:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Docker Setup

1. Build and run the containers:
```bash
docker-compose up --build
```

This will start:
- Frontend container (React) on port 3000
- Backend container (FastAPI) on port 8000
- Nginx reverse proxy on port 80

## Development

### Frontend
The frontend will be running at http://localhost:3000

### Backend
The backend API will be running at http://localhost:8000

API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Deployment

### Production Setup

1. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your production settings
```

2. Deploy using Docker Compose:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Cloud Deployment
The application is deployed on Render and can be accessed at:
https://dashboard.render.com/web/srv-cun52vd6l47c739bt3r0/deploys/dep-cun5g4lsvqrc73foaku0

### Server Requirements
- Ubuntu 20.04 or higher
- Docker
- Docker Compose
- Minimum 2GB RAM
- 20GB storage

### CI/CD Pipeline
The application uses GitHub Actions for continuous integration and deployment:
- Automated testing
- Docker image building
- Deployment to production server

## Testing

### Frontend
```bash
cd frontend
npm test
```

### Backend
```bash
cd backend
pytest
```

### Docker Testing
```bash
docker-compose -f docker-compose.test.yml up --build
```

## Project Structure
```
├── frontend/          # React frontend
│   ├── src/          # Source files
│   ├── public/       # Static files
│   ├── Dockerfile    # Frontend Docker config
│   └── package.json  # Dependencies
│
├── backend/          # FastAPI backend
│   ├── app/         # Application code
│   ├── tests/       # Test files
│   ├── Dockerfile   # Backend Docker config
│   └── requirements.txt
│
├── nginx/           # Nginx configuration
│   └── nginx.conf
│
├── docker-compose.yml        # Docker compose config
├── docker-compose.prod.yml   # Production Docker compose
├── docker-compose.test.yml   # Testing Docker compose
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- List any libraries, tools, or resources you want to acknowledge
- Credit any inspirations or references
