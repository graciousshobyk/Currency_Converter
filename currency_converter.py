"""
Simple Real-Time Currency Converter
"""

import json
import urllib.request
import urllib.error

API_BASE_URL = "https://open.er-api.com/v6/latest"


def convert_currency(from_curr: str, to_curr: str, amount: float) -> float:
    """Fetch live exchange rates and convert amount from one currency to another."""
    from_curr = from_curr.upper().strip()
    to_curr = to_curr.upper().strip()

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if from_curr == to_curr:
        return amount

    url = f"{API_BASE_URL}/{from_curr}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as err:
        raise ConnectionError(f"Network error: {err}")

    if data.get("result") != "success":
        raise ValueError(f"Could not retrieve rates for {from_curr}.")

    rates = data.get("rates", {})
    if to_curr not in rates:
        raise ValueError(f"Target currency '{to_curr}' is not supported.")

    rate = float(rates[to_curr])
    return round(amount * rate, 4)


def main():
    print("=== Basic Currency Converter ===")
    from_curr = input("From currency (e.g. USD, EUR, INR): ").strip().upper()
    to_curr = input("To currency (e.g. EUR, USD, JPY): ").strip().upper()

    try:
        amount = float(input("Enter amount: ").strip())
        result = convert_currency(from_curr, to_curr, amount)
        print(f"\n{amount:,.2f} {from_curr} = {result:,.2f} {to_curr}\n")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except ConnectionError as ce:
        print(f"Network Error: {ce}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()