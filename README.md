# new_storySummary_english_learning
users learn english through summarized stories.
# 为什么要制作这个app
- 原因一： 因为现在市面上的英语学习app基本上都是flip card。 flip card的本质就是正面单词背面它的翻译。而这种“点对点”的记忆方式及其的低效。很多单词出现一次之后， 和这个单词相关联的表达方式应该更加频繁的出现并且用已知的知识来连接新的单词和概念才是语言学习的本质。
- 原因二： 英语一直有着巨大的市场并且至今没有很好的解决方式。
- 原因三： 随着ai的崛起英语越发重要， 但国内却逆天而行限制了课外补习班的发展（包括英语）

# 什么是flip card
![image](https://github.com/gaoxiangmstrong/new_storySummary_english_learning/assets/85563264/44eb50c2-031d-4be3-ae20-418923414f2d)
![image](https://github.com/gaoxiangmstrong/new_storySummary_english_learning/assets/85563264/6e6084d4-f953-4b16-9bfe-ff51f4e86672)
# 市场上的同类竞品
- 百词斩 quizlet anki 扇贝 （本质上都是flip card）
- duolingo (这就是个玩具。娱乐 > 学习。 你以为你学会了这个单词或者这个表达， 其实你记住的是这个单词对应的图片)

# 具体的想法：
1. 先用调查问卷获得用户的兴趣。 通过兴趣匹配数据库中的故事或者新闻（bbc）。 目的： 获取用户英文水平
2. 调用文字内容然后使用gpt function get_summary() 总结全文内容。 然后根据用户水平生成难度不一的总结 目的： 根据用户的英文水平定点输出
3. AI朋友通过提问确认用户理解。 目的： 通过提问分割文本内容，然后通过AI对用户的理解进行确认。
4. 用户自主复述故事。 目的： 再一次提高复述难度。 确认用户理解。
- 好处一： 学习的不仅仅是单词。（因为记忆的是文章本身、所以你还要记忆句型、语法、固定搭配和你锻炼你的总结能力。）
- 好处二： 多次在脑中创建链接达到“复习”的效果 （先用ai_freind来确认你对文章内容的理解。当确认之后再让用户复述这个故事。）
- 好处三： 即被动又主动 （被动是指ai会问问题， 用户理解无误的话会产生一种“我能做到的”满足感。满足感可以降低对故事全片总结的“心里障碍”）

# 为什么选择内容的总结而不是故事的生成
- 原因： 我耍了很长时间的gpt以后。我发现gpt比起生成故事其实更加擅长故事的总结。初级的学生其实很适合用生成的简单文章。当级别达到一定程度之后，可以直接通过书。把一本书分成30个小章节之后让gpt总结一个个小章节。然后学生可以通过阅读书的摘要来学习整本书的内容还是不错的😹
- ai整合的新闻摘要 ： 主选新闻的原因是新闻知识覆盖面广。 人所涉及的到的领域新闻文本基本上可以覆盖
- 伊索寓言（童话）
- 动漫
- 论文的摘要

# user-flow
- 获得用户的兴趣分配给用户一个英文级别 -> 随机选择与之匹配级别的故事 -> 用户开始阅读到完成阅读 -> 

# 数据库（news_reading）： a user reads news / users read news; a news reads by a user / multiple news read by users; Many to Many
- users: id, username, password, email,
- reads: user_id, news_id, time, current_time, 
- news: id, difficulty, category, text, summary,
- likes: user_id, news_id

  

