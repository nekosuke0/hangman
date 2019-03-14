def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("""
                おっと、ようやくお目覚めかね。
                手足に違和感があると思うが、心配することはない。
                君の選択次第で自由になることができるだろう。
                これから”ハングマン”というゲームをしてもらう。
                ルールは簡単。
                私の考えた単語を当てれば良いだけ。
                勝てば、拘束具は解除され、自由になれる。
                ただし負ければ、首吊り台に吊られることになる。
                さあ、ゲームの始まりだ。
            """)
    while wrong < len(stages) - 1:
        print("\n")
        msg = "単語の１文字を予想してください（ヒントはアルファベット。チャンスは7回）"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("""
                        あなたは見事に脱出した！
                        謎の老人は悔しがっているだろう。
                        つまりは勝ち！
                        しかし、あの老人は一体何がしたかったのだろうか。
                    """)
            print(" ".join(board))
            win = True
            break
    if not win:
            print("\n".join(stages[0:wrong+1]))
            print("""
                        あなたは吊られた。
                        首が締め付けられていき、息苦しくなっていく。
                        謎の老人は嗜虐的な笑みを浮かべている。
                        つまりは負けたのだ。
                        かすんでいく視界の中、最後の気力を振り絞って正解を見ようとする
                        ”{}”
                        そうか、これが謎の老人の考えた単語……。
                    """.format(word))

hangman("cat")
