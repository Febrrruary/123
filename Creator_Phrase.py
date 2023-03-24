import uuid
from hashlib import sha256

with open('/Users/ivan/Desktop/words.rtf', 'r') as file:
    words = [word.strip().lower() for word in file.readlines()]

while True:
    uuid_num = uuid.uuid4().int
    sha256_hash = sha256(uuid_num.to_bytes(16, 'big')).digest()
    word_indexes = []
    for i in range(12):
        index = sha256_hash[i] % len(words)
        word_indexes.append(index)

    mnemonic_phrase = ' '.join([words[index] for index in word_indexes])

    with open('/Users/ivan/Desktop/Seed/mnemonic.txt', 'a') as file:
        file.write(mnemonic_phrase.replace('\\', '') + '\n')
