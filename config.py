# 公众号配置
# 公众号appId
app_id = "wx0052580b5e832501"
# 公众号appSecret
app_secret = "d332c475bbe10d9f2014d8b478107138"
# 模板消息id
# 每日消息
template_id1 = "wX-************************************"
# 课程消息,上课提醒
template_id2 = "loe1yHWr************************************"
# 晚安心语
template_id3 = "-fun9-2************************************"
# 接收公众号消息的微信号
# 这是openid
user = ["ojhdR50T******************"]

# 信息配置
# 所在省份
province = "河北"
# 所在城市
city = "石家庄"
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1，---------倒计时
birthday = "1998-05-15"
# 在一起的日子，格式同上------------计时器
love_date = "2023-09-26"
# 天行数据晚安心语 key
good_Night_Key = "46e4ecedbe16081b85b89288b4e85524"
# -------------------------------------------------------------------------
# 设置学期第一周开始日期
year = 2022
month = 8
day = 29
# 每日推送时间
post_Time = "07:35:00"、
# 晚安心语及第二天课程推送时间
good_Night_Time = "22:55:00"

# 模板 1：每日提醒模板
# 本周是开学的第: {{weeks.DATA}} 周
# 今天是: {{date.DATA}}
# 城市： {{city.DATA}}
# 天气： {{weather.DATA}}
# 最低气温: {{min_temperature.DATA}}
# 最高气温: {{max_temperature.DATA}}
# 今天是破壳日的第: {{love_day.DATA}} 天
# 距离开学还有: {{birthday.DATA}} 天
# ----------------今日课程----------------
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}

# 模板 2 课程单推
# 课程信息: {{classInfo.DATA}}

# 模板 3 晚安心语推送和第二天课程推送
# {{goodNight.DATA}}
# ----------------明日课程----------------
# 明天是: {{week.DATA}}
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}
