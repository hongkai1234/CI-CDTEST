import time
import os
import sys
import requests

FLAG_FILE = "stop.flag"

if os.path.exists(FLAG_FILE):
    os.remove(FLAG_FILE)

# 🟢 改成測試專用的 httpbin 網址，這個 100% 會回傳 200，絕對不會被阻擋！
def fetch_status():
    try:
        # Google 基本上 365 天 24 小時都絕對是 200，絕對不會噴 503！
        res = requests.get("https://www.google.com", timeout=5)
        return res.status_code
    except Exception as e:
        print(f"連線失敗: {e}")
        return None

if __name__ == '__main__':
    print("🚀 主程式已在背景成功啟動...")
    try:
        while True:
            if os.path.exists(FLAG_FILE):
                print("🛑 接收到下班暗號，正在優雅退出...")
                os.remove(FLAG_FILE)
                sys.exit(0)
                
            status = fetch_status()
            print(f"目前連線狀態碼: {status}")
            time.sleep(3)
    except KeyboardInterrupt:
        print("程式手動終止")
