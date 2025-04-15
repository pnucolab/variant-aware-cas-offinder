
How to deploy Source Code on local machines
===========================================

Docker compose tutorial
-----------------------

If the user wants to deploy on local machines, then follow the following steps.

1. Create a directory
2. Download frontend, backend, Caddyfile, and docker-compose.yml source codes to the directory
3. Download Cas-offinder from https://github.com/pnucolab/variant-aware-cas-offinder/raw/refs/heads/main/backend/cas-offinder and make it executable:

.. code-block:: bash
        
    chmod +x cas-offinder 

4. Build and start all services:

.. code-block:: bash
        
   docker compose build

5. After building, run the following command to start the services

.. code-block:: bash
        
   docker compose up -d

Check running container:

.. code-block:: bash
        
   docker compose ps

To run a command inside a running container (backend).

.. code-block:: bash
        
   docker compose exec backend sh

This is useful when you need to:

- Manually inspect or debug the backend container.
- Run Python scripts, check logs, or test API endpoints.
- Install additional dependencies inside the container temporarily.

To view logs (optional):

.. code-block:: bash
        
   docker compose logs backend

To stop the containers, run:

.. code-block:: bash
        
   docker compose down

To stop the backend, run:

.. code-block:: bash
        
   docker compose down backend



