#! /bin/bash

curl -X GET \
  -H 'Content-Type: application/json' \
  -H 'X-Auth-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ZTNkNDI5ZTdjZDQ3ZTAwNGM2N2RkMGMiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVkYzQ0NGQ1MTQ4NWM1MDA0YzBmYjIxMiJdLCJ0ZW5hbnRJZCI6IjVkYzQ0NGQzMTQ4NWM1MDA0YzBmYjIwYiIsImV4cCI6MTU4NjA4NDE1MSwidXNlcm5hbWUiOiJkZXZuZXR1c2VyIn0.EGvcTv78U7-mt0v1pPVsJOAWwghwjAa3ecWuU6qbwhA' \
   https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/
