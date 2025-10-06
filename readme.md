# Computer Vision based AC Automation Controller (CVAC)

A Python-based automation system for controlling **LG ThinQ** air conditioning units through the official LG ThinQ API. This project provides a simple interface to manage AC operations including power control, temperature settings, mode changes, and fan speed adjustments.

> **Note**: Computer Vision (CV) integration for visual AC state detection is planned for implementation this week, which will add visual monitoring capabilities to complement the API control.

## Features

- **LG ThinQ Integration**: Direct control of LG ThinQ-enabled AC units
- **Power Control**: Turn AC on/off remotely
- **Temperature Management**: Set target temperature in Celsius
- **Mode Selection**: Switch between different AC modes (AIR_DRY, COOL, FAN, AUTO)
- **Fan Speed Control**: Adjust fan speed (HIGH, AUTO, LOW, MID)
- **Status Monitoring**: Get current AC status and settings
- **Secure API Integration**: Uses Bearer token authentication with LG ThinQ API keys
- **CV Integration** (Coming Soon): Visual state detection and monitoring capabilities

## Project Structure

```
CVAC/
├── AC.py           # Main script for AC control
├── ACC.py          # ACController class implementation
├── readme.md       # This file
├── .env           # Environment variables (create this file)
└── cvac/          # Virtual environment directory
```

## Prerequisites

- Python 3.7+
- Internet connection for API calls
- **LG ThinQ-enabled air conditioning unit**
- LG ThinQ mobile app installed and AC registered
- Valid LG ThinQ API credentials

## Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/jayraneo/AC-Automation.git
   cd AC-Automation
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   python -m venv cvac
   cvac\Scripts\activate  # On Windows
   ```

3. **Install required packages**
   ```bash
   pip install requests python-dotenv
   ```

4. **Create environment variables file**
   Create a `.env` file in the project root with the following variables:
   ```env
   API_KEY=your_lg_thinq_api_key_here
   PAT=your_personal_access_token_here
   DEVICE_ID=your_ac_device_id_here
   COUNTRY=your_country_code_here
   API_LINK=https://aic.lge.com
   ```

## Getting LG ThinQ API Credentials

### Method 1: Official LG Developer Portal (Recommended)
1. **Register as LG Developer**
   - Visit [LG Developer Portal](https://developer.lge.com/)
   - Create an account and verify your email
   - Apply for ThinQ API access

2. **Create Application**
   - Navigate to "My Applications"
   - Create a new application for "ThinQ Platform"
   - Fill in application details and submit for approval

3. **Get API Credentials**
   - Once approved, you'll receive:
     - `API_KEY`: Your application's API key
     - Access to generate Personal Access Tokens (`PAT`)

### Method 2: Reverse Engineering (Advanced Users)
1. **Using Network Monitoring Tools**
   - Install network monitoring app (like Packet Capture for Android)
   - Monitor LG ThinQ app traffic during login/device control
   - Extract API endpoints and authentication tokens

2. **Using Browser Developer Tools**
   - Access LG ThinQ web interface
   - Open browser developer tools (F12)
   - Monitor Network tab during authentication
   - Copy authentication headers and tokens

### Method 3: Community Tools
- **wideq2**: Python library for LG ThinQ API
  ```bash
  pip install wideq2
  ```
- **LG ThinQ CLI**: Command-line tools for token extraction
- **GitHub Projects**: Search for "lg thinq" repositories with token generation scripts

### Getting Device Information
1. **Device ID**: 
   - Found in LG ThinQ mobile app under device settings
   - Or use API call to list registered devices

2. **Country Code**:
   - Use your country's ISO code (US, KR, IN, etc.)
   - Must match your LG account region

### Important Notes
- **Rate Limiting**: LG ThinQ API has rate limits (typically 1000 requests/day)
- **Token Expiry**: PAT tokens expire and need renewal (usually 30-90 days)
- **Device Registration**: AC must be registered in LG ThinQ app first
- **Regional Differences**: API endpoints may vary by country

## Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `API_KEY` | LG ThinQ API key from developer portal | `abc123def456` |
| `PAT` | Personal Access Token (Bearer token) | `eyJhbGciOiJIUzI1NiIs...` |
| `DEVICE_ID` | LG ThinQ device identifier for your AC | `lg_ac_12345` |
| `COUNTRY` | Country code matching your LG account | `US`, `KR`, `IN`, `JP` |
| `API_LINK` | LG ThinQ API base URL | `https://aic.lge.com` |

### Client Configuration

The system uses a fixed client ID (`JAY0066`) and generates unique message IDs for each request to ensure proper API communication.

## Usage

### Basic Usage

```python
from ACC import ACController
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize controller
ac = ACController(
    API_KEY=os.getenv("API_KEY"),
    PAT=os.getenv("PAT"),
    DEVICE_ID=os.getenv("DEVICE_ID"),
    COUNTRY=os.getenv("COUNTRY")
)

# Turn on the AC
ac.turn_on()
```

