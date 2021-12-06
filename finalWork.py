import sqlite3
import requests
import bs4
from matplotlib import pyplot as plt


# 获取数据
def getData(url):
    s = requests.Session()
    # 请求头
    headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.shanghairanking.cn/'}
    f = open('uni.txt', 'w', encoding='utf-8')
    # 爬虫异常获取
    try:
        r = s.get(url, headers=headers)
        r.encoding = 'utf-8'
        html = r.text
        # 用于保存所有的信息的列表
        all_info_list = []
        # 解析网页文本内容
        soup = bs4.BeautifulSoup(html, 'html.parser')
        # 找到table标签
        div = soup.findAll("div", {"class": "univ-detail"})
        for item in div:
            i = []
            # 从 univ-detail 中获取排名的div
            rank_div = item.find_all("div", {"class": "rank-box"})
            for r_list in rank_div:
                # 获取排名
                rank = r_list.div.text.strip().replace('\n', ' ')
                i.append(rank)

            # 从 link-container 中获取学校名称
            name_div = item.find_all("div", {"class": "link-container"})
            for n_list in name_div:
                name = n_list.text.strip().replace('\n', ' ')
                i.append(name)

            # 从 scorer 中获取学校总分
            score_div = item.find_all("div", {"class": "score"})
            for s_list in score_div:
                score = s_list.text.strip().replace('\n', ' ')
                i.append(score)

            # 再把每个大学的信息都存放下大列表中
            all_info_list.append(i)
            # 写入文件
            f.write(rank + '\t' + name + '\t' + score + '\t\n')
        f.close()
        # 建立文件、SQL、all_info_list，三个地方保存数据，确保数据准确
        return all_info_list
    except:
        print('error')


# 数据保存到数据库
def saveDatadb(dbpath, all_info_list):
    # 初始化数据库
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    # 写入数据库
    for data in all_info_list:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
                insert into rankings (
                rank,cname,score) 
                values(%s)''' % ",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


# 初始化数据库，创建表
def init_db(dbpath):
    sql = '''
        create table  rankings
        (
        id integer primary key autoincrement,
        rank numeric ,
        cname varchar ,
        score DECIMAL
        )

    '''
    # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    # 每次建表前检测是否存在，如果存在该表则删除
    cursor.execute("DROP TABLE IF EXISTS rankings")
    cursor.execute(sql)
    conn.commit()
    conn.close()


def main():
    # 爬虫获取数据
    url = 'https://www.shanghairanking.cn/rankings/bcmr/2021/080901'
    # all_info_list保存了所有排名数据：排名、名称、总分,all_info_list[][]获取数据
    all_info_list = getData(url)
    # print(all_info_list[18][1])
    dbpath = 'ranking.db'
    # 保存数据至数据库
    saveDatadb(dbpath, all_info_list)
    # 数据可视化
    dataVisualization(all_info_list)


def dataVisualization(all_info_list):
    # x代表各个大学的名称
    x = []
    for i in range(0, len(all_info_list))[::-1]:
        x.append(all_info_list[i][1])
    # y代表总分
    y = []
    for i in range(0, len(all_info_list)):
        num = all_info_list[i][2]
        b = eval(num)
        y.append(b)
        y = list(map(float, y))
        y.sort()
    # 建立画布大小
    plt.figure(figsize=(16, 9))
    # 设置x轴分数范围
    plt.xlim((0, 90))
    # 指定默认字体，Windows改成 plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False
    barh = plt.barh(x, y, align='center')
    # 给条形图添加数据标注 + 修改配色
    # zip 函数
    for a, b, i in zip(x, y, range(len(x))):
        # plt.text 函数
        plt.text(b, a, y[i], fontsize=14)
        if y[i] < 60:   # 小于60，红
            barh[i].set_color('#FA8072')
        elif y[i] < 64: # 未到前五 黄
            barh[i].set_color('#CD853F')
        else:   # 第一名，绿；前五，蓝
            barh[i].set_color('#3F51B5')
            barh[-1].set_color('#228B22')
    # 设置图片标题、xy轴名称
    plt.title('University Professional Ranking (Computer Science)')
    plt.ylabel('Score')
    plt.xlabel('University name')
    # 指定分辨率保存
    plt.savefig('rank.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    main()
    print("保存成功")
