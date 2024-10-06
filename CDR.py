# 名称：合作欺骗抢劫

# 描述：把“合作、欺骗、抢劫”用编程方式写出来，玩家数量大于等于2人，可选人机模式。

#  Student Name: Bolong Tang

#  Partner Name: Henry Tang

#  Course Name: CDR 1001

#  Unique Number: 777

#  Date Created: 12/19/2023

#  Date Last Modified: 12/27/2023

import random, time

list_of_players = []

# Make more advanced AI program: AI takes less risk as its point goes closer to 0. 

class Player(object):
    def __init__(self, initial_points, identity = 'AI'):
        
        
        self.identity = identity
        self.pts = initial_points
        
        

class Game(object):
    # Default: two players
    def __init__(self, game_name, total_players_num = 2, real_players_num = 0, round_amount = 1, initial_points = 0):
        # self.round_amount = round_amount
        self.round_amount = round_amount
        self.current_round = 0
        self.players = []
        
        
        
        # Each table is filled
        self.strat_table = []
        self.pts_change_table = []
        self.total_pts_table = []
        
        for i in range(total_players_num):
            self.players.append('')
        
        for i in range(self.round_amount):
            row = []
            for j in range(total_players_num):
                row.append(0)
            self.strat_table.append(row)
            self.pts_change_table.append(row)
            
            initial_points_row = []
            for k in range(total_players_num):
                initial_points_row.append(initial_points)
            self.total_pts_table.append(initial_points_row)
        
        # Prompt every real player to enter their name
        for i in range(real_players_num):
            name = str(input(f'>>> 玩家{i}，你的名字是？'))
            self.players[i] = Player(initial_points, name)
        
        # Add the rest of the players as AI
        if real_players_num == 0:
            print('本局游戏没有真人玩家')
        else:
            print('真人玩家已添加完成！')
        time.sleep(1)
        if real_players_num < total_players_num:
            print('向玩家列表添加AI中...')
        else:
            print('本局游戏没有AI玩家')
            
        time.sleep(0.5)
        for i in range(real_players_num, total_players_num):
            self.players[i] = Player(initial_points)
            time.sleep(random.random() / 4)
            print(f'添加{i}号AI！')
        
        
        # A list to keep track of who is matched in each round
        self.matched = []
        for i in range(len(self.players)):
            self.matched.append(False)
            
        
    
    # TODO: Needs change. Not match every pair, but have each person point to another person.     
    def match_every_possible_pair(self, strat_list):
        for i in range(len(self.players)):
            for j in range(i, len(self.players)):
                self.one_on_one(self.players[i], self.players[j], i, j, strat_list)
    
    # Have the players play against each other based on strat_list
    def match(self, strat_list):
        for i in range(len(strat_list)):
            if not self.matched[i]:
                # print(strat_list[i][1])
                self.one_on_one(self.players[i], 
                                self.players[strat_list[i][1]], 
                                i, 
                                strat_list[i][1], 
                                strat_list)
            else:
                time.sleep(random.randint(4,9) / 10)
                print('∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨')
                time.sleep(random.random() / 2)
                print(f'🛑 {i}号{self.players[i].identity}已经与{strat_list[i][1]}号{self.players[strat_list[i][1]].identity}对局过，无需再次对局！')
                time.sleep(random.randint(4,9) / 10)
                print('∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧')                
                                
    def change_players_points(self, player1, player2, ind1, ind2, player1amt, player2amt):
        player1.pts += player1amt
        player2.pts += player2amt
        time.sleep(random.randint(3,7) / 10)
        if player1amt > 0:
            print(f'{ind1}号{player1.identity}加{player1amt}分！')
        elif player1amt < 0:
            print(f'{ind1}号{player1.identity}减{abs(player1amt)}分！')
        else:
            print(f'{ind1}号{player1.identity}不加分！')
            
        time.sleep(random.randint(3,7) / 10)
            
        if player2amt > 0:
            print(f'{ind2}号{player2.identity}加{player2amt}分！')
        elif player2amt < 0:
            print(f'{ind2}号{player2.identity}减{abs(player2amt)}分！')
        else:
            print(f'{ind2}号{player2.identity}不加分！')
        self.pts_change_table[self.current_round - 1][ind1] += player1amt
        self.pts_change_table[self.current_round - 1][ind2] += player2amt
                    
    # INPUT: Two players and their index numbers, and the strat_list. 
    # OUTPUT: No output. The players' points will be updated. 
    def one_on_one(self, player1, player2, ind1, ind2, strat_list):
        time.sleep(random.randint(4,9) / 10)
        
        self.matched[ind1] = True
        # If played 2 also plays player 1
        if strat_list[ind2][1] == ind1:
            self.matched[ind2] = True
        
        strat1 = strat_list[ind1][0]
        strat2 = strat_list[ind2][0]
        print('∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨')
        time.sleep(random.randint(4,9) / 10)
        print(f'🥊 {ind1}号{player1.identity}对战{ind2}号{player2.identity}！')
        
        time.sleep(random.randint(7,11) / 10)
        
        # Same Strats
        if strat1 == strat2:
            if strat1 == 'C' and strat2 == 'C':
                print('🤝 双方同时选择合作！🤝')
                self.change_players_points(player1, player2, ind1, ind2, 1, 1)
            
        
            elif strat1 == 'D' and strat2 == 'D':
                print('😈 双方互相欺骗！😈')
                self.change_players_points(player1, player2, ind1, ind2, -2, -2)
            
            elif strat1 == 'R' and strat2 == 'R':
                print('🔪 双方同时抢劫！🔪')
                self.change_players_points(player1, player2, ind1, ind2, -3, -3)
        
        else:
            if strat1 == 'C':
                word1 = '合作🤝'
            elif strat1 == 'D':
                word1 = '欺骗😈'
            elif strat1 == 'R':
                word1 = '抢劫🔪'
                
            if strat2 == 'C':
                word2 = '合作🤝'
            elif strat2 == 'D':
                word2 = '欺骗😈'
            elif strat2 == 'R':
                word2 = '抢劫🔪'
                
            print(f'{ind1}号{player1.identity}选择{word1}，而{ind2}号{player2.identity}选择{word2}！')
            
            time.sleep(random.randint(9,15) / 10)
            
            if strat1 == 'R' or strat2 == 'R':
                print('🪙抛硬币！正面成功，背面失败')
                time.sleep(1)
            
            # Diff Strats   
            if strat1 == 'C' and strat2 == 'D':
                self.change_players_points(player1, player2, ind1, ind2, 0, 2)
            
            elif strat1 == 'C' and strat2 == 'R':
                num = random.randint(0,1)
                if num == 1:
                    # Win!
                    print('抢劫成功！💰')
                    self.change_players_points(player1, player2, ind1, ind2, -1, 3)
                else:
                    # Lose!
                    print('抢劫失败！💸')
                    self.change_players_points(player1, player2, ind1, ind2, 2, -3)
                       
            elif strat1 == 'D' and strat2 == 'R':
                num = random.randint(0,1)
                if num == 1:
                    # Win!
                    print('抢劫成功！💰')
                    self.change_players_points(player1, player2, ind1, ind2, -2, 3)
                
                else:
                    # Lose!
                    print('抢劫失败！💸')
                    self.change_players_points(player1, player2, ind1, ind2, 1, -3)
        
            elif strat2 == 'C' and strat1 == 'D':
                self.change_players_points(player1, player2, ind1, ind2, 2, 0)
            
            elif strat2 == 'C' and strat1 == 'R':
                num = random.randint(0,1)
                if num == 1:
                    # Win!
                    print('抢劫成功！💰')
                    self.change_players_points(player1, player2, ind1, ind2, 3, -1)
                else:
                    # Lose!
                    print('抢劫失败！💸')
                    self.change_players_points(player1, player2, ind1, ind2, -3, 2)
            elif strat2 == 'D' and strat1 == 'R':
                num = random.randint(0,1)
                if num == 1:
                    # Win!
                    print('抢劫成功！💰')
                    self.change_players_points(player1, player2, ind1, ind2, 3, -2)
                else:
                    # Lose!
                    print('抢劫失败！💸')
                    self.change_players_points(player1, player2, ind1, ind2, -3, 1)
        
        time.sleep(random.randint(4,9) / 10)
        print('∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧')
                
    def new_round(self):
        
        print()
        input('   🎮   输入任意键开始下一回合   🎮   ')
        print()
        
        time.sleep(random.random())
        
        for i in range(len(self.players)):
            self.matched[i] = False
        print(f'❗️第{self.current_round}回合，开始！请各位玩家做好准备！')
        
        
        strat_list = []
        for i in range(len(self.players)):
            strat_list.append('')
        
        for i in range(len(self.players)):
            # First place is for action type, second place for the player that the action is aimed at
            strat = ['','']
            
            # If player is not AI
            if self.players[i].identity != 'AI':
                # Check if inputted strategy is valid. If yes, record it
                passing = False
                while not passing:
                    time.sleep(random.randint(3,6) / 10)   
                    action = str(input(f'>>> 亲爱的{self.players[i].identity}同学，请问您要做什么？合作请扣C，欺骗请扣D，抢劫请扣R，还请从速决定！'))
                    action = action.upper()
                    if action == 'C' or action == 'D' or action == 'R':
                        passing = True
                        strat[0] = action
                        print('>>> 收到！') # TODO: 用随机数显示别的选项，以及打出很多空格，以防下一个玩家偷看上一个玩家的策略
                    else: 
                        print('>>> 回答不符合要求，请重写！')
                
                # Check if inputted name is valid. If yes, record it
                passing2 = False
                while not passing2:
                    time.sleep(random.randint(2,6) / 10)
                    do_print = input('>>> 下一步你会选择对战哪个玩家。在此之前，要不要看看玩家列表？如果需要，请输入Y；否则，请输入其他任何字符。')
                    if do_print == 'Y' or do_print == 'y':
                        print('~~~ 玩  家  列  表 ~~~')
                        for j in range(len(self.players)):
                            time.sleep(random.random() / 3)
                            print(f'玩家{j}\t{self.players[j].identity}')
                        print('~~~~~~~~~~~~~~~~~~~~~')
                    target = input(f'>>> 请输入玩家编号，从0到{len(self.players) - 1}。你是第{i}号玩家。')
                    time.sleep(random.random())
                    if is_int(target):
                        target = int(target)
                        if (target in range(len(self.players))) and (target != i):
                            passing2 = True
                            strat[1] = target
                            print('>>> 操作成功！')
                        else: 
                            if target == i:
                                print('>>> 不许选自己！')
                            else:
                                print('>>> 玩家不存在，请重新选择。')        
                strat_list[i] = strat
                
            
            # If player is AI, choose from all three strategies with equal likelihood. 
            else:
                
                num = random.randint(1,3)
                if num == 1:
                    strat[0] = 'C'
                elif num == 2:
                    strat[0] = 'D'
                elif num == 3:
                    strat[0] = 'R'
                    
                # Then choose from all players with equal likelihood. Can't choose themselves.
                target_num = i
                while target_num == i:
                    target_num = random.randint(0,len(self.players) - 1)
                
                strat[1] = target_num
                strat_list[i] = strat
                
        
        self.strat_table[self.current_round - 1] = strat_list
        # strat_list now contains the choice of everyone. 
        self.match(strat_list)
        
        
        # Now strat_list is filled with the choices of every player. 
        
        if self.current_round <= 1:
            for i in range(len(self.players)):
                self.total_pts_table[0][i] += self.pts_change_table[0][i]
        elif self.current_round >= 2:
            combined = []
            for i in range(len(self.players)):
                combined.append(0)
            # Add each element in the last total_pts_table row to each element in the the current pts_change_table row
            for i in range(len(self.players)):
                combined[i] = self.pts_change_table[self.current_round - 1][i] + self.total_pts_table[self.current_round - 2][i]
            
            self.total_pts_table[self.current_round - 1] = combined[:]
        
        print()
        for i in range(len(self.players)):
            time.sleep(random.random() / 3)
            print(f'{i}号{self.players[i].identity}现在总分{self.total_pts_table[self.current_round - 1][i]}分!')
        
    def play(self):
        
        # Play the rounds
        for i in range(self.round_amount):
            self.current_round += 1
            self.new_round()
            
        # Print rankings
        print()
        print(' 🔚 游戏结束！')
        print()
        input('🎯   输入任意键显示排行榜   🎯')
        print()
        self.print_rankings()
        
        print()
        input('🎯   输入任意键显示本次游戏数据   🎯')
        print()
        self.print_tables()
        
        # TODO: Update the pts_change_table and the other one
            
    def print_rankings(self):
        last_row = self.total_pts_table[-1][:]
        
        player_list = []
        for i in range(len(last_row)):
            player_list.append([last_row[i], self.players[i].identity, i])
        
        player_list.sort(reverse = True)
        
        time.sleep(random.randint(4,9) / 10)
        
        max_len = 0
        for k in range(len(self.players)):
            if len(f'{k}号{self.players[k].identity}') > max_len:
                max_len = len(f'{k}号{self.players[k].identity}')
                
        len_of_each_tab = 8 # letters
        
        max_tab_amt = max_len // len_of_each_tab + 1
        
        print('~~~~~ 排  行  榜 ~~~~~')
        i = 1
        j = 0
        while j < len(last_row):
            time.sleep(random.random() / 3)
            
            if j > 0:
                if player_list[j][0] == player_list[j - 1][0]:
                    i -= 1
            
            amt_tab = max_tab_amt - len(f'{player_list[j][2]}号{player_list[j][1]}') // len_of_each_tab
            
            print(f'第{i}名\t{player_list[j][2]}号{player_list[j][1]}' + '\t' * amt_tab + f'得分{player_list[j][0]}', end = '\t')
            
            if i == 1:
                print('🏅️')
            elif i == 2:
                print('🥈')
            elif i == 3:
                print('🥉')
            else:
                print()
            
            i += 1
            j += 1
            
        
        print()
            
            
    def print_tables(self):
        
        print()
        print()
        print()
        
        time.sleep(random.randint(4,9) / 10)
        
        print('-|策略一览|-')
        print()
        # Print Strat_Table
        print('', end = '\t')
        for i in range(len(self.players)):
            print(self.players[i].identity, end = '\t\t')
            time.sleep(random.random() / 8)
        print('\n')
        for i in range(len(self.strat_table)):
            time.sleep(random.random() / 8)
            print(f'第{i+1}回合', end = '\t')
            for j in range(len(self.players)): 
                time.sleep(random.random() / 8)
                print(self.strat_table[i][j], end = '\t')
            print('\n')
        
        print()
        print()
        print()    
        
        time.sleep(random.randint(4,9) / 10)
        # Print pts_change_table
        print('-|分数变动一览|-')
        print()
        print('', end = '\t')
        for i in range(len(self.players)):
            print(self.players[i].identity, end = '\t')
            time.sleep(random.random() / 8)
        print('\n')
        for i in range(len(self.pts_change_table)):
            time.sleep(random.random() / 8)
            print(f'第{i+1}回合', end = '\t')
            for j in range(len(self.players)): 
                time.sleep(random.random() / 8)
                print(self.pts_change_table[i][j], end = '\t')
            print('\n')
            
        print()
        print()
        print()
        
        time.sleep(random.random() / 8)
        # Print total_pts_table
        print('-|累计得分一览|-')
        print()
        time.sleep(random.random() / 8)
        print('', end = '\t')
        for i in range(len(self.players)):
            print(self.players[i].identity, end = '\t')
            time.sleep(random.random() / 8)
        print('\n')
        for i in range(len(self.total_pts_table)):
            time.sleep(random.random() / 8)
            print(f'第{i+1}回合', end = '\t')
            for j in range(len(self.players)): 
                time.sleep(random.random() / 8)
                print(self.total_pts_table[i][j], end = '\t')
            print('\n')
    
    # TODO: Play rounds
    
    # TODO: Print out how many points each player has
    
    # TODO: Print out the Ranking in the end
    
    # TODO: Make a memo table for each round's score for each player. Print the table in the end if requested. 
    
    # Make another table for the difference in score for eac round for each player. 
    # Use + and - signs while printing.
    
    # Two ways to play: 
    # 1. 分数线: If you exceed a certain amount, you win, and the score of the rest are compared. 
    # 2. 回合制: After finishing a certain amount of rounds, compare each pair's score. 
    
    # Way to play: 
    # A player immediately loses if their score becomes negative. Need starting point amount: 10 points.
    
    
