mem = {}

def instr_set(line, instr):
  _mem = line.split(" ")[1]
  value = line.split(" ")[2]

  if value[0] == '"':
    value = line[len(f"{instr} {_mem} "):][1:]
    _value = value[:len(value) - 1]
  else:
    _value = int(value)

  mem[_mem] = _value

def instr_jmp(line):
  _func = line.split(" ")[1]
  execute(funcs, _func)

def instr_debugmem():
  print(mem)

def instr_kp():
  print("NVASM: your program ended")
  quit

def instr_prnt(line):
  print(mem[line.split(" ")[1]])

def instr_add(line):
  mem[line.split(" ")[1]] = int(mem[line.split(" ")[2]]) + int(mem[line.split(" ")[3]])

def execute(funcs:dict={}, func:str=""):
  for line in funcs[func]:
    instr = line.split(" ")[0]

    if instr == "SET":
      instr_set(line, instr)
    if instr == "JMP":
      instr_jmp(line)
    if instr == "DEBUGMEM":
      instr_debugmem()
    if instr == "KP":
      instr_kp()
    if instr == "PRNT":
      instr_prnt(line)
    if instr == "ADD":
      instr_add(line)

with open("test.asm", "r") as file:
  code = file.read()

  lines = code.split("\n")

  last = ""
  funcs = {}

  for line in lines:
    lex = line.split(" ")

    if lex[0] == "func":
      funcs[lex[1]] = []
      last = lex[1]
    elif line != '':
      funcs[last].append(line)

  execute(funcs, "main")