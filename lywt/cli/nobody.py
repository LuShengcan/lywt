"""
    大多数(nobody)女主喜好
"""
BaiJiaHui = {
    'like': {'服饰搭配', '古典乐', '古装片', '滑雪', '美容', '民谣', '萨克斯', '桑拿', '时尚', '天文', '西餐', '演唱会', '游戏', '瑜伽', '桌游', '温泉', '吉他',
             '游泳', '度假村', '网球', '美容'},
    'dislike': {'美食', '高抬腿'}
}

GaoShanShan = {
    'like': {'高山', '有氧跑', '海边休闲', '剪纸', '民宿', '拼图', '桑拿', '派对', '爱情片', '服饰搭配', '天文', '平板支撑', '度假村', '花滑', '古典乐', '滑雪',
             '跳水'},
    'dislike': {'烹饪', '综艺', '马术', '游乐园', '足球', '科技', '瑜伽', '纯音乐'}
}

ZhuChenXi = {
    'like': {'游泳', '健身操', '瑜伽', '星座', '时尚', '农家乐', '度假村', '露营', '剪纸', '小提琴', '美食', '闽菜', '烹饪', '模玩', '刷视频', '科技'},
    'dislike': {'剧本杀', '推理片', '古装片', '警匪片', '恐怖片', '纪录片', '奇幻片', '仰卧起坐', '平板支撑', '俯卧撑', '深蹲', '高抬腿', '登山', '羽毛球', '网球',
                '逛街', '花艺', '温泉', '钢琴', '手风琴', '吉他', '演唱会', '绘画', '高山', 'up主', '动物园', '花滑', '海边休闲', '乒乓', '舞蹈', '哲学',
                '摇滚乐'}
}

mapping = {1: BaiJiaHui, 2: GaoShanShan, 3: ZhuChenXi}

if __name__ == '__main__':
    print("请选择人物: 1.白嘉卉 2.高珊珊 3.朱晨希")
    obj = mapping[int(input())]

    while 1:
        hobby = input()
        if hobby in obj['like']:
            print('like')
        elif hobby in obj['dislike']:
            print('dislike')
        else:
            print('wrong')