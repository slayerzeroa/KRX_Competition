import pandas as pd
from data import wvkospi, db
import datetime
import time
import schedule


def main():
    t = (datetime.datetime.now() - datetime.timedelta(days=2)).date()
    underlying, target = wvkospi.get_wvkospi(t=t)
    vkospi = wvkospi.get_vkospi(t=t)
    df = pd.DataFrame({'BAS_DD': [t.strftime('%Y%m%d')], 'KOSPI': [underlying], 'WVKOSPI': [target], 'VKOSPI': [vkospi]})
    db.update_wvkospi(df)
    return df


def run_main_with_retries(max_retries=5, retry_delay=60):
    """
    main()을 실행하되, 실패 시 일정 횟수 재시도.
    그래도 실패하면 스크립트를 죽이지 않고 에러 로그만 남김.
    """
    for attempt in range(1, max_retries + 1):
        try:
            main()
            return  # main() 성공 시 즉시 함수 종료
        except Exception as e:
            print(f"[{attempt}/{max_retries}] 알 수 없는 오류 발생: {e}")
            if attempt < max_retries:
                print(f"{retry_delay}초 후 재시도합니다.")
                time.sleep(retry_delay)
            else:
                print("모든 재시도에 실패했습니다. 다음 스케줄까지 대기합니다.")


print("main.py is executed.")
schedule.every().day.at("19:00").do(run_main_with_retries)
while True:
    schedule.run_pending()
    time.sleep(1)


# start = datetime.datetime(2025, 1, 3).date()

# while start <= datetime.datetime.now().date():
#     try:
#         underlying, target = wvkospi.get_wvkospi(t=start)
#         vkospi = wvkospi.get_vkospi(t=start)
#         df = pd.DataFrame({'BAS_DD': [start.strftime('%Y%m%d')], 'KOSPI': [underlying], 'WVKOSPI': [target], 'VKOSPI': [vkospi]})
#         # db.update_wvkospi(df)
#         start += datetime.timedelta(days=1)
#     except Exception as e:
#         print(e)
#         start += datetime.timedelta(days=1)
#         continue