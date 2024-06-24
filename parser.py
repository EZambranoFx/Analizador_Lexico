import ply.yacc as yacc
from lexer import tokens
import datetime
import os

# Inicio - Enrique Zambrano 

# Estructura de Datos: Declaracion de objetos
def p_object_declaration(p):
    '''object_declaration : VAR VARIABLE EQUALS NEW CLASS LPAREN RPAREN SEMI'''

# Estructura de Control: While
def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN statement'''

# Funcion: Funcion Variable
def p_function_variable(p):
    '''function_variable : FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACE'''

# Impresion
def p_print_statement(p):
    '''print_statement : ECHO LPAREN expression_list RPAREN SEMI
                       | ECHO expression_list SEMI'''

# Solicitud de Datos
def p_input_statement(p):
    '''input_statement : VARIABLE EQUALS READLINE LPAREN RPAREN SEMI'''

# Expresiones Aritmeticas
def p_expression_statement(p):
    '''expression_statement : expression SEMI'''

#Fin - Enrique Zambrano

# Inicio - Alejandro Barrera 

# Estructura de Datos: Declaración de arreglos
def p_array(p):
    '''array : ARRAY LPAREN arrayArg RPAREN SEMI'''
    
def p_arrayArg(p):
    '''arrayArg : index ARROW value
                | index ARROW value arrayArg
                | index ARROW value COMMA arrayArg'''
    
def p_index(p):
    '''index : INTEGER
            | STRING'''

# Estructura de Control: if y else
def p_ifStatement(p):
    '''ifStatement : IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI
                    | IF LPAREN condition RPAREN LBRACE statements RBRACE elseStatement'''
    
def p_elseStatement(p):
    '''elseStatement : ELSE LBRACE statements RBRACE SEMI'''
    
def p_condition(p):
    'condition : value compOperator value'
    
def p_compOperator(p):
    '''compOperator : LT
                    | GT
                    | LE
                    | GE
                    | EQ
                    | NE'''
    
def p_value(p):
    '''value : VARIABLE
            | INT
            | FLOAT
            | expression_statement'''
    
#Función: Funciones de flecha.
def p_arrowFunction(p):
    '''arrowFunction : FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI
                    | FUNCTION LPAREN VARIABLE RPAREN ARROW arrowFunction'''

#Fin - Alejandro Barrera

#-----------TODO PRATT------------

def p_class_declaration(p):
    '''class_declaration : CLASS IDENTIFIER LBRACE class_body RBRACE'''

def p_class_body(p):
    '''class_body : class_member_list'''

def p_class_member_list(p):
    '''class_member_list : class_member_list class_member
                         | empty'''

def p_class_member(p):
    '''class_member : property_declaration
                    | method_declaration
                    | constructor_declaration'''

def p_property_declaration(p):
    '''property_declaration : visibility VARIABLE SEMI'''

def p_method_declaration(p):
    '''method_declaration : visibility FUNCTION IDENTIFIER LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'''

def p_constructor_declaration(p):
    '''constructor_declaration : visibility FUNCTION CONSTRUCT LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'''

def p_visibility(p):
    '''visibility : PUBLIC
                  | PROTECTED
                  | PRIVATE'''

def p_parameter_list(p):
    '''parameter_list : parameter_list COMMA parameter
                      | empty'''

def p_parameter(p):
    '''parameter : TYPE VARIABLE
                 | VARIABLE'''

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''


parser = yacc.yacc()


def test_parser(data, username):
    result = parser.parse(data)
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"sintactico-{username}-{current_time}.txt"
    log_path = os.path.join(log_folder, log_filename)

    with open(log_path, "w") as log_file:
        if result:
            log_file.write(str(result))
            print(result)
        else:
            log_file.write("Syntax errors found")
            print("Syntax errors found")


