# API Documentation

This API provides endpoints for sending emails and retrieving server time.

## Getting Started

Before using the API, make sure you have the necessary server key and environment variables set up in the `config.env` file.

### Base URL

The base URL for the API is: `https://web.uniport.up.railway.app`

## Endpoints

### Send Authentication Email

- **Endpoint:** `/dart/auth/:mail`
- **Method:** GET

#### Parameters

- `mail` (required): The recipient's email address.
- `key` (required): Server key for verification.
- `otpLength` (optional): Length of the OTP (default: 6).
- `CompanyName` (optional): Name of the company.

#### Example Usage

```http
GET https://web.uniport.up.railway.app/dart/auth/johndoe@example.com?key=your-server-key&otpLength=4&CompanyName=ACME
```
#### Response
```json
{
    "status": 200,
    "mail": "johndoe@example.com",
    "OTP": "1234",
    "success": true
}
```
