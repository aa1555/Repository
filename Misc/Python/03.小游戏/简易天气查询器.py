def weather_report(city):
    weather_data = {
        "北京": "晴",
        "上海": "多云",
        "广州": "雨",
        "深圳": "晴",
        "杭州": "阴"
    }
    return weather_data.get(city, "未知城市")

city = input("请输入你想查询的城市名：")
print(f"{city}的天气是：{weather_report(city)}")