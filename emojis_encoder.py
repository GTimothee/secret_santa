emoji_alphabet = {
    'A': '🦅',  
    'B': '🍌',  
    'C': '🐈',  
    'D': '🐬',  
    'E': '🐘',  
    'F': '🦩', 
    'G': '🦒',  
    'H': '🚁',  
    'I': '🏝️', 
    'J': '💛',  
    'K': '🦘',  
    'L': '🦁',  
    'M': '🥭', 
    'N': '✈️', 
    'O': '🐦', 
    'P': '🐧', 
    'Q': '🥐',  
    'R': '🍇',  
    'S': '🐍', 
    'T': '🐅',  
    'U': '🍉',  
    'V': '🚗',  
    'W': '🚃',  
    'X': '🙅',  
    'Y': '⛵',  
    'Z': '🦓'   
}


class EmojiEncoder:

    @staticmethod
    def encode_name(name):
        name = name.strip()
        return [emoji_alphabet[c.upper()] for c in name]