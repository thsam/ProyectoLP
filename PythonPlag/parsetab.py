
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocMENORMAYORDEQUALSleftPLUSMINUSleftTIMESDIVIDEleftLPARENRPARENleftMODEXPleftLCORCRCORCAND COMA COMMENT DEF DEQUALS DIVIDE DPUNTOS ELIF ELSE EQUALS EXP FALSE FOR ID IF IN LCORC LPAREN MAYOR MENOR MINUS MOD NEGADOR NUMBER OR PLUS PUNTO RANGE RCORC RETURN RPAREN STRING TIMES TRUEbloque_codigo : empty\n                     | linea_codigo empty\n                     | bloque_codigo linea_codigo emptylinea_codigo : expr_funcion\n\t\t\t\t\t| expr_def_funcion\n\t\t\t\t\t| expr_asign\n\t\t\t\t\t| expr_if_else\n\t\t\t\t\t| def_for\n\t\t\t\t\t| expr_return\n\t\t\t\t\t| call_methodexpr_def_funcion : DEF expr_funcion DPUNTOSparams : variable\n\t\t\t  | params COMA variable\n\t\t\t  | expr_funcionvariable : ID\n                | expr_str\n                | NUMBER\n                | expr_float\n                | bool\n                | listaexpr_funcion : ID LPAREN params RPAREN\n                    | ID LPAREN RPARENlista : ID LCORC variable RCORC\n             | ID LCORC operaciones_algebraica RCORCexpr_str : STRINGexpr_float : NUMBER PUNTO NUMBERexpr_asign : ID EQUALS variable\n                  | ID EQUALS expr_funcion\n                  | ID EQUALS operaciones_algebraica\n                  | ID EQUALS LCORC RCORC\n                  | ID EQUALS call_methodoperador_igualdad : MAYOR\n                         | MENOR\n                         | DEQUALS\n                         | MAYOR EQUALS\n                         | MENOR EQUALS\n                         | NEGADOR EQUALSexpr_return : RETURN variable\n                   | RETURN expr_funcion\n                   | RETURN operaciones_algebraica expr_if_else : IF condiciones_expr_if_else DPUNTOS\n                     | ELIF condiciones_expr_if_else DPUNTOS\n                     | ELSE DPUNTOScondiciones_expr_if_else : condiciones\n                                | condiciones and_or condiciones_expr_if_else\n                                | LPAREN condiciones_expr_if_else RPARENcondiciones : variable\n                   | expr_funcion\n                   | operaciones_algebraica operador_igualdad variable\n                   | condiciones operador_igualdad condicionesdef_for : FOR variable IN RANGE LPAREN params_for RPAREN DPUNTOSparams_for :\tvariable_for\n                  | variable_for COMA variable_for\n                  | variable_for  COMA variable_for COMA variable_forvariable_for : variable\n                    | operaciones_algebraicabool : TRUE\n\t        | FALSE and_or : AND\n               | ORoperaciones_algebraica : p_variables_operaciones_algebraica operador_alge p_variables_operaciones_algebraica\n                              | LPAREN p_variables_operaciones_algebraica operador_alge p_variables_operaciones_algebraica RPAREN\n                              | operaciones_algebraica operador_alge p_variables_operaciones_algebraicap_variables_operaciones_algebraica : variable\n                                         | expr_funcionoperador_alge : PLUS\n\t                 | MINUS\n\t                 | TIMES\n\t                 | DIVIDE\n\t                 | MOD\n\t                 | EXPcall_method : variable PUNTO expr_funcion\n                   | call_method PUNTO expr_funcionempty : '
    
