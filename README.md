# Web Application Firewall (WAF)

A simple Web Application Firewall (WAF) implemented in Python using Flask. This WAF filters incoming HTTP requests for potential malicious content to protect web applications from common attacks such as SQL injection and Cross-Site Scripting (XSS).

## Features
- Basic detection of SQL Injection attempts.
- Basic detection of XSS attempts.
- Blocks requests containing harmful patterns.

## Technologies Used
- **Python**
- **Flask**: A lightweight WSGI web application framework.

## Requirements
- **Python 3.6+**
- **Flask** library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Web-Application-Firewall-WAF.git
   cd Web-Application-Firewall-WAF
   ```

## Usage

1. **Start the WAF:**
   ```bash
   sudo python3 waf.py
   ```
  This will start the WAF on `http://localhost:5000`.

2. Test the WAF:
- **Send a normal request:**
  ```bash
  curl -X POST http://localhost:5000/submit -d "name=John&age=30"
  ```
* **Send a malicious request:**
  ```bash
  curl -X POST http://localhost:5000/submit -d "query=SELECT * FROM users"
  ```
You should see a "403 Access Denied" response for the malicious request.

## Limitations

- This WAF implementation is very basic and should not be used in a production environment without further enhancements.
* The pattern matching is case-sensitive and can be bypassed with obfuscation.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for enhancements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Conclusion
This implementation serves as a basic foundation for a web application firewall. You can expand it by adding more sophisticated rules, integrating with a logging system, or creating a user interface for monitoring traffic.

