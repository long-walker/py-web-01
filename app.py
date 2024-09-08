from flask import Flask, render_template

app = Flask(__name__)

# Sample data - List of safelisted payers
safelisted_payers = [
    {
        "name": "John Doe",
        "account_number": "123456789",
        "bank_account_country": "USA",
        "payer_country": "Canada"
    },
    {
        "name": "Jane Smith",
        "account_number": "987654321",
        "bank_account_country": "UK",
        "payer_country": "France"
    },
    {
        "name": "Michael Johnson",
        "account_number": "456789123",
        "bank_account_country": "Australia",
        "payer_country": "New Zealand"
    }
]

@app.route('/')
def index():
    # Pass the list of safelisted payers to the template
    return render_template('index.html', payers=safelisted_payers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