_lr_action_items = {'ID':([0,1,2,3,4,5,6,7,8,9,10,12,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,38,42,45,48,49,50,51,53,54,56,59,60,61,63,67,68,69,70,71,72,73,74,75,76,77,83,84,85,86,87,88,89,90,91,92,95,96,97,98,99,100,101,104,105,106,108,110,111,113,116,118,124,125,127,],[11,11,-1,-74,-4,-5,-6,-7,-8,-9,-10,34,42,42,47,42,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,34,42,42,64,34,42,-15,-43,-38,-39,-40,42,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,42,42,-59,-60,-32,-33,-34,47,42,-66,-67,-68,-69,-70,-71,42,-42,-64,-26,-21,47,-30,-23,-24,-35,-36,-37,42,-63,-61,42,64,-62,64,-51,64,]),'DEF':([0,1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,27,28,42,45,48,49,50,53,54,56,59,60,61,63,67,68,69,70,92,95,96,97,99,100,101,110,111,118,125,],[12,12,-1,-74,-4,-5,-6,-7,-8,-9,-10,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,-15,-43,-38,-39,-40,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,-42,-64,-26,-21,-30,-23,-24,-63,-61,-62,-51,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,27,28,42,45,48,49,50,53,54,56,59,60,61,63,67,68,69,70,92,95,96,97,99,100,101,110,111,118,125,],[14,14,-1,-74,-4,-5,-6,-7,-8,-9,-10,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,-15,-43,-38,-39,-40,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,-42,-64,-26,-21,-30,-23,-24,-63,-61,-62,-51,]),'ELIF':([0,1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,27,28,42,45,48,49,50,53,54,56,59,60,61,63,67,68,69,70,92,95,96,97,99,100,101,110,111,118,125,],[15,15,-1,-74,-4,-5,-6,-7,-8,-9,-10,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,-15,-43,-38,-39,-40,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,-42,-64,-26,-21,-30,-23,-24,-63,-61,-62,-51,]),'ELSE':([0,1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,27,28,42,45,48,49,50,53,54,56,59,60,61,63,67,68,69,70,92,95,96,97,99,100,101,110,111,118,125,],[16,16,-1,-74,-4,-5,-6,-7,-8,-9,-10,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,-15,-43,-38,-39,-40,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,-42,-64,-26,-21,-30,-23,-24,-63,-61,-62,-51,]),'FOR':([0,1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,27,28,42,45,48,49,50,53,54,56,59,60,61,63,67,68,69,70,92,95,96,97,99,100,101,110,111,118,125,],[17,17,-1,-74,-4,-5,-6,-7,-8,-9,-10,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,-15,-43,-38,-39,-40,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,-42,-64,-26,-21,-30,-23,-24,-63,-61,-62,-51,]),'RETURN':([0,1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,27,28,42,45,48,49,50,53,54,56,59,60,61,63,67,68,69,70,92,95,96,97,99,100,101,110,111,118,125,],[18,18,-1,-74,-4,-5,-6,-7,-8,-9,-10,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,-15,-43,-38,-39,-40,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,-42,-64,-26,-21,-30,-23,-24,-63,-61,-62,-51,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,14,15,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,38,42,45,48,49,50,51,52,53,54,56,59,60,61,63,67,68,69,70,71,72,73,74,75,76,77,83,84,85,86,87,88,89,90,91,92,95,96,97,98,99,100,101,104,105,106,108,110,111,113,116,118,124,125,127,],[20,20,-1,-74,-4,-5,-6,-7,-8,-9,-10,20,20,20,20,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,20,20,20,20,-15,-43,-38,-39,-40,20,96,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,20,20,-59,-60,-32,-33,-34,20,20,-66,-67,-68,-69,-70,-71,20,-42,-64,-26,-21,20,-30,-23,-24,-35,-36,-37,20,-63,-61,20,20,-62,20,-51,20,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,14,15,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,38,42,45,48,49,50,51,53,54,56,59,60,61,63,67,68,69,70,71,72,73,74,75,76,77,83,84,85,86,87,88,89,90,91,92,95,96,97,98,99,100,101,104,105,106,108,110,111,113,116,118,124,125,127,],[24,24,-1,-74,-4,-5,-6,-7,-8,-9,-10,24,24,24,24,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,24,24,24,24,-15,-43,-38,-39,-40,24,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,24,24,-59,-60,-32,-33,-34,24,24,-66,-67,-68,-69,-70,-71,24,-42,-64,-26,-21,24,-30,-23,-24,-35,-36,-37,24,-63,-61,24,24,-62,24,-51,24,]),'TRUE':([0,1,2,3,4,5,6,7,8,9,10,14,15,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,38,42,45,48,49,50,51,53,54,56,59,60,61,63,67,68,69,70,71,72,73,74,75,76,77,83,84,85,86,87,88,89,90,91,92,95,96,97,98,99,100,101,104,105,106,108,110,111,113,116,118,124,125,127,],[25,25,-1,-74,-4,-5,-6,-7,-8,-9,-10,25,25,25,25,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,25,25,25,25,-15,-43,-38,-39,-40,25,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,25,25,-59,-60,-32,-33,-34,25,25,-66,-67,-68,-69,-70,-71,25,-42,-64,-26,-21,25,-30,-23,-24,-35,-36,-37,25,-63,-61,25,25,-62,25,-51,25,]),'FALSE':([0,1,2,3,4,5,6,7,8,9,10,14,15,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,38,42,45,48,49,50,51,53,54,56,59,60,61,63,67,68,69,70,71,72,73,74,75,76,77,83,84,85,86,87,88,89,90,91,92,95,96,97,98,99,100,101,104,105,106,108,110,111,113,116,118,124,125,127,],[26,26,-1,-74,-4,-5,-6,-7,-8,-9,-10,26,26,26,26,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,26,26,26,26,-15,-43,-38,-39,-40,26,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,26,26,-59,-60,-32,-33,-34,26,26,-66,-67,-68,-69,-70,-71,26,-42,-64,-26,-21,26,-30,-23,-24,-35,-36,-37,26,-63,-61,26,26,-62,26,-51,26,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,27,28,42,45,48,49,50,53,54,56,59,60,61,63,67,68,69,70,92,95,96,97,99,100,101,110,111,118,125,],[-74,0,-1,-74,-4,-5,-6,-7,-8,-9,-10,-16,-17,-18,-19,-20,-25,-57,-58,-74,-2,-15,-43,-38,-39,-40,-3,-73,-22,-27,-28,-29,-31,-65,-11,-72,-41,-42,-64,-26,-21,-30,-23,-24,-63,-61,-62,-51,]),'PUNTO':([10,11,13,19,20,21,22,23,24,25,26,42,54,56,59,63,69,96,97,100,101,],[29,-15,35,-16,52,-18,-19,-20,-25,-57,-58,-15,-73,-22,35,29,-72,-26,-21,-23,-24,]),'LPAREN':([11,14,15,18,31,32,34,38,42,64,71,72,73,74,75,76,77,104,105,106,112,116,124,127,],[30,38,38,51,51,51,30,38,30,30,38,51,-59,-60,-32,-33,-34,-35,-36,-37,116,51,51,51,]),'EQUALS':([11,75,76,78,],[31,104,105,106,]),'LCORC':([11,31,42,47,64,],[32,62,32,32,32,]),'DPUNTOS':([16,19,20,21,22,23,24,25,26,33,36,37,39,40,42,44,47,56,96,97,100,101,102,103,107,109,123,],[45,-16,-17,-18,-19,-20,-25,-57,-58,68,70,-44,-47,-48,-15,92,-15,-22,-26,-21,-23,-24,-45,-50,-46,-49,125,]),'AND':([19,20,21,22,23,24,25,26,37,39,40,42,47,56,81,82,96,97,100,101,103,109,],[-16,-17,-18,-19,-20,-25,-57,-58,73,-47,-48,-15,-15,-22,-47,-48,-26,-21,-23,-24,-50,-49,]),'OR':([19,20,21,22,23,24,25,26,37,39,40,42,47,56,81,82,96,97,100,101,103,109,],[-16,-17,-18,-19,-20,-25,-57,-58,74,-47,-48,-15,-15,-22,-47,-48,-26,-21,-23,-24,-50,-49,]),'MAYOR':([19,20,21,22,23,24,25,26,37,39,40,41,42,47,56,67,81,82,95,96,97,100,101,103,109,110,111,115,118,],[-16,-17,-18,-19,-20,-25,-57,-58,75,-47,-48,75,-15,-15,-22,-65,-47,-48,-64,-26,-21,-23,-24,75,-49,-63,-61,-61,-62,]),'MENOR':([19,20,21,22,23,24,25,26,37,39,40,41,42,47,56,67,81,82,95,96,97,100,101,103,109,110,111,115,118,],[-16,-17,-18,-19,-20,-25,-57,-58,76,-47,-48,76,-15,-15,-22,-65,-47,-48,-64,-26,-21,-23,-24,76,-49,-63,-61,-61,-62,]),'DEQUALS':([19,20,21,22,23,24,25,26,37,39,40,41,42,47,56,67,81,82,95,96,97,100,101,103,109,110,111,115,118,],[-16,-17,-18,-19,-20,-25,-57,-58,77,-47,-48,77,-15,-15,-22,-65,-47,-48,-64,-26,-21,-23,-24,77,-49,-63,-61,-61,-62,]),'NEGADOR':([19,20,21,22,23,24,25,26,37,39,40,41,42,47,56,67,81,82,95,96,97,100,101,103,109,110,111,115,118,],[-16,-17,-18,-19,-20,-25,-57,-58,78,-47,-48,78,-15,-15,-22,-65,-47,-48,-64,-26,-21,-23,-24,78,-49,-63,-61,-61,-62,]),'PLUS':([19,20,21,22,23,24,25,26,39,40,41,42,43,48,49,50,56,59,60,61,64,65,66,67,80,81,82,94,95,96,97,100,101,110,111,115,118,119,122,],[-16,-17,-18,-19,-20,-25,-57,-58,-64,-65,85,-15,85,-64,-65,85,-22,-64,-65,85,-15,-64,85,-65,85,-64,-65,85,-64,-26,-21,-23,-24,-63,-61,-61,-62,-64,85,]),'MINUS':([19,20,21,22,23,24,25,26,39,40,41,42,43,48,49,50,56,59,60,61,64,65,66,67,80,81,82,94,95,96,97,100,101,110,111,115,118,119,122,],[-16,-17,-18,-19,-20,-25,-57,-58,-64,-65,86,-15,86,-64,-65,86,-22,-64,-65,86,-15,-64,86,-65,86,-64,-65,86,-64,-26,-21,-23,-24,-63,-61,-61,-62,-64,86,]),'TIMES':([19,20,21,22,23,24,25,26,39,40,41,42,43,48,49,50,56,59,60,61,64,65,66,67,80,81,82,94,95,96,97,100,101,110,111,115,118,119,122,],[-16,-17,-18,-19,-20,-25,-57,-58,-64,-65,87,-15,87,-64,-65,87,-22,-64,-65,87,-15,-64,87,-65,87,-64,-65,87,-64,-26,-21,-23,-24,-63,-61,-61,-62,-64,87,]),'DIVIDE':([19,20,21,22,23,24,25,26,39,40,41,42,43,48,49,50,56,59,60,61,64,65,66,67,80,81,82,94,95,96,97,100,101,110,111,115,118,119,122,],[-16,-17,-18,-19,-20,-25,-57,-58,-64,-65,88,-15,88,-64,-65,88,-22,-64,-65,88,-15,-64,88,-65,88,-64,-65,88,-64,-26,-21,-23,-24,-63,-61,-61,-62,-64,88,]),'MOD':([19,20,21,22,23,24,25,26,39,40,41,42,43,48,49,50,56,59,60,61,64,65,66,67,80,81,82,94,95,96,97,100,101,110,111,115,118,119,122,],[-16,-17,-18,-19,-20,-25,-57,-58,-64,-65,89,-15,89,-64,-65,89,-22,-64,-65,89,-15,-64,89,-65,89,-64,-65,89,-64,-26,-21,-23,-24,-63,-61,-61,-62,-64,89,]),'EXP':([19,20,21,22,23,24,25,26,39,40,41,42,43,48,49,50,56,59,60,61,64,65,66,67,80,81,82,94,95,96,97,100,101,110,111,115,118,119,122,],[-16,-17,-18,-19,-20,-25,-57,-58,-64,-65,90,-15,90,-64,-65,90,-22,-64,-65,90,-15,-64,90,-65,90,-64,-65,90,-64,-26,-21,-23,-24,-63,-61,-61,-62,-64,90,]),'IN':([19,20,21,22,23,24,25,26,46,47,96,100,101,],[-16,-17,-18,-19,-20,-25,-57,-58,93,-15,-26,-23,-24,]),'RPAREN':([19,20,21,22,23,24,25,26,30,37,39,40,42,47,55,56,57,58,64,67,79,81,82,95,96,97,100,101,102,103,107,109,110,111,114,115,117,118,119,120,121,122,126,128,],[-16,-17,-18,-19,-20,-25,-57,-58,56,-44,-47,-48,-15,-15,97,-22,-12,-14,-15,-65,107,-47,-48,-64,-26,-21,-23,-24,-45,-50,-46,-49,-63,-61,-13,118,118,-62,-55,123,-52,-56,-53,-54,]),'COMA':([19,20,21,22,23,24,25,26,42,47,55,56,57,58,64,67,95,96,97,100,101,110,111,114,118,119,121,122,126,],[-16,-17,-18,-19,-20,-25,-57,-58,-15,-15,98,-22,-12,-14,-15,-65,-64,-26,-21,-23,-24,-63,-61,-13,-62,-55,124,-56,127,]),'RCORC':([19,20,21,22,23,24,25,26,42,56,62,64,65,66,67,95,96,97,100,101,110,111,118,],[-16,-17,-18,-19,-20,-25,-57,-58,-15,-22,99,-15,100,101,-65,-64,-26,-21,-23,-24,-63,-61,-62,]),'RANGE':([93,],[112,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bloque_codigo':([0,],[1,]),'empty':([0,3,27,],[2,28,53,]),'linea_codigo':([0,1,],[3,27,]),'expr_funcion':([0,1,12,14,15,18,29,30,31,32,35,38,51,71,72,84,91,108,113,116,124,127,],[4,4,33,40,40,49,54,58,60,67,69,82,67,40,40,67,67,67,67,67,67,67,]),'expr_def_funcion':([0,1,],[5,5,]),'expr_asign':([0,1,],[6,6,]),'expr_if_else':([0,1,],[7,7,]),'def_for':([0,1,],[8,8,]),'expr_return':([0,1,],[9,9,]),'call_method':([0,1,31,],[10,10,63,]),'variable':([0,1,14,15,17,18,30,31,32,38,51,71,72,83,84,91,98,108,113,116,124,127,],[13,13,39,39,46,48,57,59,65,81,95,39,39,109,95,95,114,95,95,119,119,119,]),'expr_str':([0,1,14,15,17,18,30,31,32,38,51,71,72,83,84,91,98,108,113,116,124,127,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'expr_float':([0,1,14,15,17,18,30,31,32,38,51,71,72,83,84,91,98,108,113,116,124,127,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'bool':([0,1,14,15,17,18,30,31,32,38,51,71,72,83,84,91,98,108,113,116,124,127,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'lista':([0,1,14,15,17,18,30,31,32,38,51,71,72,83,84,91,98,108,113,116,124,127,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'condiciones_expr_if_else':([14,15,38,71,],[36,44,79,102,]),'condiciones':([14,15,38,71,72,],[37,37,37,37,103,]),'operaciones_algebraica':([14,15,18,31,32,38,71,72,116,124,127,],[41,41,50,61,66,41,41,41,122,122,122,]),'p_variables_operaciones_algebraica':([14,15,18,31,32,38,51,71,72,84,91,108,113,116,124,127,],[43,43,43,43,43,80,94,43,43,110,111,115,117,43,43,43,]),'params':([30,],[55,]),'and_or':([37,],[71,]),'operador_igualdad':([37,41,103,],[72,83,72,]),'operador_alge':([41,43,50,61,66,80,94,122,],[84,91,84,84,84,108,113,84,]),'params_for':([116,],[120,]),'variable_for':([116,124,127,],[121,126,128,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> bloque_codigo","S'",1,None,None,None),
  ('bloque_codigo -> empty','bloque_codigo',1,'p_bloque_codigo','PythonPlag.py',97),
  ('bloque_codigo -> linea_codigo empty','bloque_codigo',2,'p_bloque_codigo','PythonPlag.py',98),
  ('bloque_codigo -> bloque_codigo linea_codigo empty','bloque_codigo',3,'p_bloque_codigo','PythonPlag.py',99),
  ('linea_codigo -> expr_funcion','linea_codigo',1,'p_linea_codigo','PythonPlag.py',103),
  ('linea_codigo -> expr_def_funcion','linea_codigo',1,'p_linea_codigo','PythonPlag.py',104),
  ('linea_codigo -> expr_asign','linea_codigo',1,'p_linea_codigo','PythonPlag.py',105),
  ('linea_codigo -> expr_if_else','linea_codigo',1,'p_linea_codigo','PythonPlag.py',106),
  ('linea_codigo -> def_for','linea_codigo',1,'p_linea_codigo','PythonPlag.py',107),
  ('linea_codigo -> expr_return','linea_codigo',1,'p_linea_codigo','PythonPlag.py',108),
  ('linea_codigo -> call_method','linea_codigo',1,'p_linea_codigo','PythonPlag.py',109),
  ('expr_def_funcion -> DEF expr_funcion DPUNTOS','expr_def_funcion',3,'p_expr_def_funcion','PythonPlag.py',114),
  ('params -> variable','params',1,'p_params','PythonPlag.py',118),
  ('params -> params COMA variable','params',3,'p_params','PythonPlag.py',119),
  ('params -> expr_funcion','params',1,'p_params','PythonPlag.py',120),
  ('variable -> ID','variable',1,'p_variable','PythonPlag.py',125),
  ('variable -> expr_str','variable',1,'p_variable','PythonPlag.py',126),
  ('variable -> NUMBER','variable',1,'p_variable','PythonPlag.py',127),
  ('variable -> expr_float','variable',1,'p_variable','PythonPlag.py',128),
  ('variable -> bool','variable',1,'p_variable','PythonPlag.py',129),
  ('variable -> lista','variable',1,'p_variable','PythonPlag.py',130),
  ('expr_funcion -> ID LPAREN params RPAREN','expr_funcion',4,'p_expr_funcion','PythonPlag.py',134),
  ('expr_funcion -> ID LPAREN RPAREN','expr_funcion',3,'p_expr_funcion','PythonPlag.py',135),
  ('lista -> ID LCORC variable RCORC','lista',4,'p_lista','PythonPlag.py',142),
  ('lista -> ID LCORC operaciones_algebraica RCORC','lista',4,'p_lista','PythonPlag.py',143),
  ('expr_str -> STRING','expr_str',1,'p_expr_str','PythonPlag.py',147),
  ('expr_float -> NUMBER PUNTO NUMBER','expr_float',3,'p_expr_float','PythonPlag.py',151),
  ('expr_asign -> ID EQUALS variable','expr_asign',3,'p_expr_asign','PythonPlag.py',157),
  ('expr_asign -> ID EQUALS expr_funcion','expr_asign',3,'p_expr_asign','PythonPlag.py',158),
  ('expr_asign -> ID EQUALS operaciones_algebraica','expr_asign',3,'p_expr_asign','PythonPlag.py',159),
  ('expr_asign -> ID EQUALS LCORC RCORC','expr_asign',4,'p_expr_asign','PythonPlag.py',160),
  ('expr_asign -> ID EQUALS call_method','expr_asign',3,'p_expr_asign','PythonPlag.py',161),
  ('operador_igualdad -> MAYOR','operador_igualdad',1,'p_operador_igualdad','PythonPlag.py',165),
  ('operador_igualdad -> MENOR','operador_igualdad',1,'p_operador_igualdad','PythonPlag.py',166),
  ('operador_igualdad -> DEQUALS','operador_igualdad',1,'p_operador_igualdad','PythonPlag.py',167),
  ('operador_igualdad -> MAYOR EQUALS','operador_igualdad',2,'p_operador_igualdad','PythonPlag.py',168),
  ('operador_igualdad -> MENOR EQUALS','operador_igualdad',2,'p_operador_igualdad','PythonPlag.py',169),
  ('operador_igualdad -> NEGADOR EQUALS','operador_igualdad',2,'p_operador_igualdad','PythonPlag.py',170),
  ('expr_return -> RETURN variable','expr_return',2,'p_expr_return','PythonPlag.py',174),
  ('expr_return -> RETURN expr_funcion','expr_return',2,'p_expr_return','PythonPlag.py',175),
  ('expr_return -> RETURN operaciones_algebraica','expr_return',2,'p_expr_return','PythonPlag.py',176),
  ('expr_if_else -> IF condiciones_expr_if_else DPUNTOS','expr_if_else',3,'p_expr_if_else','PythonPlag.py',180),
  ('expr_if_else -> ELIF condiciones_expr_if_else DPUNTOS','expr_if_else',3,'p_expr_if_else','PythonPlag.py',181),
  ('expr_if_else -> ELSE DPUNTOS','expr_if_else',2,'p_expr_if_else','PythonPlag.py',182),
  ('condiciones_expr_if_else -> condiciones','condiciones_expr_if_else',1,'p_codiciones_para_expr_if_else','PythonPlag.py',186),
  ('condiciones_expr_if_else -> condiciones and_or condiciones_expr_if_else','condiciones_expr_if_else',3,'p_codiciones_para_expr_if_else','PythonPlag.py',187),
  ('condiciones_expr_if_else -> LPAREN condiciones_expr_if_else RPAREN','condiciones_expr_if_else',3,'p_codiciones_para_expr_if_else','PythonPlag.py',188),
  ('condiciones -> variable','condiciones',1,'p_condiciones','PythonPlag.py',192),
  ('condiciones -> expr_funcion','condiciones',1,'p_condiciones','PythonPlag.py',193),
  ('condiciones -> operaciones_algebraica operador_igualdad variable','condiciones',3,'p_condiciones','PythonPlag.py',194),
  ('condiciones -> condiciones operador_igualdad condiciones','condiciones',3,'p_condiciones','PythonPlag.py',195),
  ('def_for -> FOR variable IN RANGE LPAREN params_for RPAREN DPUNTOS','def_for',8,'p_def_for','PythonPlag.py',199),
  ('params_for -> variable_for','params_for',1,'p_params_for','PythonPlag.py',203),
  ('params_for -> variable_for COMA variable_for','params_for',3,'p_params_for','PythonPlag.py',204),
  ('params_for -> variable_for COMA variable_for COMA variable_for','params_for',5,'p_params_for','PythonPlag.py',205),
  ('variable_for -> variable','variable_for',1,'p_variable_for','PythonPlag.py',208),
  ('variable_for -> operaciones_algebraica','variable_for',1,'p_variable_for','PythonPlag.py',209),
  ('bool -> TRUE','bool',1,'p_bool','PythonPlag.py',213),
  ('bool -> FALSE','bool',1,'p_bool','PythonPlag.py',214),
  ('and_or -> AND','and_or',1,'p_and_or','PythonPlag.py',218),
  ('and_or -> OR','and_or',1,'p_and_or','PythonPlag.py',219),
  ('operaciones_algebraica -> p_variables_operaciones_algebraica operador_alge p_variables_operaciones_algebraica','operaciones_algebraica',3,'p_operaciones_algebraica','PythonPlag.py',223),
  ('operaciones_algebraica -> LPAREN p_variables_operaciones_algebraica operador_alge p_variables_operaciones_algebraica RPAREN','operaciones_algebraica',5,'p_operaciones_algebraica','PythonPlag.py',224),
  ('operaciones_algebraica -> operaciones_algebraica operador_alge p_variables_operaciones_algebraica','operaciones_algebraica',3,'p_operaciones_algebraica','PythonPlag.py',225),
  ('p_variables_operaciones_algebraica -> variable','p_variables_operaciones_algebraica',1,'p_variables_operaciones_algebraica','PythonPlag.py',228),
  ('p_variables_operaciones_algebraica -> expr_funcion','p_variables_operaciones_algebraica',1,'p_variables_operaciones_algebraica','PythonPlag.py',229),
  ('operador_alge -> PLUS','operador_alge',1,'p_operador_alge','PythonPlag.py',233),
  ('operador_alge -> MINUS','operador_alge',1,'p_operador_alge','PythonPlag.py',234),
  ('operador_alge -> TIMES','operador_alge',1,'p_operador_alge','PythonPlag.py',235),
  ('operador_alge -> DIVIDE','operador_alge',1,'p_operador_alge','PythonPlag.py',236),
  ('operador_alge -> MOD','operador_alge',1,'p_operador_alge','PythonPlag.py',237),
  ('operador_alge -> EXP','operador_alge',1,'p_operador_alge','PythonPlag.py',238),
  ('call_method -> variable PUNTO expr_funcion','call_method',3,'p_call_method','PythonPlag.py',240),
  ('call_method -> call_method PUNTO expr_funcion','call_method',3,'p_call_method','PythonPlag.py',241),
  ('empty -> <empty>','empty',0,'p_empty','PythonPlag.py',244),
]
