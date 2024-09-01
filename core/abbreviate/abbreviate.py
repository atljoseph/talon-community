import re

from talon import Context, Module

from ..user_settings import track_csv_list

mod = Module()
ctx = Context()
mod.list("abbreviation", desc="Common abbreviation")

abbreviations_list = {}
abbreviations = {
    "J peg": "jpg",
    "abbreviate": "abbr",
    "abort": "abrt",
    "acknowledge": "ack",
    "address": "addr",
    "addresses": "addrs",
    "administrator": "admin",
    "administrators": "admins",
    "advance": "adv",
    "advanced": "adv",
    "alberta": "ab",
    "allocate": "alloc",
    "alternative": "alt",
    "apple": "appl",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "as far as i can tell": "afaict",
    "as far as i know": "afaik",
    "assembly": "asm",
    "asynchronous": "async",
    "at the moment": "atm",
    "attribute": "attr",
    "attributes": "attrs",
    "authenticate": "auth",
    "authentication": "authn",
    "authorization": "authz",
    "auto group": "augroup",
    "average": "avg",
    "away from keyboard": "afk",
    "backup": "bkp",
    "be right back": "brb",
    "binary": "bin",
    "block": "blk",
    "boolean": "bool",
    "bottom": "bot",
    "break point": "bp",
    "break points": "bps",
    "british columbia": "bc",
    "buffer": "buf",
    "button": "btn",
    "by the way": "btw",
    "calculate": "calc",
    "calculator": "calc",
    "camera": "cam",
    "canada": "ca",
    "centimeter": "cm",
    "char": "chr",
    "character": "char",
    "check": "chk",
    "child": "chld",
    "china": "cn",
    "class": "cls",
    "client": "cli",
    "column": "col",
    "command": "cmd",
    "commands": "cmds",
    "comment": "cmt",
    "communication": "comm",
    "communications": "comms",
    "compare": "cmp",
    "condition": "cond",
    "conference": "conf",
    "config": "cfg",
    "configuration": "config",
    "configurations": "configs",
    "connection": "conn",
    "constant": "const",
    "contribute": "contrib",
    "constructor": "ctor",
    "context": "ctx",
    "control flow graph": "cfg",
    "control": "ctrl",
    "coordinate": "coord",
    "coordinates": "coords",
    "copy": "cpy",
    "count": "cnt",
    "counter": "ctr",
    "credential": "cred",
    "credentials": "creds",
    "cross reference": "xref",
    "cross references": "xrefs",
    "cuddle": "ctl",
    "current": "cur",
    "cute": "qt",
    "database": "db",
    "date format": "yyyy-mm-dd",
    "debian": "deb",
    "debug": "dbg",
    "decimal": "dec",
    "declaration": "decl",
    "declare": "decl",
    "decode": "dec",
    "decrement": "dec",
    "define": "def",
    "definition": "def",
    "degree": "deg",
    "delete": "del",
    "depend": "dep",
    "depends": "deps",
    "description": "desc",
    "dest": "dst",
    "destination": "dest",
    "develop": "dev",
    "development": "dev",
    "device": "dev",
    "diagnostic": "diag",
    "dictation": "dict",
    "dictionary": "dict",
    "direction": "dir",
    "directories": "dirs",
    "directory": "dir",
    "display": "disp",
    "distance": "dist",
    "distribution": "dist",
    "document": "doc",
    "documents": "docs",
    "doing": "ing",  # some way to add 'ing' to verbs
    "double ended queue": "deque",
    "double": "dbl",
    "dupe": "dup",
    "duplicate": "dup",
    "dynamic": "dyn",
    "elastic": "elast",
    "element": "elem",
    "elements": "elems",
    "encode": "enc",
    "end of day": "eod",
    "end of month": "eom",
    "end of quarter": "eoq",
    "end of week": "eow",
    "end of year": "eoy",
    "entry": "ent",
    "enumerate": "enum",
    "environment": "env",
    "error": "err",
    "escape": "esc",
    "etcetera": "etc",
    "ethernet": "eth",
    "evaluate": "eval",
    "example": "ex",
    "exception": "exc",
    "executable": "exe",
    "executables": "exes",
    "execute": "exec",
    "experience": "exp",
    "exponent": "exp",
    "expression": "expr",
    "expressions": "exprs",
    "extend": "ext",
    "extension": "ext",
    "external": "extern",
    "eye dent": "id",
    "eye octal": "ioctl",
    "eye three": "i3",
    "feature": "feat",
    "file system": "fs",
    "fingerprint": "fp",
    "for what": "fwiw",
    "format": "fmt",
    "fortigate": "fgt",
    "framework": "fw",
    "frequency": "freq",
    "function": "func",
    "functions": "funcs",
    "funny": "lol",
    "fuzzy": "fzy",
    "generate": "gen",
    "generic": "gen",
    "hardware": "hw",
    "header": "hdr",
    "hello": "helo",
    "history": "hist",
    "hypertext": "http",
    "identity": "id",
    "ignore": "ign",
    "image": "img",
    "implement": "impl",
    "import address table": "iat",
    "import table": "iat",
    "in real life": "irl",
    "increment": "inc",
    "index": "idx",
    "information": "info",
    "infrastructure": "infra",
    "initialize": "init",
    "initializer": "init",
    "inode": "ino",
    "insert": "ins",
    "instance": "inst",
    "instruction": "insn",
    "integer": "int",
    "interpreter": "interp",
    "interrupt": "int",
    "iterate": "iter",
    "jason": "json",
    "jason five": "json5",
    "java archive": "jar",
    "javascript": "js",
    "jiff": "gif",
    "journal cuttle": "journalctl",
    "jump": "jmp",
    "just in time": "jit",
    "kay": "kk",
    "kernel": "krnl",
    "key cuttle": "keyctl",
    "keyboard": "kbd",
    "keyword arguments": "kwargs",
    "keyword": "kw",
    "kilogram": "kg",
    "kilometer": "km",
    "language": "lang",
    "laugh out loud": "lol",
    "length": "len",
    "lib see": "libc",
    "library": "lib",
    "lisp": "lsp",
    "looks good to me": "lgtm",
    "mail": "smtp",
    "make": "mk",
    "management": "mgmt",
    "manager": "mgr",
    "manitoba": "mb",
    "markdown": "md",
    "maximum": "max",
    "memory": "mem",
    "message": "msg",
    "meta sploit framework": "msf",
    "meta sploit": "msf",
    "microphone": "mic",
    "middle": "mid",
    "milligram": "mg",
    "millisecond": "ms",
    "minimum viable product": "mvp",
    "minimum": "min",
    "miscellaneous": "misc",
    "modify": "mod",
    "module": "mod",
    "modules": "mods",
    "monitor": "mon",
    "mount": "mnt",
    "multiple": "multi",
    "muscle": "musl",
    "mutate": "mut",
    "nano second": "ns",
    "neo vim": "nvim",
    "new brunswick": "nb",
    "nova scotia": "ns",
    "number": "num",
    "numbers": "nums",
    "object": "obj",
    "objects": "objs",
    "offset": "off",
    "offsets": "offs",
    "okay": "ok",
    "ontario": "on",
    "operating system": "os",
    "operation": "op",
    "operations": "ops",
    "option": "opt",
    "options": "opts",
    "original": "orig",
    "out of bounds": "oob",
    "package build": "pkgbuild",
    "package": "pkg",
    "packages": "pkgs",
    "packet": "pkt",
    "packets": "pkts",
    "parameter": "param",
    "parameters": "params",
    "password": "passwd",
    "performance": "perf",
    "physical": "phys",
    "physical address": "paddr",
    "pick": "pic",
    "pico second": "ps",
    "pie": "py",
    "ping": "png",
    "pixel": "px",
    "point": "pt",
    "pointer": "ptr",
    "pointers": "ptrs",
    "pone": "pwn",
    "position independent code": "pic",
    "position independent executable": "pie",
    "position": "pos",
    "pound bag": "pwndbg",
    "preference": "pref",
    "preferences": "prefs",
    "previous": "prev",
    "private": "priv",
    "process": "proc",
    "processor": "cpu",
    "production": "prod",
    "program": "prog",
    "programs": "progs",
    "properties": "props",
    "property": "prop",
    "protocol": "proto",
    "protocol buffers": "protobuf",
    "public": "pub",
    "python": "py",
    "quebec": "qc",
    "query string": "qs",
    "radian": "rad",
    "random": "rand",
    "read right ex": "rwx",
    "receipt": "rcpt",
    "receive": "recv",
    "record": "rec",
    "recording": "rec",
    "rectangle": "rect",
    "ref count": "refcnt",
    "reference": "ref",
    "references": "refs",
    "register": "reg",
    "registers": "regs",
    "registery": "reg",
    "regular expression": "regex",
    "regular expressions": "regex",
    "remove": "rm",
    "repel": "repl",
    "repetitive strain injury": "rsi",
    "repository": "repo",
    "represent": "repr",
    "representation": "repr",
    "request": "req",
    "requests": "reqs",
    "resources": "rsrcs",
    "response": "resp",
    "result": "res",
    "return": "ret",
    "revision": "rev",
    "round": "rnd",
    "ruby": "rb",
    "rust": "rs",
    "samba D": "smbd",
    "samba": "smb",
    "saskatchewan": "sk",
    "schedule": "sched",
    "scheduler": "sched",
    "screen": "scr",
    "scuzzy": "scsi",
    "see": "C",
    "segment": "seg",
    "select": "sel",
    "semaphore": "sem",
    "send": "snd",
    "sequel": "sql",
    "sequence": "seq",
    "service pack": "sp",
    "session id": "sid",
    "shell": "sh",
    "shellcode": "sc",
    "signal": "sig",
    "size": "sz",
    "snipped": "[...]",
    "some": "sum",
    "source": "src",
    "sources": "srcs",
    "special": "spec",
    "specific": "spec",
    "specification": "spec",
    "specify": "spec",
    "standard error": "stderr",
    "standard in": "stdin",
    "standard out": "stdout",
    "standard": "std",
    "start of day": "sod",
    "start of month": "som",
    "start of quarter": "soq",
    "start of week": "sow",
    "start of year": "soy",
    "statement": "stmt",
    "statistic": "stat",
    "statistics": "stats",
    "string": "str",
    "structure": "struct",
    "structures": "structs",
    "symbol": "sym",
    "symbolic link": "symlink",
    "symbols": "syms",
    "synchronize": "sync",
    "synchronous": "sync",
    "sys cuttle": "sysctl",
    "system call": "syscall",
    "system cuddle": "systemctl",
    "system": "sys",
    "table of contents": "toc",
    "table": "tbl",
    "taiwan": "tw",
    "talk": "toc",
    "technology": "tech",
    "temp": "tmp",
    "temperature": "temp",
    "temporary": "tmp",
    "terminal": "term",
    "text": "txt",
    "time format": "hh:mm:ss",
    "time of check time of use": "toctou",
    "time to live": "ttl",
    "token": "tok",
    "transaction": "txn",
    "typescript": "ts",
    "ultimate": "ulti",
    "unique id": "uuid",
    "unknown": "unk",
    "user id": "uid",
    "user": "usr",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "values": "vals",
    "variable": "var",
    "variables": "vars",
    "vector": "vec",
    "verify": "vrfy",
    "version": "ver",
    "versus": "vs",
    "video": "vid",
    "videos": "vids",
    "virtual machine": "vm",
    "virtual": "virt",
    "virtual address": "vaddr",
    "visual studio": "msvc",
    "visual": "vis",
    "volume": "vol",
    "vulnerable": "vuln",
    "wave": "wav",
    "web": "www",
    "what the fuck": "wtf",
    "wind": "wnd",
    "window": "win",
    "windows kernel": "ntoskrnl",
    "work in progress": "wip",
}

@mod.capture(rule="brief {user.abbreviation}")
def abbreviated(m) -> str:
    """A reverse abbreviation inside another command"""
    return m.abbreviation

@track_csv_list("abbreviations.csv", headers=("Abbreviation", "Spoken Form"), default=abbreviations)
def on_abbreviations(values):
    global abbreviations_list
	
    # Matches letters and spaces, as currently, Talon doesn't accept other characters in spoken forms.
    PATTERN = re.compile(r"^[a-zA-Z ]+$")
    abbreviation_values = {
        v: v for v in values.values() if PATTERN.match(v) is not None
    }

    # Allows the abbreviated/short form to be used as spoken phrase. eg "brief app" -> app
    abbreviations_list_with_values = {
        **{v: v for v in abbreviation_values.values()},
        **abbreviations_list,
    }

    ctx.lists["user.abbreviation"] = abbreviations_list_with_values
	
	# abbreviations_list is also imported by the create_spoken_forms module
    abbreviations_list = abbreviations_list_with_values
    ctx.lists["user.abbreviation"] = abbreviations_list_with_values
