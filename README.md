## Running The Application

## 📋 Prerequisites
1. Install **Docker** and **Docker Compose**.
2. Set up the following environment variables on your server:

```plaintext
DB_HOST=db
DB_PORT=5432
DB_USER=user
DB_PASSWORD=password
DB_NAME=document_db
OPEN_AI_KEY='your_key' 
# check this for getting OpenAI keyhttps://platform.openai.com/account/api-keys
```

3. Build and run the containers

```
    docker-compose up --build
```

4. Fix For Table

exec into db container and open the postgres shell to create the table. 
This is due to an ongoing bug in FASTApi of not triggering startup events in docker.
**Solutions For Potential Fix Are Most welcome**

NOTE:- Not using alembic versioning as there is only one table.

```
    docker exec -it postgres_db psql -U admin  -d document_db
    CREATE TABLE documents etc. 
```

5. Api Usages

🔗 API Endpoints
➡️ Document Ingestion API
Endpoint: /ingest
Method: POST
Description: Upload documents, generate embeddings, and store them.

➡️ Q&A API
Endpoint: /qa
Method: POST
Description: Submit a question and retrieve answers based on RAG.

➡️ Document Selection API
Endpoint: /select
Method: POST
Description: Specify which documents to include in the Q&A process.

