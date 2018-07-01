

class QCheckNLP:
    def GetQuestion(self, string):

            # Calculate the length of the string.
            length = len(string)

            # Check that the first character lies in [A-Z].
            # Otherwise return false.
            if string[0] < 'A' or string[0] > 'Z':
                return False

            # If the last character is not a full stop(.) no
            # need to check further.
            if string[length - 1] != '.':
                return False

            # Maintain 2 states. Previous and current state based
            # on which vertex state you are. Initialise both with
            # 0 = start state.
            prev_state = 0
            curr_state = 0

            # Keep the index to the next character in the string.
            index = 1

            # Loop to go over the string.
            while (string[index]):
                # Set states according to the input characters in the
                # string and the rule defined in the description.
                # If current character is [A-Z]. Set current state as 0.
                if string[index] >= 'A' and string[index] <= 'Z':
                    curr_state = 0

                # If current character is a space. Set current state as 1.
                elif string[index] == ' ':
                    curr_state = 1

                # If current character is a space. Set current state as 2.
                elif string[index] >= 'a' and string[index] <= 'z':
                    curr_state = 2

                # If current character is a space. Set current state as 3.
                elif string[index] == '.':
                    curr_state = 3

                # Validates all current state with previous state for the
                # rules in the description of the problem.
                if prev_state == curr_state and curr_state != 2:
                    return False

                # If we have reached last state and previous state is not 1,
                # then check next character. If next character is '\0', then
                # return true, else false
                if prev_state == 2 and curr_state == 0:
                    return False

                # Set previous state as current state before going over
                # to the next character.
                if curr_state == 3 and prev_state != 1:
                    return True

                index += 1

                prev_state = curr_state

            return False