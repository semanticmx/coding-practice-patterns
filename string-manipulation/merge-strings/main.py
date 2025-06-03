class Solution:
    def merge(self, word1: str, word2: str) -> str:
        """
        Alternative 01 (Hassan)
        1. Take the first letter of word1
            a
        2. Take the first letter of word2
            q
        3. If a word ends, keep taking letters from the other one
        Q. How dow you know which argument (word1 or word2) to check for end.
        A. Adding one more step before step 3 to check which Word is more long.

        4. Stop When are no more letters in both word
        5. Show the final result
        """

        """
        Alternative 02 (James)
        _______
        |Start|
        -------
           |
        ._______.
        | word1 |
        .-------.
            |
        ._______.
        | word2 |
        .-------.
            |
        word2 > word1

        1. User types a word, and that value is stored as a string in word1
           asd
        2. User types a word, and that value is stored as a string in word2
            qwe
        3. Is word2 larger than word1 OR is word1 larger than word2?
            No
                4. set an integer named ln as the length of word2
                5. Goto step 10
            Yes
                Continue with step 6 as normal
        6.. Check for the largest string
        Q. There's no largest string
        A. It would jump straight to step 10

        7. Check for the shortest string -- make its length an integer (named ln)
        8. Store the cut made to the largest string onto a third string -- named r_word
        9. Set a flag (named larger) to true

        10. Create an integer named pos and init it at 0
        11. Print char at index 'pos of word1
        12. Print char at index 'pos' of word2
        13. Increment pos by 1
        14. Is pos equal to ln?
            Yes
                15. Goto step 17.
            No
                16. Goto step 11.


        17. Is the flag (larger) set to true?
            Yes
                18. Print string r_word right next to the previous prints
            No
                19. Goto end 
        End
        """

        """
        Alternative 03 (John)
        1. Indicate the user to input a String or take a String from other place
            asd
        2. Indicate the user to input a String or take a String from other place
            qwe

        3. Save String 1 as word1
           word1 = "asd"
        4. Save String 2 as word2
           word2 = "qwe"

        5 Check which are the largest word , then assign it into "largest", in this case it's going to be word2 , then the shortest word will be stored into "shortest" in this case it's going to be word1

            Q. Both words are equal in length
            A. Run the statement if  and in the case of that words are the same length add a statement else to take the second word in this case word2

            largest = word2
            shortest = word1 


        6 Take "largest" and repeat  the loop the same times of the length of the word

        7 Split "largest" into letters, after that assign a number for each letter

            "q" = 1
            "w" = 2
            "e" = 3

        8 Depending the times of the repetitions assign the letter to saved_letter

            saved_letters = ["q"]

        8 Add one letter to "letters" without deleting the letter that were stored earlier 

            letters = ["q"]

        9 When the letters of "largest" ends ,skip to step 14

        10 Check if this step has already been used , in case that yes , skip this step to step 10  split "largest" into letters, after that assign a number for each letter

            "a" = 1
            "s" = 2
            "d" = 3

        11 Depending the times of the repetitions assign the letter to saved_letter2

            saved_letter2 = ["a"]

        12 Add "letters" without delete the letters that were stored earlier

        letters = ["q","a"]

        13 Goto step 8

        14 Print "letters"

        print(letters)
        """

        """
        Alternative 04 (Rich)

        1:Identify and store word1 and word2 as the input strings to be merged.
            word1 = "asd"
            word2 = "qwe"

        2:Create an empty list to hold the characters of the merged result.
            merged = []

        3:Determine how many times to loop by finding the length of the shorter word.


        4:Iterate through both words, adding one character from word1 and one from word2 at each step.

        5:After the loop, append any remaining characters from the longer word.

        6:Join the list into a final string and return the merged result.

        """

        """
        Alternative 05 (Max)
        1.User enters word1
            asd
        2.User enters word2
            qwe

        3.Determine the lenght of both words
            Save the number of characters of word1 in len1
            len1 = 3
            Save the number of characters of word2 in len2
            len2 = 3
        4.Create an empty string called result
            result = ""
        5.Initialize a variable called position with the value 0
            position = 0
        6. if position is less than len1 or less than len2 continue, otherwise goto step 11
        7. take the letter at "position" from word1 and add it to result.    
            result = ["a"]
        8. take the letter at "position" from word2 and add it to result.
            result = ["q"]
        9. Increase position by 1
            position = 1
        10. Goto step 6
        11. When there are no more positions in either word, stop.
            Q. word1 or word2 will always have letters
            A. Error of variable, it was positions no letters

        12. Display or return the string result
        """

        """
        Paso 1: 
                    Identificar las dos palabras que se van a fusionar.
                    Guardar cada palabra en una variable separada.
                        Ejemplo: `palabra1 = "abc"` y `palabra2 = "pqr"`.
                Paso 2: 
                    Crear una lista vacía para almacenar los caracteres del resultado fusionado.
                        "merged = []"
                Paso 3: 
                    Saber cuánto vas a repetir
                        Determina cuál es la palabra mas corta, y cual la mas larga 
                            "if largo1 > largo2:"
                Paso 4: 
                    Alternar letras una por una
                        Tomar una letra de la primera palabra.
                                "a""p"
                        Luego, Tomar una letra de la segunda palabra.
                                ap +"b""q"
                        Agregar ambas letras (en ese orden) al resultado 
                                ="apbqcr"
                Paso 5:
                    Agregar letras sobrantes
                    Después alternar:
                    Si la primera palabra es mas larga, agregar las letras faltantes.
                                        "abcp""pqr" = apbqcr"p

                    Si la segunda palabra era la más larga, agrege sus letras restantes.
                    "abc""pqr"s"=apbqcr"s"
                Paso 6: 
                    Unir las palabras para formar una sola cadena de texto.
                        "apbqcrs"        
        """
        return ""


if __name__ == "__main__":
    pass
