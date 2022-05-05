Tree(
    Token('RULE', 'programa'), 
    [Token('START_PROGRAM', 'Start'), 
    Token('NEW_LINE', '\n'), 
    Tree(
        Token('RULE', 'programa2'), 
        [Tree('unnumero', [
             Tree(
                Token('RULE', 'var_cte'), [
                    Token('CONST_INT', '1')])]), 
                        Tree(
                            Token('RULE', 'programa3'), []
                        )
        ]
    ), 
    Token('FINISH_PROGRAM', 'Finish')]
)


Tree(
    Token('RULE', 'programa'), [
        Token('START_PROGRAM', 'Start'), 
        Token('NEW_LINE', '\n'), 
        Tree(
            Token('RULE', 'programa2'), [
                Tree(
                    'unnumero', [
                        Tree(
                            Token('RULE', 'var_cte'), [
                                Token('CONST_INT', '1')
                            ]
                        )
                    ]
                ), 
                                Tree(
                                    Token('RULE', 'programa3'), []
                                )
            ]
        ), 
                                    Token('FINISH_PROGRAM', 'Finish')
    ]
)

Tree(Token('RULE', 'programa2'), [Tree('unnumero', [Tree(Token('RULE', 'var_cte'), [Token('CONST_INT', '1')])]), Tree(Token('RULE', 'programa3'), [])])
Finish
Tree(Token('RULE', 'programa'), [Token('START_PROGRAM', 'Start'), Token('NEW_LINE', '\n'), Tree(Token('RULE', 'programa2'), [Tree('unnumero', [Tree(Token('RULE', 'var_cte'), [Token('CONST_INT', '1')])]), Tree(Token('RULE', 'programa3'), [])]), Token('FINISH_PROGRAM', 'Finish')])


////////////////
Tree('change_color', [
    Token('COLOR', 'red'), 
    Token('COLOR', 'yellow')
    ])  
Tree('fill', [
    Tree(
        Token('RULE', 'code_block'), [
            Tree('repeat', [
                Token('NUMBER', '36'), 
                Tree(
                    Token('RULE', 'code_block'), [
                        Tree('movement', [
                            Token('MOVEMENT', 'f'), 
                            Token('NUMBER', '200')]), 
                            Tree('movement', [
                                Token('MOVEMENT', 'l'), 
                                Token('NUMBER', '170')])])])])])