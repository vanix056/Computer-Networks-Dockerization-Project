from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Coupon data
coupons = [
    {"id": 1, "title": "10% off", "expiry": "2024-12-31", "description": "Get 10% off on all items.", "code": "SAVE10"},
    {"id": 2, "title": "20% off", "expiry": "2024-12-28", "description": "Enjoy 20% off on your next purchase.", "code": "DISCOUNT20"},
    {"id": 3, "title": "Free Shipping", "expiry": "2025-01-15", "description": "Free shipping on orders over $50.", "code": "FREESHIP"},
    {"id": 4, "title": "Buy 1 Get 1 Free", "expiry": "2024-12-30", "description": "Buy one item and get another one free.", "code": "BOGO"},
    {"id": 5, "title": "15% off", "expiry": "2025-01-10", "description": "15% off on electronics.", "code": "ELECTRO15"}
]

@app.route('/coupons')
def get_coupons():
    return jsonify(coupons)

# Frontend route
@app.route('/')
def home():
    template = """
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>Abdullah's Coupon WebApp</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background: #000;
                color: #FFFFFF;
            }
            .header {
                text-align: center;
                margin-bottom: 20px;
            }
            .header h1 {
                font-size: 3em;
                color: #FFD700;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }
            .header p {
                font-size: 1.3em;
                color: #FFF;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin: 0 auto;
                max-width: 1200px;
            }
            .coupon {
                background: linear-gradient(145deg, #1e1e1e, #333);
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
                transition: transform 0.3s, box-shadow 0.3s;
                position: relative;
                overflow: hidden;
            }
            .coupon:hover {
                transform: scale(1.1);
                box-shadow: 0 8px 12px rgba(0, 0, 0, 0.7);
            }
            .coupon h2 {
                margin: 0 0 10px;
                color: #FFFFFF;
                font-size: 1.8em;
                text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.4);
            }
            .coupon p {
                margin: 8px 0;
                color: #FFF;
            }
            .coupon-code {
                font-weight: bold;
                color: #00FF00;
                font-size: 1.3em;
                margin-bottom: 10px;
            }
            .coupon-expiry {
                color: #FF4500;
                font-weight: bold;
                font-size: 1em;
            }
            .copy-btn {
                background-color: #FFD700;
                color: #000;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 1em;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .copy-btn:hover {
                background-color: #FFC107;
            }
            .footer {
                text-align: center;
                margin-top: 40px;
                color: #FFFFFF;
                font-size: 0.9em;
            }
            .footer a {
                color: #FFD700;
                text-decoration: none;
            }
            .footer a:hover {
                text-decoration: underline;
            }
        </style>
        <script>
            function copyCode(code) {
                navigator.clipboard.writeText(code).then(() => {
                    alert(`Coupon code "${code}" copied to clipboard!`);
                });
            }
        </script>
    </head>
    <body>
        <div class=\"header\">
            <h1>Abdullah's Coupon WebApp</h1>
            <p>Total Coupons Available: <span style=\"font-weight:bold; color:#FFD700;\">{{ coupons|length }}</span></p>
        </div>
        <div class=\"grid\">
        {% for coupon in coupons %}
        <div class=\"coupon\">
            <h2>{{ coupon.title }}</h2>
            <p>{{ coupon.description }}</p>
            <p class=\"coupon-expiry\"><strong>Expiry:</strong> {{ coupon.expiry }}</p>
            <p class=\"coupon-code\">Code: {{ coupon.code }}</p>
            <button class=\"copy-btn\" onclick=\"copyCode('{{ coupon.code }}')\">Copy Code</button>
        </div>
        {% endfor %}
        </div>
        <div class=\"footer\">
            <p>&copy; 2025 Abdullah's Coupon WebApp. Designed with ❤️ by Abdullah.</p>
            <p><a href=\"/coupons\">View API</a></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(template, coupons=coupons)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
