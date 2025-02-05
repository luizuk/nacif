# Fullstack Project - Backend and Frontend with Docker Compose

This project demonstrates a fullstack application using **FastAPI** for the backend and **Next.js** for the frontend, orchestrated with **Docker Compose**.

---

## Prerequisites

Before running the project, ensure the following tools are installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Project Structure

```plaintext
.
├── backend/              # Backend code (FastAPI)
│   ├── main.py           # Backend entry point
│   ├── Dockerfile        # Backend container configuration
│   ├── ...
├── frontend/             # Frontend code (Next.js)
│   ├── pages/            # Frontend routes and components
│   ├── Dockerfile        # Frontend container configuration
│   ├── ...
├── docker-compose.yml    # Docker services configuration
├── README.md             # Project documentation
└── test.db               # SQLite database
```

---

## Setup and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/luizuk/nacif
cd nacif
```

Replace `https://github.com/luizuk/nacif` with your Git repository URL.

---

### 2. Start the Services

Run the following command in the root directory of the project:

```bash
docker-compose up --build
```

This command will:

- Build the Docker images for the frontend and backend.
- Start the containers with the required environment configurations.

---

### 3. Access the Application

Once the services are running, you can access:

- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **Backend**: [http://localhost:8000/docs](http://localhost:8000/docs) (FastAPI Swagger UI)

---

## Docker Compose Configuration

The `docker-compose.yml` file defines two services: `backend` and `frontend`.

### Backend Service

- **Framework**: FastAPI
- **Port**: `8000`
- **Environment Variable**: `DATABASE_URL`
- **Database**: SQLite database (`test.db` file)

### Frontend Service

- **Framework**: Next.js
- **Port**: `3000`
- **Hot Reload**: Enabled via Docker volumes

---

## Useful Commands

### Stop Services and Remove Containers

```bash
docker-compose down -v
```

### Rebuild and Restart Services

```bash
docker-compose up --build
```

### View Logs for All Services

```bash
docker-compose logs -f
```

---

## How It Works

1. **Backend**:

   - A FastAPI server runs inside a Docker container on port `8000`.
   - SQLite is used as the database, and the `test.db` file is mounted into the container.

2. **Frontend**:
   - A Next.js development server runs inside another Docker container on port `3000`.
   - The frontend communicates with the backend API for authentication and other operations.

---

## Common Issues

### Docker Permission Error

If you encounter permission issues, ensure your user belongs to the `docker` group:

```bash
sudo usermod -aG docker $USER
```

Restart your terminal or log out and back in.

---

### Port Already in Use

If ports `3000` or `8000` are already occupied, stop the conflicting processes:

```bash
lsof -i:3000
lsof -i:8000
```

Kill the processes using the ports:

```bash
kill -9 <PID>
```

---

## Contributing

Contributions are welcome! Please open a **Pull Request** or create an **Issue** to suggest improvements.

---
