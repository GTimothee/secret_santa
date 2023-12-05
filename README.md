# Secret Santa 🎅🎁🎄

This project allows you to turn the painful task of assigning people for a secret santa into a fun game !

The main script, ```generate.py```, accepts a txt file as input, containing the names of the participants.
It then first generates a matching, and then encode each name using Cesar cipher (https://en.wikipedia.org/wiki/Caesar_cipher).
That way, you can share the list to your family, and ask everyone to decode the name of the person assigned to them.
To decode a name, you need the value you used for the encoding, e.g. 3, and shift each letter backwards by the value used for encoding.

For example: 
- the name to encode is john
- the value used is 3
- encoding works as follows:
    - j shifted by 3 letters gives m 
    - o -> r
    - h -> k
    - n -> q
- the final encoded name is mrkq
- do the reverse for decoding

What if the names have different lengths ? Then even with the encoding it is easy to guess the assignment.
Therefore, we also add some padding with random characters at the end of the shorter names so that all encoded names have the same length.

Example usage:
```bash
$ python generate.py -p participants.txt -v 3
{'john': 0, 'joe': 1}

Found a solution:
john -> joe
joe -> john

Encoding result...

Result:
john -> mrhf
joe -> mrkq
```

Script arguments:
```bash
$ python generate.py --help
usage: generate.py [-h] -p PARTICIPANTS

options:
  -h, --help            show this help message and exit
  -p PARTICIPANTS, --participants PARTICIPANTS
```

Tested with Python3.11 but should work with any Python3 version.

## Project description

Files
- name_encoder.py contains NameEncoder, the object responsible of encoding names
- generate.py is the main entrypoint

## Tests

```pip install pytest ```

```pytest test_name_encoder.py```