# Django-REST-Framework-CRUD-operations-
Implemented basic REST APIs for creating, reading, updating and deleting Planet information using Django-Rest framework.

Create: POST /v1/claim
Create resource will contain the name, expiration date (validated future), and claimed body ID (validated from the OpenData API)

Update: PUT /v1/claim/:id
Update resource allow contain the name and expiration date (validated future) to be updated.

Read: GET /v1/claim/:id
Read the resource and allow for a query parameter to optionally read all body data data from OpenData and attach it to the outbound resource

Delete: DELETE /v1/claim/:id
Delete the claim.
