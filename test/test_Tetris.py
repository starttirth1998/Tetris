import Tetris
from Tetris import *

class Test_Tetris:
    def test_updateScore(self):
        temp = Game.score
        Game.updateScore(10)
        assert Game.score == temp + 10,"Score Not updated"

    def test_selectPiece(self):
        Game.selectPiece()
        assert Game.block_x == int(column/ 2 - len(Game.block[0])/2) and Game.block_y == 0, "Block Not generated properly"

class Test_Board:
    def test_newBoard(self):
        flag = 0
        Game.board = newBoard()
        for i in range(row):
            for j in range(column):
                if Game.board[i][j] == 1:
                    flag = 1
        for i in range(column):
            if Game.board[row][i] == 0:
                flag = 1
        assert flag == 0,"Board Not Initialized Properly"

    def test_checkPiecePos_True(self):
        Game.board = newBoard()
        Game.block = shapes[random.randrange(0,len(shapes))]
        x = int(column/ 2 - len(Game.block[0])/2)
        y = 0
        for i in range(column):
            Game.board[0][i] = 1
        assert checkPiecePos(Game.board,Game.block,(x,y)) == True,"checkPiecePos should return True instead of False"

    def test_checkPiecePos_False(self):
        Game.board = newBoard()
        Game.block = shapes[random.randrange(0,len(shapes))]
        x = int(column/ 2 - len(Game.block[0])/2)
        y = 0
        for i in range(column):
            Game.board[0][i] = 0
            Game.board[1][i] = 0
        assert checkPiecePos(Game.board,Game.block,(x,y)) == False,"checkPiecePos should return False instead of True"

    def test_fillPiecePos(self):
        x=3
        y=3
        flag = 0
        board = newBoard()
        block = shapes[random.randrange(0,len(shapes))]
        new_board = fillPiecePos(board, Game.block, (x,y))
        for shape_y, row in enumerate(block):
    		for shape_x, val in enumerate(row):
    			new_board[shape_y+y-1][shape_x+x] == val
                	flag = 1
        assert flag == 1,"fillPiecePos not filling Piece properly"

    def test_removeRow(self):
        flag = 0
        board = newBoard()
        for i in range(column):
            board[3][i] = 0
        board = removeRow(board, 4)
        for i in range(column):
            if(board[4][i] != 0 or board[0][i] != 0):
                flag = 1
        assert flag == 0,"removeRow not working"

    def test_removeRow_1Rowfilledabove(self):
        flag = 0
        board = newBoard()
        for i in range(column):
            board[3][i] = 1
        board = removeRow(board, 4)
        for i in range(column):
            if(board[4][i] != 1 or board[0][i] != 0):
                flag = 1
        assert flag == 0,"removeRow not working if above row is filled"

    def test_removeRow_2RowsFilledabove(self):
        flag = 0
        board = newBoard()
        for i in range(column):
            board[2][i] = 1
        board = removeRow(board, 4)
        board = removeRow(board, 4)
        for i in range(column):
            if(board[4][i] != 1 or board[0][i] != 0):
                flag = 1
        assert flag == 0,"removeRow not working if 2 rows deleted together"

