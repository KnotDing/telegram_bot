# telegram_bot

## 功能说明

- 天气查询
- 快递查询
- 智能闲聊
- 双语翻译
- 状态查询

## 环境要求

- python3
- 使用之前需要所依赖的库:
    ```
    pip install pyTelegramBotAPI requests 
    ```
- 科学上网

## 客户端使用方法

在私聊或群聊中使用`/`可激活机器人对应功能。

- /status 用于查询服务器状态，机器人将以文本方式返回服务器当前的状态信息。
- /weather 用于查询天气状态，默认查询北京的天气信息，可使用参数查询其他地区的天气信息，如需修改默认地区请参考[服务器端使用方法](#weather)。
- /fanyi 用于中英双语翻译，机器人将返回查询词原文及其对应翻译。
- /ai 用于唤起机器人的智能闲聊功能，机器人将调用腾讯的智能闲聊API开始闲聊，也可使用@机器人或回复机器人消息的方式唤起，唤起后回复机器人消息即可连续聊天（回复功能默认启用，如需关闭请参考[服务器端使用方法](#ai)）。
- /moli 和/ai一样调用闲聊功能，但该指令调用的是茉莉机器人，智能使用/moli调用和回复机器人消息，不能直接回复，不能连续对话。茉莉机器人的特殊指令请查阅[茉莉机器人API](http://www.itpk.cn/robot.php),使用`/moli 指令`即可直接调用，如`/moli 笑话`即可调用笑话功能。
- /kuaidi 用于查询快递信息，必要参数为快递单号，可选参数为手机号后四位（仅作为备用验证），如`/kuaidi 4786265252934 7833`即可返回快递单号4786265252934的物流信息(由于快递100的API接口存在问题，该功能不定期抽风)。
- /test 用于调用测试功能，无任何可用性保证，如没有开发者许可不要使用。
- /help 用于查询帮助信息。

## 服务端使用方法

使用前请将`myboy.py`中的`bot = telebot.TeleBot('xxxxxxxx:XXXXXXXXXXXXXXXXXXXXX')`修改为自己的Token，然后运行`python3 myboy.py`。

如果不需要使用天气查询功能和智能闲聊功能则无需做其他更改，否则请将`aibot.py`、`weather.py`中的API相关信息更改为自己申请的API信息。

<span id="weather">天气功能说明</span>

天气功能默认查询北京地区填，如需修改默认地区请修改`weather.py`文件将`location = 'beijing'`中的`beijing`修改为其他地区。

<span id="ai">智能闲聊功能说明</span>

智能闲聊功能使用的是腾讯的智能闲聊API，设置中默认开启了回复功能和连续对话功能（每个聊天室绑定一个`userid`，即聊天室中所有调用机器人的对话会被认为是同一用户调用，如需修改请将`myboy.py`中的智能闲聊模块中的`message.chat.id`删除或根据需要修改为其他参数。该参数仅用于智能闲聊API获取上下文信息，不影响功能的使用）。

智能闲聊的备选API是茉莉机器人API，如果需要使用其作为主要机器人可将`myboy.py`中智能闲聊模块中的`get_nlp_textchat`替换为`send_moli`，替换后和`/ai`使用方法一致。

[茉莉机器人](http://www.itpk.cn/robot.php)

[智能闲聊](https://ai.qq.com/product/nlpchat.shtml)

[OPENWEATHER](https://openweathermap.org/api)

[快递鸟](https://www.kdniao.com/api-all)

`test.py`为开发中的功能，不稳定，如需不使用请自行在`myboy.py`中去除相关调用。


