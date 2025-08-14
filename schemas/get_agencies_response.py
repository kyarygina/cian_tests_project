get_agencies_response = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "total": {
      "type": "integer"
    },
    "limit": {
      "type": "integer"
    },
    "meta": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "keywords": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "description",
        "keywords"
      ]
    },
    "items": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "cianUserId": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "age": {
              "type": "string"
            },
            "avatarUrl": {
              "type": "string"
            },
            "offersCount": {
              "type": "string"
            },
            "hasRgrParticipation": {
              "type": "boolean"
            },
            "userTrustLevelNumber": {
              "type": "integer"
            },
            "userTrustLevelName": {
              "type": "string"
            },
            "hasVerifiedDocuments": {
              "type": "null"
            },
            "services": {
              "type": "string"
            },
            "hasKokonParticipation": {
              "type": "boolean"
            }
          },
          "required": [
            "cianUserId",
            "name",
            "age",
            "avatarUrl",
            "offersCount",
            "hasRgrParticipation",
            "userTrustLevelNumber",
            "userTrustLevelName",
            "hasVerifiedDocuments",
            "services",
            "hasKokonParticipation"
          ]
        },
        {
          "type": "object",
          "properties": {
            "cianUserId": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "age": {
              "type": "string"
            },
            "avatarUrl": {
              "type": "null"
            },
            "offersCount": {
              "type": "string"
            },
            "hasRgrParticipation": {
              "type": "boolean"
            },
            "userTrustLevelNumber": {
              "type": "null"
            },
            "userTrustLevelName": {
              "type": "null"
            },
            "hasVerifiedDocuments": {
              "type": "boolean"
            },
            "services": {
              "type": "string"
            },
            "hasKokonParticipation": {
              "type": "boolean"
            }
          },
          "required": [
            "cianUserId",
            "name",
            "age",
            "avatarUrl",
            "offersCount",
            "hasRgrParticipation",
            "userTrustLevelNumber",
            "userTrustLevelName",
            "hasVerifiedDocuments",
            "services",
            "hasKokonParticipation"
          ]
        }
      ]
    }
  },
  "required": [
    "total",
    "limit",
    "meta",
    "items"
  ]
}