### Available Methods

#### Power Control
```python
ac.turn_on()    # Turn AC on
ac.turn_off()   # Turn AC off
```

#### Temperature Control
```python
ac.set_temperature(22)  # Set temperature to 22°C
ac.set_temperature(25)  # Set temperature to 25°C
```

#### Mode Control
```python
ac.set_mode("COOL")     # Cooling mode
ac.set_mode("FAN")      # Fan only mode
ac.set_mode("AUTO")     # Auto mode
ac.set_mode("AIR_DRY")  # Dehumidify mode
```

#### Fan Speed Control
```python
ac.set_fan_speed("HIGH")  # High speed
ac.set_fan_speed("MID")   # Medium speed
ac.set_fan_speed("LOW")   # Low speed
ac.set_fan_speed("AUTO")  # Auto speed
```

#### Status Monitoring
```python
status = ac.get_status()  # Get current AC status
print(status)
```

### Running the Script

To run the main automation script:

```bash
python AC.py
```

## API Response Handling

The controller provides detailed response information for debugging:
- **Status Code**: HTTP response status
- **Raw Response**: Complete API response text
- **JSON Parsing**: Automatic JSON parsing with error handling

## Error Handling

The system includes comprehensive error handling:
- **Network Errors**: Handles connection timeouts and network issues
- **Authentication Errors**: Validates API credentials
- **JSON Parsing Errors**: Manages malformed API responses
- **Device Communication Errors**: Handles device-specific issues

## Security Considerations

- Store sensitive credentials in the `.env` file (never commit to version control)
- Add `.env` to your `.gitignore` file
- Use environment-specific API endpoints
- Regularly rotate your API keys and tokens

## Troubleshooting

### Common Issues

1. **Authentication Errors (401/403)**
   - Check your LG ThinQ API_KEY and PAT values
   - Ensure your PAT token hasn't expired (renew if needed)
   - Verify your LG developer account is active
   - Confirm device is properly registered in LG ThinQ app

2. **Device Not Found (404)**
   - Confirm DEVICE_ID matches exactly from LG ThinQ app
   - Check if AC is online and connected to Wi-Fi
   - Ensure device is registered under the same LG account

3. **Rate Limiting (429)**
   - LG ThinQ has daily API limits (typically 1000 requests)
   - Wait for rate limit reset or reduce request frequency
   - Consider implementing request caching

4. **Network Timeouts**
   - Verify internet connection
   - Check if `aic.lge.com` is accessible from your network
   - Consider firewall/proxy restrictions
   - Some corporate networks block IoT API endpoints

5. **Country/Region Issues**
   - Ensure COUNTRY code matches your LG account region
   - Some features may be region-specific
   - API endpoints might differ by country

### Debug Mode

All API calls print status codes and raw responses for debugging. Monitor the console output to troubleshoot issues.

## Dependencies

- `requests`: HTTP library for LG ThinQ API calls
- `python-dotenv`: Environment variable management
- `uuid`: Unique identifier generation (built-in)
- `os`: Operating system interface (built-in)

### Optional Dependencies (For CV Integration)
Coming this week:
- `opencv-python`: Computer vision processing
- `numpy`: Numerical operations for image processing
- `pillow`: Image manipulation and processing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check with your AC manufacturer regarding API usage terms and conditions.

## Support

For issues related to:
- **Code**: Open an issue on GitHub
- **LG ThinQ API**: Contact LG Developer Support or check [LG Developer Portal](https://developer.lge.com/)
- **Device Setup**: Refer to your LG ThinQ AC unit's documentation
- **LG ThinQ App**: LG Customer Support

### Useful Resources
- [LG ThinQ Developer Documentation](https://developer.lge.com/resource/thinq)
- [LG ThinQ Mobile App](https://www.lg.com/us/support/mobile-app)
- [Community LG ThinQ Projects](https://github.com/topics/lg-thinq)
- [wideq2 Library Documentation](https://github.com/ollo69/ha-smartthinq-sensors)

## Changelog

### v1.1.0 (Coming This Week)
- **CV Integration**: Computer vision capabilities for visual AC state detection
- **Image Processing**: Real-time monitoring of AC display/indicators
- **Visual Feedback**: Complement API control with visual confirmation

### v1.0.0
- Initial release with LG ThinQ integration
- Basic AC control functionality (power, temperature, mode, fan speed)
- LG ThinQ API integration with authentication
- Environment variable configuration
- Comprehensive error handling and debugging

---

**Note**: This controller is specifically designed for LG ThinQ-enabled air conditioning units. Ensure you have proper authorization to control the target AC device and comply with LG's terms of service and API usage policies. The upcoming CV integration will provide additional visual monitoring capabilities for enhanced automation control.