from tkinter import *


class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("体测计算器")

        self.init_window_name.geometry('400x700+300+200')

        # 身高
        self.tall_data_label = Label(self.init_window_name, text="身高(m)")
        self.tall_data_label.grid(row=3, column=1)

        # 体重
        self.heavy_data_label = Label(self.init_window_name, text="体重(kg)")
        self.heavy_data_label.grid(row=5, column=1)

        # 肺活量
        self.fei_data_label = Label(self.init_window_name, text="肺活量(ml)")
        self.fei_data_label.grid(row=7, column=1)

        # 引体向上
        self.up_data_label = Label(self.init_window_name, text="引体向上(个)")
        self.up_data_label.grid(row=9, column=1)

        # 立定跳远
        self.jump_data_label = Label(self.init_window_name, text="立定跳远(cm)")
        self.jump_data_label.grid(row=11, column=1)

        # 50m短跑
        self.sr_data_label = Label(self.init_window_name, text="50m短跑(s)")
        self.sr_data_label.grid(row=13, column=1)

        # 1000长跑
        self.lr_data_label = Label(self.init_window_name, text="1000长跑(min)")
        self.lr_data_label.grid(row=15, column=1)

        # 坐位体前屈
        self.qu_data_label = Label(self.init_window_name, text="坐位体前屈(cm)")
        self.qu_data_label.grid(row=17, column=1)

        # 结果
        self.log_label = Label(self.init_window_name, text="结果")
        self.log_label.grid(row=19, column=1)

        # 身高 输入
        self.tall_data_Text = Text(self.init_window_name, width=60, height=2)
        self.tall_data_Text.grid(row=4, column=1, rowspan=1, columnspan=10)

        # 体重 输入
        self.heavy_data_Text = Text(self.init_window_name, width=60, height=2)
        self.heavy_data_Text.grid(row=6, column=1, columnspan=10)

        # 肺活量 输入
        self.fei_data_Text = Text(self.init_window_name, width=60, height=2)
        self.fei_data_Text.grid(row=8, column=1, columnspan=10)

        # 引体向上 输入
        self.up_data_Text = Text(self.init_window_name, width=60, height=2)
        self.up_data_Text.grid(row=10, column=1, columnspan=10)

        # 立定跳远 输入
        self.jump_data_Text = Text(self.init_window_name, width=60, height=2)
        self.jump_data_Text.grid(row=12, column=1, columnspan=10)

        # 50m短跑 输入
        self.sr_data_Text = Text(self.init_window_name, width=60, height=2)
        self.sr_data_Text.grid(row=14, column=1, columnspan=10)

        # 1000m长跑 输入
        self.lr_data_Text = Text(self.init_window_name, width=60, height=2)
        self.lr_data_Text.grid(row=16, column=1, columnspan=10)

        # 坐位体前屈 输入
        self.qu_data_Text = Text(self.init_window_name, width=60, height=2)
        self.qu_data_Text.grid(row=18, column=1, columnspan=10)

        # 计算
        self.str_button = Button(self.init_window_name, text="计算", bg="lightblue", width=10,
                                 command=self.get_result_count)  # 调用内部方法  加()为直接调用
        self.str_button.grid(row=19, column=4)

        # 结果
        self.result_data_Text = Text(self.init_window_name, width=60, height=10)  # 处理结果展示
        self.result_data_Text.grid(row=20, column=1, rowspan=10, columnspan=10)

    def get_result_count(self):
        try:
            tall = float(self.tall_data_Text.get(1.0, END).strip().replace("\n", ""))
            heavy = float(self.heavy_data_Text.get(1.0, END).strip().replace("\n", ""))
            fei = float(self.fei_data_Text.get(1.0, END).strip().replace("\n", ""))
            up = float(self.up_data_Text.get(1.0, END).strip().replace("\n", ""))
            jump = float(self.jump_data_Text.get(1.0, END).strip().replace("\n", ""))
            sr = float(self.sr_data_Text.get(1.0, END).strip().replace("\n", ""))
            lr = float(self.lr_data_Text.get(1.0, END).strip().replace("\n", ""))
            qu = float(self.qu_data_Text.get(1.0, END).strip().replace("\n", ""))

            # 肺活量成绩
            if fei < 2350:
                gfei = 10
            elif fei >= 2520 and fei < 2690:
                gfei = 20
            elif fei >= 2690 and fei < 2860:
                gfei = 30
            elif fei >= 2860 and fei < 3030:
                gfei = 40
            elif fei >= 3030 and fei < 3200:
                gfei = 50
            elif fei >= 3200 and fei < 3320:
                gfei = 60
            elif fei >= 3320 and fei < 3440:
                gfei = 62
            elif fei >= 3440 and fei < 3560:
                gfei = 64
            elif fei >= 3560 and fei < 3680:
                gfei = 66
            elif fei >= 3680 and fei < 3800:
                gfei = 68
            elif fei >= 3800 and fei < 3920:
                gfei = 70
            elif fei >= 3920 and fei < 4040:
                gfei = 72
            elif fei >= 4040 and fei < 4160:
                gfei = 74
            elif fei >= 4160 and fei < 4280:
                gfei = 76
            elif fei >= 4280 and fei < 4400:
                gfei = 78
            elif fei >= 4400 and fei < 4650:
                gfei = 80
            elif fei >= 4650 and fei < 4900:
                gfei = 85
            elif fei >= 4900 and fei < 5020:
                gfei = 90
            elif fei >= 5020 and fei < 5140:
                gfei = 95
            elif fei >= 5140:
                gfei = 100

            # 50m成绩
            if sr <= 6.6:
                gsr = 100
            elif sr > 6.6 and sr <= 6.7:
                gsr = 95
            elif sr > 6.7 and sr <= 6.8:
                gsr = 90
            elif sr > 6.8 and sr <= 6.9:
                gsr = 85
            elif sr > 6.9 and sr <= 7.0:
                gsr = 80
            elif sr > 7.0 and sr <= 7.2:
                gsr = 78
            elif sr > 7.2 and sr <= 7.4:
                gsr = 76
            elif sr > 7.4 and sr <= 7.6:
                gsr = 74
            elif sr > 7.6 and sr <= 7.8:
                gsr = 72
            elif sr > 7.8 and sr <= 8.0:
                gsr = 70
            elif sr > 8.0 and sr <= 8.2:
                gsr = 68
            elif sr > 8.2 and sr <= 8.4:
                gsr = 66
            elif sr > 8.4 and sr <= 8.6:
                gsr = 64
            elif sr > 8.6 and sr <= 8.8:
                gsr = 62
            elif sr > 8.8 and sr <= 9.0:
                gsr = 60
            elif sr > 9.0 and sr <= 9.2:
                gsr = 50
            elif sr > 9.2 and sr <= 9.4:
                gsr = 40
            elif sr > 9.4 and sr <= 9.6:
                gsr = 30
            elif sr > 9.6 and sr <= 9.8:
                gsr = 20
            elif sr > 9.8 and sr <= 10.0:
                gsr = 20
            elif sr > 10.0:
                gsr = 10

            # 1000m成绩
            if lr <= 3.15:
                glr = 100
            elif lr > 3.15 and lr <= 3.20:
                glr = 95
            elif lr > 3.20 and lr <= 3.25:
                glr = 90
            elif lr > 3.25 and lr <= 3.32:
                glr = 85
            elif lr > 3.32 and lr <= 3.40:
                glr = 80
            elif lr > 3.40 and lr <= 3.45:
                glr = 78
            elif lr > 3.45 and lr <= 3.50:
                glr = 76
            elif lr > 3.50 and lr <= 3.55:
                glr = 74
            elif lr > 3.55 and lr <= 4.00:
                glr = 72
            elif lr > 4.00 and lr <= 4.05:
                glr = 70
            elif lr > 4.05 and lr <= 4.10:
                glr = 68
            elif lr > 4.10 and lr <= 4.15:
                glr = 68
            elif lr > 4.15 and lr <= 4.20:
                glr = 66
            elif lr > 4.20 and lr <= 4.25:
                glr = 66
            elif lr > 4.25 and lr <= 4.30:
                glr = 64
            elif lr > 4.30 and lr <= 4.50:
                glr = 62
            elif lr > 4.50 and lr <= 5.10:
                glr = 60
            elif lr > 5.10 and lr <= 5.30:
                glr = 50
            elif lr > 5.30 and lr <= 5.50:
                glr = 40
            elif lr > 5.50 and lr <= 6.10:
                glr = 30
            elif lr > 6.10:
                glr = 20

            # 坐位体前屈成绩
            if qu < -0.8:
                gqu = 10
            elif qu >= -0.8 and qu < 0.2:
                gqu = 20
            elif qu >= 0.2 and qu < 1.2:
                gqu = 30
            elif qu >= 1.2 and qu < 2.2:
                gqu = 40
            elif qu >= 2.2 and qu < 3.2:
                gqu = 50
            elif qu >= 3.2 and qu < 4.2:
                gqu = 60
            elif qu >= 4.2 and qu < 5.6:
                gqu = 62
            elif qu >= 5.6 and qu < 7.0:
                gqu = 64
            elif qu >= 7.0 and qu < 8.4:
                gqu = 66
            elif qu >= 8.4 and qu < 9.8:
                gqu = 68
            elif qu >= 9.8 and qu < 11.2:
                gqu = 70
            elif qu >= 11.2 and qu < 12.6:
                gqu = 72
            elif qu >= 12.6 and qu < 14.0:
                gqu = 74
            elif qu >= 14.0 and qu < 15.4:
                gqu = 76
            elif qu >= 15.4 and qu < 16.8:
                gqu = 78
            elif qu >= 16.8 and qu < 18.2:
                gqu = 80
            elif qu >= 18.2 and qu < 19.9:
                gqu = 85
            elif qu >= 19.9 and qu < 21.5:
                gqu = 90
            elif qu >= 21.5 and qu < 23.3:
                gqu = 95
            elif qu >= 25.1:
                gqu = 100

            # 立定跳远成绩
            if jump < 190:
                gjump = 10
            elif jump >= 190 and jump < 195:
                gjump = 20
            elif jump >= 195 and jump < 200:
                gjump = 30
            elif jump >= 200 and jump < 205:
                gjump = 40
            elif jump >= 205 and jump < 210:
                gjump = 50
            elif jump >= 210 and jump < 214:
                gjump = 60
            elif jump >= 214 and jump < 218:
                gjump = 62
            elif jump >= 218 and jump < 222:
                gjump = 64
            elif jump >= 222 and jump < 226:
                gjump = 66
            elif jump >= 226 and jump < 230:
                gjump = 68
            elif jump >= 230 and jump < 234:
                gjump = 70
            elif jump >= 234 and jump < 238:
                gjump = 72
            elif jump >= 238 and jump < 242:
                gjump = 74
            elif jump >= 246 and jump < 250:
                gjump = 76
            elif jump >= 250 and jump < 258:
                gjump = 78
            elif jump >= 258 and jump < 258:
                gjump = 80
            elif jump >= 258 and jump < 265:
                gjump = 85
            elif jump >= 265 and jump < 270:
                gjump = 90
            elif jump >= 270 and jump < 275:
                gjump = 95
            elif jump >= 275:
                gjump = 100

            # 引体向上成绩
            if up < 7:
                gup = 10
            elif up >= 7 and up < 8:
                gup = 20
            elif up >= 8 and up < 9:
                gup = 30
            elif up >= 9 and up < 10:
                gup = 40
            elif up >= 10 and up < 11:
                gup = 50
            elif up >= 11 and up < 12:
                gup = 60
            elif up >= 12 and up < 13:
                gup = 64
            elif up >= 13 and up < 14:
                gup = 68
            elif up >= 14 and up < 15:
                gup = 72
            elif up >= 15 and up < 16:
                gup = 76
            elif up >= 16 and up < 17:
                gup = 80
            elif up >= 18 and up < 19:
                gup = 85
            elif up >= 19 and up < 20:
                gup = 90
            elif up >= 20 and up < 21:
                gup = 95
            elif up >= 21 and up < 30:
                gup = 100 + (up - 21) * 10
            elif up >= 30:
                gup = 200

            # 身高体重成绩
            ht = heavy / (tall * tall)
            if ht >= 17.9 and ht <= 23.9:
                ght = 100
            elif ht <= 17.8:
                ght = 80
            elif ht >= 24 and ht <= 27.9:
                ght = 80
            elif ht >= 28:
                ght = 60

            # 总成绩
            result = (ght + gfei) * 0.15 + (gsr + glr) * 0.2 + (gqu + gjump + gup) * 0.1

            self.write_to_Text(result)
        except Exception as e:
            self.write_to_Text(result)

            # 输出结果

    def write_to_Text(self, result):
        self.result_data_Text.delete(1.0, 10.0)
        self.result_data_Text.insert(END, result)


def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()


if __name__ == '__main__':
    gui_start()

