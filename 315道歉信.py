import json
from random import randint
sorry = ["表示真诚的歉意","诚恳的道歉","表示深深的歉意","表示最诚恳的歉意","表达我们的抱歉","深深的道歉",
         "说一声抱歉","给予真诚的歉意"]
say_sorry = sorry[randint(0,7)]
fansi = ["接受广大人们群众的批评","感谢央视指出问题","非常感谢广大群众发现我们的问题","接受来自央视和群众的批评之争",
         "从广大人们群众的批评中看到了我们的不足","坚决支持广大人民群众对我们的批评指正"]
say_fansi = fansi[randint(0,5)]
gaizhen = ["不断进行自我完善","继续完善管理","找到并改正自身问题","不断改善我们的服务","坚决做到提供最好的服务",
           "继续调查并给出最新的调查进度","继续努力，以达到人民群众的要求"]
say_gaizhen = gaizhen[randint(0,6)]
xiwang = ["希望大家能继续支持我们","希望大家能与我们继续前进","希望大家能一如既往的支持我们","希望我们能在将来的时光中继续合作前行",
          "希望大家能继续激励我们","希望大家能与我们同在"]
say_xiwang = xiwang[randint(0,5)]
companyy = input('公司名称（如汉堡王中国）：')
whatyd = input('涉事人/公司 发生了什么事（如投放大量广告，注意，这里不用写 问题 这两个字）：')
whod = input('谁涉及了此次事件？（如X地X公司）:')
whatd = input('涉事的人/公司 需要干什么？（如全面停业整顿 ，关闭 ，开除等）：')
whatgi = input('对受害者有什么赔偿或通知：(如全额退回受害者学费)')
models = [f'''
{companyy}声明：

针对”3.15晚会“对我司{whatyd}问题的报道，我司对相关事件高度重视，并对造成的影响{say_sorry}。我们{say_fansi},并将{say_gaizhen}
{companyy}特别工作组决议：
一、涉事{whod}即日起立刻{whatd}。
二、所有部门开展严格自查，一经发现，严肃处理
三、{whatgi}
{say_xiwang}
''',
f'''
针对中央电视台3.15晚会报道的{whod}{whatyd}问题，{companyy}高度重视，并充分意识到在公司管理上仍
有诸多不足，对于给用户带来的困扰和影响，{companyy}{say_sorry}。针对央视指出的问题，{companyy}
已迅速成立专项工作组，正在对涉事{whod}进行全面彻查，目前，涉事{whod}已{whatd},同时，公司开展全面
自查，一旦发现相关问题，坚决严肃处理。
我们高度重视{whatyd}问题，{say_fansi}，{companyy}会负责到底，我们也会{say_gaizhen}，欢迎广大媒体给{companyy}提出建议和意见
同时，我们将{whatgi}，我们也对此事再次{say_sorry}
{say_xiwang}
''',
f'''
我们已经关注到央视3.15晚会提及的{whod}{whatyd}问题。{companyy}对此非常重视，立即成立工作组并
对{whod}立即{whatd}。
报道中提及的{whod}对我们的企业宗旨严重背离，是我们管理的失误，辜负了广大消费者对{companyy}的信
任，对此我们{say_sorry}，并{say_fansi}。
我们在{say_gaizhen}同时，也将{whatgi}，并再次对用户{say_sorry}
{say_xiwang}
'''
f'''
对于央视3.15晚会报道的{whod}{whatyd}问题，{companyy}对此高度重视，并已成立转型调查组，对此事
展开调查，由此对用户造成的困扰，我们{say_sorry}，并将{say_gaizhen}
我们{say_fansi},也{say_xiwang}
'''
]
file = open('output.txt',mode='w',encoding='utf-8')
for i in models:
    print(i)
    file.write(i)
a = input('请按回车键继续.....')
