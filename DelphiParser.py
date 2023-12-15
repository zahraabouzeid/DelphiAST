import ply.yacc as yacc
from DelphiLexer import Lexer

def p_assignment_statement(p):
    '''
    assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON
    '''

def p_expression(p):
    '''
    expression : NUMBER
    '''

def p_error(p):
    print(f"Syntax error at line {p.lineno}")

def p_var_declaration(p):
    '''
    var_declaration : VAR identifier_list COLON type_specifier SEMICOLON
    '''

def p_type_specifier(p):
    '''
    type_specifier : BYTE
                   | SHORTINT
                   | WORD
                   | SMALLINT
                   | LONGWORD
                   | INTEGER
                   | INT64
                   | SINGLE
                   | DOUBLE
                   | EXTENDED
                   | CHAR
                   | ANSICHAR
                   | STRING
                   | ANSISTRING
                   | WIDESTRING
                   | SHORTSTRING
                   | BOOLEAN
                   | ENUMERATION
                   | SET
                   | POINTER
                   | PCHAR
                   | VARIANT
                   | ARRAY
                   | DYNAMICARRAY
                   | RECORD
                   | FILE
                   | CLASS
                   | INTERFACE
    '''

def p_class_declaration(p):
    '''
    class_declaration : IDENTIFIER EQUAL LPAREN IDENTIFIER RPAREN
                      | IDENTIFIER EQUAL CLASS SEMICOLON
    '''

def p_identifier_list(p):
    '''
    identifier_list : IDENTIFIER
                    | IDENTIFIER COMMA identifier_list
    '''

if __name__ == "__main__":
    data = str
    parser = yacc.yacc()
    tokens = Lexer(data)
    result = parser.parse(tokens)