OPCODES = {
    0x00: {
        "ins" : "brk",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 7
    },

    0x01: {
        "ins" : "ora",
        "addr_mode" : "ind_x",
        "len" : 2,
        "cycles" : 6
        
    },

    0x05: {
        "ins" : "ora",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0x06: {
        "ins" : "asl",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 5            
    },

    0x08: {
        "ins" : "php",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 3
    },

    0x09: {
        "ins" : "ora",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0x0A: {
        "ins" : "asl",
        "addr_mode" : "impl", #Implied with accumulator, A
        "len" : 1,
        "cycles" : 2
    },

    0x0D: {
        "ins" : "ora",
        "addr_mode" : "abs",
        "len" : 2,
        "cycles" : 4 
    },

    0x0E: {
        "ins" : "asl",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 6 
    },

    0x10 : {
        "ins" : "bpl",
        "addr_mode" : "rel",
        "len" : 2,
        "cycles" : 2 #Actually 2 + t + p, t = 1 if branch is taken, p = 1 if page is crossed
    },

    0x11 : {
        "ins" : "ora",
        "addr_mode" : "ind_y",
        "len" : 2,
        "cycles" : 5 #Actually 5 + p, p = 1 if page is crossed
    },

    0x15 : {
        "ins" : "ora",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0x16 : {
        "ins" : "asl",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 6
    },

    0x18 : {
        "ins" : "clc",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0x19 : {
        "ins" : "ora",    
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page is crossed
    },

    0x1D : {
        "ins" : "ora",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page is crossed
    },

    0x1E : {
        "ins" : "asl",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 7
    },

    0x20 : {
        "ins" : "jsr",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 6
    },

    0x21 : {
        "ins" : "and",
        "addr_mode" : "ind_x",
        "len" : 2,
        "cycles" : 6
    },

    0x24 : {
        "ins" : "bit",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0x25 : {
        "ins" : "and",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0x26 : {
        "ins" : "rol",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 5
    },

    0x28 : {
        "ins" : "plp",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 4
    },

    0x29 : {
        "ins" : "and",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0x2A : {
        "ins" : "rol",
        "addr_mode" : 'impl',
        "len" : 1,
        "cycles" : 2
    },

    0x2C : {
        "ins" : "bit",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4 
    },

    0x2D : {
        "ins" : "and",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0x2E : {
        "ins" : "rol",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 6
    },

    0x30 : {
        "ins" : "bmi",
        "addr_mode" : "rel",
        "len" : 2,
        "cycles" : 2 #Actually 2 + t + p, t = 1 if branch taken, p = 1 if page crossed
    },

    0x31 : {
        "ins" : "and",
        "addr_mode" : "ind_y",
        "len" : 2,
        "cycles" : 5 #Actually 5 + p, p = 1 if page crossed
    },

    0x35 : {
        "ins" : "and",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0x36 : {
        "ins" : "rol",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 6
    },

    0x38 : {
        "ins" : "sec",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0x39 : {
        "ins" : "and",
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0x3D : {
        "ins" : "and",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0x3E : {
        "ins" : "rol",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 7
    },

    0x40 : {
        "ins" : "rti",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 6
    },

    0x41 : {
        "ins" : "eor",
        "addr_mode" : "ind_x",
        "len" : 2,
        "cycles" : 6
    },

    0x45 : {
        "ins" : "eor",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0x46 : {
        "ins" : "lsr",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 5
    },

    0x48 : {
        "ins" : "pha",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 3
    },

    0x49 : {
        "ins" : "eor",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0x4A : {
        "ins" : "lsr",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },
    
    0x4C : {
        "ins" : "jmp",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 3
    },

    0x4D : {
        "ins" : "eor",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0x4E : {
        "ins" : "lsr",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 6
    },

    0x50 : {
        "ins" : "bvc",
        "addr_mode" : "rel",
        "len" : 2,
        "cycles" : 2 #Actually 2 + p + t, p = 1 if page crossed, t = 1 if branch taken
    },

    0x51 : {
        "ins" : "eor",
        "addr_mode" : "ind_y",
        "len" : 2,
        "cycles" : 5 #Actually 4 + p, p = 1 if page crossed 
    },

    0x55 : {
        "ins" : "eor",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0x56 : {
        "ins" : "lsr",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 6
    },

    0x58 : {
        "ins" : "cli",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0x59 : {
        "ins" : "eor",
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0x5D : {
        "ins" : "eor",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0x5E : {
        "ins" : "lsr",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 7
    },

    0x60 : {
        "ins" : "rts",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 6
    },

    0x61 : {
        "ins" : "adc",
        "addr_mode" : "ind_x",
        "len" : 2,
        "cycles" : 6
    },

    0x65 : {
        "ins" : "adc",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0x66 : {
        "ins" : "ror",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 5
    },

    0x68 : {
        "ins" : "pla",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 4
    },

    0x69 : {
        "ins" : "adc",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0x6A : {
        "ins" : "ror",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0x6C : {
        "ins" : "jmp",
        "addr_mode" : "ind",
        "len" : 3,
        "cycles" : 5
    },

    0x6D : {
        "ins" : "adc",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0x6E : {
        "ins" : "ror",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 6
    },

    0x70 : {
        "ins" : "bvs",
        "addr_mode" : "rel",
        "len" : 2,
        "cycles" : 2 #Actually 2 + t + p, t = 1 if branch taken, p = 1 if page crossed
    },

    0x71 : {
        "ins" : "adc",
        "addr_mode" : "ind_y",
        "len" : 2,
        "cycles" : 5 #Actually 5 + p, p = 1 if page is crossed
    },

    0x75 : {
        "ins" : "adc",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0x76 : {
        "ins" : "ror",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 6
    },

    0x78 : {
        "ins" : "sei",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0x79 : {
        "ins" : "adc",
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0x7D : {
        "ins" : "adc",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },
 
    0x7E : {
        "ins" : "ror",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 7
    },

    0x81 : {
        "ins" : "sta",
        "addr_mode" : "ind_x",
        "len" : 2,
        "cycles" : 6
    },

    0x84 : {
        "ins" : "sty",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0x85 : {
        "ins" : "sta",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0x86 : {
        "ins" : "stx",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0x88 : {
        "ins" : "dey",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0x8A : {
        "ins" : "txa",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2            
    },

    0x8C : {
        "ins" : "sty",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0x8D : {
        "ins" : "sta",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0x8E : {
        "ins" : "stx",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0x90 : {
        "ins" : "bcc",
        "addr_mode" : "rel",
        "len" : 2,
        "cycles" : 2 #Actually 2 + t + p, t = 1 if branch taken, p = 1 if page crossed
    },

    0x91 : {
        "ins" : "sta",
        "addr_mode" : "ind_y",
        "len" : 2,
        "cycles" : 6
    },

    0x94 : {
        "ins" : "sty",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0x95 : {
        "ins" : "sta",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0x96 : {
        "ins" : "stx",
        "addr_mode" : "zpg_y",
        "len" : 2,
        "cycles" : 4
    },

    0x98 : {
        "ins" : "tya",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0x99 : {
        "ins" : "sta",
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 5
    },

    0x9A : {
        "ins" : "txs",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0x9D : {
        "ins" : "sta",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 5
    },

    0xA0 : {
        "ins" : "ldy",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0xA1 : {
        "ins" : "lda",
        "addr_mode" : "ind_x",
        "len": 2,
        "cycles" : 6
    },

    0xA2 : {
        "ins" : "ldx",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0xA4 : {
        "ins" : "ldy",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0xA5 : {
        "ins" : "lda",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0xA6 : {
        "ins" : "ldx",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0xA8 : {
        "ins" : "tay",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0xA9 : {
        "ins" : "lda",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0xAA : {
        "ins" : "tax",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2    
    },

    0xAC : {
        "ins" : "ldy",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0xAD : {
        "ins" : "lda",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0xAE : {
        "ins" : "ldx",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0xB0 : {
        "ins" : "bcs",
        "addr_mode" : "rel",
        "len" : 2,
        "cycles" : 2 #Actually 2 + t + p, p = 1 if page crossed, t = 1 if branch taken
    },

    0xB1 : {
        "ins" : "lda",
        "addr_mode" : "ind_y",
        "len" : 2,
        "cycles" : 5 #Actually 5 + p , p = 1 if page crossed
    },

    0xB4 : {
        "ins" : "ldy",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0xB5 : {
        "ins" : "lda",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0xB6 : {
        "ins" : "ldx",
        "addr_mode" : "zpg_y",
        "len" : 2,
        "cycles" : 4
    },

    0xB8 : {
        "ins" : "clv",
        "addr_mode" : "impl",
        "len" : 1, 
        "cycles" : 2   
    },

    0xB9 : {
        "ins" : "lda",
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0xBA : {
        "ins" : "tsx",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0xBC : {
        "ins" : "ldy",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0xBD : {
        "ins" : "lda",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0xBE : {
        "ins" : "ldx",
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0xC0 : {
        "ins" : "cpy",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0xC1 : {
        "ins" : "cmp",
        "addr_mode" : "ind_x",
        "len" : 2,
        "cycles" : 6
    },

    0xC4 : {
        "ins" : "cpy",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0xC5 : {
        "ins" : "cmp",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0xC6 : {
        "ins" : "dec",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 5  
    },

    0xC8 : {
        "ins" : "iny",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0xC9 : {
        "ins" : "cmp",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0xCA : {
        "ins" : "dex",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0xCC : {
        "ins" : "cpy",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0xCD : {
        "ins" : "cmp",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0xCE : {
        "ins" : "dec",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 6
    },

    0xD0 : {
        "ins" : "bne",
        "addr_mode" : "rel",
        "len" : 2,
        "cycles" : 2 #Actually 2 + t + p, t = 1 if branch taken, p = 1 if page crossed
    },

    0xD1 : {
        "ins" : "cmp",
        "addr_mode" : "ind_y",
        "len" : 2,
        "cycles" : 5 #Actually 5 + p, p = 1 if page crossed
    },

    0xD5 : {
        "ins" : "cmp",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0xD6 : {
        "ins" : "dec",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 6
    },

    0xD8 : {
        "ins" : "cld",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0xD9 : {
        "ins" : "cmp",
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0xDD : {
        "ins" : "cmp",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0xDE : {
        "ins" : "dec",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 7
    },

    0xE0 : {
        "ins" : "cpx",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0xE1 : {
        "ins" : "sbc",
        "addr_mode" : "ind_x",
        "len" : 2,
        "cycles" : 6
    },

    0xE4 : {
        "ins" : "cpx",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3
    },

    0xE5 : {
        "ins" : "sbc",
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 3    
    },

    0xE6 : {
        "ins" : 'inc',
        "addr_mode" : "zpg",
        "len" : 2,
        "cycles" : 5
    },

    0xE8 : {
        "ins" : "inx",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0xE9 : {
        "ins" : "sbc",
        "addr_mode" : "imd",
        "len" : 2,
        "cycles" : 2
    },

    0xEA : {
        "ins" : "nop",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0xEC : {
        "ins" : "cpx",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0xED : {
        "ins" : "sbc",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 4
    },

    0xEE : {
        "ins" : "inc",
        "addr_mode" : "abs",
        "len" : 3,
        "cycles" : 6
    },

    0xF0 : {
        "ins" : "beq",
        "addr_mode" : "rel",
        "len" : 2,
        "cycles" : 2 #Actually 2 + t + p, t = 1 if branch taken, p = 1 if page crossed
    },

    0xF1 : {
        "ins" : "sbc",
        "addr_mode" : "ind_y",
        "len" : 2,
        "cycles" : 5 #Actually 5 + p, p = 1 if page crossed
    },

    0xF5 : {
        "ins" : "sbc",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 4
    },

    0xF6 : {
        "ins" : "inc",
        "addr_mode" : "zpg_x",
        "len" : 2,
        "cycles" : 6
    },

    0xF8 : {
        "ins" : "sed",
        "addr_mode" : "impl",
        "len" : 1,
        "cycles" : 2
    },

    0xF9 : {
        "ins" : "sbc",
        "addr_mode" : "abs_y",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0xFD : {
        "ins" : "sbc",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 4 #Actually 4 + p, p = 1 if page crossed
    },

    0xFE : {
        "ins" : "inc",
        "addr_mode" : "abs_x",
        "len" : 3,
        "cycles" : 7    
    }

}