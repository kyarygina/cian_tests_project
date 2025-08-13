add_favorite_response = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "folder": {
      "type": ["boolean", "null"]
    },
    "hasFolders": {
      "type": ["boolean", "null"]
    },
    "newbuildingId": {
      "type": "integer"
    },
    "isAdded": {
      "type": "boolean"
    }
  },
  "required": [
    "folder",
    "hasFolders",
    "newbuildingId",
    "isAdded"
  ]
}