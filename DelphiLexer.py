import ply.lex as lex

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'COMMA',
    'ASSIGN',
    'DOT',
    'COLON',
    'EQUALS',
    'NOT_EQUALS',
    'LESS_THAN',
    'LESS_THAN_OR_EQUAL',
    'GREATER_THAN',
    'GREATER_THAN_OR_EQUAL',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'TIMES_ASSIGN',
    'DIVIDE_ASSIGN',
    'MOD',
    'AND',
    'OR',
    'XOR',
    'NOT',
    'IF',
    'THEN',
    'ELSE',
    'FOR',
    'TO',
    'DOWNTO',
    'DO',
    'WHILE',
    'REPEAT',
    'UNTIL',
    'ARRAY',
    'BEGIN',
    'END',
    'FUNCTION',
    'PROCEDURE',
    'VAR',
    'CONST',
    'TYPE',
    'PROGRAM',
    'ABSTRACT',
    'ASM',
    'ASSEMBLER',
    'AUTOMATED',
    'BREAK',
    'CASE',
    'CDECL',
    'CLASS',
    'CONSTRUCTOR',
    'CONTINUE',
    'CURRENCY',
    'DEFAULT',
    'DESTRUCTOR',
    'DISPID',
    'DISPINTERFACE',
    'DIV',
    'DYNAMIC',
    'EXCE',
    'EXIT',
    'EXPORT',
    'EXPORTS',
    'EXTERNAL',
    'FALSE',
    'FAR',
    'FILE',
    'FINAL',
    'FINALIZATION',
    'FINALLY',
    'FORWARD',
    'GOTO',
    'IMPLEMENTATION',
    'IN',
    'INHERITED',
    'INITIALIZATION',
    'INLINE',
    'INTERFACE',
    'IS',
    'LABEL',
    'LIBRARY',
    'LONGINT',
    'LONGWORD',
    'MESSAGE',
    'NIL',
    'OBJECT',
    'OF',
    'OLEVARIANT',
    'ON',
    'OPERATOR',
    'OUT',
    'OVERLOAD',
    'OVERRIDE',
    'PACKED',
    'PASCAL',
    'POINTERSYMBOL',
    'PRIVATE',
    'PROPERTY',
    'PROTECTED',
    'PUBLIC',
    'PUBLISHED',
    'RAISE',
    'READ',
    'REAL',
    'RECORD',
    'REFERENCE',
    'REGISTER',
    'REQUIRES',
    'RESIDENT',
    'RESOURCESTRING',
    'ROUNDCLOSE',
    'ROUNDOPEN',
    'RUNERROR',
    'SAFECALL',
    'SEALED',
    'SET',
    'SHL',
    'SHORTINT',
    'SHORTSTRING',
    'SHR',
    'SINGLE',
    'SLASH',
    'SMALLINT',
    'SQUARECLOSE',
    'SQUAREOPEN',
    'STAR',
    'STDCALL',
    'STRING',
    'STRINGRESOURCE',
    'SYMBOL',
    'THREADVAR',
    'TRY',
    'UNIT',
    'UNKNOWN',
    'USES',
    'VARIANT',
    'VIRTUAL',
    'WIDECHAR',
    'WIDESTRING',
    'WITH',
    'WORD',
    'WORDBOOL',
    'WRITE',
    'QUOTE',
    'BYTE',
    'INTEGER',
    'INT64',
    'DOUBLE',
    'EXTENDED',
    'CHAR',
    'ANSICHAR',
    'ANSISTRING',
    'BOOLEAN',
    'ENUMERATION',
    'POINTER',
    'PCHAR',
    'DYNAMICARRAY'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_ASSIGN = r':='
