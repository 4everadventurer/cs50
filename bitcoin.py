import sys
import requests

def get_bitcoin_price():
    """현재 비트코인 가격을 CoinCap API에서 가져오는 함수"""
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()  # 요청이 실패하면 예외 발생
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price.")

def main():
    """사용자로부터 비트코인 개수를 입력받아 총 가격을 계산하는 메인 함수"""
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")
    
    try:
        bitcoins = float(sys.argv[1])  # 명령줄 인수를 float로 변환
    except ValueError:
        sys.exit("Error: Invalid number of bitcoins.")

    price_per_bitcoin = get_bitcoin_price()'''get_bitcoin_price()치치 함수를 직접 사용하지 않는 이유는 여러번 호출 시 매번 API를 호출하게 므로 비효율적.'''
    total_cost = bitcoins * price_per_bitcoin

    print(f"${total_cost:,.4f}")  # 4자리 소수점, 천 단위 콤마 적용

if __name__ == "__main__":
 ''' __name___은 파이썬 내장변수로 파이썬 파일이 실행될 때 그 파일의 이름을 나타내는 수한 변수, 이 변수는 파이썬 파일이
 직접 실행되었는지 임푸트 되었는지에 따라 다르게 설정된다.'''
    main()
 