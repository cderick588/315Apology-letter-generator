import json
from random import randint
companyy = input('公司名称（如汉堡王中国）：')
whatyd = input('公司发生了什么事（如投放大量广告，注意，这里不用写 问题 这两个字）：')
whod = input('谁涉及了此次事件？（如X地X公司）:')
whatd = input('涉事的人/公司 需要干什么？（如全面停业整顿 ，关闭 ，开除等）：')
whatgi = input('对受害者有什么赔偿或通知：(如全额退回受害者学费)')
models = [f'''
{companyy}声明：

针对”3.15晚会“对我司{whatyd}问题的报道，我司对相关事件高度重视，并对造成的影响诚恳道歉。
{companyy}特别工作组决议：
一、涉事{whod}即日起立刻{whatd}。
二、所有部门开展严格自查，一经发现，严肃处理
三、{whatgi}
''',
f'''
针对中央电视台3.15晚会报道的{whod}{whatyd}问题，{companyy}高度重视，并充分意识到在公司管理上仍
有诸多不足，对于给用户带来的困扰和影响，{companyy}表示诚恳的道歉。针对央视指出的问题，{companyy}
已迅速成立专项工作组，正在对涉事{whod}进行全面彻查，目前，涉事{whod}已{whatd},同时，公司开展全面
自查，一旦发现相关问题，坚决严肃处理。
我们高度重视{whatyd}问题，非常感谢央视等媒体及社会各界的监督和批评，{companyy}会负责到底，同时
也欢迎广大媒体给{companyy}提出建议和意见，我们会不断进行自我完善，继续为广大用户做好服务
同时，我们将{whatgi}，并再次对用户表示诚恳的道歉
''',
f'''
我们已经关注到央视3.15晚会提及的{whod}{whatyd}问题。{companyy}对此非常重视，立即成立工作组并
对{whod}立即{whatd}。
报道中提及的{whod}对我们的企业总值严重背离，是我们管理的失误，辜负了广大消费者对{companyy}的信
任，对此我们表示深深的歉意
同时，我们将{whatgi},并再次表示深深的歉意
'''
f'''
对于央视3.15晚会报道的{whod}{whatyd}问题，{companyy}对此高度重视，并已成立转型调查组，对此事
展开调查，由此对用户造成的困扰，我们表示最诚恳的歉意
'''
]
file = open('output.txt',mode='w',encoding='utf-8')
for i in models:
    print(i)
    file.write(i)
a = input('请按回车键继续.....')
