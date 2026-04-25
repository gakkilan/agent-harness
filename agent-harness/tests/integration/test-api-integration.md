# Integration Test: Multi-step Task

## Task
Create a simple REST API with Flask that:
1. Accepts POST requests with JSON data
2. Validates the input
3. Stores data in memory
4. Returns appropriate HTTP status codes

## Requirements
- Endpoint: `/api/data`
- Methods: POST, GET
- Validation: required fields, data types
- Error handling: 400 for bad input, 404 for missing data

## Test Steps
1. Create Flask app
2. Implement POST endpoint
3. Implement GET endpoint
4. Test with valid data
5. Test with invalid data
6. Verify error responses

## Success Criteria
- All endpoints work correctly
- Proper validation
- Correct status codes
- Error messages are informative