t_DOT = r'\.'
t_COLON = r':'
t_EQUALS = r'='
t_NOT_EQUALS = r'<>'
t_LESS_THAN = r'<'
t_LESS_THAN_OR_EQUAL = r'<='
t_GREATER_THAN = r'>'
t_GREATER_THAN_OR_EQUAL = r'>='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_BYTE = r'BYTE'
t_INTEGER = r'INTEGER'
t_INT64 = r'INT64'
t_DOUBLE = r'DOUBLE'
t_EXTENDED = r'EXTENDED'
t_CHAR = r'CHAR'
t_ANSICHAR = r'ANSICHAR'
t_ANSISTRING = r'ANSISTRING'
t_BOOLEAN = r'BOOLEAN'
t_ENUMERATION = r'ENUMERATION'
t_POINTER = r'POINTER'
t_PCHAR = r'PCHAR'
t_DYNAMICARRAY = r'DYNAMICARRAY'
t_MOD = r'MOD'
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_IF = r'IF'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_FOR = r'FOR'
t_DO = r'DO'
t_REPEAT = r'REPEAT'
t_ARRAY = r'ARRAY'
t_OF = r'OF'
t_BEGIN = r'BEGIN'
t_END = r'END'
t_FUNCTION = r'FUNCTION'
t_PROCEDURE = r'PROCEDURE'
t_VAR = r'VAR'
t_PROGRAM = r'PROGRAM'
t_ABSTRACT = r'ABSTRACT'
t_ASM = r'ASM'
t_ASSEMBLER = r'ASSEMBLER'
t_AUTOMATED = r'AUTOMATED'
t_BREAK = r'BREAK'
t_CASE = r'CASE'
t_CDECL = r'CDECL'
t_CLASS = r'CLASS'
t_CONST = r'CONST'
t_CONSTRUCTOR = r'CONSTRUCTOR'
t_CONTINUE = r'CONTINUE'
t_CURRENCY = r'CURRENCY'
t_DEFAULT = r'DEFAULT'
t_DESTRUCTOR = r'DESTRUCTOR'
t_DISPID = r'DISPID'
t_DISPINTERFACE = r'DISPINTERFACE'
t_DIV = r'DIV'
t_DOWNTO = r'DOWNTO'
t_DYNAMIC = r'DYNAMIC'
t_EXCE = r'EXCE'
t_EXIT = r'EXIT'
t_EXPORT = r'EXPORT'
t_EXPORTS = r'EXPORTS'
t_EXTERNAL = r'EXTERNAL'
t_FALSE = r'FALSE'
t_FAR = r'FAR'
t_FILE = r'FILE'
t_FINAL = r'FINAL'
t_FINALIZATION = r'FINALIZATION'
t_FINALLY = r'FINALLY'
t_FORWARD = r'FORWARD'
t_GOTO = r'GOTO'
t_IMPLEMENTATION = r'IMPLEMENTATION'
t_IN = r'IN'
t_INHERITED = r'INHERITED'
t_INITIALIZATION = r'INITIALIZATION'
t_INLINE = r'INLINE'
t_INTERFACE = r'INTERFACE'
t_IS = r'IS'
t_LABEL = r'LABEL'
t_LIBRARY = r'LIBRARY'
t_LONGINT = r'LONGINT'
t_LONGWORD = r'LONGWORD'
t_MESSAGE = r'MESSAGE'
t_NIL = r'NIL'
t_OBJECT = r'OBJECT'
t_OLEVARIANT = r'OLEVARIANT'
t_ON = r'ON'
t_OPERATOR = r'OPERATOR'
t_OUT = r'OUT'
t_OVERLOAD = r'OVERLOAD'
t_OVERRIDE = r'OVERRIDE'
t_PACKED = r'PACKED'
t_PASCAL = r'PASCAL'
t_POINTERSYMBOL = r'POINTERSYMBOL'
t_PRIVATE = r'PRIVATE'
t_PROPERTY = r'PROPERTY'
t_PROTECTED = r'PROTECTED'
t_PUBLIC = r'PUBLIC'
t_PUBLISHED = r'PUBLISHED'
t_RAISE = r'RAISE'
t_READ = r'READ'
t_REAL = r'REAL'
t_RECORD = r'RECORD'
t_REFERENCE = r'REFERENCE'
t_REGISTER = r'REGISTER'
t_REQUIRES = r'REQUIRES'
t_RESIDENT = r'RESIDENT'
t_RESOURCESTRING = r'RESOURCESTRING'
t_ROUNDCLOSE = r'ROUNDCLOSE'
t_ROUNDOPEN = r'ROUNDOPEN'
t_RUNERROR = r'RUNERROR'
t_SAFECALL = r'SAFECALL'
t_SEALED = r'SEALED'
t_SET = r'SET'
t_SHL = r'SHL'
t_SHORTINT = r'SHORTINT'
t_SHORTSTRING = r'SHORTSTRING'
t_SHR = r'SHR'
t_SINGLE = r'SINGLE'
t_SLASH = r'SLASH'
t_SMALLINT = r'SMALLINT'
t_SQUARECLOSE = r'SQUARECLOSE'
t_SQUAREOPEN = r'SQUAREOPEN'
t_STAR = r'STAR'
t_STDCALL = r'STDCALL'
t_STRING = r'STRING'
t_STRINGRESOURCE = r'STRINGRESOURCE'
t_SYMBOL = r'SYMBOL'
t_THREADVAR = r'THREADVAR'
t_TO = r'TO'
t_TRY = r'TRY'
t_TYPE = r'TYPE'
t_UNIT = r'UNIT'
t_UNKNOWN = r'UNKNOWN'
t_UNTIL = r'UNTIL'
t_USES = r'USES'
t_VARIANT = r'VARIANT'
t_VIRTUAL = r'VIRTUAL'
t_WHILE = r'WHILE'
t_WIDECHAR = r'WIDECHAR'
t_WIDESTRING = r'WIDESTRING'
t_WITH = r'WITH'
t_WORD = r'WORD'
t_WORDBOOL = r'WORDBOOL'
t_WRITE = r'WRITE'
t_XOR = r'XOR'
t_ignore = ' \t'
t_QUOTE = r"'"

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in tokens:
        t.type = t.value.upper()
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

def Lexer(_data):
    lexer = lex.lex()
    lexer.input(_data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break 
        tokens.append(tok)
    return(tokens)


if __name__ == '__main__':
    data = str
    Lexer(data)