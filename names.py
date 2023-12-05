

def get_names(participants_filepath: str) -> list:
    with open(participants_filepath, 'r') as f:
        lines = f.readlines() 
    return [line.strip().lower() for line in lines]