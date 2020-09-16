

def karkat(text: str) -> str:
    return(text.upper())

def Kanaya(text: str) -> str:
    out_val = f"{text[0].upper()}"
    for i in range(1, len(text)):
        if text[i-1] == " ":
            out_val = f"{out_val}{text[i].upper()}"
        else:
            out_val = f"{out_val}{text[i].lower()}"
    return(out_val)

def tavros(text: str) -> str:
    out_val = f"{text[0].lower()}{text[1].upper()}"
    for i in range(2, len(text)):
        if text[i-2:i] == ". " or text[i-2:i] == ", ":
            out_val = f"{out_val}{text[i].lower()}"
        else:
            out_val = f"{out_val}{text[i].upper()}"
    return(out_val)

def terezi(text: str) -> str:
    out_val = ""
    for i in text.upper():
        if i == "I":
            out_val = f"{out_val}1"
        elif i == "E":
            out_val = f"{out_val}3"
        elif i == "A":
            out_val = f"{out_val}4"
        else:
            out_val = f"{out_val}{i}"
    return(out_val)

def pyrope(text: str) -> str:  #A remaster of Terezi, using different logic
    text = text.upper()
    text = text.replace("A", "4")
    text = text.replace("E", "3")
    text = text.replace("I", "1")
    return text


def caliope(text: str) -> str:
    out_val = ""
    for i in text.lower():
        if i == "u":
            out_val = f"{out_val}U"
        else:
            out_val = f"{out_val}{i}"
    return(out_val)

def caliborn(text: str) -> str:
    out_val = ""
    for i in text.upper():
        if i == "U":
            out_val = f"{out_val}u"
        else:
            out_val = f"{out_val}{i}"
    return(out_val)


def xeno(text: str) -> str:
    out_val = ""
    for x in text:
        if x == "i":
            out_val = f"{out_val}I"
        else:
            out_val = f"{out_val}{x}"
    return(out_val)

def pre_format(text: str) -> str:
    removals = "1 2 3 4 5 6 7 8 9 0 , .  \" ? ' £ $ % & * ( ) -".split(" ")
    for i in removals:
        if i in text:
            text = text.replace(i, "")
    return text

def lt(text: str) -> str:
    inval = pre_format(text).split(" ")
    outval = ""
    for i in inval:
        if 0 < len(i) <= 3:
            outval += i[0].lower()
        elif len(i) <= 4:
            outval += i[0].upper()
    return outval.strip()


def meme_text(text: str) -> str:
    out_val = ""
    for i in text:
        out_val = f"{out_val}{i.upper()} "
    return(out_val.strip())

print(meme_text("test? test!"))

print(lt("This is a Test String"))  #TiaTS
print(lt("isn't it?"))
print(lt("I'm not Sure."))

print(pyrope("This is a test, dumbass"))