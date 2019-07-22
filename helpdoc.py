def helpdocs():
    help_docu = '*说明文档*\n'
    help_docu += '/status 查询服务器状态\n'
    help_docu += '/weather 查询天气信息（默认为浦口地区，其他地区请使用/weather location方式查询）\n'
    help_docu += '/fanyi 查询中英文释义\n'
    help_docu += '/zhihu 用于获取知乎日报\n'
    help_docu += '/drive 用于代下Google drive文件\n'
    help_docu += '/shell 用于远程执行命令并返回结果\n'
    help_docu += '/need 用于向管理员提新需求\n'
    help_docu += '/kuaidi 查询物流信息（默认为/kuaidi packageNum查询，某些情况下需使用/kuaidi packageNum phoneNum进行查询）\n'
    help_docu += '/ai 和狗子聊天或者……你@它也行，或者你接茬也行…… \n'
    help_docu += '/moli 让狗子查资料（@qq @lol @sfz @shj @cy @tq @ip ip 天气 笑话 观音灵签 月老灵签 财神爷灵签）'
    return help_docu

if __name__ == '__main__':
    data = helpdocs()
    print(data)