def is_int(word):
    try:
        int(word)
    except ValueError:
        return False
        
    return True
    
def is_float(word):
    try:
        float(word)
    except ValueError:
        return False
        
    return True
    
def main():
    # Create a game
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print('||==============================')
    print('||  欢迎游玩 "合作、欺骗、抢劫"  ')
    print('||    制作人: Bolong Tang    ')
    print('|| 特别感谢 Henry Tang 参与内测')
    print('||==============================')
    time.sleep(0.5)
    
    print()
    show_rule = input('>>> 请问您是否要查看游戏规则？若想，请按R：')
    if show_rule == 'R':
        time.sleep(1)
        print('||==============================')
        print('|| 游戏需要至少两名玩家，但不一定要有真\n|| 人玩家。至少要玩一局。在每一局中，每\n|| 名玩家要在三种策略——合作、欺骗、抢劫\n|| ——中选一种，对一名指定的玩家使用。当\n|| 所有玩家选择好策略后，游戏会自动对战\n|| 各对玩家，并在每一局结束后显示玩家分\n|| 数。选择抢劫的玩家会抛硬币。如果抛中\n|| 正面，那么抢劫成功；如果抛中背面，就\n|| 是抢劫失败。分数计算如下：\n|| · 一方合作而另一方欺骗\n||\t - 合作方不加分，欺骗方加2分\n|| · 一方合作而另一方抢劫\n||\t - 如果抢劫成功，合作方扣1分，抢劫方加3分\n||\t - 反之，如果抢劫失败，合作方加2分，抢劫方扣3分\n|| · 一方欺骗而另一方抢劫\n||\t - 如果抢劫成功，欺骗方扣2分，抢劫方加3分\n||\t - 如果抢劫失败，欺骗方加1分，抢劫方扣3分\n|| · 双方同时合作\n||\t - 各加1分\n|| · 双方同时欺骗\n||\t - 各扣2分\n|| · 双方同时抢劫\n||\t - 各扣3分')
        print('|| ')
        print('|| 本游戏也可以配合手上游戏，作为计分器\n|| 使用。建议玩法是：所有玩家坐在一圈，\n|| 大喊“合作、欺骗、抢劫”，然后同时指向\n|| 所选玩家。伸一根手指是合作，两根是欺\n|| 骗，三根是抢劫。')
        print('||==============================')
    print()
    
    print()
    show_develop_message = input('>>> 若想查看更多游戏信息，请输入more：')
    print()
    time.sleep(0.5)
    if show_develop_message == 'more':
        print('||==============================')
        time.sleep(1.7)
        print('||    此游戏灵感来源于“信任的进化”，   ')
        time.sleep(1.7)
        print('||   五年前被Bolong改编为手上多人游戏。')
        time.sleep(1.7)
        print('||  因为需要手动记分，游戏过程比较繁琐，')
        time.sleep(1.7)
        print('||      从而想到要自动化记分过程，   ')
        time.sleep(1.7)
        print('||        这个游戏才得以诞生。      ')
        time.sleep(1.7)
        print('||==============================')
        time.sleep(1.7)
        print('|| 开发：2023年12月19日至27日 ')
        time.sleep(1.7)
        print('||   平均工作量每天一个半小时  ')
        time.sleep(1.7)
        print('||   自Henry寒假的第一天开始； ')
        time.sleep(1.7)
        print('||      前三天完成大体架构，   ')
        time.sleep(1.7)
        print('||  后六天注重试玩、添加小细节、 ')
        time.sleep(1.7)
        print('||   以及修补各种大大小小的bug  ')
        time.sleep(1.7)
        print('||    27日首次与全家人共同试玩   ')
        time.sleep(1.7)
        print('||==============================')
        time.sleep(random.random())
    
    print()
    print()
    print('🏹️ 🎮 🎲       输入任意键开始       🏹️ 🎮 🎲')
    print()
    input()
    for i in range(random.randint(3,8)):
        time.sleep(random.random() / 2)
        option = random.randint(1,7)
        if option == 1:
            print('\t获取文件标准中...')
        elif option == 2:
            print('\t加载字体中...')
        elif option == 3:
            print('\t组装资源模块中...')
        elif option == 4:
            print('\t初始化游戏环境中...')
        elif option == 5:
            print('\t加载游戏界面中...')
        elif option == 6:
            print('\t初始化电脑玩家中...')
        elif option == 7:
            print('\t整理缓存资源中...')
            
    num = 0

    while num <= 100:
        num += random.randint(1,17)
        if num <= 100:
            print(f'\t加载中...{num}%')
            time.sleep(random.random() / 3)
    
    print('\t游戏加载完毕！')
    time.sleep(0.5)
    print('\t⚠️  若想在任何时候中止游戏，请按control + C')
    print()
    
    
    time.sleep(random.random() + 0.5)
    
    print('\t输入完成后请按Enter/Return键')
    print()
    
    time.sleep(random.random())
        
    game_name = str(input('>>> 这一局游戏的名字是？请输入：'))
    
    time.sleep(random.random())
    
    print('\n\t*以下设定中请输入整数，起始分数可以是小数*')
    
    time.sleep(random.random())
    
    passing1 = passing2 = passing3 = passing4 = False
    
    while not (passing1 and passing2 and passing3 and passing4):
        passing1 = passing2 = passing3 = passing4 = False
        
        print()
        
        total_player_num = input('>>> 算上AI，有多少玩家？最少2个。')
        if is_int(total_player_num):
            total_player_num = int(total_player_num)
            if (total_player_num >= 2):
                passing1 = True
        
        
        time.sleep(random.random())
        real_player_num = input('>>> 玩家有多少真人？可以没有。')
        if is_int(real_player_num) and is_int(total_player_num):
            real_player_num = int(real_player_num)
            if (0 <= real_player_num <= total_player_num):
                passing2 = True
        
        time.sleep(random.random())
        round_amt = input('>>> 要玩多少局呢？最低1局。')
        if is_int(round_amt):
            round_amt = int(round_amt)
            if (round_amt >= 1):
                passing3 = True
        
        time.sleep(random.random())
        initial_points = input('>>> 请输入每个玩家的起始分数：')
        if is_float(initial_points):
            initial_points = float(initial_points)
            passing4 = True
            
        time.sleep(random.random())
        if not (passing1 and passing2 and passing3 and passing4):
            print('>>> 至少有一项设定不符合要求，请重新输入！')
            time.sleep(random.randint(3,5) / 10)
        else:
            print('>>> 收到！游戏马上开始！')
            time.sleep(random.random() + 0.7)
            
    
    game = Game(game_name, total_player_num, real_player_num, round_amt, initial_points)
    
    # Play the game
    game.play()
    
    # Print the ranking after playing
    print()
    
    # Print the three tables
    
if __name__ == '__main__':
    main()