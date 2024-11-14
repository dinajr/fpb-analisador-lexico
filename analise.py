import regex

class Analisador:
    #Esta classe precisa ser fornecida com os tokens da analíse para criar a expressão regular
    def __init__(self, token_def):
        self.tokens = r""
        for index, i in enumerate(token_def):
            if index == 0:
                self.tokens = self.tokens + '(?<%s>%s)' % (i[0], i[1])
            else:
                self.tokens = self.tokens + '|' + '(?<%s>%s)' % (i[0], i[1])

    #Os tokens são colocados em uma lista após serem encontrados
    def lex_line(self, line):
        self.line_tokens = []
        for i in regex.finditer(self.tokens, line):
            token_name = i.lastgroup
            token = i.group()        
            if token == "\n":
                 self.line_tokens.append("<{0}>, ".format(token_name))
            else:
                self.line_tokens.append("<{0}, {1} >, ".format(token_name, token))
            
        return self.line_tokens
