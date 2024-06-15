class String(str):

    def __init__(self, word):
        self.word = word
        self.rules = []

    def count(self, value, start, end):
        return self.word.count(value, start, end)

    def islower(self):
        return self.word.islower()

    def isupper(self):
        return self.word.isupper()

    def __add__(self, other):
        if type(other) == type(self):
            answer = self.word + other.word
        else:
            answer = self.word + other
        return String(answer)

    def __mul__(self, number):
        return String(super().__mul__(number))

    def __len__(self):
        return len(self.word)

    def __eq__(self, other):
        if isinstance(other, String):
            return self.word == other.word
        return self.word == other

    def __iter__(self):
        self.iteration = 0
        return self

    def __str__(self):
        return self.word

    def __next__(self):
        if self.iteration < len(self.word):
            char = self.word[self.iteration]
            self.iteration += 1
            return String(char)
        else:
            raise StopIteration

    def __radd__(self, other):
        val = str(other) + str(self)
        return String(val)

    def __getitem__(self, item):
        return String(super().__getitem__(item))

    def __setslice__(self, i, j, sequence):
        return String(self.word[i, j, sequence])

    def get8_bit_binary(self):  # convert string to ascii and then convert to  8 bit binary
        return ''.join(format(ord(char), '08b') for char in self.word)

    def base64(self) -> 'String':
        '''
        Encode the String (self) to a base64 string
        :return: a new instance of String with the encoded string.
        '''

        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U",
                    "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                    "p",
                    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "+",
                    "/"]
        binary_str = self.get8_bit_binary()
        six_bit_pieces = []
        index = 0
        base64_word = ""
        while index < len(binary_str):
            six_bit_pieces.append(binary_str[index:index + 6])
            index += 6

        for item in six_bit_pieces:
            if len(item) < 6:
                item = item + (6 - len(item)) * "0"
            base64_word += alphabet[int(item, 2)]

        return String(base64_word)

    def choose_group(self) -> int:
        # return priority group
        appearance_list = []
        for char in self.word:
            ascii_value = ord(char)
            if 33 <= ascii_value <= 47 or 58 <= ascii_value <= 64 or 91 <= ascii_value <= 96 or 124 <= ascii_value <= 126:
                number = 1
            if 48 <= ascii_value <= 57:
                number = 2
            if 65 <= ascii_value <= 90:
                number = 3
            if 97 <= ascii_value <= 122:
                number = 4
            appearance_list.append(number)

        priority_choose = 1
        other_repeat = appearance_list.count(1)
        digits_repeat = appearance_list.count(2)
        upper_case_repeat = appearance_list.count(3)
        lower_case_repeat = appearance_list.count(4)

        if other_repeat == 0:
            return priority_choose
        if digits_repeat == 0:
            priority_choose = 2
            return priority_choose
        if upper_case_repeat == 0:
            priority_choose = 3
            return priority_choose
        if lower_case_repeat == 0:
            priority_choose = 4
            return priority_choose
        raise BytePairError

    def build_pair_list(self, word) -> list:
        # build a list with all the pairs
        pair_list = []
        for index in range(len(word)):
            # Build pair list
            if index + 3 < len(word):
                if word[index] == word[index + 1] == word[index + 2]:
                    if word[index] == word[index + 1] == word[index + 2] == word[index + 3]:
                        pass
                    else:
                        continue
            if index + 1 < len(word):
                pair = word[index] + word[index + 1]
                pair_list.append(pair)
        return pair_list

    def build_dict(self, word):
        pair_dict = {}
        pair_list = self.build_pair_list(word)
        for pair in pair_list:
            count_appearance = pair_list.count(pair)
            pair_dict[pair] = count_appearance

        list_sorted = sorted(pair_dict, key=pair_dict.get, reverse=True)
        dict_result = {}
        for pair in list_sorted:
            dict_result[pair] = pair_dict[pair]

        return dict_result

    def update_dict(self, pair_dict, decimal_value, word):
        # Update the list to group 2, 3 or 4
        rules = []
        while max(pair_dict.values()) > 1:
            maximum_appearance_str = max(pair_dict, key=pair_dict.get)
            rule_str = chr(decimal_value) + " = " + maximum_appearance_str
            rules.append(rule_str)
            word = word.replace(maximum_appearance_str, chr(decimal_value))
            pair_dict = self.build_dict(word)
            decimal_value += 1

        return word, rules

    def replace_pair(self, group_number: int, pair_dict: dict):
        word = self.word
        rules = []
        if group_number == 1:
            decimal_value = 33
            while max(pair_dict.values()) > 1:
                maximum_appearance_str = max(pair_dict, key=pair_dict.get)
                rule_str = chr(decimal_value) + " = " + maximum_appearance_str
                rules.append(rule_str)
                word = word.replace(maximum_appearance_str, chr(decimal_value))
                pair_dict = self.build_dict(word)
                decimal_value += 1

                if decimal_value == 48:
                    decimal_value = 58
                if decimal_value == 65:
                    decimal_value = 91
                if decimal_value == 97:
                    decimal_value = 124

        if group_number == 2:
            decimal_value = 48
            word, rules = self.update_dict(pair_dict, decimal_value, word)

        if group_number == 3:
            decimal_value = 65
            word, rules = self.update_dict(pair_dict, decimal_value, word)

        if group_number == 4:
            decimal_value = 97
            word, rules = self.update_dict(pair_dict, decimal_value, word)

        return word, rules

    def byte_pair_encoding(self) -> 'String':
        '''
        Encode the String (self) to a byte pair string
        :return: a new instance of String with the encoded string.
        :exception: BytePairError
        '''

        group_number = self.choose_group()
        pair_dict = self.build_dict(self.word)
        word, rules = self.replace_pair(group_number, pair_dict)
        encoding_string = String(word)
        encoding_string.rules = rules
        return encoding_string

    def cyclic_bits(self, num: int) -> 'String':
        '''
        Encode the String (self) to a cyclic bits string
        :return: a new instance of String with the encoded string.
        '''
        if num >= 0:
            binary_word = self.get8_bit_binary()
            # Build list of binary digits word
            binary_list = self.convert_string_to_list(binary_word)

            for i in range(num):
                # Cyclic the bits in the list
                backup_char = binary_list[0]
                binary_list.pop(0)
                binary_list.append(backup_char)

            shifted_str = self.convert_list_to_string(binary_list)
            eight_bit_list = self.build_8bit_list(shifted_str)
            shifted_str = self.binary_8_bit_list_to_string(eight_bit_list)

        else:
            shifted_str = self.decode_cyclic_bits(abs(num))

        return String(shifted_str)

    def cyclic_chars(self, num: int) -> 'String':
        '''
        Encode the String (self) to a cyclic chars string
        :return: a new instance of String with the encoded string.
        :exception: CyclicCharsError
        '''
        if num >= 0:
            last_location = 126
            first_location = 32
            shifted_lst = []
            for char in self.word:
                ascii_value = ord(char)
                if ascii_value > last_location or ascii_value < first_location:
                    raise CyclicCharsError
                increase_value = ascii_value + num
                if increase_value <= last_location:
                    shifted_lst.append(increase_value)
                else:
                    extra = (increase_value - last_location - 1) % (last_location + 1 - first_location)
                    shifted_lst.append(first_location + extra)

            shifted_str = ""
            for item in shifted_lst:
                shifted_str += chr(item)
        else:
            shifted_str = self.decode_cyclic_chars(abs(num))

        return String(shifted_str)

    def histogram_of_chars(self) -> dict:
        '''
        calculate the histogram of the String (self). The bins are
        "control code", "digits", "upper", "lower" , "other printable"
        and "higher than 128".
        :return: a dictonery of the histogram. keys are bins.
        '''
        count_control_code = 0
        count_digits = 0
        count_upper = 0
        count_lower = 0
        count_other_printable = 0
        count_higher_than128 = 0
        for char in self.word:
            ascii_value = ord(char)
            if 128 <= ascii_value:
                count_higher_than128 += 1
            if 48 <= ascii_value <= 57:
                count_digits += 1
            if 65 <= ascii_value <= 90:
                count_upper += 1
            if 97 <= ascii_value <= 122:
                count_lower += 1
            if 0 <= ascii_value <= 31 or ascii_value == 127:
                count_control_code += 1
            if 32 <= ascii_value <= 47 or 58 <= ascii_value <= 64 or 91 <= ascii_value <= 96 or 123 <= ascii_value <= 126:
                count_other_printable += 1

        bin_dict = {"control code": count_control_code, "digits": count_digits, "upper": count_upper,
                    "lower": count_lower, "other printable:": count_other_printable,
                    "higher than 128": count_higher_than128}
        return bin_dict

    def build_8bit_list(self, binary_str) -> list:
        eight_bit_pieces = []
        index = 0
        while index < len(binary_str):
            eight_bit_pieces.append(binary_str[index:index + 8])
            index += 8

        return eight_bit_pieces

    def convert_list_to_string(self, list) -> str:
        word = ""
        for item in list:
            word += item

        return word

    def binary_8_bit_list_to_string(self, binary_list) -> str:
        decode_word = ""
        for item in binary_list:
            if len(item) < 8:
                item = item + (8 - len(item)) * "0"
            ascii_value = (int(item, 2))
            if ascii_value == 0:
                continue
            if ascii_value < 32 or ascii_value > 126:
                raise Base64DecodeError
            decode_word += chr(ascii_value)

        return decode_word

    def convert_string_to_list(self, value) -> list:
        lst = []
        for char in value:
            lst.append(char)
        return lst

    @property
    def decode_base64(self) -> 'String':
        '''
        Decode the String (self) to its original base64 string.
        :return: a new instance of String with the endecoded string.
        :exception: Base64DecodeError
        '''
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U",
                    "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                    "p",
                    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "+",
                    "/"]
        binary_str = ""
        for letter in self.word:
            index_letter = alphabet.index(letter)
            bin_letter = bin(index_letter).lstrip("0b")
            if len(bin_letter) < 6:
                bin_letter = (6 - len(bin_letter)) * "0" + bin_letter
            binary_str += bin_letter

        eight_bit_pieces = self.build_8bit_list(binary_str)

        decode_word = self.binary_8_bit_list_to_string(eight_bit_pieces)
        return String(decode_word)

    def decode_byte_pair(self) -> 'String':
        '''
        Decode the String (self) to its original byte pair string.
        Uses the property rules.
        :return: a new instance of String with the endecoded string.
        :exception: BytePairDecodeError
        '''
        decode_word = self.word
        if not self.rules:
            raise BytePairDecodeError
        reverse_rules = self.rules[::-1]
        for rule in reverse_rules:
            char_to_change = rule[0]
            decode_pair = rule[4:]
            decode_word = decode_word.replace(char_to_change, decode_pair)

        return decode_word

    def decode_cyclic_bits(self, num: int) -> 'String':
        '''
        Decode the String (self) to its original cyclic bits string.
        :return: a new instance of String with the endecoded string.
        '''
        if num >= 0:
            binary_word = self.get8_bit_binary()
            # Build list of binary digits word
            binary_list = self.convert_string_to_list(binary_word)
            last_index = len(binary_list) - 1

            for i in range(num):
                # Cyclic the bits in the list
                backup_char = binary_list[last_index]
                binary_list.pop(last_index)
                binary_list.insert(0, backup_char)

            shifted_str = self.convert_list_to_string(binary_list)
            eight_bit_list = self.build_8bit_list(shifted_str)
            shifted_str = self.binary_8_bit_list_to_string(eight_bit_list)

        else:
            shifted_str = self.cyclic_bits(abs(num))

        return String(shifted_str)

    def decode_cyclic_chars(self, num: int) -> 'String':
        '''
        Decode the String (self) to its original cyclic chars string.
        :return: a new instance of String with the endecoded string.
        :exception: CyclicCharsDecodeError
        '''
        if num >= 0:
            shifted_lst = []
            last_location = 126
            first_location = 32
            for item in self.word:
                ascii_value = ord(item)
                if ascii_value > last_location or ascii_value < first_location:
                    raise CyclicCharsDecodeError
                shifted_value = ascii_value - num
                if shifted_value < first_location - last_location:
                    shifted_value = shifted_value % (last_location - first_location) + 1
                if first_location <= shifted_value <= last_location:
                    decode_value = shifted_value
                if shifted_value < 32:
                    remains_subtract = ascii_value - first_location + 1
                    decode_value = last_location - ((num - remains_subtract) % (last_location + 1 - first_location))

                shifted_lst.append(decode_value)

            shifted_str = ""
            for item in shifted_lst:
                shifted_str += chr(item)

        else:
            shifted_str = self.cyclic_chars(abs(num))

        return String(shifted_str)


class BytePairError(Exception):
    pass


class BytePairDecodeError(Exception):
    pass


class Base64DecodeError(Exception):
    pass


class CyclicCharsError(Exception):
    pass


class CyclicCharsDecodeError(Exception):
    pass