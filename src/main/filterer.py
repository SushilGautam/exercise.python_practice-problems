# Created by Leon Hunter at 12:10 PM 12/08/2020
class Filterer(object):
    def remove_characters(self, string_to_remove_from, characters_to_remove):
        result= str(string_to_remove_from)
        for removable in characters_to_remove:
            result = result.replace(removable, '')
        return result

    def remove_vowels(self, string_to_remove_from):
        lower_case_vowels = 'aeiou'
        upper_case_vowels = lower_case_vowels.upper()
        vowels = lower_case_vowels + upper_case_vowels
        vowels_list = list(vowels)
        return  self.remove_characters(string_to_remove_from, vowels_list)

    def remove_consonants(self, string_to_remove_from):
        lower_case_consonants = 'bcdfghjklmnpqrstvwxyz'
        upper_case_consonants = lower_case_consonants.upper()
        consonants = lower_case_consonants + upper_case_consonants
        consonants_list = list(consonants)
        return  self.remove_characters(string_to_remove_from, consonants_list)



