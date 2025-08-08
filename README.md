# Medical Chatbot with LLMs, LangChain, Pinecone, Flask & AWS

A comprehensive medical chatbot built using Large Language Models (LLMs) with Retrieval Augmented Generation (RAG) architecture. This project demonstrates how to create an intelligent chatbot that can answer medical queries by leveraging custom knowledge bases.

## 🏗️ Architecture Overview

This project implements a RAG (Retrieval Augmented Generation) system that:
1. **Retrieves** relevant documents from a vector database
2. **Splits** documents into manageable chunks
3. **Stores** embeddings in Pinecone vector database for semantic search
4. **Retrieves** relevant context based on user queries
5. **Generates** responses using LLM with retrieved context

## 🚀 Features

- **Custom Knowledge Base**: Built from medical documents using RAG architecture
- **Semantic Search**: Powered by Pinecone vector database
- **LLM Integration**: Uses OpenAI GPT for natural language responses
- **Web Interface**: Clean Flask-based chat interface
- **Cloud Deployment**: Full AWS deployment with CI/CD pipeline
- **Conversation Memory**: Maintains chat history for better context

## 🛠️ Tech Stack

- **Programming Language**: Python 3.10
- **LLM**: OpenAI GPT
- **Orchestration**: LangChain
- **Vector Database**: Pinecone
- **Web Framework**: Flask (Frontend & Backend)
- **Deployment**: AWS (EC2, ECR)
- **CI/CD**: GitHub Actions
- **Containerization**: Docker

## 📋 Prerequisites

- Python 3.10+
- Conda or Python virtual environment
- OpenAI API key
- Pinecone API key
- AWS Account (for deployment)

## 🏃‍♂️ Quick Start

### STEP 1: Clone the Repository
```bash
git clone https://github.com/your-username/medical-chatbot-rag.git
cd medical-chatbot-rag
```

### STEP 2: Create Virtual Environment
```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### STEP 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### STEP 4: Environment Configuration
Create a `.env` file in the root directory:
```env
PINECONE_API_KEY=your_pinecone_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### STEP 5: Initialize Knowledge Base
```bash
# Store embeddings to Pinecone (run once)
python store_index.py
```

### STEP 6: Run the Application
```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
medical-chatbot/
├── .github/
│   └── workflows/
│       └── cicd.yaml          # GitHub Actions CI/CD
├── templates/
│   └── chat.html              # Frontend template
├── static/
│   └── style.css              # Styling
├── src/
│   ├── helper.py              # Utility functions
│   └── prompt.py              # Prompt templates
├── store_index.py             # Vector store initialization
├── app.py                     # Flask application
├── requirements.txt           # Dependencies
├── Dockerfile                 # Docker configuration
└── README.md
```

## 🔧 Key Components

### RAG Pipeline
1. **Document Loading**: Extract text from medical documents
2. **Text Chunking**: Split documents into manageable pieces
3. **Embedding Generation**: Convert text to vectors using sentence transformers
4. **Vector Storage**: Store embeddings in Pinecone for semantic search
5. **Query Processing**: Retrieve relevant context and generate responses

### Workflow vs Agents
- **Workflows (LangChain)**: Linear chains with predefined tasks
- **Agents (LangGraph)**: Complex, autonomous decision-making systems with retry logic

## ☁️ AWS Deployment

### Prerequisites
- AWS Account
- IAM User with appropriate permissions
- Docker installed locally

### Deployment Steps

#### 1. Create IAM User
Create an IAM user with the following policies:
- `AmazonEC2ContainerRegistryFullAccess`
- `AmazonEC2FullAccess`

#### 2. Create ECR Repository
```bash
# Create ECR repository
aws ecr create-repository --repository-name medicalbot
```
Save the repository URI: `812612911905.dkr.ecr.us-east-1.amazonaws.com/medicalbot`

#### 3. Launch EC2 Instance
- Choose Ubuntu AMI
- Instance type: t2.medium (recommended)
- Storage: 30GB
- Security Groups: Allow HTTP (80), HTTPS (443), Custom TCP (8080)

#### 4. Configure EC2 Instance
```bash
# Update system
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

#### 5. Setup Self-Hosted Runner
1. Go to GitHub Repository → Settings → Actions → Runners
2. Click "New self-hosted runner"
3. Choose Linux
4. Follow the provided commands on your EC2 instance

#### 6. Configure GitHub Secrets
Add the following secrets in GitHub repository settings:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION` (e.g., us-east-1)
- `ECR_REPO` (e.g., medicalbot)
- `PINECONE_API_KEY`
- `OPENAI_API_KEY`

### Docker Configuration

**Dockerfile:**
```dockerfile
FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]
```

### CI/CD Pipeline

The GitHub Actions workflow automatically:
1. Builds Docker image on code push
2. Pushes image to ECR
3. Deploys to EC2 instance
4. Handles port mapping and service restart

## 🔍 Understanding Vector Databases

Vector databases store data as numerical vectors in high-dimensional space, enabling:
- **Semantic Search**: Find similar content based on meaning, not exact matches
- **Efficient Retrieval**: Fast similarity searches using vector proximity
- **Scalable Storage**: Handle large volumes of unstructured data

## 📊 Monitoring & Optimization

### LangSmith Integration
Monitor your deployed chatbot with LangSmith for:
- Performance tracking
- Token cost analysis
- Failure detection and debugging
- Usage analytics

### Key Parameters to Tune
- **Chunk Size**: Balance between context and relevance (typically 500-1000 tokens)
- **Chunk Overlap**: Prevent context loss (typically 10-20% of chunk size)
- **K Value**: Number of retrieved documents (typically 3-5)
- **Temperature**: LLM creativity vs consistency

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**Issue**: Pinecone connection errors
**Solution**: Verify API key and index configuration

**Issue**: OpenAI rate limits
**Solution**: Implement exponential backoff or upgrade API plan

**Issue**: Memory errors during embedding
**Solution**: Reduce chunk size or process documents in batches

**Issue**: EC2 deployment fails
**Solution**: Check security groups and port configurations

## 📚 Additional Resources

- [LangChain Documentation](https://docs.langchain.com/)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
