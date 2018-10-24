### 分析12306 查询API

原始 API 接口：`https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-10-25&leftTicketDTO.from_station=WHN&leftTicketDTO.to_station=LSG&purpose_codes=ADULT`

分析：

* leftTicketDTO.train\_date 容易看出是按照 `2018-10-25` 格式的生成的字符串
* leftTicketDTO.from\_station
  
    搜索时输入的为 __武汉__，这里发出请求的为 __WHN__，大致猜出为武汉，经过搜索得知为站点代码
    
    且获取接口为：`https://kyfw.12306.cn/otn/resources/js/framework/station_name.js`
* leftTicketDTO.to\_station 同上
* purpose\_codes 分为成年人和学生固定选项

### 具体实现

环境：Python3，requests 库

* 获取并解析站点名字 -> 代码：
  
    发送请求：`https://kyfw.12306.cn/otn/resources/js/framework/station_name.js`
    
    获取 JS 文件循环格式：`@bjb|北京北|VAP|beijingbei|bjb|0`
    
    选取需要部分：`北京北|VAP`
    
    解析方式：正则表达式
    
    pattern：`([\u4e00-\u9fa5]+)\|([A-Z]+)` （前面匹配中文后面匹配英文，同时使用捕获模式，即使用括号）
    
    代码：
    
    ```python
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    result = re.findall(pattern, r.text)
    station = dict(result)
    ```
* 根据日期、出发站、终点站拼装 URL
  
    根据上面保存的站点 -> 代码信息，映射站点代码，拼装URL
    
    URL示例：`https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-10-25&leftTicketDTO.from_station=WHN&leftTicketDTO.to_station=LSG&purpose_codes=ADULT`
* 解析返回数据
  
    关键：站点代码 -> 站点名字

最终效果：



![2018-10-24 17-03-09屏幕截图.png | left | 747x347](https://cdn.nlark.com/yuque/0/2018/png/189883/1540371862509-6e277179-071f-436a-8551-fc29f53a9a40.png)


代码见：[https://github.com/mu-mo/12306-API](https://github.com/mu-mo/12306-API)
