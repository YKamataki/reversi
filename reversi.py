class ReversiGame:
    """リバーシのゲームを扱うためのクラス
    ゲームの内部処理のみを行う。UIは提供しない"""

#クラスの定数を定義
#盤面
    WALL = 9 #盤面の外側
    NONE = 0 #石がない
    WHITE = 1 #白石
    BLACK = 2 #黒石

    def __init__(self, game_data_dictionary:dict):
        """盤面を初期化する。"""

        #設定を読み込む
        self.pl1_name = game_data_dictionary['pl1_name']
        self.pl2_name = game_data_dictionary['pl2_name']
        self.board_size = game_data_dictionary['board_size']

        #盤面を作成する
        """外側がカラム、内側が行
        board[1][2]は、一番左の上から2番目。ExcelのA2
        盤面の外側にWALLが存在する"""
        self.board = [ [] for i in range(self.board_size+2)] #columns
        #まずはすべて空にする
        for column in self.board:
            for i in range(self.board_size+2):
                column.append(self.NONE)
        """
        #次に盤面の外側をWALLで埋める
        for row in self.board[0]: #左端の壁
            for p in range(row):
                row[p] = self.WALL
        for row in self.board[self.board_size+1]: #右端の壁
            for p in range(row):
                row[p] = self.WALL

        #上下の壁
        for i in range(len(self.board)):
            self.board[i][0] = self.WALL
            self.board[i][len(self.board)-1] = self.WALL
        """

if __name__ == '__main__': #テストを以下に記述
    data = {
        'pl1_name':'A',
        'pl2_name':'B',
        'board_size':8,
    }
    game = ReversiGame(data)
    #盤面を表示
    tmp = []
    for c in range(len(game.board)):
        for r in range(len(game.board)):
            tmp.append(game.board[c][r])
        print(tmp)
        tmp = []
