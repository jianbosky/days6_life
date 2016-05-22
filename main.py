#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-
import time
class Person(object):
    money = 0  # 初始化金钱
    def __init__(self, name, age, sex, role):
        '''
        :param name: 名字
        :param age:  年龄
        :param sex:  性别
        :param role: 角色
        :return:
        '''
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        if self.role == "poor":
            self.money += 5000
            print("\033[36;1mHI，大家好我叫[%s]，今年[%s]岁,一个贫穷的男孩。我只有[%s]元钱，希望通过努力工作来改变自己的生活！\033[0m"%(self.name,self.age,self.money))
        elif self.role == "beauty":
            self.money += 10000
            print("\033[36;1mHI，大家好我叫[%s]，今年[%s]岁,一个漂亮的女孩。我只有[%s]元钱，但是我很漂亮。我不希望永远到贫穷下去！\033[0m"%(self.name,self.age,self.money))
        elif self.role == "rich":
            self.money += 1000000000
            print("\033[36;1mHI，大家好我叫[%s]，今年[%s]岁,一个富二代的男孩。我有车有房，喜欢泡漂亮的姑娘，我有这么多[%s]元钱！\033[0m"%(self.name,self.age,self.money))

    def Talk(self,msg, tone = "None"):
        '''
        :param msg: 对话内容
        :param tone: 不同情绪字体颜色的变化
        :return:
        '''
        if tone == "None":
            print ("[\033[30;35m%s]: %s\033[0m" % (self.name, msg))
        elif tone == 'angry':
            print ("[\033[31;1m%s]: %s\033[0m" % (self.name, msg))
    def Assets(self, money, action):
        '''
        资产函数
        :param: money  钱
        :param: action  赚与花费
        '''
        # 赚
        if action == 'earn':
            self.money += money
            print('\033[32;1m%s赚了 %s 元!现在拥有 %s 元\033[0m'
                    % (self.name, money, self.money))
        # 花费
        elif action == 'cost':
            self.money -= money
            print('\033[31;1m%s花了 %s 元! 现在还剩余 %s 元\033[0m'
                    % (self.name, money, self.money))
def Induction():
    '''
    入职
    :return:
    '''
    print('－' * 50)
    print('第一章：入职公司'.center(50))
    print('－' * 50)
    print('\033[20;1m小王和小丽是从小一起长大的青梅竹马，毕业后一起在同一家公司上班。\033[0m'
          '\033[20;1m\n他俩埋头苦干的工作，都想努力赚多点钱。\033[0m'
          '\033[20;1m\n两年都过去了，他们赚到了多少钱呢？\033[0m')
    p1.Assets(80000, 'earn')
    b1.Assets(75000, 'earn')
    time.sleep(2)

def Feelings():
    '''
    感情纠纷
    :return:
    '''
    print('-' * 150)
    print('第二章：感情危机'.center(50))
    print('-' * 150)
    b1.Talk("小王，我们恋爱那么久，都没车没房，生活怎么过啊？")
    p1.Talk("小丽，我们一起奋斗，以后生活肯定会过得更好的！")
    b1.Talk("不，现在我想结束这样的生活。小江对我很好，他有车有房，能给与我很多，所以我想他在一起！")
    r1.Talk("对，我是真心爱小丽的，你这么穷，就别做美梦了吧！")
    p1.Talk("小丽，我们在一起很开心啊！小江不是表面上那么好的人。")
    b1.Talk("那不是我要的生活，我们分手吧！")
    p1.Talk("给我考虑3天时间，到时候你我重新做决定吧！")
    b1.Talk("好吧，就给你3天时间！")
    time.sleep(1)

def Break_Up():
    '''
    分手函数
    :return:
    '''
    print('-' * 150)
    print('第三章：分手结局'.center(150))
    print('-' * 150)
    p1.Talk("小丽，你既然决定要分手，好吧，那就分吧！")
    p1.Talk("总有一天你会后悔的，等着瞧")
    b1.Talk("小江，我们走！")
    print("伤心过后的小王，通过参加Python培训，他最终当上IT总监。他也买有车、房了。")
    print("有一天，小王开车路过的大街上，看到两个人吵架，挡住前方的路。他下车看看情况，让他大吃一惊！")
    p1.Talk("你们让一下，不要挡着路！让我开车过去")
    b1.Talk("小王，我是小丽啊，他就是小江。" )
    print("此时的他们，小江因为花心，花光了所有钱。小丽也因为小江也变得贫穷。因为钱，他们已经分手吵架了。")
    p1.Talk("你们的报应啊，早知道这样，何必当初呢！")
    b1.Talk("小王，我想再次和你在一起，好吗？")
    b1.Talk("别做梦啦，当初你因为钱而跟了小江，现在是回不来头了。说完开着车走了！")
    print("最终小丽不再美丽了，变回了穷女孩。而小江也因为过度玩乐，花光所有的钱，变成穷光蛋！")
    print('\033[31;1m  剧 终  \033[0m'.center(150, '*'))

def  Together():
    '''
    在一起
    :return:
    '''
    print('-' * 150)
    print('第三章：完美结局'.center(150))
    print('-' * 150)
    print("小王和小丽选择了继续好下去，永不分开！")
    p1.Talk("小丽，你终于想通啦，我们才是天生一对！")
    b1.Talk("嗯，即使小江有车有房，但是他整天去泡多个姑娘，这种人不值得在一起！")
    b1.Talk("我们通过自己的努力，也会赚到很多钱的！")
    r1.Talk("小丽，我不是你说的那样的人，那些姑娘是主动约我的，我也无耐啊！")
    b1.Talk("小王，我们一起辞职吧！我不想在看到小江！")
    p1.Talk("好，我们一起努力，终有收获的！")
    print("小王和小丽通过自己的努力，最终也买车买房了。而小江因为整天泡妞，拥有的钱都花光了，变成了穷屌丝！")
    print('\033[31;1m  剧 终  \033[0m'.center(150, '*'))


def Choose():
    '''
    冲突选择
    :return:
    '''
    print('-' * 150)
    print('约定的时间到了，你我重新选择:\033[31;1m1 分手 2 继续好下去\033[0m')
    while True:
        input_chose1 = input("小王，请选择1或者2：").strip()
        if input_chose1 == "":
            continue
        input_chose2 = input("小丽，请选择1或者2：").strip()
        if input_chose2 == "":
            continue
        if input_chose1 in ['1', '2'] and input_chose2 in ['1', '2']:
            if input_chose1 == '2' and input_chose2 == '2':   # 双方决定在一起
                time.sleep(1)
                Together()
                break
            elif input_chose1 == '1' or input_chose2 == '1':  # 任意一方选择分手
                time.sleep(1)
                Break_Up()
                break
        else:
            print('你选择的不正确，请重新选择！')


if __name__ == '__main__':
    p1 = Person('小王', 26, 'man', 'poor')
    time.sleep(3)
    r1 = Person('小江', 27, 'man', 'rich')
    time.sleep(3)
    b1 = Person('小丽', 24, 'female', 'beauty')
    time.sleep(3)
    Induction()    # 入职公司部分
    time.sleep(3)
    Feelings()     # 感情危机部分
    time.sleep(3)
    Choose()