class Test_Block:
    def test_addLines(self):
        Game.score = 100
        Game.level = 1
        Game.addLines()
        assert Game.level == 2,"addLines: level not increasing properly"

    def test_addLines_speedup_controlled(self):
        Game.score = 1000
        Game.level = 10
        Game.addLines()
        assert Game.level == 11,"addLines: speed_up gone negative"

    def test_fall_gameOver_True(self):
        Game.gameOver = True
        assert Game.fall() == False,"fall: Game is over block should not fall"

    def test_fall_gameOver_False_checkPiecePos_False(self):
        Game.gameOver = False
        Game.board = newBoard()
        Game.block_x = int(column/ 2 - len(Game.block[0])/2)
        Game.block_y = 0
        Game.block = shapes[random.randrange(0,len(shapes))]
        for i in range(column):
            Game.board[0][i] = 0
            Game.board[1][i] = 0
        assert (Game.fall() == False and Game.block_y == 1),"fall: gameOver-> False,checkPiecePos->False"

    def test_fall_gameOver_False_checkPiecePos_True(self):
        Game.gameOver = False
        Game.board = newBoard()
        Game.block_x = int(column/ 2 - len(Game.block[0])/2)
        Game.block_y = 2
        Game.block = shapes[random.randrange(0,len(shapes))]
        for i in range(column):
            Game.board[3][i] = 1
        boolean = Game.fall()
        assert (boolean == True),"fall: gameOver-> False,checkPiecePos->False"

    def test_moveLeft(self):
        Game.block = shapes[random.randrange(0,len(shapes))]
        Game.block_x = 1
        Game.board = newBoard()
        Game.moveLeft()
        assert Game.block_x == 0,"moveLeft: moveLeft not working"

    def test_moveLeft_outofGrid(self):
        Game.block = shapes[random.randrange(0,len(shapes))]
        Game.block_x = 0
        Game.board = newBoard()
        Game.moveLeft()
        assert Game.block_x == 0,"moveLeft: Block outside grid on moveleft"

    def test_moveLeft_Override_Piece(self):
        Game.block = shapes[random.randrange(0,len(shapes))]
        Game.block_x = 1
        Game.board = newBoard()
        for i in range(row):
            Game.board[i][0] = 1
        Game.moveLeft()
        assert Game.block_x == 1,"moveLeft: Block over another block"

    def test_moveRight_PieceLength3(self):
        Game.block = shapes[1]
        Game.block_x = column - len(Game.block[0]) - 1
        Game.block_y = 1
        Game.board = newBoard()
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]),"moveRight: moveRight not working"

    def test_moveRight_outofGrid_PieceLength3(self):
        Game.block = shapes[1]
        Game.block_x = column - len(Game.block[0])
        Game.block_y = 1
        Game.board = newBoard()
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]),"moveRight: Block outside grid on move right"

    def test_moveRight_Override_Piece_PieceLength3(self):
        Game.block = shapes[1]
        Game.block_x = column - len(Game.block[0]) - 1
        Game.block_y = 1
        Game.board = newBoard()
        for i in range(row):
            Game.board[i][column - len(Game.block[0])] = 1
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]) - 1,"moveRight: Block over another block"

    def test_moveRight_PieceLength2(self):
        Game.block = shapes[23]
        Game.block_x = column - len(Game.block[0]) - 1
        Game.block_y = 1
        Game.board = newBoard()
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]),"moveRight: moveRight not working"

    def test_moveRight_outofGrid_PieceLength2(self):
        Game.block = shapes[23]
        Game.block_x = column - len(Game.block[0])
        Game.block_y = 1
        Game.board = newBoard()
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]),"moveRight: Block outside grid on move right"

    def test_moveRight_Override_Piece_PieceLength2(self):
        Game.block = shapes[23]
        Game.block_x = column - len(Game.block[0]) - 1
        Game.block_y = 1
        Game.board = newBoard()
        for i in range(row):
            Game.board[i][column - len(Game.block[0])] = 1
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]) - 1,"moveRight: Block over another block"

    def test_moveRight_PieceLength4(self):
        Game.block = shapes[45]
        Game.block_x = column - len(Game.block[0]) - 1
        Game.block_y = 1
        Game.board = newBoard()
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]),"moveRight: moveRight not working"

    def test_moveRight_outofGrid_PieceLength4(self):
        Game.block = shapes[45]
        Game.block_x = column - len(Game.block[0])
        Game.block_y = 1
        Game.board = newBoard()
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]),"moveRight: Block outside grid on move right"

    def test_moveRight_Override_Piece_PieceLength4(self):
        Game.block = shapes[45]
        Game.block_x = column - len(Game.block[0]) - 1
        Game.block_y = 1
        Game.board = newBoard()
        for i in range(row):
            Game.board[i][column - len(Game.block[0])] = 1
        Game.moveRight()
        assert Game.block_x == column - len(Game.block[0]) - 1,"moveRight: Block over another block"

    def test_rotate_blockedBelow_BlockLength3(self):
        Game.block = shapes[1]
        Game.board = newBoard()
        Game.block_x = 2
        Game.block_y = 3
        for i in range(column):
            Game.board[3][i] = 1
        Game.rotate(Game.block)
        assert shapes[1] == Game.block,"rotate: Block of length 3 should not rotate... It is blocked below"

    def test_rotate_blockedSide_BlockLength3(self):
        Game.block = shapes[1]
        Game.block_x = 2
        Game.block_y = 3
        Game.board = newBoard()
        Game.rotate(Game.block)
        temp = Game.block
        for i in range(row):
            Game.board[i][4] = 1
        Game.rotate(Game.block)
        assert temp == Game.block,"rotate: Block of length 3 should not rotate... It is blocked on side"

    def test_rotate_blockedBelow_BlockLength4(self):
        Game.block = shapes[45]
        Game.board = newBoard()
        Game.block_x = 2
        Game.block_y = 3
        for i in range(column):
            Game.board[5][i] = 1
        Game.rotate(Game.block)
        assert shapes[45] == Game.block,"rotate: Block of length 4 should not rotate... It is blocked below"

    def test_rotate_blockedSide_BlockLength4(self):
        Game.block = shapes[45]
        Game.block_x = 2
        Game.block_y = 3
        Game.board = newBoard()
        Game.rotate(Game.block)
        temp = Game.block
        for i in range(row):
            Game.board[i][4] = 1
        Game.rotate(Game.block)
        assert temp == Game.block,"rotate: Block of length 4 should not rotate... It is blocked on side"

Game = GamePlay()
